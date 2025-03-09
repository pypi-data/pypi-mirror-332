"""
Python module generated from Java source file com.google.gson.internal.bind.JsonAdapterAnnotationTypeAdapterFactory

Java source file obtained from artifact gson version 2.10.1

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson import Gson
from com.google.gson import JsonDeserializer
from com.google.gson import JsonSerializer
from com.google.gson import TypeAdapter
from com.google.gson import TypeAdapterFactory
from com.google.gson.annotations import JsonAdapter
from com.google.gson.internal import ConstructorConstructor
from com.google.gson.internal.bind import *
from com.google.gson.reflect import TypeToken
from typing import Any, Callable, Iterable, Tuple


class JsonAdapterAnnotationTypeAdapterFactory(TypeAdapterFactory):
    """
    Given a type T, looks for the annotation JsonAdapter and uses an instance of the
    specified class as the default type adapter.

    Since
    - 2.3
    """

    def __init__(self, constructorConstructor: "ConstructorConstructor"):
        ...


    def create(self, gson: "Gson", targetType: "TypeToken"["T"]) -> "TypeAdapter"["T"]:
        ...
