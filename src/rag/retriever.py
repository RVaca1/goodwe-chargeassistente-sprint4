from .vector_store import open_store

def build_retriever(k=8, persist_directory="data/chroma_db"):
    return open_store(persist_directory).as_retriever(search_kwargs={"k": k})
