"""
Python module generated from Java source file com.google.gson.stream.MalformedJsonException

Java source file obtained from artifact gson version 2.8.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson.stream import *
from java.io import IOException
from typing import Any, Callable, Iterable, Tuple


class MalformedJsonException(IOException):
    """
    Thrown when a reader encounters malformed JSON. Some syntax errors can be
    ignored by calling JsonReader.setLenient(boolean).
    """

    def __init__(self, msg: str):
        ...


    def __init__(self, msg: str, throwable: "Throwable"):
        ...


    def __init__(self, throwable: "Throwable"):
        ...
