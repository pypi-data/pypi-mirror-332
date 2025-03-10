"""
Python module generated from Java source file com.google.gson.internal.LinkedTreeMap

Java source file obtained from artifact gson version 2.8.9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson.internal import *
from java.io import IOException
from java.io import InvalidObjectException
from java.io import ObjectInputStream
from java.io import ObjectStreamException
from java.io import Serializable
from java.util import AbstractSet
from java.util import Comparator
from java.util import ConcurrentModificationException
from java.util import Iterator
from java.util import NoSuchElementException
from typing import Any, Callable, Iterable, Tuple


class LinkedTreeMap(AbstractMap, Serializable):
    """
    A map of comparable keys to values. Unlike `TreeMap`, this class uses
    insertion order for iteration order. Comparison order is only used as an
    optimization for efficient insertion and removal.
    
    This implementation was derived from Android 4.1's TreeMap class.
    """

    def __init__(self):
        """
        Create a natural order, empty tree map whose keys must be mutually
        comparable and non-null.
        """
        ...


    def __init__(self, comparator: "Comparator"["K"]):
        """
        Create a tree map ordered by `comparator`. This map's keys may only
        be null if `comparator` permits.

        Arguments
        - comparator: the comparator to order elements with, or `null` to
            use the natural ordering.
        """
        ...


    def size(self) -> int:
        ...


    def get(self, key: "Object") -> "V":
        ...


    def containsKey(self, key: "Object") -> bool:
        ...


    def put(self, key: "K", value: "V") -> "V":
        ...


    def clear(self) -> None:
        ...


    def remove(self, key: "Object") -> "V":
        ...


    def entrySet(self) -> set["Entry"["K", "V"]]:
        ...


    def keySet(self) -> set["K"]:
        ...
