"""
Python module generated from Java source file com.google.gson.internal.bind.TreeTypeAdapter

Java source file obtained from artifact gson version 2.10.1

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson import Gson
from com.google.gson import JsonDeserializationContext
from com.google.gson import JsonDeserializer
from com.google.gson import JsonElement
from com.google.gson import JsonParseException
from com.google.gson import JsonSerializationContext
from com.google.gson import JsonSerializer
from com.google.gson import TypeAdapter
from com.google.gson import TypeAdapterFactory
from com.google.gson.internal import $Gson$Preconditions
from com.google.gson.internal import Streams
from com.google.gson.internal.bind import *
from com.google.gson.reflect import TypeToken
from com.google.gson.stream import JsonReader
from com.google.gson.stream import JsonWriter
from java.io import IOException
from java.lang.reflect import Type
from typing import Any, Callable, Iterable, Tuple


class TreeTypeAdapter(SerializationDelegatingTypeAdapter):
    """
    Adapts a Gson 1.x tree-style adapter as a streaming TypeAdapter. Since the
    tree adapter may be serialization-only or deserialization-only, this class
    has a facility to lookup a delegate type adapter on demand.
    """

    def __init__(self, serializer: "JsonSerializer"["T"], deserializer: "JsonDeserializer"["T"], gson: "Gson", typeToken: "TypeToken"["T"], skipPast: "TypeAdapterFactory", nullSafe: bool):
        ...


    def __init__(self, serializer: "JsonSerializer"["T"], deserializer: "JsonDeserializer"["T"], gson: "Gson", typeToken: "TypeToken"["T"], skipPast: "TypeAdapterFactory"):
        ...


    def read(self, in: "JsonReader") -> "T":
        ...


    def write(self, out: "JsonWriter", value: "T") -> None:
        ...


    def getSerializationDelegate(self) -> "TypeAdapter"["T"]:
        """
        Returns the type adapter which is used for serialization. Returns `this`
        if this `TreeTypeAdapter` has a .serializer; otherwise returns
        the delegate.
        """
        ...


    @staticmethod
    def newFactory(exactType: "TypeToken"[Any], typeAdapter: "Object") -> "TypeAdapterFactory":
        """
        Returns a new factory that will match each type against `exactType`.
        """
        ...


    @staticmethod
    def newFactoryWithMatchRawType(exactType: "TypeToken"[Any], typeAdapter: "Object") -> "TypeAdapterFactory":
        """
        Returns a new factory that will match each type and its raw type against
        `exactType`.
        """
        ...


    @staticmethod
    def newTypeHierarchyFactory(hierarchyType: type[Any], typeAdapter: "Object") -> "TypeAdapterFactory":
        """
        Returns a new factory that will match each type's raw type for assignability
        to `hierarchyType`.
        """
        ...
