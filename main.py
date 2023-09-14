import sys

print("Python sys.path:", sys.path)

import os
from dataclasses import dataclass

from dotenv import load_dotenv

from core import run_llm

load_dotenv()


@dataclass
class PineconeCredentials:
    api_key: str
    index_name: str
    environment_region: str


if __name__ == "__main__":
    pinecone_env = PineconeCredentials(
        api_key=os.environ.get("PINECONE_API_KEY"),
        index_name=os.environ.get("PINECONE_INDEX_NAME"),
        environment_region=os.environ.get("PINECONE_ENVIRONMENT_REGION"),
    )
    run_llm(pinecone_env)
