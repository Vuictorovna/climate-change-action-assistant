import os

from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Pinecone

from reader import pdf_doc_loader
from utils import PineconeCredentials, init_pinecone

if os.path.exists("env.py"):
    import env

import pinecone


def ingest_docs(pinecone_env: PineconeCredentials) -> None:
    """
    Ingest documents into Pinecone vector index after processing and embedding.

    Parameters:
    - pinecone_env (PineconeCredentials): Pinecone environment credentials.

    Returns:
    - None

    Side Effects:
    - Loads vectors into the Pinecone index.
    """
    pinecone.init(
        api_key=pinecone_env.api_key, environment=pinecone_env.environment_region
    )
    
    pdf_directory = "pdfs"

    raw_docs = pdf_doc_loader(pdf_directory)

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=200, chunk_overlap=50, separators=["\n\n", "\n", " ", ""]
    )

    documents = text_splitter.split_documents(raw_docs)

    embeddings = OpenAIEmbeddings(openai_api_key=os.environ.get("OPENAI_API_KEY"))

    Pinecone.from_documents(
        documents=documents, embedding=embeddings, index_name=pinecone_env.index_name
    )

    print("Successfully loaded vectors in Pinecone.")


if __name__ == "__main__":
    pinecone_env = init_pinecone()

    ingest_docs(pinecone_env)
