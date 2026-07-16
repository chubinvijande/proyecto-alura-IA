import os

from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI

from src.config import LLM_MODEL

def load_llm():

    load_dotenv()

    api_key = os.getenv("GOOGLE_API_KEY")

    llm = ChatGoogleGenerativeAI(
    model=LLM_MODEL,
    google_api_key=api_key,
    temperature=0
    )
    return llm

if __name__ == "__main__":

    llm = load_llm()

    print("✅ LLM cargado correctamente.")