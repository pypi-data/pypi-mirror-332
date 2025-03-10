"""
Python module generated from Java source file com.google.gson.internal.bind.TimeTypeAdapter

Java source file obtained from artifact gson version 2.8.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson import Gson
from com.google.gson import JsonSyntaxException
from com.google.gson import TypeAdapter
from com.google.gson import TypeAdapterFactory
from com.google.gson.internal.bind import *
from com.google.gson.reflect import TypeToken
from com.google.gson.stream import JsonReader
from com.google.gson.stream import JsonToken
from com.google.gson.stream import JsonWriter
from java.io import IOException
from java.text import DateFormat
from java.text import ParseException
from java.text import SimpleDateFormat
from java.util import Date
from typing import Any, Callable, Iterable, Tuple


class TimeTypeAdapter(TypeAdapter):
    """
    Adapter for Time. Although this class appears stateless, it is not.
    DateFormat captures its time zone and locale when it is created, which gives
    this class state. DateFormat isn't thread safe either, so this class has
    to synchronize its read and write methods.
    """

    FACTORY = TypeAdapterFactory() {
    
        // we use a runtime check to make sure the 'T's equal
        @SuppressWarnings("unchecked")
        @Override
        public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> typeToken) {
            return typeToken.getRawType() == Time.class ? (TypeAdapter<T>) TimeTypeAdapter() : null;
        }
    }


    def read(self, in: "JsonReader") -> "Time":
        ...


    def write(self, out: "JsonWriter", value: "Time") -> None:
        ...
