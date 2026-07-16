from src.chat import ask

tests = [
    ("¿Cuántos días de vacaciones tengo?", "14 días"),
    ("¿Cómo solicito un reembolso?", "15 días"),
    ("¿Tengo cobertura médica?", "Sí"),
]

for question, expected in tests:
    answer, _ = ask(question)

    if expected.lower() in answer.lower():
        print(f"✅ {question}")
    else:
        print(f"❌ {question}")