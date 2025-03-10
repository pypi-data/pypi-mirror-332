"""
Python module generated from Java source file com.google.gson.JsonParseException

Java source file obtained from artifact gson version 2.10

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson import *
from typing import Any, Callable, Iterable, Tuple


class JsonParseException(RuntimeException):
    """
    This exception is raised if there is a serious issue that occurs during parsing of a Json
    string. One of the main usages for this class is for the Gson infrastructure. If the incoming
    Json is bad/malicious, an instance of this exception is raised.
    
    This exception is a RuntimeException because it is exposed to the client. Using a
    RuntimeException avoids bad coding practices on the client side where they catch the
    exception and do nothing. It is often the case that you want to blow up if there is a parsing
    error (i.e. often clients do not know how to recover from a JsonParseException.

    Author(s)
    - Joel Leitch
    """

    def __init__(self, msg: str):
        """
        Creates exception with the specified message. If you are wrapping another exception, consider
        using .JsonParseException(String, Throwable) instead.

        Arguments
        - msg: error message describing a possible cause of this exception.
        """
        ...


    def __init__(self, msg: str, cause: "Throwable"):
        """
        Creates exception with the specified message and cause.

        Arguments
        - msg: error message describing what happened.
        - cause: root exception that caused this exception to be thrown.
        """
        ...


    def __init__(self, cause: "Throwable"):
        """
        Creates exception with the specified cause. Consider using
        .JsonParseException(String, Throwable) instead if you can describe what happened.

        Arguments
        - cause: root exception that caused this exception to be thrown.
        """
        ...
