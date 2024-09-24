import os
from langchain_openai import OpenAIEmbeddings


def get_langchain_openai_embedding():
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if openai_api_key is None:
        raise ValueError(
            "You need to set an embedding function or set an OPENAI_API_KEY environment variable."
        )
    embed = OpenAIEmbeddings(
        base_url="https://one-api.s.metames.cn:38443/v1",
        api_key=os.getenv("OPENAI_API_KEY"),
        model="bce-embedding-base_v1",
    )
    return embed
