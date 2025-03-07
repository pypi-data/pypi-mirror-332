# langchain-netmind

This package contains the LangChain integration with Netmind

## Installation

```bash
pip install -U langchain-netmind
```

And you should configure credentials by setting the following environment variables:

* TODO: fill this out

## Chat Models

`ChatNetmind` class exposes chat models from Netmind.

```python
from langchain_netmind import ChatNetmind

llm = ChatNetmind()
llm.invoke("Sing a ballad of LangChain.")
```

## Embeddings

`NetmindEmbeddings` class exposes embeddings from Netmind.

```python
from langchain_netmind import NetmindEmbeddings

embeddings = NetmindEmbeddings()
embeddings.embed_query("What is the meaning of life?")
```
