from pathlib import Path

from src.config import TOP_K
from src.vector_store_loader import load_vector_store



question = "¿Cuántos días de vacaciones corresponden a un empleado de Solution Service AI?"

vector_store = load_vector_store()

results = vector_store.similarity_search_with_score(
    question,
    k=TOP_K
)

for i, (doc, score) in enumerate(results, start=1):

    print(f"Resultado {i}")

    print(f"Fuente: {Path(doc.metadata['source']).name}")

    print(f"Score: {score:.4f}")

    print()

    print(doc.page_content)