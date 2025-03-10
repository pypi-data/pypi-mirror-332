"""
Python module generated from Java source file com.google.gson.internal.JsonReaderInternalAccess

Java source file obtained from artifact gson version 2.8.9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson.internal import *
from com.google.gson.stream import JsonReader
from java.io import IOException
from typing import Any, Callable, Iterable, Tuple


class JsonReaderInternalAccess:
    """
    Internal-only APIs of JsonReader available only to other classes in Gson.
    """

    INSTANCE = None


    def promoteNameToValue(self, reader: "JsonReader") -> None:
        """
        Changes the type of the current property name token to a string value.
        """
        ...
