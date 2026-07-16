import streamlit as st
from src.chat import ask
import time 

st.set_page_config(
    page_title="Solution Service AI",
    page_icon="🤖"
)

st.title("🤖 Solution Service AI")

st.caption(
    "Asistente inteligente basado en IA para consultar documentación corporativa."
)
with st.sidebar:

    st.header("🤖 Solution Service AI")

    st.divider()

    st.subheader("Conversación")

    if st.button("🗑 Limpiar historial"):

        st.session_state.messages = []

        st.rerun()

    st.divider()

    st.subheader("Tecnologías")

    st.markdown("""
    - LangChain
    - Google Gemini
    - FAISS
    - Hugging Face
    - Streamlit
    """)

    st.divider()

    st.caption("Versión 1.0")

# Crear historial la primera vez
if "messages" not in st.session_state:
    st.session_state.messages = []
# Pantalla de bienvenida
if len(st.session_state.messages) == 0:

    st.markdown("## 👋 ¡Bienvenido!")

    st.write(
        "Soy **Solution Service AI**, un asistente inteligente "
        "capaz de responder preguntas utilizando únicamente la "
        "documentación interna de la empresa."
    )

    st.markdown("### 💡 Puedes preguntarme:")

    st.markdown("""
    - 📅 ¿Cuántos días de vacaciones tengo?
    - 💰 ¿Cómo solicito un reembolso?
    - 🔐 ¿Cómo recupero mi contraseña?
    - 💻 ¿Puedo trabajar desde mi casa?
    - 🏥 ¿Tengo cobertura médica?
    """)

# Mostrar todo el historial
for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.write(message["content"])

        if (
            message["role"] == "assistant"
            and "sources" in message
        ):

            with st.expander("📄 Fuentes utilizadas"):

                for source in message["sources"]:
                    st.write(f"• {source}")


# Esperar una nueva pregunta
question = st.chat_input("Escribe tu pregunta...")

# Si el usuario escribió algo
if question:

# Mostrar mensaje del usuario
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.write(question)

   
    try:
        
        start_time = time.time()
        with st.spinner("🤖 Buscando información..."):
            answer, sources = ask(question)
            response_time = time.time() - start_time
# Guardar respuesta del asistente
        st.session_state.messages.append({
            "role": "assistant",
            "content": answer,
            "sources": sources
        })

# Mostrar respuesta
        with st.chat_message("assistant"):

                    st.write(answer)

                    st.caption(
                        f"⏱ Tiempo de respuesta: {response_time:.2f} segundos"
                    )

                    with st.expander("📄 Fuentes utilizadas"):

                        for source in sources:
                            st.write(f"• {source}")
    except Exception as e:

        st.error(
        "⚠ No fue posible obtener una respuesta.\n\n"
        "Verifica tu conexión o la cuota disponible de Gemini."
        )

        #st.exception(e)

        st.stop()
        

      