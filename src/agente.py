# Carregando os dados
import json 
import pandas as pd 
import requests 
import streamlit as st 

# Configurações do modelo
OLLAMA_URL = "http://localhost:11434/api/chat" 
MODELO = "phi3"

historico = pd.read_csv('./data/historico_financeiro.csv')
produtos = pd.read_csv('./data/produtos.csv')
perfil = json.load(open('./data/perfil_negocio.json'))
base_conhecimento = json.load(open('./data/base_conhecimento_financeira.json'))

# Cálculos necessários para a análise

historico['lucro'] = (
    historico['receita_total']
    - historico['custos_fixos']
    - historico['custos_variaveis']
    - historico['impostos']
    - historico['investimento_marketing']
)

receita_media = historico['receita_total'].mean()
lucro_medio = historico['lucro'].mean()
margem_media = lucro_medio / receita_media

contexto = f"""
NEGÓCIO: {perfil['nome_negocio']}
TIPO: {perfil['tipo_negocio']}
TEMPO DE MERCADO: {perfil['tempo_mercado']}
FUNCIONÁRIOS: {perfil['funcionarios']}
META DE MARGEM: {perfil['meta_margem_lucro']*100}%

RESUMO FINANCEIRO:
Receita média: R$ {receita_media:.2f}
Lucro médio: R$ {lucro_medio:.2f}
Margem média: {margem_media*100:.2f}%

HISTÓRICO COMPLETO:
{historico.to_string(index=False)}

PRODUTOS:
{produtos.to_string(index=False)}

REGRAS DE ANÁLISE:
{json.dumps(base_conhecimento, indent=2, ensure_ascii=False)}
"""

SYSTEM_PROMPT = """Você é a Celine, uma educadora e contabilista amigável, didática e prática.

OBJETIVO:
Ajudar os clientes a entender se seus empreendimentos estão gerando lucro real ou não

REGRAS:
- NUNCA recomende investimentos específicos ou formas do cliente aumentar seu lucro, apenas mostre ao cliente explique se seu negócio está gerando lucro ou não;
- JAMAIS responda a perguntas fora do tema ensino de finanças pessoais.
  Quando ocorrer, responda lembrando o seu papel de contabilista e educadora;
- Use os dados fornecidos para dar exemplos personalizados;
- NUNCA use os dados do cliente X para aconselhar o cliente Y, apenas compare com o mercado financeiro, nunca com outros cliente
- NUNCA aconselhe o cliente a comprar um produto ou serviço específico, se ocorrer lembre o cliente que seu papel é calcular o lucro real dele e explicar como isso afeta seu empreendimento;
- Responda apenas questões relacionadas à análise financeira do negócio;
- Linguagem simples, como se explicasse para um amigo;
- Se não souber algo, admita: "Não tenho essa informação, mas posso explicar...";
- Sempre pergunte se o cliente entendeu;
- Responda de forma sucinta e direta, com no máximo 4 parágrafos.
- Responda apenas à pergunta do usuário.
- Não repita o prompt ou o contexto.
"""

# Função que envia a pergunta ao modelo

def perguntar(msg):
    r = requests.post(
        OLLAMA_URL,
        json={
            "model": MODELO,
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": f"CONTEXTO DO CLIENTE:\n{contexto}\n\nPergunta: {msg}"}
            ],
            "stream": False
        }
    )

    return r.json()["message"]["content"]


#Interface

st.title("Celine - Análise Financeira Personalizada")

if pergunta := st.chat_input("Deseja calcular o lucro real do seu negócio?"):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_message("assistant").write(perguntar(pergunta))
