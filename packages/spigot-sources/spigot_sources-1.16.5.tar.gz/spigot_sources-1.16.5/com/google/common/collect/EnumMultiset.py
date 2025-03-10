"""
Python module generated from Java source file com.google.common.collect.EnumMultiset

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
from java.util import EnumMap
from java.util import Iterator
from typing import Any, Callable, Iterable, Tuple


class EnumMultiset(AbstractMapBasedMultiset):
    """
    Multiset implementation backed by an EnumMap.
    
    See the Guava User Guide article on <a href=
    "https://github.com/google/guava/wiki/NewCollectionTypesExplained#multiset">
    `Multiset`</a>.

    Author(s)
    - Jared Levy

    Since
    - 2.0
    """

    @staticmethod
    def create(type: type["E"]) -> "EnumMultiset"["E"]:
        """
        Creates an empty `EnumMultiset`.
        """
        ...


    @staticmethod
    def create(elements: Iterable["E"]) -> "EnumMultiset"["E"]:
        """
        Creates a new `EnumMultiset` containing the specified elements.
        
        This implementation is highly efficient when `elements` is itself a Multiset.

        Arguments
        - elements: the elements that the multiset should contain

        Raises
        - IllegalArgumentException: if `elements` is empty
        """
        ...


    @staticmethod
    def create(elements: Iterable["E"], type: type["E"]) -> "EnumMultiset"["E"]:
        """
        Returns a new `EnumMultiset` instance containing the given elements.  Unlike
        EnumMultiset.create(Iterable), this method does not produce an exception on an empty
        iterable.

        Since
        - 14.0
        """
        ...
