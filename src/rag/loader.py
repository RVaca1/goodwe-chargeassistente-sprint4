from pathlib import Path
from langchain_community.document_loaders import PyMuPDFLoader, TextLoader

def load_documents(directory):
    documents = []
    for path in sorted(Path(directory).rglob("*")):
        if path.name.lower() == "readme.md" or not path.is_file() or path.suffix.lower() not in {".pdf", ".md", ".txt"}:
            continue
        loader = PyMuPDFLoader(str(path)) if path.suffix.lower() == ".pdf" else TextLoader(str(path), encoding="utf-8")
        for document in loader.load():
            document.metadata["source"] = str(path)
            documents.append(document)
    return documents
