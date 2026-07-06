class ConversationMemory:

    def __init__(self):

        self.history = []

    def add(self, question, answer):

        self.history.append({

            "question": question,

            "answer": answer

        })

    def get_history(self):

        return self.history
    
    def get_history_text(self):

        history_text = ""

        for conversation in self.history:

            history_text += (
            f"Usuario: {conversation['question']}\n"
            f"Asistente: {conversation['answer']}\n\n"
            )
            return history_text