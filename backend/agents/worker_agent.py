import os
import requests
from tools.file_tools import write_file

HF_API_KEY = os.getenv("HF_API_KEY")
MODEL_URL = "https://api-inference.huggingface.co/models/Qwen/Qwen2.5-Coder-7B-Instruct"

def run_worker(subtask: str):
    prompt = f"""
You are a coding agent.

Task:
{subtask}

Return ONLY valid JSON:
{{"filename": "README.md", "content": "text content"}}
"""
    headers = {"Authorization": f"Bearer {HF_API_KEY}"}
    response = requests.post(MODEL_URL, headers=headers, json={"inputs": prompt}, timeout=60)
    data = response.json()
    text = data[0]["generated_text"]

    start = text.find("{")
    end = text.rfind("}") + 1
    payload = eval(text[start:end])

    write_file(payload["filename"], payload["content"])

    return {"subtask": subtask, "file_written": payload["filename"]}
