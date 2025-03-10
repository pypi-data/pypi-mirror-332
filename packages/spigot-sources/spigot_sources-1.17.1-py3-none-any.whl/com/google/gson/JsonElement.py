"""
Python module generated from Java source file com.google.gson.JsonElement

Java source file obtained from artifact gson version 2.8.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson import *
from com.google.gson.internal import Streams
from com.google.gson.stream import JsonWriter
from java.io import IOException
from java.io import StringWriter
from java.math import BigDecimal
from java.math import BigInteger
from typing import Any, Callable, Iterable, Tuple


class JsonElement:
    """
    A class representing an element of Json. It could either be a JsonObject, a
    JsonArray, a JsonPrimitive or a JsonNull.

    Author(s)
    - Joel Leitch
    """

    def isJsonArray(self) -> bool:
        """
        provides check for verifying if this element is an array or not.

        Returns
        - True if this element is of type JsonArray, False otherwise.
        """
        ...


    def isJsonObject(self) -> bool:
        """
        provides check for verifying if this element is a Json object or not.

        Returns
        - True if this element is of type JsonObject, False otherwise.
        """
        ...


    def isJsonPrimitive(self) -> bool:
        """
        provides check for verifying if this element is a primitive or not.

        Returns
        - True if this element is of type JsonPrimitive, False otherwise.
        """
        ...


    def isJsonNull(self) -> bool:
        """
        provides check for verifying if this element represents a null value or not.

        Returns
        - True if this element is of type JsonNull, False otherwise.

        Since
        - 1.2
        """
        ...


    def getAsJsonObject(self) -> "JsonObject":
        """
        convenience method to get this element as a JsonObject. If the element is of some
        other type, a IllegalStateException will result. Hence it is best to use this method
        after ensuring that this element is of the desired type by calling .isJsonObject()
        first.

        Returns
        - get this element as a JsonObject.

        Raises
        - IllegalStateException: if the element is of another type.
        """
        ...


    def getAsJsonArray(self) -> "JsonArray":
        """
        convenience method to get this element as a JsonArray. If the element is of some
        other type, a IllegalStateException will result. Hence it is best to use this method
        after ensuring that this element is of the desired type by calling .isJsonArray()
        first.

        Returns
        - get this element as a JsonArray.

        Raises
        - IllegalStateException: if the element is of another type.
        """
        ...


    def getAsJsonPrimitive(self) -> "JsonPrimitive":
        """
        convenience method to get this element as a JsonPrimitive. If the element is of some
        other type, a IllegalStateException will result. Hence it is best to use this method
        after ensuring that this element is of the desired type by calling .isJsonPrimitive()
        first.

        Returns
        - get this element as a JsonPrimitive.

        Raises
        - IllegalStateException: if the element is of another type.
        """
        ...


    def getAsJsonNull(self) -> "JsonNull":
        """
        convenience method to get this element as a JsonNull. If the element is of some
        other type, a IllegalStateException will result. Hence it is best to use this method
        after ensuring that this element is of the desired type by calling .isJsonNull()
        first.

        Returns
        - get this element as a JsonNull.

        Raises
        - IllegalStateException: if the element is of another type.

        Since
        - 1.2
        """
        ...


    def getAsBoolean(self) -> bool:
        """
        convenience method to get this element as a boolean value.

        Returns
        - get this element as a primitive boolean value.

        Raises
        - ClassCastException: if the element is of not a JsonPrimitive and is not a valid
        boolean value.
        - IllegalStateException: if the element is of the type JsonArray but contains
        more than a single element.
        """
        ...


    def getAsNumber(self) -> "Number":
        """
        convenience method to get this element as a Number.

        Returns
        - get this element as a Number.

        Raises
        - ClassCastException: if the element is of not a JsonPrimitive and is not a valid
        number.
        - IllegalStateException: if the element is of the type JsonArray but contains
        more than a single element.
        """
        ...


    def getAsString(self) -> str:
        """
        convenience method to get this element as a string value.

        Returns
        - get this element as a string value.

        Raises
        - ClassCastException: if the element is of not a JsonPrimitive and is not a valid
        string value.
        - IllegalStateException: if the element is of the type JsonArray but contains
        more than a single element.
        """
        ...


    def getAsDouble(self) -> float:
        """
        convenience method to get this element as a primitive double value.

        Returns
        - get this element as a primitive double value.

        Raises
        - ClassCastException: if the element is of not a JsonPrimitive and is not a valid
        double value.
        - IllegalStateException: if the element is of the type JsonArray but contains
        more than a single element.
        """
        ...


    def getAsFloat(self) -> float:
        """
        convenience method to get this element as a primitive float value.

        Returns
        - get this element as a primitive float value.

        Raises
        - ClassCastException: if the element is of not a JsonPrimitive and is not a valid
        float value.
        - IllegalStateException: if the element is of the type JsonArray but contains
        more than a single element.
        """
        ...


    def getAsLong(self) -> int:
        """
        convenience method to get this element as a primitive long value.

        Returns
        - get this element as a primitive long value.

        Raises
        - ClassCastException: if the element is of not a JsonPrimitive and is not a valid
        long value.
        - IllegalStateException: if the element is of the type JsonArray but contains
        more than a single element.
        """
        ...


    def getAsInt(self) -> int:
        """
        convenience method to get this element as a primitive integer value.

        Returns
        - get this element as a primitive integer value.

        Raises
        - ClassCastException: if the element is of not a JsonPrimitive and is not a valid
        integer value.
        - IllegalStateException: if the element is of the type JsonArray but contains
        more than a single element.
        """
        ...


    def getAsByte(self) -> int:
        """
        convenience method to get this element as a primitive byte value.

        Returns
        - get this element as a primitive byte value.

        Raises
        - ClassCastException: if the element is of not a JsonPrimitive and is not a valid
        byte value.
        - IllegalStateException: if the element is of the type JsonArray but contains
        more than a single element.

        Since
        - 1.3
        """
        ...


    def getAsCharacter(self) -> str:
        """
        convenience method to get this element as a primitive character value.

        Returns
        - get this element as a primitive char value.

        Raises
        - ClassCastException: if the element is of not a JsonPrimitive and is not a valid
        char value.
        - IllegalStateException: if the element is of the type JsonArray but contains
        more than a single element.

        Since
        - 1.3
        """
        ...


    def getAsBigDecimal(self) -> "BigDecimal":
        """
        convenience method to get this element as a BigDecimal.

        Returns
        - get this element as a BigDecimal.

        Raises
        - ClassCastException: if the element is of not a JsonPrimitive.
        * @throws NumberFormatException if the element is not a valid BigDecimal.
        - IllegalStateException: if the element is of the type JsonArray but contains
        more than a single element.

        Since
        - 1.2
        """
        ...


    def getAsBigInteger(self) -> "BigInteger":
        """
        convenience method to get this element as a BigInteger.

        Returns
        - get this element as a BigInteger.

        Raises
        - ClassCastException: if the element is of not a JsonPrimitive.
        - NumberFormatException: if the element is not a valid BigInteger.
        - IllegalStateException: if the element is of the type JsonArray but contains
        more than a single element.

        Since
        - 1.2
        """
        ...


    def getAsShort(self) -> int:
        """
        convenience method to get this element as a primitive short value.

        Returns
        - get this element as a primitive short value.

        Raises
        - ClassCastException: if the element is of not a JsonPrimitive and is not a valid
        short value.
        - IllegalStateException: if the element is of the type JsonArray but contains
        more than a single element.
        """
        ...


    def toString(self) -> str:
        """
        Returns a String representation of this element.
        """
        ...
