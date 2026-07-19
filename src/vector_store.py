from src.config import VECTOR_STORE_PATH, EMBEDDING_MODEL

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

_embeddings = None
_vector_store = None


def load_vector_store():
    global _embeddings, _vector_store

    if _vector_store is not None:
        return _vector_store

    if _embeddings is None:
        _embeddings = HuggingFaceEmbeddings(
            model_name=EMBEDDING_MODEL
        )

    _vector_store = FAISS.load_local(
        str(VECTOR_STORE_PATH),
        _embeddings,
        allow_dangerous_deserialization=True
    )

    return _vector_store