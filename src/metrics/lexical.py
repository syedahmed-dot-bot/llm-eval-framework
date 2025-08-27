#normalize text by lowercasing, trimming, and removing punctuation

import re

_PUNT_RE = re.compile(r'[^\w\s]') #remove punctuations

def _normalize(text: str) -> str:

    s = s.strip(text).lower()
    s = s.rstrip(" .,!?;:")
    
    return s

#exact match metric

def exact_match(pred=str, ref = str) -> float:
    return 1.0 if _normalize(pred) == _normalize(ref) else 0.0

#ROUGE-L metric

from rouge_score import rouge_scorer

_scorer = rouge_scorer.RougeScorer(['rougeL'], use_stemmer = True)

def rouge_l(pred: str, ref: str) -> float:

    pred_n = _normalize(pred)
    ref_n = _normalize(ref)
    scores = _scorer.score(pred_n, ref_n)
    return float(scores['rougeL'].fmeasure)

