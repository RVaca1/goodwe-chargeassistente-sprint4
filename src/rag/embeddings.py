import os
from langchain_ollama import OllamaEmbeddings

def build_embeddings():
    return OllamaEmbeddings(model=os.getenv("EMBEDDING_MODEL", "nomic-embed-text"), base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"))
