"""
Python module generated from Java source file java.util.LinkedHashSet

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import *
from typing import Any, Callable, Iterable, Tuple


class LinkedHashSet(HashSet, Set, Cloneable, Serializable):

    def __init__(self, initialCapacity: int, loadFactor: float):
        """
        Constructs a new, empty linked hash set with the specified initial
        capacity and load factor.

        Arguments
        - initialCapacity: the initial capacity of the linked hash set
        - loadFactor: the load factor of the linked hash set

        Raises
        - IllegalArgumentException: if the initial capacity is less
                      than zero, or if the load factor is nonpositive
        """
        ...


    def __init__(self, initialCapacity: int):
        """
        Constructs a new, empty linked hash set with the specified initial
        capacity and the default load factor (0.75).

        Arguments
        - initialCapacity: the initial capacity of the LinkedHashSet

        Raises
        - IllegalArgumentException: if the initial capacity is less
                     than zero
        """
        ...


    def __init__(self):
        """
        Constructs a new, empty linked hash set with the default initial
        capacity (16) and load factor (0.75).
        """
        ...


    def __init__(self, c: Iterable["E"]):
        """
        Constructs a new linked hash set with the same elements as the
        specified collection.  The linked hash set is created with an initial
        capacity sufficient to hold the elements in the specified collection
        and the default load factor (0.75).

        Arguments
        - c: the collection whose elements are to be placed into
                  this set

        Raises
        - NullPointerException: if the specified collection is null
        """
        ...


    def spliterator(self) -> "Spliterator"["E"]:
        """
        Creates a *<a href="Spliterator.html#binding">late-binding</a>*
        and *fail-fast* `Spliterator` over the elements in this set.
        
        The `Spliterator` reports Spliterator.SIZED,
        Spliterator.DISTINCT, and `ORDERED`.  Implementations
        should document the reporting of additional characteristic values.

        Returns
        - a `Spliterator` over the elements in this set

        Since
        - 1.8

        Unknown Tags
        - The implementation creates a
        *<a href="Spliterator.html#binding">late-binding</a>* spliterator
        from the set's `Iterator`.  The spliterator inherits the
        *fail-fast* properties of the set's iterator.
        The created `Spliterator` additionally reports
        Spliterator.SUBSIZED.
        """
        ...
