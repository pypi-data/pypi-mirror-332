"""
Python module generated from Java source file com.google.gson.stream.JsonToken

Java source file obtained from artifact gson version 2.10

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson.stream import *
from enum import Enum
from typing import Any, Callable, Iterable, Tuple


class JsonToken(Enum):
    """
    A structure, name or value type in a JSON-encoded string.

    Author(s)
    - Jesse Wilson

    Since
    - 1.6
    """

    BEGIN_ARRAY = 0
    """
    The opening of a JSON array. Written using JsonWriter.beginArray
    and read using JsonReader.beginArray.
    """
    END_ARRAY = 1
    """
    The closing of a JSON array. Written using JsonWriter.endArray
    and read using JsonReader.endArray.
    """
    BEGIN_OBJECT = 2
    """
    The opening of a JSON object. Written using JsonWriter.beginObject
    and read using JsonReader.beginObject.
    """
    END_OBJECT = 3
    """
    The closing of a JSON object. Written using JsonWriter.endObject
    and read using JsonReader.endObject.
    """
    NAME = 4
    """
    A JSON property name. Within objects, tokens alternate between names and
    their values. Written using JsonWriter.name and read using JsonReader.nextName
    """
    STRING = 5
    """
    A JSON string.
    """
    NUMBER = 6
    """
    A JSON number represented in this API by a Java `double`, `long`, or `int`.
    """
    BOOLEAN = 7
    """
    A JSON `True` or `False`.
    """
    NULL = 8
    """
    A JSON `null`.
    """
    END_DOCUMENT = 9
    """
    The end of the JSON stream. This sentinel value is returned by JsonReader.peek() to signal that the JSON-encoded value has no more
    tokens.
    """
