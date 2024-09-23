# chroma-langchain

## Intro

This repo is based on [brandonstarxel/chunking_evaluation](https://github.com/brandonstarxel/chunking_evaluation), and all classes are implement from [TokenTextSplitter](https://python.langchain.com/v0.2/api_reference/text_splitters/base/langchain_text_splitters.base.TokenTextSplitter.html#).

## Install

Just clone this repo and in the root directory, run code:

```python
pip install -e .
```

## Usage

If you want to use your own LLM, try to modify `get_custom_embedding_function` in `src/chroma_langchain/utils.py`.

Before using those splitters, make sure you have set up your api well.

```python
import os
os.environ["OPENAI_API_KEY"] = "xxx"
```

The example code written in jupyter notebook could be found in `examples` folder. 