import argparse
from src.rag.vector_store import index_documents

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--chunk-size", type=int, default=800)
    parser.add_argument("--overlap", type=int, default=120)
    args = parser.parse_args()
    print(index_documents(chunk_size=args.chunk_size, chunk_overlap=args.overlap))
