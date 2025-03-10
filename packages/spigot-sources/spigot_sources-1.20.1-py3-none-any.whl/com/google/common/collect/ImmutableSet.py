"""
Python module generated from Java source file com.google.common.collect.ImmutableSet

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import VisibleForTesting
from com.google.common.collect import *
from com.google.common.math import IntMath
from com.google.common.primitives import Ints
from com.google.errorprone.annotations import CanIgnoreReturnValue
from com.google.errorprone.annotations.concurrent import LazyInit
from com.google.j2objc.annotations import RetainedWith
from java.io import Serializable
from java.math import RoundingMode
from java.util import Arrays
from java.util import Collections
from java.util import EnumSet
from java.util import Iterator
from java.util import SortedSet
from java.util import Spliterator
from java.util.function import Consumer
from java.util.stream import Collector
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class ImmutableSet(ImmutableCollection, Set):
    """
    A Set whose contents will never change, with many other important properties detailed at
    ImmutableCollection.

    Since
    - 2.0
    """

    @staticmethod
    def toImmutableSet() -> "Collector"["E", Any, "ImmutableSet"["E"]]:
        """
        Returns a `Collector` that accumulates the input elements into a new `ImmutableSet`. Elements appear in the resulting set in the encounter order of the stream; if
        the stream contains duplicates (according to Object.equals(Object)), only the first
        duplicate in encounter order will appear in the result.

        Since
        - 21.0
        """
        ...


    @staticmethod
    def of() -> "ImmutableSet"["E"]:
        """
        Returns the empty immutable set. Preferred over Collections.emptySet for code
        consistency, and because the return type conveys the immutability guarantee.
        
        **Performance note:** the instance returned is a singleton.
        """
        ...


    @staticmethod
    def of(element: "E") -> "ImmutableSet"["E"]:
        """
        Returns an immutable set containing `element`. Preferred over Collections.singleton for code consistency, `null` rejection, and because the return
        type conveys the immutability guarantee.
        """
        ...


    @staticmethod
    def of(e1: "E", e2: "E") -> "ImmutableSet"["E"]:
        """
        Returns an immutable set containing the given elements, minus duplicates, in the order each was
        first specified. That is, if multiple elements are Object.equals equal, all except
        the first are ignored.
        """
        ...


    @staticmethod
    def of(e1: "E", e2: "E", e3: "E") -> "ImmutableSet"["E"]:
        """
        Returns an immutable set containing the given elements, minus duplicates, in the order each was
        first specified. That is, if multiple elements are Object.equals equal, all except
        the first are ignored.
        """
        ...


    @staticmethod
    def of(e1: "E", e2: "E", e3: "E", e4: "E") -> "ImmutableSet"["E"]:
        """
        Returns an immutable set containing the given elements, minus duplicates, in the order each was
        first specified. That is, if multiple elements are Object.equals equal, all except
        the first are ignored.
        """
        ...


    @staticmethod
    def of(e1: "E", e2: "E", e3: "E", e4: "E", e5: "E") -> "ImmutableSet"["E"]:
        """
        Returns an immutable set containing the given elements, minus duplicates, in the order each was
        first specified. That is, if multiple elements are Object.equals equal, all except
        the first are ignored.
        """
        ...


    @staticmethod
    def of(e1: "E", e2: "E", e3: "E", e4: "E", e5: "E", e6: "E", *others: Tuple["E", ...]) -> "ImmutableSet"["E"]:
        """
        Returns an immutable set containing the given elements, minus duplicates, in the order each was
        first specified. That is, if multiple elements are Object.equals equal, all except
        the first are ignored.
        
        The array `others` must not be longer than `Integer.MAX_VALUE - 6`.

        Since
        - 3.0 (source-compatible since 2.0)
        """
        ...


    @staticmethod
    def copyOf(elements: Iterable["E"]) -> "ImmutableSet"["E"]:
        """
        Returns an immutable set containing each of `elements`, minus duplicates, in the order
        each appears first in the source collection.
        
        **Performance note:** This method will sometimes recognize that the actual copy operation
        is unnecessary; for example, `copyOf(copyOf(anArrayList))` will copy the data only once.
        This reduces the expense of habitually making defensive copies at API boundaries. However, the
        precise conditions for skipping the copy operation are undefined.

        Raises
        - NullPointerException: if any of `elements` is null

        Since
        - 7.0 (source-compatible since 2.0)
        """
        ...


    @staticmethod
    def copyOf(elements: Iterable["E"]) -> "ImmutableSet"["E"]:
        """
        Returns an immutable set containing each of `elements`, minus duplicates, in the order
        each appears first in the source iterable. This method iterates over `elements` only
        once.
        
        **Performance note:** This method will sometimes recognize that the actual copy operation
        is unnecessary; for example, `copyOf(copyOf(anArrayList))` should copy the data only
        once. This reduces the expense of habitually making defensive copies at API boundaries.
        However, the precise conditions for skipping the copy operation are undefined.

        Raises
        - NullPointerException: if any of `elements` is null
        """
        ...


    @staticmethod
    def copyOf(elements: Iterator["E"]) -> "ImmutableSet"["E"]:
        """
        Returns an immutable set containing each of `elements`, minus duplicates, in the order
        each appears first in the source iterator.

        Raises
        - NullPointerException: if any of `elements` is null
        """
        ...


    @staticmethod
    def copyOf(elements: list["E"]) -> "ImmutableSet"["E"]:
        """
        Returns an immutable set containing each of `elements`, minus duplicates, in the order
        each appears first in the source array.

        Raises
        - NullPointerException: if any of `elements` is null

        Since
        - 3.0
        """
        ...


    def equals(self, object: "Object") -> bool:
        ...


    def hashCode(self) -> int:
        ...


    def iterator(self) -> "UnmodifiableIterator"["E"]:
        ...


    @staticmethod
    def builder() -> "Builder"["E"]:
        """
        Returns a new builder. The generated builder is equivalent to the builder created by the Builder constructor.
        """
        ...


    @staticmethod
    def builderWithExpectedSize(expectedSize: int) -> "Builder"["E"]:
        """
        Returns a new builder, expecting the specified number of distinct elements to be added.
        
        If `expectedSize` is exactly the number of distinct elements added to the builder
        before Builder.build is called, the builder is likely to perform better than an unsized
        .builder() would have.
        
        It is not specified if any performance benefits apply if `expectedSize` is close to,
        but not exactly, the number of distinct elements added to the builder.

        Since
        - 23.1
        """
        ...


    class Builder(Builder):
        """
        A builder for creating `ImmutableSet` instances. Example:
        
        ````static final ImmutableSet<Color> GOOGLE_COLORS =
            ImmutableSet.<Color>builder()
                .addAll(WEBSAFE_COLORS)
                .add(new Color(0, 191, 255))
                .build();````
        
        Elements appear in the resulting set in the same order they were first added to the builder.
        
        Building does not change the state of the builder, so it is still possible to add more
        elements and to build again.

        Since
        - 2.0
        """

        def __init__(self):
            ...


        def add(self, element: "E") -> "Builder"["E"]:
            ...


        def add(self, *elements: Tuple["E", ...]) -> "Builder"["E"]:
            ...


        def addAll(self, elements: Iterable["E"]) -> "Builder"["E"]:
            """
            Adds each element of `elements` to the `ImmutableSet`, ignoring duplicate
            elements (only the first duplicate element is added).

            Arguments
            - elements: the elements to add

            Returns
            - this `Builder` object

            Raises
            - NullPointerException: if `elements` is null or contains a null element
            """
            ...


        def addAll(self, elements: Iterator["E"]) -> "Builder"["E"]:
            ...


        def build(self) -> "ImmutableSet"["E"]:
            ...
