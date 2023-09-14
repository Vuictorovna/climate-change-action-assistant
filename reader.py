from langchain.document_loaders import PyPDFDirectoryLoader

def pdf_doc_loader(pdfs):
    """
    Load PDF documents from a given directory.

    Parameters:
    - pdfs (str): The directory path where the PDF files are located.

    Returns:
    - list: A list of loaded PDF documents.
    """
    loader = PyPDFDirectoryLoader(pdfs)
    docs = loader.load()
    return docs
