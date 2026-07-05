import os 
from config import VECTOR_STORE_PATH, EMBEDDING_MODEL
from dotenv import load_dotenv

from split_documents import split_documents

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings



def create_vector_store():

    chunks = split_documents()

    embeddings = HuggingFaceEmbeddings(
    model_name=EMBEDDING_MODEL
)

    vector_store = FAISS.from_documents(
        chunks,
        embeddings
    )

    VECTOR_STORE_PATH.mkdir(exist_ok=True)

    vector_store.save_local(str(VECTOR_STORE_PATH))

    print("✅ Vector Store creado correctamente.")


    #preguntas locales:
    question = "¿Cuántos días de vacaciones tengo?"

    documents = retriever.invoke(question)

    print()

    print("RESULTADOS ENCONTRADOS")

    print("=" * 80)

    for i, doc in enumerate(documents, start=1):

     print(f"\nDocumento {i}")

     print("-" * 40)

     print(doc.page_content)


if __name__ == "__main__":
    create_vector_store()