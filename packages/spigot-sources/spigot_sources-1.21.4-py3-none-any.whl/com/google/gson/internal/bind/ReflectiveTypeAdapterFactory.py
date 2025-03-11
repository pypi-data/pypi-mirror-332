"""
Python module generated from Java source file com.google.gson.internal.bind.ReflectiveTypeAdapterFactory

Java source file obtained from artifact gson version 2.11.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson import FieldNamingStrategy
from com.google.gson import Gson
from com.google.gson import JsonIOException
from com.google.gson import JsonParseException
from com.google.gson import JsonSyntaxException
from com.google.gson import ReflectionAccessFilter
from com.google.gson.ReflectionAccessFilter import FilterResult
from com.google.gson import TypeAdapter
from com.google.gson import TypeAdapterFactory
from com.google.gson.annotations import JsonAdapter
from com.google.gson.annotations import SerializedName
from com.google.gson.internal import $Gson$Types
from com.google.gson.internal import ConstructorConstructor
from com.google.gson.internal import Excluder
from com.google.gson.internal import ObjectConstructor
from com.google.gson.internal import Primitives
from com.google.gson.internal import ReflectionAccessFilterHelper
from com.google.gson.internal import TroubleshootingGuide
from com.google.gson.internal.bind import *
from com.google.gson.internal.reflect import ReflectionHelper
from com.google.gson.reflect import TypeToken
from com.google.gson.stream import JsonReader
from com.google.gson.stream import JsonToken
from com.google.gson.stream import JsonWriter
from java.io import IOException
from java.lang.reflect import AccessibleObject
from java.lang.reflect import Constructor
from java.lang.reflect import Field
from java.lang.reflect import InvocationTargetException
from java.lang.reflect import Member
from java.lang.reflect import Method
from java.lang.reflect import Modifier
from java.lang.reflect import Type
from java.util import Arrays
from java.util import Collections
from typing import Any, Callable, Iterable, Tuple


class ReflectiveTypeAdapterFactory(TypeAdapterFactory):
    """
    Type adapter that reflects over the fields and methods of a class.
    """

    def __init__(self, constructorConstructor: "ConstructorConstructor", fieldNamingPolicy: "FieldNamingStrategy", excluder: "Excluder", jsonAdapterFactory: "JsonAdapterAnnotationTypeAdapterFactory", reflectionFilters: list["ReflectionAccessFilter"]):
        ...


    def create(self, gson: "Gson", type: "TypeToken"["T"]) -> "TypeAdapter"["T"]:
        ...


    class Adapter(TypeAdapter):

        def write(self, out: "JsonWriter", value: "T") -> None:
            ...


        def read(self, in: "JsonReader") -> "T":
            ...
