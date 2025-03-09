"""
Python module generated from Java source file com.google.gson.internal.bind.SerializationDelegatingTypeAdapter

Java source file obtained from artifact gson version 2.10.1

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson import TypeAdapter
from com.google.gson.internal.bind import *
from typing import Any, Callable, Iterable, Tuple


class SerializationDelegatingTypeAdapter(TypeAdapter):
    """
    Type adapter which might delegate serialization to another adapter.
    """

    def getSerializationDelegate(self) -> "TypeAdapter"["T"]:
        """
        Returns the adapter used for serialization, might be `this` or another adapter.
        That other adapter might itself also be a `SerializationDelegatingTypeAdapter`.
        """
        ...
