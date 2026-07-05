from retriever import load_retriever
from llm import load_llm

retriever = load_retriever()
llm = load_llm()

def ask(question):
    documents = retriever.invoke(question)


    context = "\n\n".join(
    doc.page_content for doc in documents
    )


    prompt = f"""
Eres un asistente de Solution Service AI.

Responde únicamente utilizando la información del contexto.

Si la respuesta no está en el contexto, responde:

"No encontré información sobre ese tema en la documentación."

ontexto:

{context}

Pregunta:  

{question}
"""
    response = llm.invoke(prompt)
    
    return response.content

if __name__ == "__main__":

     question = input("Pregunta: ")

     answer = ask(question)

     print("\nRespuesta:\n")

     print(answer)