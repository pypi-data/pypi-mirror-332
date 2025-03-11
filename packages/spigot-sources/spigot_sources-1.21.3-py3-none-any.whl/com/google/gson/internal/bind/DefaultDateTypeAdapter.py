"""
Python module generated from Java source file com.google.gson.internal.bind.DefaultDateTypeAdapter

Java source file obtained from artifact gson version 2.10.1

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson import JsonSyntaxException
from com.google.gson import TypeAdapter
from com.google.gson import TypeAdapterFactory
from com.google.gson.internal import JavaVersion
from com.google.gson.internal import PreJava9DateFormatProvider
from com.google.gson.internal.bind import *
from com.google.gson.internal.bind.util import ISO8601Utils
from com.google.gson.stream import JsonReader
from com.google.gson.stream import JsonToken
from com.google.gson.stream import JsonWriter
from java.io import IOException
from java.text import DateFormat
from java.text import ParseException
from java.text import ParsePosition
from java.text import SimpleDateFormat
from java.util import Date
from java.util import Locale
from java.util import Objects
from typing import Any, Callable, Iterable, Tuple


class DefaultDateTypeAdapter(TypeAdapter):
    """
    This type adapter supports subclasses of date by defining a
    DefaultDateTypeAdapter.DateType and then using its `createAdapterFactory`
    methods.

    Author(s)
    - Joel Leitch
    """

    def write(self, out: "JsonWriter", value: "Date") -> None:
        ...


    def read(self, in: "JsonReader") -> "T":
        ...


    def toString(self) -> str:
        ...


    class DateType:

        DATE = DateType<Date>(Date.class) {
        
            @Override
            protected Date deserialize(Date date) {
                return date;
            }
        }


        def createAdapterFactory(self, datePattern: str) -> "TypeAdapterFactory":
            ...


        def createAdapterFactory(self, style: int) -> "TypeAdapterFactory":
            ...


        def createAdapterFactory(self, dateStyle: int, timeStyle: int) -> "TypeAdapterFactory":
            ...


        def createDefaultsAdapterFactory(self) -> "TypeAdapterFactory":
            ...
