"""
Python module generated from Java source file com.google.gson.JsonIOException

Java source file obtained from artifact gson version 2.10.1

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson import *
from typing import Any, Callable, Iterable, Tuple


class JsonIOException(JsonParseException):
    """
    This exception is raised when Gson was unable to read an input stream
    or write to one.

    Author(s)
    - Joel Leitch
    """

    def __init__(self, msg: str):
        ...


    def __init__(self, msg: str, cause: "Throwable"):
        ...


    def __init__(self, cause: "Throwable"):
        """
        Creates exception with the specified cause. Consider using
        .JsonIOException(String, Throwable) instead if you can describe what happened.

        Arguments
        - cause: root exception that caused this exception to be thrown.
        """
        ...
