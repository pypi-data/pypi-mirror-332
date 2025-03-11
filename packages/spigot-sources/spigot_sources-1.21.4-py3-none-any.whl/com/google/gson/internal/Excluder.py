"""
Python module generated from Java source file com.google.gson.internal.Excluder

Java source file obtained from artifact gson version 2.11.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson import ExclusionStrategy
from com.google.gson import FieldAttributes
from com.google.gson import Gson
from com.google.gson import TypeAdapter
from com.google.gson import TypeAdapterFactory
from com.google.gson.annotations import Expose
from com.google.gson.annotations import Since
from com.google.gson.annotations import Until
from com.google.gson.internal import *
from com.google.gson.internal.reflect import ReflectionHelper
from com.google.gson.reflect import TypeToken
from com.google.gson.stream import JsonReader
from com.google.gson.stream import JsonWriter
from java.io import IOException
from java.lang.reflect import Field
from java.lang.reflect import Modifier
from java.util import Collections
from typing import Any, Callable, Iterable, Tuple


class Excluder(TypeAdapterFactory, Cloneable):
    """
    This class selects which fields and types to omit. It is configurable, supporting version
    attributes Since and Until, modifiers, synthetic fields, anonymous and local
    classes, inner classes, and fields with the Expose annotation.
    
    This class is a type adapter factory; types that are excluded will be adapted to null. It may
    delegate to another type adapter if only one direction is excluded.

    Author(s)
    - Jesse Wilson
    """

    DEFAULT = Excluder()


    def withVersion(self, ignoreVersionsAfter: float) -> "Excluder":
        ...


    def withModifiers(self, *modifiers: Tuple[int, ...]) -> "Excluder":
        ...


    def disableInnerClassSerialization(self) -> "Excluder":
        ...


    def excludeFieldsWithoutExposeAnnotation(self) -> "Excluder":
        ...


    def withExclusionStrategy(self, exclusionStrategy: "ExclusionStrategy", serialization: bool, deserialization: bool) -> "Excluder":
        ...


    def create(self, gson: "Gson", type: "TypeToken"["T"]) -> "TypeAdapter"["T"]:
        ...


    def excludeField(self, field: "Field", serialize: bool) -> bool:
        ...


    def excludeClass(self, clazz: type[Any], serialize: bool) -> bool:
        ...
