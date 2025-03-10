"""
Python module generated from Java source file com.google.common.collect.ObjectArrays

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import GwtIncompatible
from com.google.common.collect import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.lang.reflect import Array
from java.util import Arrays
from javax.annotation import Nullable
from typing import Any, Callable, Iterable, Tuple


class ObjectArrays:
    """
    Static utility methods pertaining to object arrays.

    Author(s)
    - Kevin Bourrillion

    Since
    - 2.0
    """

    @staticmethod
    def newArray(type: type["T"], length: int) -> list["T"]:
        """
        Returns a new array of the given length with the specified component type.

        Arguments
        - type: the component type
        - length: the length of the new array
        """
        ...


    @staticmethod
    def newArray(reference: list["T"], length: int) -> list["T"]:
        """
        Returns a new array of the given length with the same type as a reference
        array.

        Arguments
        - reference: any array of the desired type
        - length: the length of the new array
        """
        ...


    @staticmethod
    def concat(first: list["T"], second: list["T"], type: type["T"]) -> list["T"]:
        """
        Returns a new array that contains the concatenated contents of two arrays.

        Arguments
        - first: the first array of elements to concatenate
        - second: the second array of elements to concatenate
        - type: the component type of the returned array
        """
        ...


    @staticmethod
    def concat(element: "T", array: list["T"]) -> list["T"]:
        """
        Returns a new array that prepends `element` to `array`.

        Arguments
        - element: the element to prepend to the front of `array`
        - array: the array of elements to append

        Returns
        - an array whose size is one larger than `array`, with
            `element` occupying the first position, and the
            elements of `array` occupying the remaining elements.
        """
        ...


    @staticmethod
    def concat(array: list["T"], element: "T") -> list["T"]:
        """
        Returns a new array that appends `element` to `array`.

        Arguments
        - array: the array of elements to prepend
        - element: the element to append to the end

        Returns
        - an array whose size is one larger than `array`, with
            the same contents as `array`, plus `element` occupying the
            last position.
        """
        ...
