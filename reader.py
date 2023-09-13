# PDF loader/reader

# Import packages
from langchain.document_loaders import PyPDFLoader

# Directory path to downloaded pdfs
pdf_directory = 'pdfs'

# Function to load pdfs
def pdf_doc_loader(pdfs):
   loader = PyPDFLoader(pdfs)
   docs = loader.load()
   return docs
print("Loaded pdfs")

# Function to extract text from pdfs