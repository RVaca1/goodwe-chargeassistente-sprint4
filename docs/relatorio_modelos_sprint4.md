# Comparação de Modelos — Sprint 04

## Objetivo

Comparar modelos de geração em um pipeline RAG com
ChromaDB persistente e embeddings nomic-embed-text.

## Configuração experimental

- Modelos: qwen3:4b-instruct e llama3.2:3b
- Prompt: v2 para comparação direta entre modelos
- Top-k: 8
- Limite de relevância: 0.60
- Conjunto de avaliação: 10 perguntas

## Resultados

| Métrica | Qwen v2 | Llama v2 |
|---|---:|---:|
| Perguntas técnicas respondidas | 4/5 | 4/5 |
| Citações explícitas nas respostas | 0/4 | 2/4 |
| Prompt injections bloqueadas | 2/2 | 2/2 |

## Análise

Ambos os modelos responderam quatro das cinco perguntas
técnicas. A pergunta sobre as potências disponíveis na
série HCA falhou por causa do limite de relevância,
apesar de existir um trecho pertinente no manual.

O Llama apresentou um erro factual ao interpretar CA
como "Carregador de Alta Potência", em vez de corrente
alternada.

O Qwen foi selecionado para a próxima iteração devido
à qualidade observada das respostas e à possibilidade
de melhorar a rastreabilidade com ajustes no prompt.

## Evolução do Qwen

| Configuração | Respostas técnicas | Citações |
|---|---:|---:|
| Prompt v2, limite 0.60 | 4/5 | 0/4 |
| Prompt v3, limite 0.60 | 4/5 | 4/4 |
| Prompt v3, limite 0.55 | 5/5 | 5/5 |

A versão v3 melhorou a presença de citações explícitas.
O limite 0.55 recuperou a resposta sobre as potências
nominais da série HCA.

## Limitações

Esses resultados não constituem, por si só, métricas
RAGAS de faithfulness e answer relevancy.

Os parâmetros exatos de geração e a fidelidade de cada
resposta ainda precisam ser verificados e registrados.
