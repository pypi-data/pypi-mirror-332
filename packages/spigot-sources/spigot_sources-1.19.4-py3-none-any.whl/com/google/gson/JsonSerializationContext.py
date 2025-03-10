"""
Python module generated from Java source file com.google.gson.JsonSerializationContext

Java source file obtained from artifact gson version 2.10

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson import *
from java.lang.reflect import Type
from typing import Any, Callable, Iterable, Tuple


class JsonSerializationContext:
    """
    Context for serialization that is passed to a custom serializer during invocation of its
    JsonSerializer.serialize(Object, Type, JsonSerializationContext) method.

    Author(s)
    - Joel Leitch
    """

    def serialize(self, src: "Object") -> "JsonElement":
        """
        Invokes default serialization on the specified object.

        Arguments
        - src: the object that needs to be serialized.

        Returns
        - a tree of JsonElements corresponding to the serialized form of `src`.
        """
        ...


    def serialize(self, src: "Object", typeOfSrc: "Type") -> "JsonElement":
        """
        Invokes default serialization on the specified object passing the specific type information.
        It should never be invoked on the element received as a parameter of the
        JsonSerializer.serialize(Object, Type, JsonSerializationContext) method. Doing
        so will result in an infinite loop since Gson will in-turn call the custom serializer again.

        Arguments
        - src: the object that needs to be serialized.
        - typeOfSrc: the actual genericized type of src object.

        Returns
        - a tree of JsonElements corresponding to the serialized form of `src`.
        """
        ...
