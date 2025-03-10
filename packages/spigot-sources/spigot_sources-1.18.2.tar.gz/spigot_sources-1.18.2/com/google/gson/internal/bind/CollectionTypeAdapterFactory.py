"""
Python module generated from Java source file com.google.gson.internal.bind.CollectionTypeAdapterFactory

Java source file obtained from artifact gson version 2.8.9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson import Gson
from com.google.gson import TypeAdapter
from com.google.gson import TypeAdapterFactory
from com.google.gson.internal import $Gson$Types
from com.google.gson.internal import ConstructorConstructor
from com.google.gson.internal import ObjectConstructor
from com.google.gson.internal.bind import *
from com.google.gson.reflect import TypeToken
from com.google.gson.stream import JsonReader
from com.google.gson.stream import JsonToken
from com.google.gson.stream import JsonWriter
from java.io import IOException
from java.lang.reflect import Type
from typing import Any, Callable, Iterable, Tuple


class CollectionTypeAdapterFactory(TypeAdapterFactory):
    """
    Adapt a homogeneous collection of objects.
    """

    def __init__(self, constructorConstructor: "ConstructorConstructor"):
        ...


    def create(self, gson: "Gson", typeToken: "TypeToken"["T"]) -> "TypeAdapter"["T"]:
        ...
