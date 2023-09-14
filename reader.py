import os

from langchain.document_loaders import PyPDFLoader


# Function to load pdfs
def pdf_doc_loader(pdfs):
    loader = PyPDFLoader(pdfs)
    docs = loader.load()
    return docs


pdf_directory = (
    "C:\\Users\\VolhaSakharevich\\Documents\\Dev\\climate-change-action-assistant\\pdfs"
)

for filename in os.listdir(pdf_directory):
    if filename.endswith(".pdf"):
        pdf_file_path = os.path.join(pdf_directory, filename)
