"""
Python module generated from Java source file com.google.common.primitives.Primitives

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.primitives import *
from java.util import Collections
from typing import Any, Callable, Iterable, Tuple


class Primitives:
    """
    Contains static utility methods pertaining to primitive types and their corresponding wrapper
    types.

    Author(s)
    - Kevin Bourrillion

    Since
    - 1.0
    """

    @staticmethod
    def allPrimitiveTypes() -> set[type[Any]]:
        """
        Returns an immutable set of all nine primitive types (including `void`). Note that a
        simpler way to test whether a `Class` instance is a member of this set is to call Class.isPrimitive.

        Since
        - 3.0
        """
        ...


    @staticmethod
    def allWrapperTypes() -> set[type[Any]]:
        """
        Returns an immutable set of all nine primitive-wrapper types (including Void).

        Since
        - 3.0
        """
        ...


    @staticmethod
    def isWrapperType(type: type[Any]) -> bool:
        """
        Returns `True` if `type` is one of the nine primitive-wrapper types, such as Integer.

        See
        - Class.isPrimitive
        """
        ...


    @staticmethod
    def wrap(type: type["T"]) -> type["T"]:
        """
        Returns the corresponding wrapper type of `type` if it is a primitive type; otherwise
        returns `type` itself. Idempotent.
        
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
        Returns the corresponding primitive type of `type` if it is a wrapper type; otherwise
        returns `type` itself. Idempotent.
        
        ```
            unwrap(Integer.class) == int.class
            unwrap(int.class) == int.class
            unwrap(String.class) == String.class
        ```
        """
        ...
