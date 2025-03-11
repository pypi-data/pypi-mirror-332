"""
Python module generated from Java source file com.google.gson.internal.sql.SqlTimestampTypeAdapter

Java source file obtained from artifact gson version 2.11.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson import Gson
from com.google.gson import TypeAdapter
from com.google.gson import TypeAdapterFactory
from com.google.gson.internal.sql import *
from com.google.gson.reflect import TypeToken
from com.google.gson.stream import JsonReader
from com.google.gson.stream import JsonWriter
from java.io import IOException
from java.util import Date
from typing import Any, Callable, Iterable, Tuple


class SqlTimestampTypeAdapter(TypeAdapter):

    def read(self, in: "JsonReader") -> "Timestamp":
        ...


    def write(self, out: "JsonWriter", value: "Timestamp") -> None:
        ...
