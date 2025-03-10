"""
Python module generated from Java source file com.google.gson.internal.bind.TypeAdapterRuntimeTypeWrapper

Java source file obtained from artifact gson version 2.10

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson import Gson
from com.google.gson import TypeAdapter
from com.google.gson.internal.bind import *
from com.google.gson.reflect import TypeToken
from com.google.gson.stream import JsonReader
from com.google.gson.stream import JsonWriter
from java.io import IOException
from java.lang.reflect import Type
from java.lang.reflect import TypeVariable
from typing import Any, Callable, Iterable, Tuple


class TypeAdapterRuntimeTypeWrapper(TypeAdapter):

    def read(self, in: "JsonReader") -> "T":
        ...


    def write(self, out: "JsonWriter", value: "T") -> None:
        ...
