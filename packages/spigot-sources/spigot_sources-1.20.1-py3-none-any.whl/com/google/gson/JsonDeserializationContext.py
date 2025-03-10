"""
Python module generated from Java source file com.google.gson.JsonDeserializationContext

Java source file obtained from artifact gson version 2.10

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson import *
from java.lang.reflect import Type
from typing import Any, Callable, Iterable, Tuple


class JsonDeserializationContext:
    """
    Context for deserialization that is passed to a custom deserializer during invocation of its
    JsonDeserializer.deserialize(JsonElement, Type, JsonDeserializationContext)
    method.

    Author(s)
    - Joel Leitch
    """

    def deserialize(self, json: "JsonElement", typeOfT: "Type") -> "T":
        """
        Invokes default deserialization on the specified object. It should never be invoked on
        the element received as a parameter of the
        JsonDeserializer.deserialize(JsonElement, Type, JsonDeserializationContext) method. Doing
        so will result in an infinite loop since Gson will in-turn call the custom deserializer again.
        
        Type `<T>`: The type of the deserialized object.

        Arguments
        - json: the parse tree.
        - typeOfT: type of the expected return value.

        Returns
        - An object of type typeOfT.

        Raises
        - JsonParseException: if the parse tree does not contain expected data.
        """
        ...
