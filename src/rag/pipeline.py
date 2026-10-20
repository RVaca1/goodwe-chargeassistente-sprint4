import re
from pathlib import Path
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from src.chain.builder import build_llm
from src.guardrails import moderate_input
from .vector_store import open_store
from .prompt_rag import load_rag_prompt

REFUSAL = "Não encontrei essa informação nos documentos disponíveis. Consulte a documentação oficial ou o suporte GoodWe."
INJECTION = re.compile(r"ignore (previous|all|suas|as).*instructions|system prompt|developer message|ignore.*instruções|reveal.*prompt", re.I)

class GoodWeRAG:
    def __init__(self, model=None, provider=None, prompt_version="v3", k=8, persist_directory="data/chroma_db", score_threshold=0.55):
        self.store = open_store(persist_directory)
        self.k = k
        self.score_threshold = score_threshold
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", load_rag_prompt(prompt_version)),
            ("human", "<retrieved_context>\n{context}\n</retrieved_context>\n<user_question>{question}</user_question>"),
        ])
        self.chain = self.prompt | build_llm(model, provider) | StrOutputParser()

    def ask(self, question):
        decision = moderate_input(question)
        if not decision.allowed:
            return {"answer": decision.response, "sources": [], "status": decision.category}
        # Chroma cosine distances vary by metric; use relevance scores with a configurable threshold.
        matches = self.store.similarity_search_with_relevance_scores(question, k=self.k)
        usable = [(doc, score) for doc, score in matches if score >= self.score_threshold and not INJECTION.search(doc.page_content)]
        if not usable:
            return {"answer": REFUSAL, "sources": [], "status": "insufficient_context"}
        context_parts, sources = [], []
        for i, (doc, score) in enumerate(usable, 1):
            source = Path(doc.metadata.get("source", "unknown")).name
            page = doc.metadata.get("page")
            label = f"{source}, página {page + 1}" if isinstance(page, int) else source
            context_parts.append(f"[Trecho {i}; fonte: {label}]\n{doc.page_content}")
            sources.append({"file": source, "page": page + 1 if isinstance(page, int) else None, "score": round(float(score), 3), "excerpt": doc.page_content[:400]})
        answer = self.chain.invoke({"context": "\n\n".join(context_parts), "question": question})
        return {"answer": answer, "sources": sources, "status": "answered"}
