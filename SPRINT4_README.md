# Sprint 04 — instruções de execução

A implementação preserva a Sprint 03 e adiciona RAG em `src/rag/` e interface em `app/streamlit_app.py`.

## Instalação
```bash
python -m venv .venv
# Linux/macOS: source .venv/bin/activate
# Windows: .venv\Scripts\activate
pip install -r requirements.txt
ollama pull nomic-embed-text
ollama pull qwen3:4b-instruct
```

Configure `.env` com `LLM_PROVIDER=ollama`, `OLLAMA_MODEL=qwen3:4b-instruct`, `OLLAMA_BASE_URL=http://localhost:11434`, `EMBEDDING_MODEL=nomic-embed-text`. O serviço Ollama deve estar ativo. Alternativamente, configure um provedor LLM já suportado em `src/chain/builder.py`, mas **os embeddings continuam dependendo do endpoint Ollama**.

1. Coloque PDFs oficiais/verificados em `data/knowledge_base/` (README.md não é fonte de especificações; remova ou exclua da indexação antes de medir).
2. `python -m scripts.index_knowledge`
3. `streamlit run app/streamlit_app.py`
4. `python -m evals.run_sprint4 --prompt v1 --output evals/iteracao1.json`
5. `python -m evals.run_sprint4 --prompt v2 --output evals/iteracao2.json`
6. Revise scores usando `evals/manual_rubric.md`, compare modelos e complete os relatórios.

**Atenção:** Não há documentação oficial GoodWe nem credenciais no ZIP fornecido. Portanto, nenhuma avaliação real, score, melhoria ou conformidade com as exigências de fontes pode ser afirmada antes da indexação e dos testes. O ChromaDB usa relevância configurável (`RAG_MIN_RELEVANCE`, padrão 0.65); calibre com seus documentos. Para evitar documentos removidos permanecerem indexados, apague `data/chroma_db` e reindexe após mudanças de corpus. Os documentos recuperados são citados, mas as afirmações ainda exigem validação.
