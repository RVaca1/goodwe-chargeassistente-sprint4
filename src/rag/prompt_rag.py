from pathlib import Path

def load_rag_prompt(version="v2"):
    return (Path(__file__).resolve().parents[2] / "prompts" / f"rag_prompt_{version}.md").read_text(encoding="utf-8")
