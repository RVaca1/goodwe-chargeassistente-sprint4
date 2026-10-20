# GoodWe ChargeAssistente — EV Challenge Sprint 04

**Turma:** CCPH — Ciência da Computação, 2º semestre.  
**Equipe:** Victor Manzini (RM 572123), Guilherme de Oliveira Santos (RM 572195), Caio Marinho Pereira (RM 572873), Ricardo Tunes (RM 555919), Luiz Cesar Conti Salvador (RM 571305).

A Sprint 04 amplia o chatbot da Sprint 03 com **RAG documental**: manuais GoodWe → extração PDF → chunks → embeddings Ollama → ChromaDB persistente → recuperação filtrada → geração com fontes → Streamlit.

## Executar localmente

Requer Python, Ollama em execução e os manuais PDF em `data/knowledge_base/` (quando não distribuídos, obtenha os documentos oficiais antes de indexar).

```bash
python -m pip install -r requirements.txt
ollama pull nomic-embed-text
ollama pull qwen3:4b-instruct
ollama pull llama3.2:3b  # comparação, opcional para uso normal
python -m scripts.index_knowledge
PYTHONPATH=. python -m streamlit run app/streamlit_app.py
```

**Configuração testada:** `OLLAMA_MODEL=qwen3:4b-instruct`, `LLM_PROVIDER=ollama`, prompt `v3`, `RAG_TOP_K=8`, `RAG_MIN_RELEVANCE=0.55`, embedding `nomic-embed-text`; Ollama local na porta 11434. Variáveis de ambiente ou `.env` podem substituir os padrões. A interface legada da Sprint 03 permanece em `streamlit_app.py` (raiz); **use `app/streamlit_app.py` para o RAG**.

## Reproduzir avaliações

Os resultados **já registrados** estão em `evals/qwen_v2_10.json`, `evals/qwen_v3_10.json`, `evals/llama_v2_10.json` e `evals/qwen_v3_threshold055.json`. Todos usam `evals/sprint4_eval_set.json` (10 perguntas). Para executar novos testes, consulte `python -m evals.run_sprint4 --help`; informe `--k 8` e o prompt/modelo pretendido. O limite de relevância é configurado no pipeline (ou em parâmetro específico se suportado pelo script); anote-o ao comparar execuções.

| Configuração | Cobertura técnica | Citações explícitas |
|---|---:|---:|
| Qwen v2 / 0.60 | 4/5 | 0/4 |
| Qwen v3 / 0.60 | 4/5 | 4/4 |
| Llama v2 / 0.60 | 4/5 | 2/4 |
| Qwen v3 / 0.55 | 5/5 | 5/5 |

**Importante:** citações explícitas ≠ fidelidade verificada. As notas manuais comparativas estão em `evals/avaliacao_manual_comparativa_sprint4.json` e foram aplicadas somente às respostas técnicas produzidas; recusas são contabilizadas à parte. Não são scores calculados pela biblioteca RAGAS. O conjunto é pequeno e não representa desempenho geral.

## Relatórios

- [`docs/relatorio_rag.md`](docs/relatorio_rag.md): pipeline, resultados, rubrica e segurança.
- [`docs/relatorio_modelos.md`](docs/relatorio_modelos.md): comparação entre modelos da Sprint 04 e histórico da Sprint 03.
- [`docs/relatorio_evolucao_sprint4.md`](docs/relatorio_evolucao_sprint4.md): evolução e limitações.
- [`relatorio_evolucao_sprint04_goodwe.pdf`](relatorio_evolucao_sprint04_goodwe.pdf): PDF de evolução (verificar conteúdo e limite de 5 páginas antes da entrega).
- [`integrantes.txt`](integrantes.txt): equipe e RMs.

## Segurança e limitações

Perguntas com tentativa explícita de injection foram bloqueadas (2/2); um trecho malicioso simulado foi descartado em teste isolado com `unittest.mock`. Isso **não prova segurança universal**. O filtro de relevância 0.55 foi escolhido em um conjunto reduzido. O ChromaDB e PDFs podem ser omitidos da publicação por tamanho/licença; nesse caso a indexação deve ser refeita localmente. **Não publique `.env`, chaves ou dados privados.**
