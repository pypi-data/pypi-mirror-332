"""
Python module generated from Java source file com.google.gson.internal.bind.JsonTreeWriter

Java source file obtained from artifact gson version 2.11.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.errorprone.annotations import CanIgnoreReturnValue
from com.google.gson import JsonArray
from com.google.gson import JsonElement
from com.google.gson import JsonNull
from com.google.gson import JsonObject
from com.google.gson import JsonPrimitive
from com.google.gson.internal.bind import *
from com.google.gson.stream import JsonWriter
from java.io import IOException
from java.io import Writer
from java.util import Objects
from typing import Any, Callable, Iterable, Tuple


class JsonTreeWriter(JsonWriter):
    """
    This writer creates a JsonElement.
    """

    def __init__(self):
        ...


    def get(self) -> "JsonElement":
        """
        Returns the top level object produced by this writer.
        """
        ...


    def beginArray(self) -> "JsonWriter":
        ...


    def endArray(self) -> "JsonWriter":
        ...


    def beginObject(self) -> "JsonWriter":
        ...


    def endObject(self) -> "JsonWriter":
        ...


    def name(self, name: str) -> "JsonWriter":
        ...


    def value(self, value: str) -> "JsonWriter":
        ...


    def value(self, value: bool) -> "JsonWriter":
        ...


    def value(self, value: "Boolean") -> "JsonWriter":
        ...


    def value(self, value: float) -> "JsonWriter":
        ...


    def value(self, value: float) -> "JsonWriter":
        ...


    def value(self, value: int) -> "JsonWriter":
        ...


    def value(self, value: "Number") -> "JsonWriter":
        ...


    def nullValue(self) -> "JsonWriter":
        ...


    def jsonValue(self, value: str) -> "JsonWriter":
        ...


    def flush(self) -> None:
        ...


    def close(self) -> None:
        ...
