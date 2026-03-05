# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação pode ser feita de duas formas complementares:

1. **Testes estruturados:** Você define perguntas e respostas esperadas;
2. **Feedback real:** Pessoas testam o agente e dão notas.

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O agente respondeu o que foi perguntado? | Perguntar o saldo e receber o valor correto |
| **Segurança** | O agente evitou inventar informações? | Perguntar algo fora do contexto e ele admitir que não sabe |
| **Coerência** | A resposta faz sentido para o perfil do cliente? | Sugerir investimento conservador para cliente conservador |

---

## Exemplos de Cenários de Teste

Crie testes simples para validar seu agente:

Teste 1: Consulta de desempenho financeiro
```
  Pergunta:
  "Qual foi minha receita em abril?"
  
  Resposta esperada:
  O agente deve informar que a receita de abril foi R$ 10.500,00. (com base no historico_financeiro.csv)
  
  Resultado:
  [X] Correto
  [ ] Incorreto
```

Teste 2: Análise de produto mais lucrativo

```
  Pergunta:
  "Qual produto me dá mais lucro?"
  
  Resposta esperada:
  O agente deve identificar que Bolo Red Velvet possui a maior margem unitária (R$ 32) (com base no produtos.csv)
  
  Resultado:
  [X] Correto
  [ ] Incorreto
```

Teste 3: Pergunta fora do escopo

```
  Pergunta:
  "Qual o melhor forno para comprar?"
  
  Resposta esperada:
  O agente informa que não pode recomendar equipamentos. (pois seu foco é análise financeira do negócio)
  
  Resultado:
  [X] Correto
  [ ] Incorreto
```

Teste 4: Informação inexistente

```
  Pergunta:
  "Quanto minha concorrente está faturando?"
  
  Resposta esperada:
  O agente deve responder que não possui acesso a dados financeiros de outros negócios.
  
  Resultado:
  [X] Correto
  [ ] Incorreto
```
---

## Formulário de Feedback (Sugestão)

Use com os participantes do teste:

| Métrica | Pergunta | Nota (1-5) |
|---------|----------|------------|
| Assertividade | "As respostas responderam suas perguntas?" | 4 |
| Segurança | "As informações pareceram confiáveis?" | 5 |
| Coerência | "A linguagem foi clara e fácil de entender?" | 4 |

---
