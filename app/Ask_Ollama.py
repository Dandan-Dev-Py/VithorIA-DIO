from prompts import SYSTEM_PROMPT, contexto
import requests

# ====================== API DO OLLAMA =====================
OLLAMA_URL = "http://localhost:11434/api/generate"
<<<<<<< HEAD
MODELO = "minimax-m3:cloud"
=======
MODELO = "gpt-oss"
>>>>>>> 0b26e53c7112f88e61205ccbaf13665f73a47774

# ========== CHAMAR OLLAMA =====================

def perguntar(msg):
    prompt = f'''
    {SYSTEM_PROMPT}

    CONTEXTO DO CLIENTE:
    {contexto}

    Pergunta: {msg}'''

    r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False})
    return r.json()['response']



