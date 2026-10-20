import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from src.rag import GoodWeRAG

parser = argparse.ArgumentParser()
parser.add_argument("--model", default=None)
parser.add_argument("--k", type=int, default=4)
parser.add_argument("--provider", default=None)
parser.add_argument("--prompt", default="v2")
parser.add_argument("--output", default="evals/sprint4_results.json")
args = parser.parse_args()
rag = GoodWeRAG(model=args.model, provider=args.provider, prompt_version=args.prompt, k=args.k)
cases = json.loads(Path("evals/sprint4_eval_set.json").read_text(encoding="utf-8"))
results = []
for case in cases:
    try:
        result = rag.ask(case["question"])
        results.append({**case, **result, "faithfulness": None, "answer_relevancy": None, "reviewer_notes": "Pendente de avaliação humana ou RAGAS"})
    except Exception as exc:
        results.append({**case, "error": str(exc)})
output = {"timestamp": datetime.now(timezone.utc).isoformat(), "model": args.model, "provider": args.provider, "prompt": args.prompt, "results": results, "note": "Scores não calculados: preencha manualmente conforme rubrica ou execute RAGAS."}
Path(args.output).write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Saved {args.output}")
