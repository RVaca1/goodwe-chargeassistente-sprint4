import hashlib
from pathlib import Path
from langchain_chroma import Chroma
from .embeddings import build_embeddings
from .loader import load_documents
from .chunking import split_documents

def open_store(persist_directory="data/chroma_db"):
    return Chroma(collection_name="goodwe_sprint4", embedding_function=build_embeddings(), persist_directory=str(persist_directory))

def index_documents(knowledge_base="data/knowledge_base", persist_directory="data/chroma_db", chunk_size=800, chunk_overlap=120):
    documents = load_documents(knowledge_base)
    if not documents:
        raise ValueError("Base vazia: adicione PDFs ou arquivos .md/.txt verificados em data/knowledge_base/.")
    chunks = split_documents(documents, chunk_size, chunk_overlap)
    store = open_store(persist_directory)
    ids = [hashlib.sha256((str(c.metadata.get("source"))+str(c.metadata.get("page"))+str(c.metadata.get("start_index"))+c.page_content).encode()).hexdigest() for c in chunks]
    store.add_documents(chunks, ids=ids)
    return {"documents": len(documents), "chunks": len(chunks), "database": str(persist_directory)}
