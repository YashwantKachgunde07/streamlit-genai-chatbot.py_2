from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq

# Load environment variables from .env
load_dotenv()

# Streamlit page setup
st.set_page_config(
    page_title="Generative AI Chatbot",
    page_icon="🤖",
    layout="centered",
)

st.title("🤖 Generative AI Chatbot")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]): # with: context manager everything belongs to that chat bubble.
        st.markdown(message["content"])

# Initialize LLM
llm = ChatGroq(
    model="llama-3.3-70b-versatile", # we can use different models from groq
    temperature=0.0, # controls randomness
)

# Chat input
user_prompt = st.chat_input("Ask a question...")

if user_prompt: # runs only if user entered something

    # Display user message
    with st.chat_message("user"):
        st.markdown(user_prompt)

    # Save user message
    st.session_state.chat_history.append(
        {"role": "user", "content": user_prompt}
    )

    # Generate response
    response = llm.invoke(
        [
            {"role": "system", "content": "You are a helpful assistant"},
            *st.session_state.chat_history,
        ]
    )

    assistant_response = response.content

    # Display assistant response
    with st.chat_message("assistant"):
        st.markdown(assistant_response)

    # Save assistant response
    st.session_state.chat_history.append(
        {"role": "assistant", "content": assistant_response}
    )