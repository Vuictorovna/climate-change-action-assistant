import streamlit as st
from streamlit_chat import message
from typing import Dict
import os

if os.path.exists("env.py"):
    import env

import pinecone
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Pinecone


class PineconeCredentials:
    def __init__(self, api_key, environment_region, index_name):
        self.api_key = api_key
        self.environment_region = environment_region
        self.index_name = index_name


# Initialize Pinecone and other components outside the Streamlit app loop
def initialize_pinecone(query: str, pinecone_env, chat_history = None):

    pinecone.init(api_key=pinecone_env.api_key, environment=pinecone_env.environment_region)

    if chat_history is None:
        chat_history = []

    embeddings = OpenAIEmbeddings(openai_api_key=os.environ.get("OPENAI_API_KEY"))

    doc_search = Pinecone.from_existing_index(
        index_name=pinecone_env.index_name, embedding=embeddings
    )

    chat_model = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=1, verbose=True)

    qa = ConversationalRetrievalChain.from_llm(
        chain_type="stuff",
        llm=chat_model, retriever=doc_search.as_retriever()
    )

    return qa({"question": query, "chat_history": chat_history})

st.write("# Welcome to The Climate Change Chat Assistant!")
st.write("Do you have a question for me, today? Enter 'q' to quit.")

chat_history = []

pinecone_env = PineconeCredentials(
    api_key=os.environ.get("PINECONE_API_KEY"),
    environment_region=os.environ.get("PINECONE_ENVIRONMENT_REGION"),
    index_name=os.environ.get("PINECONE_INDEX_NAME")
)

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
        response = initialize_pinecone(user_input, pinecone_env, chat_history)
        print("RESPONSE:", response)
        st.session_state.chat_history.append((user_input, response["answer"]))
        st.session_state.bot_response.append(response["answer"])
        print("BOT:",st.session_state.bot_response)
        st.session_state.user_input.append(user_input)

st.write("Chat History:")
if st.session_state.chat_history:
    for prompt, response in zip(st.session_state.user_input, st.session_state.bot_response):
        message(prompt, is_user=True)
        message(response)
