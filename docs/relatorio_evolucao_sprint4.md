# Evolução do GoodWe ChargeAssistente — Sprint 04

**Turma CCPH — Ciência da Computação, 2º semestre.** Equipe e RMs em [`../integrantes.txt`](../integrantes.txt).

## Antes → depois

- **Sprint 03:** chatbot conversacional com LangChain, memória e guardrails; sem os resultados RAG da Sprint 04.
- **Sprint 04:** ingestão de manuais GoodWe, chunking 800/120, embeddings `nomic-embed-text`, ChromaDB persistente, recuperação filtrada, prompt com citações e Streamlit que mostra fontes e páginas.

## Iterações e resultados

| Iteração | Cobertura técnica | Citações explícitas |
|---|---:|---:|
| Qwen v2 / 0.60 | 4/5 | 0/4 |
| Qwen v3 / 0.60 | 4/5 | 4/4 |
| Qwen v3 / 0.55 | 5/5 | 5/5 |

O conjunto tem 10 perguntas, 5 técnicas. Faithfulness e answer relevancy foram avaliadas manualmente por rubrica equivalente, com justificativas e médias em `evals/avaliacao_manual_comparativa_sprint4.json`. As médias não evidenciam ganho de faithfulness entre versões; os ganhos observados são de cobertura e citações. Não existe baseline RAGAS diretamente comparável das Sprints 1/2.

## Problemas e soluções

1. Respostas sem referência verificável → prompt v3 exige documento e página.
2. Trecho relevante com score 0.569 bloqueado pelo limiar 0.60 → ajuste para 0.55; requer novos testes de robustez.
3. Expansões indevidas de siglas (CA no Llama; RCD não demonstrado) → notas conservadoras e recomendação de validação antes de responder termos técnicos.
4. Injection documental simulada → filtro descartou trecho malicioso antes da geração; não equivale a garantia universal.

## Configuração final

Qwen3 4B instruct; Ollama; temperature 0.2; top_p 0.9; max_tokens 512; k=8; score_threshold=0.55; chunk size 800; overlap 120; ChromaDB persistente; `nomic-embed-text`; prompt v3.

## Limitações

Amostra de 10 perguntas, rubrica manual e citações avaliadas por presença textual; falta auditoria completa de todas as afirmações e teste de robustez fora da amostra. As execuções e notas estão em `evals/`.
