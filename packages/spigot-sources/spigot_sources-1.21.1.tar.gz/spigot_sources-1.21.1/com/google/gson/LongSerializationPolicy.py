"""
Python module generated from Java source file com.google.gson.LongSerializationPolicy

Java source file obtained from artifact gson version 2.10.1

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson import *
from enum import Enum
from typing import Any, Callable, Iterable, Tuple


class LongSerializationPolicy(Enum):
    """
    Defines the expected format for a `long` or `Long` type when it is serialized.

    Author(s)
    - Joel Leitch

    Since
    - 1.3
    """

    DEFAULT = 0
    """
    This is the "default" serialization policy that will output a `Long` object as a JSON
    number. For example, assume an object has a long field named "f" then the serialized output
    would be:
    `{"f":123`}
    
    A `null` value is serialized as JsonNull.
    """
    STRING = 1
    """
    Serializes a long value as a quoted string. For example, assume an object has a long field 
    named "f" then the serialized output would be:
    `{"f":"123"`}
    
    A `null` value is serialized as JsonNull.
    """


    def serialize(self, value: "Long") -> "JsonElement":
        """
        Serialize this `value` using this serialization policy.

        Arguments
        - value: the long value to be serialized into a JsonElement

        Returns
        - the serialized version of `value`
        """
        ...
