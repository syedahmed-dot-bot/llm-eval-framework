#SBERT cosine metric for semantic similarity

from sentence_transformers import SentenceTransformer, util

_model = None

def _get_model():
    global _model
    if _model is None:
        _model = SentenceTransformer('all-MiniLM-L6-v2')
    return _model

def sbert_cosine(pred: str, ref: str) -> float:
    m = _get_model()
    emb = m.encode([pred, ref], convert_to_tensor = True, normalize_embbeddings = True)
    sim = util.cos_sim(emb[0], emb[1]).item()
    return float(sim)