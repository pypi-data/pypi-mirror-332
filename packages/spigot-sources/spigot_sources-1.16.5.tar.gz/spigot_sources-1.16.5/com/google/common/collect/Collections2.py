"""
Python module generated from Java source file com.google.common.collect.Collections2

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtCompatible
from com.google.common.base import Function
from com.google.common.base import Joiner
from com.google.common.base import Predicate
from com.google.common.base import Predicates
from com.google.common.collect import *
from com.google.common.math import IntMath
from com.google.common.primitives import Ints
from java.util import AbstractCollection
from java.util import Arrays
from java.util import Collections
from java.util import Comparator
from java.util import Iterator
from java.util import Spliterator
from java.util.function import Consumer
from javax.annotation import Nullable
from typing import Any, Callable, Iterable, Tuple


class Collections2:
    """
    Provides static methods for working with `Collection` instances.
    
    **Java 8 users:** several common uses for this class are now more comprehensively addressed
    by the new java.util.stream.Stream library. Read the method documentation below for
    comparisons. These methods are not being deprecated, but we gently encourage you to migrate to
    streams.

    Author(s)
    - Jared Levy

    Since
    - 2.0
    """

    @staticmethod
    def filter(unfiltered: Iterable["E"], predicate: "Predicate"["E"]) -> Iterable["E"]:
        ...


    @staticmethod
    def transform(fromCollection: Iterable["F"], function: "Function"["F", "T"]) -> Iterable["T"]:
        """
        Returns a collection that applies `function` to each element of
        `fromCollection`. The returned collection is a live view of `fromCollection`; changes to one affect the other.
        
        The returned collection's `add()` and `addAll()` methods
        throw an UnsupportedOperationException. All other collection
        methods are supported, as long as `fromCollection` supports them.
        
        The returned collection isn't threadsafe or serializable, even if
        `fromCollection` is.
        
        When a live view is *not* needed, it may be faster to copy the
        transformed collection and use the copy.
        
        If the input `Collection` is known to be a `List`, consider
        Lists.transform. If only an `Iterable` is available, use
        Iterables.transform.
        
        **`Stream` equivalent:** Stream.map.
        """
        ...


    @staticmethod
    def orderedPermutations(elements: Iterable["E"]) -> Iterable[list["E"]]:
        """
        Returns a Collection of all the permutations of the specified
        Iterable.
        
        *Notes:* This is an implementation of the algorithm for
        Lexicographical Permutations Generation, described in Knuth's "The Art of
        Computer Programming", Volume 4, Chapter 7, Section 7.2.1.2. The
        iteration order follows the lexicographical order. This means that
        the first permutation will be in ascending order, and the last will be in
        descending order.
        
        Duplicate elements are considered equal. For example, the list [1, 1]
        will have only one permutation, instead of two. This is why the elements
        have to implement Comparable.
        
        An empty iterable has only one permutation, which is an empty list.
        
        This method is equivalent to
        `Collections2.orderedPermutations(list, Ordering.natural())`.

        Arguments
        - elements: the original iterable whose elements have to be permuted.

        Returns
        - an immutable Collection containing all the different
            permutations of the original iterable.

        Raises
        - NullPointerException: if the specified iterable is null or has any
            null elements.

        Since
        - 12.0
        """
        ...


    @staticmethod
    def orderedPermutations(elements: Iterable["E"], comparator: "Comparator"["E"]) -> Iterable[list["E"]]:
        """
        Returns a Collection of all the permutations of the specified
        Iterable using the specified Comparator for establishing
        the lexicographical ordering.
        
        Examples: ```   `for (List<String> perm : orderedPermutations(asList("b", "c", "a"))) {
            println(perm);`
          // -> ["a", "b", "c"]
          // -> ["a", "c", "b"]
          // -> ["b", "a", "c"]
          // -> ["b", "c", "a"]
          // -> ["c", "a", "b"]
          // -> ["c", "b", "a"]
        
          for (List<Integer> perm : orderedPermutations(asList(1, 2, 2, 1))) {
            println(perm);
          }
          // -> [1, 1, 2, 2]
          // -> [1, 2, 1, 2]
          // -> [1, 2, 2, 1]
          // -> [2, 1, 1, 2]
          // -> [2, 1, 2, 1]
          // -> [2, 2, 1, 1]}```
        
        *Notes:* This is an implementation of the algorithm for
        Lexicographical Permutations Generation, described in Knuth's "The Art of
        Computer Programming", Volume 4, Chapter 7, Section 7.2.1.2. The
        iteration order follows the lexicographical order. This means that
        the first permutation will be in ascending order, and the last will be in
        descending order.
        
        Elements that compare equal are considered equal and no new permutations
        are created by swapping them.
        
        An empty iterable has only one permutation, which is an empty list.

        Arguments
        - elements: the original iterable whose elements have to be permuted.
        - comparator: a comparator for the iterable's elements.

        Returns
        - an immutable Collection containing all the different
            permutations of the original iterable.

        Raises
        - NullPointerException: If the specified iterable is null, has any
            null elements, or if the specified comparator is null.

        Since
        - 12.0
        """
        ...


    @staticmethod
    def permutations(elements: Iterable["E"]) -> Iterable[list["E"]]:
        """
        Returns a Collection of all the permutations of the specified
        Collection.
        
        *Notes:* This is an implementation of the Plain Changes algorithm
        for permutations generation, described in Knuth's "The Art of Computer
        Programming", Volume 4, Chapter 7, Section 7.2.1.2.
        
        If the input list contains equal elements, some of the generated
        permutations will be equal.
        
        An empty collection has only one permutation, which is an empty list.

        Arguments
        - elements: the original collection whose elements have to be permuted.

        Returns
        - an immutable Collection containing all the different
            permutations of the original collection.

        Raises
        - NullPointerException: if the specified collection is null or has any
            null elements.

        Since
        - 12.0
        """
        ...
