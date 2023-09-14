import os

import pinecone
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Pinecone


def prepare_llm(query: str, pinecone_env, chat_history=None):
    """
    Prepare a Language Learning Model (LLM) for conversational retrieval with Pinecone.

    Parameters:
    - query (str): The user's query.
    - pinecone_env: Pinecone environment credentials.
    - chat_history (list, optional): A list of chat history. Default is an empty list.

    Returns:
    - A dictionary containing the answer from the model.
    """
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
