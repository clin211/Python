"""Jev 工单分诊示例。

    python main.py                 # 有 TYPESAFE_API_KEY 时调用真实 API，否则走离线示例
    python main.py --offline       # 强制离线
    python main.py "your ticket"   # 分诊自己的工单（需要 API Key）
"""

import argparse
import os

from typesafe_sdk import TypeSafeAuthenticationError, TypeSafeClient

from offline import SAMPLE_ANSWERS, offline_client
from triage import triage

ACTION_LABELS = {"auto_assign": "✅ 自动分派", "confirm_assign": "🟡 确认后分派", "human_review": "🔴 转人工"}


def bar(p: float, width: int = 20) -> str:
    return "█" * round(p * width) + "·" * (width - round(p * width))


def show(ticket: str, response, decision) -> None:
    dept = response.choices["department"]
    frustration = response.scores["frustration"]
    urgent = response.nouls["is_urgent"]

    print("=" * 64)
    print(f"工单：{ticket}")
    print(f"\n[Choice] department → {dept.choice}  (confidence {dept.confidence:.2f})")
    for label, p in sorted(dept.probabilities.items(), key=lambda kv: -kv[1]):
        print(f"    {label:<10} {bar(p)} {p:.2f}")
    level = round(frustration.score)
    print(f"[Score]  frustration → {frustration.score:.2f}  ≈ {frustration.legend[level]}")
    print(f"[Noul]   is_urgent → {urgent.noul:.2f}")
    print(f"\n决策：{ACTION_LABELS[decision.action]}  team={decision.team}  priority={decision.priority}")
    print(f"原因：{decision.reason}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Jev 工单分诊示例")
    parser.add_argument("ticket", nargs="?", help="要分诊的工单文本；不填则跑内置示例")
    parser.add_argument("--offline", action="store_true", help="使用离线示例数据，不调用 API")
    args = parser.parse_args()

    live = not args.offline and os.environ.get("TYPESAFE_API_KEY")
    if args.ticket and not live:
        parser.error("分诊自定义工单需要真实 API：请先设置环境变量 TYPESAFE_API_KEY")
    client = TypeSafeClient() if live else offline_client()
    print("模式：真实 API（jev-latest）" if live else "模式：离线示例（示例数据，非真实模型输出）")

    tickets = [args.ticket] if args.ticket else list(SAMPLE_ANSWERS)
    for ticket in tickets:
        try:
            response, decision = triage(client, ticket)
        except TypeSafeAuthenticationError:
            raise SystemExit("API Key 无效：请检查 TYPESAFE_API_KEY，或加 --offline 先跑离线示例")
        show(ticket, response, decision)
    print("=" * 64)
    print(f"模型：{response.model}")


if __name__ == "__main__":
    main()
