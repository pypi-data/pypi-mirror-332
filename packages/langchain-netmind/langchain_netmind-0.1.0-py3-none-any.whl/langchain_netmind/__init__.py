from importlib import metadata

from langchain_netmind.chat_models import ChatNetmind
from langchain_netmind.embeddings import NetmindEmbeddings


try:
    __version__ = metadata.version(__package__)
except metadata.PackageNotFoundError:
    # Case where package metadata is not available.
    __version__ = ""
del metadata  # optional, avoids polluting the results of dir(__package__)

__all__ = [
    "ChatNetmind",
    "NetmindEmbeddings",
    "__version__",
]
