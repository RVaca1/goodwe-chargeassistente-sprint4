# Sprint 04 — Document inventory

Seven unique PDFs were integrated locally. Two supplied HCA G2 English user manuals were byte-for-byte identical; one was excluded.

## Included

- HCA Series user manuals: Portuguese, English and Spanish.
- HCA G2 English user manual.
- HCA and HCA G2 quick installation guides (multilingual).
- ANEEL 2025 rectification notice concerning Resolution 1000 — **not the full regulation**.

## Important restrictions

GoodWe manuals state restrictions on reproducing and uploading their content to public platforms without authorization. This ZIP is for local academic use. PDFs are ignored by Git and should not be committed to a public GitHub repository unless permission has been obtained. The chatbot must cite source document and page, and should not reproduce extensive copyrighted passages.

## Coverage gaps

- Official distributor tariff tables with region and validity period.
- Full applicable regulatory text, if legal/regulatory Q&A is required.
- Actual condominium charging policy (do not invent one).
- Product datasheets if comparison across models is desired.

## Run

From the project root, after installing dependencies and configuring Ollama, run:

```bash
python -m scripts.index_knowledge
streamlit run app/streamlit_app.py
```

Indexing, model access, citations, and RAGAS scoring still require live testing. The image-heavy G2 quick installation guide may not yield searchable text; the English user manual is a stronger retrieval source.
