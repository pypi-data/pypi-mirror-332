"""
Python module generated from Java source file com.google.gson.annotations.JsonAdapter

Java source file obtained from artifact gson version 2.11.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson import Gson
from com.google.gson import GsonBuilder
from com.google.gson import InstanceCreator
from com.google.gson import JsonDeserializer
from com.google.gson import JsonSerializer
from com.google.gson import TypeAdapter
from com.google.gson import TypeAdapterFactory
from com.google.gson.annotations import *
from typing import Any, Callable, Iterable, Tuple


class JsonAdapter:

    def value(self) -> type[Any]:
        """
        Either a TypeAdapter or TypeAdapterFactory, or one or both of JsonDeserializer or JsonSerializer.
        """
        ...


    def nullSafe(self) -> bool:
        """
        Whether the adapter referenced by .value() should be made TypeAdapter.nullSafe() null-safe.
        
        If `True` (the default), it will be made null-safe and Gson will handle `null`
        Java objects on serialization and JSON `null` on deserialization without calling the
        adapter. If `False`, the adapter will have to handle the `null` values.
        """
        return True
