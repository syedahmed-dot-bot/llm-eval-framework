import json
from typing import Dict, List
from pathlib import Path

TEMPLATES: Dict[str, str] = {
    "qa": "Answer consisely:\n {question} \nAnswer:",
    "summarization": "Summarize objectively in one line:\n {text}:\n Summary:"
}

#minimal json loader

def read_jsonl(path: str) -> List[Dict]:
    rows = []
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            rows.append(json.loads(line))
    
    return rows

#prompt builder per task schema

def build_prompt(item: dict) -> str:
    task = item['task']
    if task == 'qa':    
        return TEMPLATES['qa'].format(question=item['input'])
    elif task == 'summarization':
        return TEMPLATES['summarization'].format(text = item['input'])
    else:
        raise ValueError(f'Unknown task type: {task}')

#main smoke check function    

def main():
    root = Path(__file__).resolve().parents[1]  # repo root
    qa_path = root / "src" / "data" / "tasks" / "qa_tiny.jsonl"
    sum_path = root / "src" / "data" / "tasks" / "summarization_tiny.jsonl"

    for name, path in [("QA", qa_path), ("Summarization", sum_path)]:
        print(f"\n=== {name} dataset: {path} ===")
        items = read_jsonl(str(path))
        # schema sanity
        for i, it in enumerate(items, 1):
            for key in ("id", "task", "input", "reference"):
                assert key in it, f"Missing '{key}' in item: {it}"
            # build prompt
            prompt = build_prompt(it)
            # print only the first 2 examples per dataset
            if i <= 2:
                print("\n--- Example", i, "---")
                print("ID       :", it["id"])
                print("Task     :", it["task"])
                print("Input    :", it["input"])
                print("Reference:", it["reference"])
                print("Prompt   :\n" + prompt)

    print("\nSmoke check OK: datasets load and prompts render.")

    print(exact_match("Paris", "paris"))                 # 1.0
    print(exact_match("The capital is Paris.", "Paris")) # 0.0

    print(round(rouge_l("The capital is Paris.", "Paris"), 3)) # > 0.0 (likely ~0.3–0.5)

    print(round(sbert_cosine("The capital is Paris.", "Paris"), 3)) # high-ish, ~0.7–0.9

if __name__ == "__main__":
    main()