import os 
from src.config import VECTOR_STORE_PATH, EMBEDDING_MODEL
from dotenv import load_dotenv

from src.split_documents import split_documents

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


if __name__ == "__main__":
    create_vector_store()