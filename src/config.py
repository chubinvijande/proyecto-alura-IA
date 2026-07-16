from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "data"

KNOWLEDGE_PATH = BASE_DIR / "knowledge_base"

VECTOR_STORE_PATH = BASE_DIR / "vector_store"

CHUNK_SIZE = 500

CHUNK_OVERLAP = 100

TOP_K = 4

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

LLM_MODEL = "gemini-2.5-flash"