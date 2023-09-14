import os

import streamlit as st
from streamlit_chat import message

if os.path.exists("env.py"):
    import env

from core import prepare_llm
from utils import init_pinecone


pinecone_env = init_pinecone()

st.write("# Welcome to The Climate Change Chat Assistant!")
st.write("Do you have a question for me, today? Enter 'q' to quit.")

chat_history = []

if "user_input" not in st.session_state:
    st.session_state.user_input = []

if "bot_response" not in st.session_state:
    st.session_state.bot_response = []

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("Question", placeholder="Enter your question here...")

if st.button("Submit"):
    if user_input.lower() == "q":
        st.write("Bot: Goodbye! See you next time!.")
        st.stop()  # Stop the Streamlit app

    if not user_input.strip():
        st.warning("Please enter a valid question.")
    else:
        response = prepare_llm(user_input, pinecone_env, chat_history)
        print("RESPONSE:", response)
        st.session_state.chat_history.append((user_input, response["answer"]))
        st.session_state.bot_response.append(response["answer"])
        print("BOT:", st.session_state.bot_response)
        st.session_state.user_input.append(user_input)

st.write("Chat History:")
if st.session_state.chat_history:
    for prompt, response in zip(
        st.session_state.user_input, st.session_state.bot_response
    ):
        message(prompt, is_user=True)
        message(response)
