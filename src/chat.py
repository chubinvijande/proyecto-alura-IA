from retriever import load_retriever
from llm import load_llm
from pathlib import Path
from prompts import build_prompt
from memory import ConversationMemory

memory = ConversationMemory()
retriever = load_retriever()
llm = load_llm()

def ask(question):

    documents = retriever.invoke(question)

    sources = {
    Path(doc.metadata["source"]).name
    for doc in documents
    }

    print("\nFuentes consultadas:")

    for source in sorted(sources):
        print(f"• {source}")

    context = "\n\n".join(
        doc.page_content for doc in documents
        )
    
    history = memory.get_history_text()

    prompt = build_prompt(
        history,
        context,
        question)
    
    response = llm.invoke(prompt)

    answer = response.content

    memory.add(question, answer)

    return answer
    

if __name__ == "__main__":

    print("=" * 60)
    print("🤖 Solution Service AI")
    print("Escribe 'salir' para finalizar.")
    print("=" * 60)

    while True:

        question = input("\n👤 Tú: ")

        if question.lower() == "salir":
            print("\n👋 ¡Hasta luego!")
            break

        answer = ask(question)

        print(f"\n🤖 Asistente:\n{answer}")