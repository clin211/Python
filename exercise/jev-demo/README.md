# jev-demo：用 Jev 做客服工单分诊

配套文章《别再让大模型“写一段话”再去解析了：认识 Jev，一个直接返回决策的模型》的完整示例。

一次调用向 Jev 提出三个问题（Choice / Score / Noul），再由代码根据置信度决定：**自动分派、确认后分派，还是转人工**。

## 文件

| 文件 | 作用 |
|---|---|
| `triage.py` | 核心：问题定义、风险阈值、`route()` 决策策略 |
| `main.py` | 命令行入口：跑示例工单并打印概率条与决策 |
| `offline.py` | 离线模式：用假的 HTTP 传输层返回示例数据，无需 API Key |

## 运行

需要 Python ≥ 3.10。

```bash
cd jev-demo
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# 1) 离线模式：不需要 API Key，先看懂答案结构和控制流
python main.py --offline

# 2) 真实 API：从 TypeSafe 控制台获取 Key（可能产生费用）
export TYPESAFE_API_KEY=你的密钥      # Windows PowerShell: $env:TYPESAFE_API_KEY="你的密钥"
python main.py
python main.py "I was charged twice for my order, please refund one of them."
```

## 说明

- 离线模式下，请求仍完整经过 `typesafe-sdk` 的序列化与响应解析，只是 HTTP 层被替换成本地示例数据。
  第 1 条示例的数据取自官方 Quickstart 的响应，其余为人工编写，**不是真实模型输出**，只用于演示控制流。
- 真实模式的结果会与离线示例不同；阈值（`triage.py` 顶部）应根据你自己的数据调整。
- 想系统学习，可以看 Datawhale 的开源学习资料 Jev Cookbook：<https://datawhalechina.github.io/jev-cookbook/>
