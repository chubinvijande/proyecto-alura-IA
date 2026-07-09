from config import VECTOR_STORE_PATH, EMBEDDING_MODEL,    TOP_K
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from vector_store_loader import load_vector_store


def load_retriever():

    vector_store = load_vector_store()

    return vector_store.as_retriever(
        search_kwargs={"k": TOP_K}
    )
    
    
    

if __name__ == "__main__":

    retriever = load_retriever()

    print("✅ Retriever cargado correctamente.")

    question = "¿Cuántos días de vacaciones tengo?"

    documents = retriever.invoke(question)

    print("RESULTADOS ENCONTRADOS")

    print("=" * 80)

    for i, doc in enumerate(documents, start=1):    

        print(f"\nDocumento {i}")

        print("-" * 40)

        print(doc.page_content)