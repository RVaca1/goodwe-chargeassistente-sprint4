# Relatório de evolução — Sprint 04 (rascunho; exportar para PDF, até 5 páginas)

## 1. Evolução
Sprint 03: núcleo conversacional LangChain, memória e Pydantic. Sprint 04: módulo de ingestão, ChromaDB persistente, retrieval, prompt RAG e Streamlit com exibição de fontes.

## 2. Decisões
Chunking inicial de 800 caracteres, overlap 120; embeddings nomic-embed-text; top-k=4; filtro de relevância ajustável. Comparar alternativas no mesmo eval set.

## 3. Antes/depois — preencher com medições reais
| Métrica | Sprints 1/2 (original) | Sprint 04 (RAG avaliado) |
|---|---|---|
| Faithfulness | A MEDIR | A MEDIR |
| Answer relevancy | A MEDIR | A MEDIR |
| Qualidade do contexto recuperado | A MEDIR | A MEDIR |
| Respostas com fonte visível | A MEDIR | A MEDIR |

## 4. Problemas e soluções — confirmar após testes
1. Dependência de documentos verificados: bloquear respostas sem contexto; adicionar manuais reais.
2. Instruções maliciosas nos documentos: separar dados de instruções e filtrar trechos suspeitos; testar ataques.

## 5. Equipe
Preencher nome, RM, turma e responsabilidade real de cada integrante.

**Não apresentar este rascunho como relatório final medido.**
