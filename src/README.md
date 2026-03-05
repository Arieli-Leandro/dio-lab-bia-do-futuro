# Passo a Passo de Execução

## Setup do Ollama

```bash
# 1. Instalar Ollama (ollama.com)
# 2. Baixar um modelo leve
ollama pull phi3

# 3. Testar se funciona
ollama run phi3 "Olá!"
```

## Código Completo

Todo o código-fonte está no arquivo `app.py`.

## Como Rodar

```bash
# 1. Instalar dependências
pip install streamlit pandas requests

# 2. Garantir que Ollama está rodando
ollama serve

# 3. Rodar o app
streamlit run .\src\agente.py
```

## Evidência de Execução

<img width="1032" height="796" alt="image" src="https://github.com/user-attachments/assets/0d8f3e92-f49d-4aea-9476-b06af0e00ca2" />

