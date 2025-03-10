"""
Python module generated from Java source file com.google.gson.DefaultDateTypeAdapter

Java source file obtained from artifact gson version 2.8.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson import *
from com.google.gson.internal.bind.util import ISO8601Utils
from java.lang.reflect import Type
from java.text import DateFormat
from java.text import ParseException
from java.text import ParsePosition
from java.text import SimpleDateFormat
from java.util import Date
from java.util import Locale
from typing import Any, Callable, Iterable, Tuple


class DefaultDateTypeAdapter(JsonSerializer, JsonDeserializer):
    """
    This type adapter supports three subclasses of date: Date, Timestamp, and
    java.sql.Date.

    Author(s)
    - Joel Leitch
    """

    def __init__(self, dateStyle: int, timeStyle: int):
        ...


    def serialize(self, src: "Date", typeOfSrc: "Type", context: "JsonSerializationContext") -> "JsonElement":
        ...


    def deserialize(self, json: "JsonElement", typeOfT: "Type", context: "JsonDeserializationContext") -> "Date":
        ...


    def toString(self) -> str:
        ...
