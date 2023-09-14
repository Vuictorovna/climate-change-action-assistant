from langchain.document_loaders import PyPDFDirectoryLoader


# Function to load pdfs
def pdf_doc_loader(pdfs):
   loader = PyPDFDirectoryLoader(pdfs)
   docs = loader.load()
   return docs

