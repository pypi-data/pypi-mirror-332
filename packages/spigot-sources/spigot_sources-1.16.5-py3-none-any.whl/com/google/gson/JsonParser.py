"""
Python module generated from Java source file com.google.gson.JsonParser

Java source file obtained from artifact gson version 2.8.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson import *
from com.google.gson.internal import Streams
from com.google.gson.stream import JsonReader
from com.google.gson.stream import JsonToken
from com.google.gson.stream import MalformedJsonException
from java.io import IOException
from java.io import Reader
from java.io import StringReader
from typing import Any, Callable, Iterable, Tuple


class JsonParser:
    """
    A parser to parse Json into a parse tree of JsonElements

    Author(s)
    - Joel Leitch

    Since
    - 1.3
    """

    def parse(self, json: str) -> "JsonElement":
        """
        Parses the specified JSON string into a parse tree

        Arguments
        - json: JSON text

        Returns
        - a parse tree of JsonElements corresponding to the specified JSON

        Raises
        - JsonParseException: if the specified text is not valid JSON

        Since
        - 1.3
        """
        ...


    def parse(self, json: "Reader") -> "JsonElement":
        """
        Parses the specified JSON string into a parse tree

        Arguments
        - json: JSON text

        Returns
        - a parse tree of JsonElements corresponding to the specified JSON

        Raises
        - JsonParseException: if the specified text is not valid JSON

        Since
        - 1.3
        """
        ...


    def parse(self, json: "JsonReader") -> "JsonElement":
        """
        Returns the next value from the JSON stream as a parse tree.

        Raises
        - JsonParseException: if there is an IOException or if the specified
            text is not valid JSON

        Since
        - 1.6
        """
        ...
