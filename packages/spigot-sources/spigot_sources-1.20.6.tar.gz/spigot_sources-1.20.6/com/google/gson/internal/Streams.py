"""
Python module generated from Java source file com.google.gson.internal.Streams

Java source file obtained from artifact gson version 2.10.1

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson import JsonElement
from com.google.gson import JsonIOException
from com.google.gson import JsonNull
from com.google.gson import JsonParseException
from com.google.gson import JsonSyntaxException
from com.google.gson.internal import *
from com.google.gson.internal.bind import TypeAdapters
from com.google.gson.stream import JsonReader
from com.google.gson.stream import JsonWriter
from com.google.gson.stream import MalformedJsonException
from java.io import EOFException
from java.io import IOException
from java.io import Writer
from java.util import Objects
from typing import Any, Callable, Iterable, Tuple


class Streams:
    """
    Reads and writes GSON parse trees over streams.
    """

    @staticmethod
    def parse(reader: "JsonReader") -> "JsonElement":
        """
        Takes a reader in any state and returns the next value as a JsonElement.
        """
        ...


    @staticmethod
    def write(element: "JsonElement", writer: "JsonWriter") -> None:
        """
        Writes the JSON element to the writer, recursively.
        """
        ...


    @staticmethod
    def writerForAppendable(appendable: "Appendable") -> "Writer":
        ...
