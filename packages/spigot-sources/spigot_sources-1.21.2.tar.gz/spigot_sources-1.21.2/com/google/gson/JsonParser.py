"""
Python module generated from Java source file com.google.gson.JsonParser

Java source file obtained from artifact gson version 2.10.1

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
    A parser to parse JSON into a parse tree of JsonElements.

    Author(s)
    - Joel Leitch

    Since
    - 1.3
    """

    def __init__(self):
        """
        Deprecated
        - No need to instantiate this class, use the static methods instead.
        """
        ...


    @staticmethod
    def parseString(json: str) -> "JsonElement":
        """
        Parses the specified JSON string into a parse tree.
        An exception is thrown if the JSON string has multiple top-level JSON elements,
        or if there is trailing data.
        
        The JSON string is parsed in JsonReader.setLenient(boolean) lenient mode.

        Arguments
        - json: JSON text

        Returns
        - a parse tree of JsonElements corresponding to the specified JSON

        Raises
        - JsonParseException: if the specified text is not valid JSON

        Since
        - 2.8.6
        """
        ...


    @staticmethod
    def parseReader(reader: "Reader") -> "JsonElement":
        """
        Parses the complete JSON string provided by the reader into a parse tree.
        An exception is thrown if the JSON string has multiple top-level JSON elements,
        or if there is trailing data.
        
        The JSON data is parsed in JsonReader.setLenient(boolean) lenient mode.

        Arguments
        - reader: JSON text

        Returns
        - a parse tree of JsonElements corresponding to the specified JSON

        Raises
        - JsonParseException: if there is an IOException or if the specified
            text is not valid JSON

        Since
        - 2.8.6
        """
        ...


    @staticmethod
    def parseReader(reader: "JsonReader") -> "JsonElement":
        """
        Returns the next value from the JSON stream as a parse tree.
        Unlike the other `parse` methods, no exception is thrown if the JSON data has
        multiple top-level JSON elements, or if there is trailing data.
        
        The JSON data is parsed in JsonReader.setLenient(boolean) lenient mode,
        regardless of the lenient mode setting of the provided reader. The lenient mode setting
        of the reader is restored once this method returns.

        Raises
        - JsonParseException: if there is an IOException or if the specified
            text is not valid JSON

        Since
        - 2.8.6
        """
        ...


    def parse(self, json: str) -> "JsonElement":
        """
        Deprecated
        - Use JsonParser.parseString
        """
        ...


    def parse(self, json: "Reader") -> "JsonElement":
        """
        Deprecated
        - Use JsonParser.parseReader(Reader)
        """
        ...


    def parse(self, json: "JsonReader") -> "JsonElement":
        """
        Deprecated
        - Use JsonParser.parseReader(JsonReader)
        """
        ...
