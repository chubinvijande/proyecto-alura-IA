from src.config import DATA_PATH
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_community.document_loaders.csv_loader import CSVLoader




def load_documents():
    """
    Carga todos los documentos PDF y CSV de la carpeta data.
    """

    # Cargar PDFs
    pdf_loader = PyPDFDirectoryLoader(DATA_PATH)
    pdf_documents = pdf_loader.load()

    # Cargar CSV
    csv_documents = []

    for csv_file in DATA_PATH.rglob("*.csv"):
        loader = CSVLoader(file_path=str(csv_file))
        csv_documents.extend(loader.load())

    # Unir documentos
    documents = pdf_documents + csv_documents

  
    return documents

 
if __name__ == "__main__":
 
    documents = load_documents()

    print(f"📄 PDFs cargados: {len([d for d in documents if d.metadata['source'].endswith('.pdf')])}")
    print(f"📚 Total de documentos: {len(documents)}")