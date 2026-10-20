from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_documents(documents, chunk_size=800, chunk_overlap=120):
    return RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap, add_start_index=True).split_documents(documents)
