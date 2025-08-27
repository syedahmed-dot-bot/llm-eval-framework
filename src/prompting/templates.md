# Prompt Templates (v0)

## QA (factoid)
**Prompt Template**


**Notes**
- `{question}` will be replaced by the dataset item’s `input` value.
- The model is nudged to give short, direct answers (so metrics like Exact Match aren’t penalized by rambling).
- Works for factual questions (capitals, names, numbers, acronyms).

**Normalization Rules**
- Ignore case when scoring (e.g., “paris” vs “Paris”).
- Strip trailing punctuation (e.g., “Paris.” vs “Paris”).

---

## Summarization (1-sentence)
**Prompt Template**


**Notes**
- `{text}` will be replaced by the dataset item’s `input` value.
- Forces a 1-sentence summary so output length is controlled across models.
- Supports metrics like ROUGE-L and SBERT cosine.

**Normalization Rules**
- Compare against reference summaries without case sensitivity.
- Allow slight paraphrasing (semantic similarity is more important than Exact Match here).

