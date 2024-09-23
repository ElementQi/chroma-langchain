import os
from chromadb.utils import embedding_functions


def get_custom_embedding_function():
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if openai_api_key is None:
        raise ValueError(
            "You need to set an embedding function or set an OPENAI_API_KEY environment variable."
        )
    embedding_function = embedding_functions.OpenAIEmbeddingFunction(
        api_base="https://one-api.s.metames.cn:38443/v1",
        api_key=os.getenv("OPENAI_API_KEY"),
        model_name="bce-embedding-base_v1",
    )
    return embedding_function
