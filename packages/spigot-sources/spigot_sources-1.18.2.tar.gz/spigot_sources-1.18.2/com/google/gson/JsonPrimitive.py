"""
Python module generated from Java source file com.google.gson.JsonPrimitive

Java source file obtained from artifact gson version 2.8.9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson import *
from com.google.gson.internal import $Gson$Preconditions
from com.google.gson.internal import LazilyParsedNumber
from java.math import BigDecimal
from java.math import BigInteger
from typing import Any, Callable, Iterable, Tuple


class JsonPrimitive(JsonElement):
    """
    A class representing a Json primitive value. A primitive value
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
        since Json only supports String.

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
        convenience method to get this element as a boolean value.

        Returns
        - get this element as a primitive boolean value.
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
        convenience method to get this element as a Number.

        Returns
        - get this element as a Number.

        Raises
        - NumberFormatException: if the value contained is not a valid Number.
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
        """
        convenience method to get this element as a String.

        Returns
        - get this element as a String.
        """
        ...


    def getAsDouble(self) -> float:
        """
        convenience method to get this element as a primitive double.

        Returns
        - get this element as a primitive double.

        Raises
        - NumberFormatException: if the value contained is not a valid double.
        """
        ...


    def getAsBigDecimal(self) -> "BigDecimal":
        """
        convenience method to get this element as a BigDecimal.

        Returns
        - get this element as a BigDecimal.

        Raises
        - NumberFormatException: if the value contained is not a valid BigDecimal.
        """
        ...


    def getAsBigInteger(self) -> "BigInteger":
        """
        convenience method to get this element as a BigInteger.

        Returns
        - get this element as a BigInteger.

        Raises
        - NumberFormatException: if the value contained is not a valid BigInteger.
        """
        ...


    def getAsFloat(self) -> float:
        """
        convenience method to get this element as a float.

        Returns
        - get this element as a float.

        Raises
        - NumberFormatException: if the value contained is not a valid float.
        """
        ...


    def getAsLong(self) -> int:
        """
        convenience method to get this element as a primitive long.

        Returns
        - get this element as a primitive long.

        Raises
        - NumberFormatException: if the value contained is not a valid long.
        """
        ...


    def getAsShort(self) -> int:
        """
        convenience method to get this element as a primitive short.

        Returns
        - get this element as a primitive short.

        Raises
        - NumberFormatException: if the value contained is not a valid short value.
        """
        ...


    def getAsInt(self) -> int:
        """
        convenience method to get this element as a primitive integer.

        Returns
        - get this element as a primitive integer.

        Raises
        - NumberFormatException: if the value contained is not a valid integer.
        """
        ...


    def getAsByte(self) -> int:
        ...


    def getAsCharacter(self) -> str:
        ...


    def hashCode(self) -> int:
        ...


    def equals(self, obj: "Object") -> bool:
        ...
