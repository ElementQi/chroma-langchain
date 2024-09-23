from setuptools import setup, find_packages

setup(
    name="chroma_langchain",
    version="0.1.0",
    description="A package for integrating Chroma with LangChain.",
    author="Mengqi Li",
    author_email="limq01@foxmail.com",
    url="https://github.com/ElementQi/chroma-langchain",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "langchain",
        "chunking_evaluation @ git+https://github.com/ElementQi/chroma_chunking_evaluation.git",
    ],
    python_requires=">=3.7",  # Specify Python version requirements
)
