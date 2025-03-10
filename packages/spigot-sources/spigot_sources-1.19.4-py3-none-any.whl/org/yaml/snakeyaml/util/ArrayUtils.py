"""
Python module generated from Java source file org.yaml.snakeyaml.util.ArrayUtils

Java source file obtained from artifact snakeyaml version 1.33

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import AbstractList
from java.util import Collections
from org.yaml.snakeyaml.util import *
from typing import Any, Callable, Iterable, Tuple


class ArrayUtils:
    """
    Array manipulation
    """

    @staticmethod
    def toUnmodifiableList(elements: list["E"]) -> list["E"]:
        """
        Returns an unmodifiable `List` backed by the given array. The method doesn't copy the
        array, so the changes to the array will affect the `List` as well.
        
        Type `<E>`: class of the elements in the array

        Arguments
        - elements: - array to convert

        Returns
        - `List` backed by the given array
        """
        ...


    @staticmethod
    def toUnmodifiableCompositeList(array1: list["E"], array2: list["E"]) -> list["E"]:
        """
        Returns an unmodifiable `List` containing the second array appended to the first one. The
        method doesn't copy the arrays, so the changes to the arrays will affect the `List` as
        well.
        
        Type `<E>`: class of the elements in the array

        Arguments
        - array1: - the array to extend
        - array2: - the array to add to the first

        Returns
        - `List` backed by the given arrays
        """
        ...
