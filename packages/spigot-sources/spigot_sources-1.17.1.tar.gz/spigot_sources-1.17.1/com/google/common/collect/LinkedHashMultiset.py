"""
Python module generated from Java source file com.google.common.collect.LinkedHashMultiset

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


class LinkedHashMultiset(AbstractMapBasedMultiset):
    """
    A `Multiset` implementation with predictable iteration order. Its
    iterator orders elements according to when the first occurrence of the
    element was added. When the multiset contains multiple instances of an
    element, those instances are consecutive in the iteration order. If all
    occurrences of an element are removed, after which that element is added to
    the multiset, the element will appear at the end of the iteration.
    
    See the Guava User Guide article on <a href=
    "https://github.com/google/guava/wiki/NewCollectionTypesExplained#multiset">
    `Multiset`</a>.

    Author(s)
    - Jared Levy

    Since
    - 2.0
    """

    @staticmethod
    def create() -> "LinkedHashMultiset"["E"]:
        """
        Creates a new, empty `LinkedHashMultiset` using the default initial
        capacity.
        """
        ...


    @staticmethod
    def create(distinctElements: int) -> "LinkedHashMultiset"["E"]:
        """
        Creates a new, empty `LinkedHashMultiset` with the specified expected
        number of distinct elements.

        Arguments
        - distinctElements: the expected number of distinct elements

        Raises
        - IllegalArgumentException: if `distinctElements` is negative
        """
        ...


    @staticmethod
    def create(elements: Iterable["E"]) -> "LinkedHashMultiset"["E"]:
        """
        Creates a new `LinkedHashMultiset` containing the specified elements.
        
        This implementation is highly efficient when `elements` is itself
        a Multiset.

        Arguments
        - elements: the elements that the multiset should contain
        """
        ...
