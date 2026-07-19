from src.retriever import load_retriever
from src.llm import load_llm
from src.prompts import build_prompt
from src.memory import ConversationMemory
from src.sources import get_sources

memory = ConversationMemory()

retriever = None
llm = None


def initialize():

    global retriever
    global llm

    if retriever is None:
        retriever = load_retriever()

    if llm is None:
        llm = load_llm()


def ask(question):

    initialize()

    documents = retriever.invoke(question)

    sources = get_sources(documents)

    context = "\n\n".join(
        doc.page_content for doc in documents
    )

    history = memory.get_history_text()

    prompt = build_prompt(
        history,
        context,
        question
    )

    response = llm.invoke(prompt)

    answer = response.content

    memory.add(question, answer)

    return answer, sorted(sources)


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

        answer, sources = ask(question)

        print(answer)

        print("\nFuentes:")

        for source in sources:
            print(source)