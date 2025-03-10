"""
Python module generated from Java source file com.google.gson.JsonPrimitive

Java source file obtained from artifact gson version 2.10

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson import *
from com.google.gson.internal import LazilyParsedNumber
from java.math import BigDecimal
from java.math import BigInteger
from java.util import Objects
from typing import Any, Callable, Iterable, Tuple


class JsonPrimitive(JsonElement):
    """
    A class representing a JSON primitive value. A primitive value
    is either a String, a Java primitive, or a Java primitive
    wrapper type.

    Author(s)
    - Joel Leitch
    """

    def __init__(self, bool: "Boolean"):
        """
        Create a primitive containing a boolean value.

        Arguments
        - bool: the value to create the primitive with.
        """
        ...


    def __init__(self, number: "Number"):
        """
        Create a primitive containing a Number.

        Arguments
        - number: the value to create the primitive with.
        """
        ...


    def __init__(self, string: str):
        """
        Create a primitive containing a String value.

        Arguments
        - string: the value to create the primitive with.
        """
        ...


    def __init__(self, c: "Character"):
        """
        Create a primitive containing a character. The character is turned into a one character String
        since JSON only supports String.

        Arguments
        - c: the value to create the primitive with.
        """
        ...


    def deepCopy(self) -> "JsonPrimitive":
        """
        Returns the same value as primitives are immutable.

        Since
        - 2.8.2
        """
        ...


    def isBoolean(self) -> bool:
        """
        Check whether this primitive contains a boolean value.

        Returns
        - True if this primitive contains a boolean value, False otherwise.
        """
        ...


    def getAsBoolean(self) -> bool:
        """
        Convenience method to get this element as a boolean value.
        If this primitive .isBoolean() is not a boolean, the string value
        is parsed using Boolean.parseBoolean(String). This means `"True"` (ignoring
        case) is considered `True` and any other value is considered `False`.
        """
        ...


    def isNumber(self) -> bool:
        """
        Check whether this primitive contains a Number.

        Returns
        - True if this primitive contains a Number, False otherwise.
        """
        ...


    def getAsNumber(self) -> "Number":
        """
        Convenience method to get this element as a Number.
        If this primitive .isString() is a string, a lazily parsed `Number`
        is constructed which parses the string when any of its methods are called (which can
        lead to a NumberFormatException).

        Raises
        - UnsupportedOperationException: if this primitive is neither a number nor a string.
        """
        ...


    def isString(self) -> bool:
        """
        Check whether this primitive contains a String value.

        Returns
        - True if this primitive contains a String value, False otherwise.
        """
        ...


    def getAsString(self) -> str:
        ...


    def getAsDouble(self) -> float:
        """
        Raises
        - NumberFormatException: 
        """
        ...


    def getAsBigDecimal(self) -> "BigDecimal":
        """
        Raises
        - NumberFormatException: 
        """
        ...


    def getAsBigInteger(self) -> "BigInteger":
        """
        Raises
        - NumberFormatException: 
        """
        ...


    def getAsFloat(self) -> float:
        """
        Raises
        - NumberFormatException: 
        """
        ...


    def getAsLong(self) -> int:
        """
        Convenience method to get this element as a primitive long.

        Returns
        - this element as a primitive long.

        Raises
        - NumberFormatException: 
        """
        ...


    def getAsShort(self) -> int:
        """
        Raises
        - NumberFormatException: 
        """
        ...


    def getAsInt(self) -> int:
        """
        Raises
        - NumberFormatException: 
        """
        ...


    def getAsByte(self) -> int:
        """
        Raises
        - NumberFormatException: 
        """
        ...


    def getAsCharacter(self) -> str:
        """
        Raises
        - UnsupportedOperationException: if the string value of this
        primitive is empty.

        Deprecated
        - This method is misleading, as it does not get this element as a char but rather as
        a string's first character.
        """
        ...


    def hashCode(self) -> int:
        """
        Returns the hash code of this object.
        """
        ...


    def equals(self, obj: "Object") -> bool:
        """
        Returns whether the other object is equal to this. This method only considers
        the other object to be equal if it is an instance of `JsonPrimitive` and
        has an equal value.
        """
        ...
