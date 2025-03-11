"""
Python module generated from Java source file com.google.gson.JsonArray

Java source file obtained from artifact gson version 2.11.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.errorprone.annotations import CanIgnoreReturnValue
from com.google.gson import *
from com.google.gson.internal import NonNullElementWrapperList
from java.math import BigDecimal
from java.math import BigInteger
from java.util import Iterator
from typing import Any, Callable, Iterable, Tuple


class JsonArray(JsonElement, Iterable):
    """
    A class representing an array type in JSON. An array is a list of JsonElements each of
    which can be of a different type. This is an ordered list, meaning that the order in which
    elements are added is preserved. This class does not support `null` values. If `null`
    is provided as element argument to any of the methods, it is converted to a JsonNull.
    
    `JsonArray` only implements the Iterable interface but not the List
    interface. A `List` view of it can be obtained with .asList().
    
    See the JsonElement documentation for details on how to convert `JsonArray` and
    generally any `JsonElement` from and to JSON.

    Author(s)
    - Joel Leitch
    """

    def __init__(self):
        """
        Creates an empty JsonArray.
        """
        ...


    def __init__(self, capacity: int):
        """
        Creates an empty JsonArray with the desired initial capacity.

        Arguments
        - capacity: initial capacity.

        Raises
        - IllegalArgumentException: if the `capacity` is negative

        Since
        - 2.8.1
        """
        ...


    def deepCopy(self) -> "JsonArray":
        """
        Creates a deep copy of this element and all its children.

        Since
        - 2.8.2
        """
        ...


    def add(self, bool: "Boolean") -> None:
        """
        Adds the specified boolean to self.

        Arguments
        - bool: the boolean that needs to be added to the array.

        Since
        - 2.4
        """
        ...


    def add(self, character: "Character") -> None:
        """
        Adds the specified character to self.

        Arguments
        - character: the character that needs to be added to the array.

        Since
        - 2.4
        """
        ...


    def add(self, number: "Number") -> None:
        """
        Adds the specified number to self.

        Arguments
        - number: the number that needs to be added to the array.

        Since
        - 2.4
        """
        ...


    def add(self, string: str) -> None:
        """
        Adds the specified string to self.

        Arguments
        - string: the string that needs to be added to the array.

        Since
        - 2.4
        """
        ...


    def add(self, element: "JsonElement") -> None:
        """
        Adds the specified element to self.

        Arguments
        - element: the element that needs to be added to the array.
        """
        ...


    def addAll(self, array: "JsonArray") -> None:
        """
        Adds all the elements of the specified array to self.

        Arguments
        - array: the array whose elements need to be added to the array.
        """
        ...


    def set(self, index: int, element: "JsonElement") -> "JsonElement":
        """
        Replaces the element at the specified position in this array with the specified element.

        Arguments
        - index: index of the element to replace
        - element: element to be stored at the specified position

        Returns
        - the element previously at the specified position

        Raises
        - IndexOutOfBoundsException: if the specified index is outside the array bounds
        """
        ...


    def remove(self, element: "JsonElement") -> bool:
        """
        Removes the first occurrence of the specified element from this array, if it is present. If the
        array does not contain the element, it is unchanged.

        Arguments
        - element: element to be removed from this array, if present

        Returns
        - True if this array contained the specified element, False otherwise

        Since
        - 2.3
        """
        ...


    def remove(self, index: int) -> "JsonElement":
        """
        Removes the element at the specified position in this array. Shifts any subsequent elements to
        the left (subtracts one from their indices). Returns the element that was removed from the
        array.

        Arguments
        - index: index the index of the element to be removed

        Returns
        - the element previously at the specified position

        Raises
        - IndexOutOfBoundsException: if the specified index is outside the array bounds

        Since
        - 2.3
        """
        ...


    def contains(self, element: "JsonElement") -> bool:
        """
        Returns True if this array contains the specified element.

        Arguments
        - element: whose presence in this array is to be tested

        Returns
        - True if this array contains the specified element.

        Since
        - 2.3
        """
        ...


    def size(self) -> int:
        """
        Returns the number of elements in the array.

        Returns
        - the number of elements in the array.
        """
        ...


    def isEmpty(self) -> bool:
        """
        Returns True if the array is empty.

        Returns
        - True if the array is empty.

        Since
        - 2.8.7
        """
        ...


    def iterator(self) -> Iterator["JsonElement"]:
        """
        Returns an iterator to navigate the elements of the array. Since the array is an ordered list,
        the iterator navigates the elements in the order they were inserted.

        Returns
        - an iterator to navigate the elements of the array.
        """
        ...


    def get(self, i: int) -> "JsonElement":
        """
        Returns the i-th element of the array.

        Arguments
        - i: the index of the element that is being sought.

        Returns
        - the element present at the i-th index.

        Raises
        - IndexOutOfBoundsException: if `i` is negative or greater than or equal to the
            .size() of the array.
        """
        ...


    def getAsNumber(self) -> "Number":
        """
        Convenience method to get this array as a Number if it contains a single element. This
        method calls JsonElement.getAsNumber() on the element, therefore any of the exceptions
        declared by that method can occur.

        Returns
        - this element as a number if it is single element array.

        Raises
        - IllegalStateException: if the array is empty or has more than one element.
        """
        ...


    def getAsString(self) -> str:
        """
        Convenience method to get this array as a String if it contains a single element. This
        method calls JsonElement.getAsString() on the element, therefore any of the exceptions
        declared by that method can occur.

        Returns
        - this element as a String if it is single element array.

        Raises
        - IllegalStateException: if the array is empty or has more than one element.
        """
        ...


    def getAsDouble(self) -> float:
        """
        Convenience method to get this array as a double if it contains a single element. This method
        calls JsonElement.getAsDouble() on the element, therefore any of the exceptions
        declared by that method can occur.

        Returns
        - this element as a double if it is single element array.

        Raises
        - IllegalStateException: if the array is empty or has more than one element.
        """
        ...


    def getAsBigDecimal(self) -> "BigDecimal":
        """
        Convenience method to get this array as a BigDecimal if it contains a single element.
        This method calls JsonElement.getAsBigDecimal() on the element, therefore any of the
        exceptions declared by that method can occur.

        Returns
        - this element as a BigDecimal if it is single element array.

        Raises
        - IllegalStateException: if the array is empty or has more than one element.

        Since
        - 1.2
        """
        ...


    def getAsBigInteger(self) -> "BigInteger":
        """
        Convenience method to get this array as a BigInteger if it contains a single element.
        This method calls JsonElement.getAsBigInteger() on the element, therefore any of the
        exceptions declared by that method can occur.

        Returns
        - this element as a BigInteger if it is single element array.

        Raises
        - IllegalStateException: if the array is empty or has more than one element.

        Since
        - 1.2
        """
        ...


    def getAsFloat(self) -> float:
        """
        Convenience method to get this array as a float if it contains a single element. This method
        calls JsonElement.getAsFloat() on the element, therefore any of the exceptions declared
        by that method can occur.

        Returns
        - this element as a float if it is single element array.

        Raises
        - IllegalStateException: if the array is empty or has more than one element.
        """
        ...


    def getAsLong(self) -> int:
        """
        Convenience method to get this array as a long if it contains a single element. This method
        calls JsonElement.getAsLong() on the element, therefore any of the exceptions declared
        by that method can occur.

        Returns
        - this element as a long if it is single element array.

        Raises
        - IllegalStateException: if the array is empty or has more than one element.
        """
        ...


    def getAsInt(self) -> int:
        """
        Convenience method to get this array as an integer if it contains a single element. This method
        calls JsonElement.getAsInt() on the element, therefore any of the exceptions declared
        by that method can occur.

        Returns
        - this element as an integer if it is single element array.

        Raises
        - IllegalStateException: if the array is empty or has more than one element.
        """
        ...


    def getAsByte(self) -> int:
        """
        Convenience method to get this array as a primitive byte if it contains a single element. This
        method calls JsonElement.getAsByte() on the element, therefore any of the exceptions
        declared by that method can occur.

        Returns
        - this element as a primitive byte if it is single element array.

        Raises
        - IllegalStateException: if the array is empty or has more than one element.
        """
        ...


    def getAsCharacter(self) -> str:
        """
        Convenience method to get this array as a character if it contains a single element. This
        method calls JsonElement.getAsCharacter() on the element, therefore any of the
        exceptions declared by that method can occur.

        Returns
        - this element as a primitive short if it is single element array.

        Raises
        - IllegalStateException: if the array is empty or has more than one element.

        Deprecated
        - This method is misleading, as it does not get this element as a char but rather as
            a string's first character.
        """
        ...


    def getAsShort(self) -> int:
        """
        Convenience method to get this array as a primitive short if it contains a single element. This
        method calls JsonElement.getAsShort() on the element, therefore any of the exceptions
        declared by that method can occur.

        Returns
        - this element as a primitive short if it is single element array.

        Raises
        - IllegalStateException: if the array is empty or has more than one element.
        """
        ...


    def getAsBoolean(self) -> bool:
        """
        Convenience method to get this array as a boolean if it contains a single element. This method
        calls JsonElement.getAsBoolean() on the element, therefore any of the exceptions
        declared by that method can occur.

        Returns
        - this element as a boolean if it is single element array.

        Raises
        - IllegalStateException: if the array is empty or has more than one element.
        """
        ...


    def asList(self) -> list["JsonElement"]:
        """
        Returns a mutable List view of this `JsonArray`. Changes to the `List` are
        visible in this `JsonArray` and the other way around.
        
        The `List` does not permit `null` elements. Unlike `JsonArray`'s `null` handling, a NullPointerException is thrown when trying to add `null`. Use
        JsonNull for JSON null values.

        Returns
        - mutable `List` view

        Since
        - 2.10
        """
        ...


    def equals(self, o: "Object") -> bool:
        """
        Returns whether the other object is equal to this. This method only considers the other object
        to be equal if it is an instance of `JsonArray` and has equal elements in the same order.
        """
        ...


    def hashCode(self) -> int:
        """
        Returns the hash code of this array. This method calculates the hash code based on the elements
        of this array.
        """
        ...
