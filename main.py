import sys

print("Python sys.path:", sys.path)


from dotenv import load_dotenv

from core import run_llm
from utils1 import init_pinecone
load_dotenv()



if __name__ == "__main__":
    pinecone_env = init_pinecone()
    run_llm(pinecone_env)
