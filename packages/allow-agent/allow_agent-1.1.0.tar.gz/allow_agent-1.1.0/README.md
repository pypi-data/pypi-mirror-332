<h1 align="center">
    <span style="font-size: 125px;">👍</span><br>
    <span style="font-size: 125px;">allow-agent</span>
  <br>
  <a href="https://github.com/EthicsGPT/allow-agent">
    <img src="https://img.shields.io/badge/%F0%9F%94%8D%20prompt-visibility-75C46B?style=flat-square">
  </a>
</h1>

<p align="center">
  <em>A lightweight Python framework for agent content moderation.</em>
</p>

---

## Installation

```bash
pip install allow-agent
```

## What is allow-agent?

**allow-agent** is a simple yet powerful framework that automatically intercepts outbound HTTP requests made by AI agents. It gives you complete visibility and control over what your AI agents are doing behind the scenes.

## Quick Start

### 1. Define a Request Handler

Place this at the top of your file to automatically intercept all outbound API requests:

```python
from allow_agent import *

# This decorator enables automatic request interception
@request
def request(url, method, headers, body):
    if url == "https://api.openai.com/v1/chat/completions":
        print(f"OpenAI API Request: {body['messages'][0]}")
        
    return True  # Allow all requests by default
```

### 2. Use the rest normally

The handler will automatically intercept all outbound requests. No need for any special configuration.

```python
# Your code works normally - requests are automatically intercepted
from openai import OpenAI

client = OpenAI()
response = client.chat.completions.create(
    model="o1-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "This is a test prompt."}
    ]
)
print(response.choices[0].message.content)
```

## Compatibility

| Library | Status |
|-------------------|--------|
| **openai** | ✅ Supported |
| **anthropic** | 🔄 Coming soon |
| **langchain** | 🔄 Coming soon |
| **browser-use** | 🔄 Coming soon |
| **aisuite** | 🔄 Coming soon |
| **requests** | 🔄 Coming soon |
| **google-generativeai** | 🔄 Coming soon |

### Block requests

```python
@request
def request(url, method, headers, body):
    # Block requests containing sensitive keywords
    if "api.openai.com" in url:
        messages_text = str(body.get("messages", ""))
        sensitive_terms = ["password", "credit card", "ssn"]
        
        for term in sensitive_terms:
            if term in messages_text.lower():
                print(f"Blocked request containing sensitive term: {term}")
                return False  # Block the request
                
    return True  # Allow all other requests
```

## Common Use Cases

- **Logging**: Monitor all prompts sent to AI models
- **Content Filtering**: Block requests containing sensitive information
- **Cost Control**: Limit the number or size of API calls
- **Compliance**: Ensure all AI interactions follow regulatory requirements
- **Debugging**: Inspect exactly what data is being sent to external services

## ⭐ Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
