import ollama

def call_model(messages,tools):
    return ollama.chat(
        model='qwen3',
        messages=messages,
        tools=tools
    )
