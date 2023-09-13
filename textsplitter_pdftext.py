import os

if os.path.exists(""):
    import env  # This imports the 'env' module if a specific file exists (Will need to specify the correct filename in os.path.exists)

# Import OpenAI as the main Language Model (LLM) service
from langchain.llms import OpenAI

# Import the PyPDFLoader to load PDF documents
from langchain.document_loaders import PyPDFLoader

# Import the RecursiveCharacterTextSplitter for text splitting
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Import OpenAIEmbeddings for document embeddings
from langchain.embeddings import OpenAIEmbeddings

# Import Pinecone for indexing
from langchain.vectorstores import Pinecone

# Import Pinecone Python SDK
import pinecone

# Import Streamlit for building the user interface
import streamlit as st

# Initialise the OpenAI LLM with a specific temperature value
llm = OpenAI(temperature=0.9)

# Define a function to ingest and process documents
def ingest_docs(subject: str, pinecone_env: PineconeCredentials) -> None:
    
    # Initialise Pinecone with the provided API key and environment region
    pinecone.init(api_key=pinecone_env.api_key, environment=pinecone_env.environment_region)

    # Load a PDF document using PyPDFLoader (specify the 'subject' for loading)
    loader = PyPDFLoader(query=subject, load_max_docs=1)
    raw_text = loader.load()

    # Print a message indicating that the document has been loaded
    print(f"Loaded {subject}")

    # Initialize the RecursiveCharacterTextSplitter with specific parameters
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=200,            # Size of each text chunk
        chunk_overlap=50,          # Overlap between adjacent chunks
        separators=["\n\n", "\n", " ", ""]  # Separators used to split text
    )

    # Split the raw text into smaller documents based on the specified parameters
    documents = text_splitter.split_documents(raw_text)

    # Initialise OpenAIEmbeddings for document embeddings
    embeddings = OpenAIEmbeddings(openai_api_key=os.environ.get("OPENAI_API_KEY"))

    # Index the split documents with their embeddings in Pinecone
    Pinecone.from_documents(documents=documents, embedding=embeddings, index_name=pinecone_env.index_name)

    # Print a success message indicating that the vectors have been loaded into Pinecone
    print("Successfully loaded vectors in Pinecone.")

# Main execution block
if __name__ == "__main__":
    # Initialise Pinecone environment settings 
    pinecone_env = init_pinecone()

    # Call the 'ingest_docs' function to process and index documents (empty string for 'subject' in this case)
    ingest_docs("", pinecone_env)
