# Comparação de modelos — Sprint 04 (com histórico Sprint 03)

## Experimento controlado

Modelos locais: `qwen3:4b-instruct` e `llama3.2:3b`; prompt v2, k=8, limiar 0.60, mesmo conjunto de 10 perguntas. Temperature=0.2, top_p=0.9, max_tokens=512; embeddings `nomic-embed-text`; chunks 800/120; ChromaDB persistente.

| Modelo | Perguntas técnicas respondidas | Citações explícitas | Faithfulness média* | Answer relevancy média* |
|---|---:|---:|---:|---:|
| qwen3:4b-instruct | 4/5 | 0/4 | 0.75 | 1.00 |
| llama3.2:3b | 4/5 | 1/4 | 0.75 | 1.00 |

*Notas manuais equivalentes, somente entre respostas técnicas produzidas, com justificativas em `evals/avaliacao_manual_comparativa_sprint4.json`; não são RAGAS. Llama errou a expansão de CA; ambos produziram expansão não verificada de RCD. Qwen foi escolhido como modelo principal. A taxa de citação, isoladamente, não mede correção.

## Evolução da configuração Qwen

| Iteração | Cobertura | Citações explícitas |
|---|---:|---:|
| v2, limiar 0.60 | 4/5 | 0/4 |
| v3, limiar 0.60 | 4/5 | 4/4 |
| v3, limiar 0.55 | 5/5 | 5/5 |

O prompt v3 elevou a rastreabilidade; o limiar 0.55 recuperou uma resposta antes recusada. As médias de faithfulness das respostas geradas não melhoraram no conjunto analisado. Isso é uma limitação explicitada, não um ganho inventado.

## Histórico (Sprint 03)

A Sprint 03 possuía comparações próprias de chatbot conversacional e provedores externos; seus resultados **não devem ser comparados diretamente** aos testes RAG desta Sprint 04, pois os conjuntos e critérios diferem. Provedores NVIDIA/OpenRouter continuam opcionais e exigem credenciais; os testes de Sprint 04 documentados foram locais.
