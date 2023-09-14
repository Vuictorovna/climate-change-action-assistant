import os

import pinecone
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Pinecone


def prepare_llm(query: str, pinecone_env, chat_history=None):
    pinecone.init(
        api_key=pinecone_env.api_key, environment=pinecone_env.environment_region
    )

    if chat_history is None:
        chat_history = []

    embeddings = OpenAIEmbeddings(openai_api_key=os.environ.get("OPENAI_API_KEY"))

    doc_search = Pinecone.from_existing_index(
        index_name=pinecone_env.index_name, embedding=embeddings
    )

    chat_model = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=1, verbose=True)

    qa = ConversationalRetrievalChain.from_llm(
        chain_type="stuff", llm=chat_model, retriever=doc_search.as_retriever()
    )

    return qa({"question": query, "chat_history": chat_history})
