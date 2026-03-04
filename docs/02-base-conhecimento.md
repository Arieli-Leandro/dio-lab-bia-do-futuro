# Base de Conhecimento

## Dados Utilizados

| Arquivo                             | Formato | Para que serve no Agente?                                                                     |
| ----------------------------------- | ------- | --------------------------------------------------------------------------------------------- |
| `historico_financeiro.csv`          | CSV     | Permite analisar evolução da receita, custos, lucro e crescimento mensal do negócio.          |
| `produtos.csv`                      | CSV     | Permite calcular margem por produto e identificar quais itens são mais lucrativos.            |
| `perfil_negocio.json`               | JSON    | Personaliza as recomendações com base no tipo, metas e estrutura do negócio.                  |
| `base_conhecimento_financeira.json` | JSON    | Fornece conceitos e regras de análise financeira que o agente usa para explicar diagnósticos. |

---

## Adaptações nos Dados

Os dados foram criados para simular uma confeitaria artesanal chamada “Delícias da Ana”, permitindo:

- Simular sazonalidade de vendas
- Avaliar crescimento mensal
- Calcular margem de lucro
- Identificar risco financeiro
- Simular ponto de equilíbrio

Os valores foram ajustados para representar um microempreendimento realista de pequeno porte, com:
- 2 funcionários
- Custos fixos recorrentes
- Variação de custos variáveis
- Meta de margem de 25%
  
---
⚙️ Estratégia de Integração
Como os dados são carregados?

Os dados podem ser carregados diretamente via código:

```python

  import pandas as pd
  import json
  
  historico = pd.read_csv('./data/historico_financeiro.csv')
  produtos = pd.read_csv('./data/produtos.csv')
  perfil = json.load(open('./data/perfil_negocio.json'))
  base_conhecimento = json.load(open('./data/base_conhecimento_financeira.json'))

```

Como os dados são usados no prompt?

Para o MVP, os dados podem ser sintetizados e injetados diretamente no prompt, garantindo que o agente tenha contexto suficiente para gerar análises financeiras inteligentes.
Em versões mais avançadas, pode-se utilizar RAG para consultar apenas as informações relevantes dinamicamente.

---

📥 Exemplo de Dados Injetados no Prompt

Perfil do Negócio (perfil_negocio.json)
```python

{
  "nome_negocio": "Delícias da Ana",
  "tipo_negocio": "Confeitaria artesanal",
  "tempo_mercado": "2 anos",
  "modelo_vendas": "Encomendas via Instagram e WhatsApp",
  "funcionarios": 2,
  "meta_margem_lucro": 0.25
}

```
Histórico Financeiro (historico_financeiro.csv)
```python
mes,receita_total,custos_fixos,custos_variaveis,impostos,investimento_marketing
Janeiro,8500,2500,3200,600,400
Fevereiro,9200,2500,3500,650,500
Março,7800,2500,3000,580,300
Abril,10500,2700,4200,750,600

```
Produtos e Margens (produtos.csv)

```python
produto,preco_venda,custo_producao,media_vendas_mensais
Bolo de Chocolate,45,18,120
Bolo de Cenoura,40,15,95
Bolo Red Velvet,60,28,70

```
Regras de Análise (base_conhecimento_financeira.json)
```python
{
  "margem_baixa": "Margem abaixo de 15% indica risco financeiro.",
  "marketing_ideal": "Investimento ideal em marketing entre 5% e 10% da receita.",
  "crescimento_saudavel": "Crescimento mensal ideal entre 5% e 12%."
}

```
---

🧠 Exemplo de Contexto Montado para o LLM

Abaixo está um exemplo de como os dados podem ser sintetizados antes de enviar ao modelo, reduzindo consumo de tokens:

DADOS DO NEGÓCIO:
- Nome: Delícias da Ana
- Tipo: Confeitaria artesanal
- Funcionários: 2
- Meta de margem: 25%

RESUMO FINANCEIRO (Últimos 4 meses):
- Receita média: R$ 9.500
- Custos fixos médios: R$ 2.550
- Custos variáveis médios: R$ 3.475
- Investimento médio em marketing: R$ 450
- Crescimento irregular (queda em Março)

ANÁLISE DE PRODUTOS:
- Bolo de Chocolate: margem unitária R$ 27
- Bolo de Cenoura: margem unitária R$ 25
- Red Velvet: margem unitária R$ 32

REGRAS DE ALERTA:
- Margem abaixo de 15% = risco
- Marketing ideal: 5% a 10% da receita
- Crescimento ideal: 5% a 12%

INSTRUÇÃO PARA O AGENTE:
Analise a saúde financeira do negócio, identifique riscos, oportunidades de melhoria e sugira ações práticas.
