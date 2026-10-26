"""工单分诊：用 Jev 一次回答三个问题，再由代码根据置信度决定怎么处理。"""

from dataclasses import dataclass

from typesafe_sdk import Choice, Noul, Score, SystemOneResponse, TypeSafeClient

# ---- 1. 定义问题：三种原语各一个 ----
QUESTIONS = {
    "department": Choice(
        instructions="Which team should handle this",
        criteria={
            "billing": "Payment or subscription issues",
            "technical": "Bugs or integration problems",
            "sales": "Pricing or account questions",
        },
    ),
    "frustration": Score(
        instructions="How frustrated the customer appears",
        criteria=[
            "Calm, just stating facts",
            "Frustrated but civil",
            "Very angry, strong language",
        ],
    ),
    "is_urgent": Noul(
        instructions="The message conveys urgency or time-sensitivity",
    ),
}

# ---- 2. 风险阈值：由代码决定，而不是写在提示词里 ----
MIN_CONFIDENCE = 0.5  # 低于它：模型确实不确定，不猜
AUTO_ASSIGN_CONFIDENCE = 0.75  # 高于它：自动分派
URGENT_THRESHOLD = 0.8  # noul 高于它视为紧急
ANGRY_THRESHOLD = 1.5  # frustration 高于它视为非常不满


@dataclass
class Decision:
    action: str  # auto_assign / confirm_assign / human_review
    team: str | None
    priority: str  # high / normal
    reason: str


def route(response: SystemOneResponse) -> Decision:
    """把类型化答案变成业务动作：分支、阈值、回退全在这里。"""
    dept = response.choices["department"]
    frustration = response.scores["frustration"]
    urgent = response.nouls["is_urgent"]

    high = urgent.noul >= URGENT_THRESHOLD or frustration.score >= ANGRY_THRESHOLD
    priority = "high" if high else "normal"

    if dept.confidence < MIN_CONFIDENCE:
        return Decision("human_review", None, priority, f"部门判断不确定（confidence={dept.confidence:.2f}），转人工")
    if dept.confidence >= AUTO_ASSIGN_CONFIDENCE:
        return Decision("auto_assign", dept.choice, priority, f"置信度足够（{dept.confidence:.2f}），自动分派")
    return Decision("confirm_assign", dept.choice, priority, f"置信度中等（{dept.confidence:.2f}），分派前请值班同学确认")


def triage(client: TypeSafeClient, ticket: str) -> tuple[SystemOneResponse, Decision]:
    # ---- 3. 一次调用，三个问题针对同一份 state 并行评估 ----
    response = client.system_one(state=ticket, questions=QUESTIONS)
    return response, route(response)
