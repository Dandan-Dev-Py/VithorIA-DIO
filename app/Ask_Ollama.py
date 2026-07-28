from prompts import SYSTEM_PROMPT, contexto
import requests

# ====================== API DO OLLAMA =====================
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gpt-oss"

# ========== CHAMAR OLLAMA =====================

def perguntar(msg):
    prompt = f'''
    {SYSTEM_PROMPT}

    CONTEXTO DO CLIENTE:
    {contexto}

    Pergunta: {msg}'''

    r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False})
    return r.json()['response']



