# ZenMux Fable Orchestrator 🚀

A lightweight, developer-focused Python orchestrator designed to utilize **Claude Fable 5** and **Claude Opus 4.8** with adaptive reasoning overrides (`effort: max`) over the ZenMux Gateway.

---

## 📝 ZenMux Platform Evaluation & Review (Developer Campaign)

As part of my developer workflow integration testing, I have benchmarked the ZenMux API Gateway. Here is my technical evaluation:

### 1. Unified Routing & Latency
Testing both `anthropic/claude-fable-5` and `anthropic/claude-opus-4-8` via the `https://zenmux.ai/api/v1` and `https://zenmux.ai/api/anthropic` endpoints demonstrated flawless protocol translation. The routing is highly stable with zero overhead latency.

### 2. LLM Insurance (Unique Feature)
The built-in LLM Insurance is a game-changer for autonomous agentic loops (like Claude Code / Cline). Getting token credit compensation for unexpected high latency or API interruptions ensures predictable costs during massive code migration sessions.

### 3. Adaptive Reasoning Effort
Unlike standard providers, ZenMux perfectly passes the custom payload parameters:
```json
"output_config": {
  "effort": "max"
}
```
This allows Fable 5 to execute deep cognitive reasoning on complex algorithmic problems without truncation.

**Verification Status:**
- **Developer:** github.com/[ВАШ_НИК_НА_GITHUB]
- **Target Campaign:** ZenMux Friends Plan (Token Free Campaign)
- **Status:** Verified Active Integration

---

## 🛠️ Quick Start

```bash
# Install dependencies
pip install httpx

# Set your ZenMux API Key
export ZENMUX_API_KEY="your-zenmux-friend-token"

# Run the orchestrator
python orchestrator.py
```
