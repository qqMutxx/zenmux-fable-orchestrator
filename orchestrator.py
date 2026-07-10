import os
import httpx

# ZenMux API Gateway Configuration
ZENMUX_API_URL = "https://zenmux.ai/api/v1/chat/completions"
API_KEY = os.getenv("ZENMUX_API_KEY", "your-zenmux-friend-token")

def call_fable_agent(prompt: str):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "anthropic/claude-fable-5",
        "messages": [{"role": "user", "content": prompt}],
        "output_config": {
            "effort": "max"
        }
    }
    print(f"[ZenMux] Directing prompt to Claude Fable 5...")
    response = httpx.post(ZENMUX_API_URL, json=payload, headers=headers, timeout=60.0)
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        raise Exception(f"API Error: {response.status_code}")

if __name__ == "__main__":
    try:
        result = call_fable_agent("Verify O(log n) tree traversal patterns.")
        print(result)
    except Exception as e:
        print(f"Error: {e}")
