import os
from dataclasses import dataclass

if os.path.exists("env.py"):
    import env


@dataclass
class PineconeCredentials:
    """
    Data class to store Pinecone credentials.

    Attributes:
        api_key (str): API key for Pinecone service.
        index_name (str): Name of the index used in Pinecone.
        environment_region (str): Environment region for the Pinecone service.
    """
    api_key: str
    index_name: str
    environment_region: str


def init_pinecone():
    """
    Initialize and return Pinecone credentials.

    This function reads API key, index name, and environment region from environment variables,
    checks if they are not None, and returns them wrapped in a PineconeCredentials object.

    Returns:
        PineconeCredentials: Object containing the Pinecone credentials.

    Raises:
        ValueError: If any of the environment variables for Pinecone credentials are not set.
    """
    api_key = os.environ.get("PINECONE_API_KEY")
    index_name = os.environ.get("PINECONE_INDEX_NAME")
    environment = os.environ.get("PINECONE_ENVIRONMENT_REGION")

    if api_key is None:
        msg = "PINECONE_API_KEY environment variable is not set."
        raise ValueError(msg)

    if index_name is None:
        msg = "PINECONE_INDEX_NAME environment variable is not set."
        raise ValueError(msg)

    if environment is None:
        msg = "PINECONE_ENVIRONMENT_REGION environment variable is not set."
        raise ValueError(msg)

    return PineconeCredentials(
        api_key=api_key, index_name=index_name, environment_region=environment
    )
