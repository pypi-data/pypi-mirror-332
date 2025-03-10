"""
Python module generated from Java source file com.google.gson.internal.bind.ObjectTypeAdapter

Java source file obtained from artifact gson version 2.10

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson import Gson
from com.google.gson import ToNumberPolicy
from com.google.gson import ToNumberStrategy
from com.google.gson import TypeAdapter
from com.google.gson import TypeAdapterFactory
from com.google.gson.internal import LinkedTreeMap
from com.google.gson.internal.bind import *
from com.google.gson.reflect import TypeToken
from com.google.gson.stream import JsonReader
from com.google.gson.stream import JsonToken
from com.google.gson.stream import JsonWriter
from java.io import IOException
from java.util import ArrayDeque
from java.util import Deque
from typing import Any, Callable, Iterable, Tuple


class ObjectTypeAdapter(TypeAdapter):
    """
    Adapts types whose static type is only 'Object'. Uses getClass() on
    serialization and a primitive/Map/List on deserialization.
    """

    @staticmethod
    def getFactory(toNumberStrategy: "ToNumberStrategy") -> "TypeAdapterFactory":
        ...


    def read(self, in: "JsonReader") -> "Object":
        ...


    def write(self, out: "JsonWriter", value: "Object") -> None:
        ...
