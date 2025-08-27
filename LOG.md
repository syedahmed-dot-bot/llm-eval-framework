## 2025-08-25 — Step 0.1: Windows scaffold
- Switched to Windows-native commands (PowerShell/CMD) instead of bash.
- Created directories: src/{data/tasks,prompting,models,metrics,pipeline,utils}, scripts, tests, docs, examples, runs, .github/workflows
- Added placeholder files (.keep/.gitkeep, README.md, LOG.md, .gitignore, .env.example, pyproject.toml, LICENSE, tests/test_smoke.py)
- Fixed typos: `src/metrics` (not `mmetrics`), `src/pipeline` (not `pipline`)

## 2025-08-26 — Step 1B: GitHub setup
- Initialized Git repository locally.
- Created new public repo on GitHub: `llm-eval-framework`.
- Linked local repo → GitHub remote (`origin`).
- First push to `main` branch with scaffold commit.
- Created `dev` branch for active development.

## 2025-08-26 — Step 1D: Prompt templates
- Added `src/prompting/templates.md` with fixed QA and Summarization templates.
- Purpose: enforce consistent prompting across models for fair, apples-to-apples evaluation.
- Note: normalization rules documented for Exact Match.

## 2025-08-26 — Step 1E: Add Summarization tiny dataset
- Created `src/data/tasks/summarization_tiny.jsonl` with 5 factual paragraphs and 1-sentence gold summaries.
- Purpose: exercise ROUGE-L and semantic similarity under a different prompt template than QA.
- Rationale: verifies the pipeline can swap task templates and still score consistently.

## 2025-08-26 — Step 1F: Smoke check script
- Added `scripts/smoke_check.py` to load JSONL datasets and render prompts using fixed templates.
- Purpose: validate schema and prompt rendering before any model/metrics code.
- Outcome: QA and Summarization examples render correctly; ready to integrate free HF model next.