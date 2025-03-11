"""
Python module generated from Java source file com.google.gson.internal.bind.DefaultDateTypeAdapter

Java source file obtained from artifact gson version 2.11.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson import Gson
from com.google.gson import JsonSyntaxException
from com.google.gson import TypeAdapter
from com.google.gson import TypeAdapterFactory
from com.google.gson.internal import JavaVersion
from com.google.gson.internal import PreJava9DateFormatProvider
from com.google.gson.internal.bind import *
from com.google.gson.internal.bind.util import ISO8601Utils
from com.google.gson.reflect import TypeToken
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
from java.util import TimeZone
from typing import Any, Callable, Iterable, Tuple


class DefaultDateTypeAdapter(TypeAdapter):
    """
    This type adapter supports subclasses of date by defining a DefaultDateTypeAdapter.DateType and then using its `createAdapterFactory` methods.
    
    **Important:** Instances of this class (or rather the SimpleDateFormat they use)
    capture the current default Locale and TimeZone when they are created. Therefore
    avoid storing factories obtained from DateType in `static` fields, since they only
    create a single adapter instance and its behavior would then depend on when Gson classes are
    loaded first, and which default `Locale` and `TimeZone` was used at that point.

    Author(s)
    - Joel Leitch
    """

    DEFAULT_STYLE_FACTORY = // Because SimpleDateFormat captures the default TimeZone when it was created, let the factory
    // always create DefaultDateTypeAdapter instances (which are then cached by the Gson
    // instances) instead of having a single static DefaultDateTypeAdapter instance
    // Otherwise the behavior would depend on when an application first loads Gson classes and
    // which default TimeZone is set at that point, which would be quite brittle
    TypeAdapterFactory() {
    
        // we use a runtime check to make sure the 'T's equal
        @SuppressWarnings("unchecked")
        @Override
        public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> typeToken) {
            return typeToken.getRawType() == Date.class ? (TypeAdapter<T>) DefaultDateTypeAdapter<>(DateType.DATE, DateFormat.DEFAULT, DateFormat.DEFAULT) : null;
        }
    
        @Override
        public String toString() {
            return "DefaultDateTypeAdapter#DEFAULT_STYLE_FACTORY";
        }
    }
    """
    Factory for Date adapters which use DateFormat.DEFAULT as style.
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


        def createAdapterFactory(self, dateStyle: int, timeStyle: int) -> "TypeAdapterFactory":
            ...
