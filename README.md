# Climate Change Action Assistant

## Objective

This project aims to develop an application that leverages the power of Large Language Models (LLM) to summarize and answer questions related to current Climate Change legislation and initiatives. The project ingests PDF documents from Climate Change Consortium, processes them into semantic text embeddings using Langchain, and stores them in Pinecone for efficient retrieval. Users can interact with the system to get summarized and contextual information based on their queries.

## Features

- **PDF Document Handling**: Efficiently loads and processes PDFs.
- **Semantic Text Embeddings**: Transforms processed text into semantic embeddings using OpenAI's language models.
- **User Interaction**: Streamlit interface for querying the database and receiving information.

## Technologies Used

### Langchain
A versatile toolkit that provides capabilities for data fetching, transformation, and semantic text embeddings.

- [Langchain Documentation](https://python.langchain.com/docs/)
- [Document Loaders](https://python.langchain.com/docs/modules/data_connection/document_loaders/)
- [Text Embeddings](https://python.langchain.com/docs/integrations/text_embedding/openai)

### Pinecone
A vector database for efficient storage and retrieval of text embeddings.

- [Pinecone Documentation](https://docs.pinecone.io/docs/quickstart)

### Streamlit
An open-source Python library that makes it easy to create custom web apps for machine learning and data science.

- [Streamlit Website](https://www.streamlit.io/)

### OpenAI
Utilized for generating semantic text embeddings.

- [OpenAI API](https://openai.com/)

## Setup

### Prerequisites

1. Python 3.x
2. Pip

### Installation

1. Clone the repository.

    ```bash
    git clone https://github.com/Vuictorovna/climate-change-action-assistant.git
    ```

2. Navigate into the directory.

    ```bash
    cd climate-change-action-assistant
    pip install -r requirements.txt
    ```

3. Setting Up a Virtual Environment.

    To isolate the project dependencies, it's recommended to create a virtual environment. 
    Run the following commands in your terminal to create and activate a virtual environment:

    **On macOS and Linux:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

    **On Windows:**

    ```bash
    python -m venv venv
    Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
    .\venv\Scripts\activate
    ```

4. Install the required packages.

    ```bash
    pip install -r requirements.txt
    ```

### API Keys

1. You'll need an API key from OpenAI and Pinecone.
2. Create a file named `env.py` in the project root directory.
3. Store your API keys in `env.py` as environment variables. For example:

    ```python
    os.environ.setdefault("OPENAI_API_KEY", "YOUR_API_KEY")
    os.environ.setdefault("PINECONE_API_KEY", "YOUR_API_KEY")
    os.environ.setdefault("PINECONE_INDEX_NAME", "YOUR_INDEX_NAME")
    os.environ.setdefault("PINECONE_ENVIRONMENT_REGION", "YOUR_ENVIRONMENT_REGION")
    ```

## Usage

1. **Load PDFs**

    Run the `reader.py` script to load PDF files.

    ```bash
    python reader.py
    ```

2. **Text Slicing and Storage**

    Execute the `textslicer.py` to process the PDF texts.

    ```bash
    python textslicer.py
    ```

3. **User Interaction**

    ```bash
    streamlit run interface.py
    ```

## Minimal Viable Product (MVP)

1. Instructional welcome message.
2. Query processing from the terminal.
3. Handling of invalid (empty) queries.
4. Exit option from the application.

## Contributors

- Volha Sakharevich [@Vuictorovna](https://github.com/Vuictorovna)
- Tolani Oladimeji [@T-meji](https://github.com/T-meji)
- James Corfe [@jdc338](https://github.com/jdc338)
- Jamie Adieze [@jamieadieze](https://github.com/jamieadieze)
- Zulq Ansari [@ZulqAnsari](https://github.com/ZulqAnsari)


**Good luck and have fun building your Climate Change Action Assistant!**
