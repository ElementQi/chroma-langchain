# chroma-langchain

## Intro

This repo is based on [brandonstarxel/chunking_evaluation](https://github.com/brandonstarxel/chunking_evaluation), and all classes are implement from [TextSplitter](https://python.langchain.com/v0.2/api_reference/text_splitters/base/langchain_text_splitters.base.TextSplitter.html#).

## Install

Just clone this repo and in the root directory, run code:

```python
pip install -e .
```

## Usage

If you want to use your own LLM, try to modify `get_langchain_openai_embedding` in `src/chroma_langchain/utils.py`. Make sure this embedding is an implementation of `langchain_core.embeddings.Embeddings`.

Before using those splitters, make sure you have set up your api well.

```python
import os
os.environ["OPENAI_API_KEY"] = "xxx"
```

The example code written in jupyter notebook could be found in `examples` folder.

## Change Log

[2024/9/24]

Could support langchain embeddings by changing logic:

```python
embeddings = self._embedding_function.embed_documents(batch_sentences)
```

Added one example using langchain embeddings(OpenAI).
