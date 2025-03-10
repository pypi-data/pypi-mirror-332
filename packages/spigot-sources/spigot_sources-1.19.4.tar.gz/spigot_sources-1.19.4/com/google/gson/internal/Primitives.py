"""
Python module generated from Java source file com.google.gson.internal.Primitives

Java source file obtained from artifact gson version 2.10

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson.internal import *
from java.lang.reflect import Type
from typing import Any, Callable, Iterable, Tuple


class Primitives:
    """
    Contains static utility methods pertaining to primitive types and their
    corresponding wrapper types.

    Author(s)
    - Kevin Bourrillion
    """

    @staticmethod
    def isPrimitive(type: "Type") -> bool:
        """
        Returns True if this type is a primitive.
        """
        ...


    @staticmethod
    def isWrapperType(type: "Type") -> bool:
        """
        Returns `True` if `type` is one of the nine
        primitive-wrapper types, such as Integer.

        See
        - Class.isPrimitive
        """
        ...


    @staticmethod
    def wrap(type: type["T"]) -> type["T"]:
        """
        Returns the corresponding wrapper type of `type` if it is a primitive
        type; otherwise returns `type` itself. Idempotent.
        ```
            wrap(int.class) == Integer.class
            wrap(Integer.class) == Integer.class
            wrap(String.class) == String.class
        ```
        """
        ...


    @staticmethod
    def unwrap(type: type["T"]) -> type["T"]:
        """
        Returns the corresponding primitive type of `type` if it is a
        wrapper type; otherwise returns `type` itself. Idempotent.
        ```
            unwrap(Integer.class) == int.class
            unwrap(int.class) == int.class
            unwrap(String.class) == String.class
        ```
        """
        ...
