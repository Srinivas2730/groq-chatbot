# app.py
import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Get API key from environment
api_key = os.getenv("GROQ_API_KEY")

# Initialize Groq client
client = Groq(api_key=api_key)

# Streamlit page settings
st.set_page_config(page_title="Groq Chatbot", layout="centered")
st.title("🤖 Chat with Groq LLaMA3")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User input
prompt = st.chat_input("Ask me anything...")

# Display chat history
for role, message in st.session_state.chat_history:
    with st.chat_message(role):
        st.markdown(message)

# If user enters a prompt
if prompt:
    # Show user message
    st.session_state.chat_history.append(("user", prompt))
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate response using Groq LLaMA3
    with st.chat_message("assistant"):
        response_area = st.empty()
        full_response = ""

        with st.spinner("Thinking..."):
            stream = client.chat.completions.create(
                model="llama3-70b-8192",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."}
                ] + [{"role": role, "content": msg} for role, msg in st.session_state.chat_history],
                stream=True,
            )

            for chunk in stream:
                content = chunk.choices[0].delta.content or ""
                full_response += content
                response_area.markdown(full_response)

        st.session_state.chat_history.append(("assistant", full_response))
