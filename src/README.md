# Código da Aplicação

Esta pasta contém o código do Vithor AI em Python

## Setup do Ollama

```bash
# 1. Instalar Ollama (ollama.com)
# 2. Baixar um modelo leve (caso tenha problemas instalando modelo, tente usar um modelo em nuvem)
ollama pull gpt-oss

# 3. Testar se o modelo funciona
ollama run gpt-oss "Olá!"
```

## Código completo

Codigo fonte inteiro disponivel no arquivo `app.py`.

## Como Rodar

```bash
# 1. Instalar dependências
pip install streamlit pandas requests

# 2. Garantir que Ollama está rodando
ollama serve

# 3. Rodar o app
streammlit run .\src\app.py
```



## Estrutura 

```
src/
├── app.py              # Aplicação completa
```

## Evidência de execução

<img width="1869" height="947" alt="image" src="https://github.com/user-attachments/assets/11701243-d082-4f26-a096-fd2629bf63fd" />
