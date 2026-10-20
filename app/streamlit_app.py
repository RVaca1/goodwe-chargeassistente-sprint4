import os
import streamlit as st
from src.rag import GoodWeRAG

st.set_page_config(page_title="GoodWe ChargeAssistente — Sprint 04", page_icon="⚡")
st.title("⚡ GoodWe ChargeAssistente")
st.caption("Respostas baseadas em documentos, com fontes verificáveis")
try:
    for key in ("LLM_PROVIDER", "NVIDIA_API_KEY", "NVIDIA_MODEL", "OPENROUTER_API_KEY", "OPENROUTER_MODEL", "OLLAMA_BASE_URL", "EMBEDDING_MODEL"):
        if key in st.secrets:
            os.environ[key] = str(st.secrets[key])
except FileNotFoundError:
    pass

@st.cache_resource(show_spinner="Conectando à base documental...")
def rag():
    return GoodWeRAG(k=int(os.getenv("RAG_TOP_K", "8")), score_threshold=float(os.getenv("RAG_MIN_RELEVANCE", "0.55")))

if "rag_messages" not in st.session_state:
    st.session_state.rag_messages = []
for msg in st.session_state.rag_messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if msg.get("sources"):
            with st.expander("Fontes consultadas"):
                for source in msg["sources"]:
                    st.markdown(f"**{source['file']}**" + (f" — página {source['page']}" if source['page'] else ""))
                    st.caption(source["excerpt"])

if question := st.chat_input("Pergunte sobre recarga e documentos GoodWe..."):
    st.session_state.rag_messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)
    with st.chat_message("assistant"):
        try:
            result = rag().ask(question)
        except Exception as exc:
            st.error("Não foi possível consultar o RAG. Verifique o Ollama, o modelo de embeddings e a indexação.")
            st.exception(exc)
        else:
            st.markdown(result["answer"])
            if result["sources"]:
                with st.expander("Fontes consultadas", expanded=True):
                    for source in result["sources"]:
                        st.markdown(f"**{source['file']}**" + (f" — página {source['page']}" if source['page'] else ""))
                        st.caption(source["excerpt"])
            st.session_state.rag_messages.append({"role": "assistant", "content": result["answer"], "sources": result["sources"]})
