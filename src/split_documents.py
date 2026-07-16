from langchain_text_splitters import RecursiveCharacterTextSplitter
from src.load_documents import load_documents
from src.config import CHUNK_SIZE, CHUNK_OVERLAP


def split_documents():

    documents=load_documents()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        separators=[
        "\n\n",
        "\n",
        ". ",
        " ",
        ""
        ]
)

    chunks = text_splitter.split_documents(documents)

    print(f"Documentos originales :{len(documents)}")
    print(f"Chunks generados: {len(chunks)}")
    return chunks

if __name__ == "__main__":
    chunks = split_documents()
    print("\nPrimer chunk:\n")
    print(chunks[0].page_content)



