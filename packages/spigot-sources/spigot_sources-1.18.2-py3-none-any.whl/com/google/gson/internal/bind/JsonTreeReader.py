"""
Python module generated from Java source file com.google.gson.internal.bind.JsonTreeReader

Java source file obtained from artifact gson version 2.8.9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson import JsonArray
from com.google.gson import JsonElement
from com.google.gson import JsonNull
from com.google.gson import JsonObject
from com.google.gson import JsonPrimitive
from com.google.gson.internal.bind import *
from com.google.gson.stream import JsonReader
from com.google.gson.stream import JsonToken
from java.io import IOException
from java.io import Reader
from java.util import Arrays
from java.util import Iterator
from typing import Any, Callable, Iterable, Tuple


class JsonTreeReader(JsonReader):
    """
    This reader walks the elements of a JsonElement as if it was coming from a
    character stream.

    Author(s)
    - Jesse Wilson
    """

    def __init__(self, element: "JsonElement"):
        ...


    def beginArray(self) -> None:
        ...


    def endArray(self) -> None:
        ...


    def beginObject(self) -> None:
        ...


    def endObject(self) -> None:
        ...


    def hasNext(self) -> bool:
        ...


    def peek(self) -> "JsonToken":
        ...


    def nextName(self) -> str:
        ...


    def nextString(self) -> str:
        ...


    def nextBoolean(self) -> bool:
        ...


    def nextNull(self) -> None:
        ...


    def nextDouble(self) -> float:
        ...


    def nextLong(self) -> int:
        ...


    def nextInt(self) -> int:
        ...


    def close(self) -> None:
        ...


    def skipValue(self) -> None:
        ...


    def toString(self) -> str:
        ...


    def promoteNameToValue(self) -> None:
        ...


    def getPath(self) -> str:
        ...
