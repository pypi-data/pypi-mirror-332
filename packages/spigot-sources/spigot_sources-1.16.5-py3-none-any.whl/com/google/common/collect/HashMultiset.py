"""
Python module generated from Java source file com.google.common.collect.HashMultiset

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import GwtIncompatible
from com.google.common.collect import *
from java.io import IOException
from java.io import ObjectInputStream
from java.io import ObjectOutputStream
from typing import Any, Callable, Iterable, Tuple


class HashMultiset(AbstractMapBasedMultiset):
    """
    Multiset implementation backed by a HashMap.

    Author(s)
    - Jared Levy

    Since
    - 2.0
    """

    @staticmethod
    def create() -> "HashMultiset"["E"]:
        """
        Creates a new, empty `HashMultiset` using the default initial
        capacity.
        """
        ...


    @staticmethod
    def create(distinctElements: int) -> "HashMultiset"["E"]:
        """
        Creates a new, empty `HashMultiset` with the specified expected
        number of distinct elements.

        Arguments
        - distinctElements: the expected number of distinct elements

        Raises
        - IllegalArgumentException: if `distinctElements` is negative
        """
        ...


    @staticmethod
    def create(elements: Iterable["E"]) -> "HashMultiset"["E"]:
        """
        Creates a new `HashMultiset` containing the specified elements.
        
        This implementation is highly efficient when `elements` is itself
        a Multiset.

        Arguments
        - elements: the elements that the multiset should contain
        """
        ...
