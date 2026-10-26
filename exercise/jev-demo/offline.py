"""离线模式：用一个假的 HTTP 传输层替代真实 API。

请求照常经过 SDK 的序列化与响应解析，只是返回的是事先写好的示例数据。
第 1 条示例取自官方 Quickstart 的响应；其余为人工编写，仅用于演示控制流，
不是真实模型输出。
"""

import json

import httpx2

from typesafe_sdk import RetryPolicy, TypeSafeClient


def _choice(probs: dict[str, float], confidence: float) -> dict:
    return {"type": "choice", "choice": max(probs, key=probs.get), "confidence": confidence, "probabilities": probs}


def _score(probs: list[float], confidence: float, legend: list[str]) -> dict:
    return {
        "type": "score",
        "score": round(sum(i * p for i, p in enumerate(probs)), 2),
        "confidence": confidence,
        "legend": {str(i): text for i, text in enumerate(legend)},
        "probabilities": {str(i): p for i, p in enumerate(probs)},
    }


def _noul(p: float) -> dict:
    return {"type": "noul", "noul": p}


# 每条示例工单对应的“答案”：(department, frustration, is_urgent)
SAMPLE_ANSWERS = {
    "Hi, I've been trying to connect my Stripe account for 3 days and the integration keeps failing. "
    "I'm losing sales. Please help ASAP.": (
        _choice({"technical": 0.85, "sales": 0.0, "billing": 0.15}, 0.78),
        [0.0, 1.0, 0.0], 1.0, 1.0,
    ),
    "Hello, could you tell me whether the annual plan includes priority support? Thanks!": (
        _choice({"technical": 0.03, "sales": 0.9, "billing": 0.07}, 0.84),
        [0.95, 0.05, 0.0], 0.97, 0.05,
    ),
    "You charged my card AGAIN after I cancelled. This is ridiculous, fix it now!": (
        _choice({"technical": 0.08, "sales": 0.1, "billing": 0.82}, 0.73),
        [0.0, 0.2, 0.8], 0.82, 0.96,
    ),
    "My account looks weird since yesterday.": (
        _choice({"technical": 0.42, "sales": 0.21, "billing": 0.37}, 0.12),
        [0.6, 0.4, 0.0], 0.55, 0.2,
    ),
}


def _handler(request: httpx2.Request) -> httpx2.Response:
    body = json.loads(request.content)
    if body["state"] not in SAMPLE_ANSWERS:
        return httpx2.Response(400, json={"error": {"message": "离线模式只包含内置示例工单，请设置 TYPESAFE_API_KEY 使用真实 API"}})
    dept, frustration_probs, frustration_conf, urgent = SAMPLE_ANSWERS[body["state"]]
    legend = body["questions"]["frustration"]["criteria"]
    answers = {
        "department": dept,
        "frustration": _score(frustration_probs, frustration_conf, legend),
        "is_urgent": _noul(urgent),
    }
    return httpx2.Response(200, json={
        "model": "offline-sample",
        "answers": {k: v for k, v in answers.items() if k in body["questions"]},
        "usage": {"input_tokens": None, "output_tokens": None},
    })


def offline_client() -> TypeSafeClient:
    return TypeSafeClient(
        api_key="offline-demo",
        transport=httpx2.MockTransport(_handler),
        compression=False,
        retry=RetryPolicy(max_retries=0),
    )
