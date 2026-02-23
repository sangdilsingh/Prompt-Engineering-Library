# 📊 LLM Evaluation: GPT-4o vs Claude 3.5 Sonnet

Is project mein hum check kar rahe hain ki different AI models instructions ko kitni accuracy se follow karte hain. Ye RLHF (Reinforcement Learning from Human Feedback) skills ko showcase karta hai.

## Case Study 1: Feedback Summarization (Negative Constraints)

| Category | GPT-4o Details | Claude 3.5 Details |
| :--- | :--- | :--- |
| **Task / Prompt** | Summarize feedback in 3 bullet points. **No intro text.** | Summarize feedback in 3 bullet points. **No intro text.** |
| **Factuality** | ⭐⭐⭐⭐⭐ (5/5) | ⭐⭐⭐⭐⭐ (5/5) |
| **Constraint Following** | ⭐⭐ (2/5) | ⭐⭐⭐⭐⭐ (5/5) |
| **Tone & Style** | ⭐⭐⭐⭐ (4/5) | ⭐⭐⭐⭐⭐ (5/5) |
| **Verbosity** | ⭐⭐⭐⭐ (4/5) | ⭐⭐⭐⭐ (4/5) |

### 🔍 Detailed Comparison

| Model | Response Snippet | Why this rating? |
| :--- | :--- | :--- |
| **GPT-4o** | "Here is the summary: 1. Fast..." | **Failed.** It included conversational filler despite being told "No intro text". |
| **Claude 3.5** | "1. Fast software..." | **Winner.** Strictly followed the negative constraint and provided a clean output. |

### 🧠 Reasoning Box
**Winner: Claude 3.5 Sonnet.** While both models were factually correct, Claude demonstrated superior instruction following. In high-stakes AI training (like Mindrift or Outlier projects), following specific negative constraints is crucial for quality data.
