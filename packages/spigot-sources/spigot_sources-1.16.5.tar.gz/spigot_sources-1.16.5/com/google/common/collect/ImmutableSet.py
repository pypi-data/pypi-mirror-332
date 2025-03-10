"""
Python module generated from Java source file com.google.common.collect.ImmutableSet

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import VisibleForTesting
from com.google.common.collect import *
from com.google.common.primitives import Ints
from com.google.errorprone.annotations import CanIgnoreReturnValue
from com.google.errorprone.annotations.concurrent import LazyInit
from com.google.j2objc.annotations import RetainedWith
from java.io import Serializable
from java.util import Arrays
from java.util import Collections
from java.util import EnumSet
from java.util import Iterator
from java.util import Spliterator
from java.util.function import Consumer
from java.util.stream import Collector
from javax.annotation import Nullable
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
        Returns a `Collector` that accumulates the input elements into a new
        `ImmutableSet`.  Elements are added in encounter order; if the
        elements contain duplicates (according to Object.equals(Object)),
        only the first duplicate in encounter order will appear in the result.

        Since
        - 21.0
        """
        ...


    @staticmethod
    def of() -> "ImmutableSet"["E"]:
        """
        Returns the empty immutable set. Preferred over Collections.emptySet for code
        consistency, and because the return type conveys the immutability guarantee.
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


    def asList(self) -> "ImmutableList"["E"]:
        ...


    @staticmethod
    def builder() -> "Builder"["E"]:
        """
        Returns a new builder. The generated builder is equivalent to the builder
        created by the Builder constructor.
        """
        ...


    class Builder(ArrayBasedBuilder):
        """
        A builder for creating `ImmutableSet` instances. Example: ```   `static final ImmutableSet<Color> GOOGLE_COLORS =
              ImmutableSet.<Color>builder()
                  .addAll(WEBSAFE_COLORS)
                  .add(new Color(0, 191, 255))
                  .build();````
        
        Building does not change the state of the builder, so it is still possible to add more
        elements and to build again.

        Since
        - 2.0
        """

        def __init__(self):
            """
            Creates a new builder. The returned builder is equivalent to the builder
            generated by ImmutableSet.builder.
            """
            ...


        def add(self, element: "E") -> "Builder"["E"]:
            """
            Adds `element` to the `ImmutableSet`.  If the `ImmutableSet` already contains `element`, then `add` has no
            effect (only the previously added element is retained).

            Arguments
            - element: the element to add

            Returns
            - this `Builder` object

            Raises
            - NullPointerException: if `element` is null
            """
            ...


        def add(self, *elements: Tuple["E", ...]) -> "Builder"["E"]:
            """
            Adds each element of `elements` to the `ImmutableSet`,
            ignoring duplicate elements (only the first duplicate element is added).

            Arguments
            - elements: the elements to add

            Returns
            - this `Builder` object

            Raises
            - NullPointerException: if `elements` is null or contains a
                null element
            """
            ...


        def addAll(self, elements: Iterable["E"]) -> "Builder"["E"]:
            """
            Adds each element of `elements` to the `ImmutableSet`,
            ignoring duplicate elements (only the first duplicate element is added).

            Arguments
            - elements: the `Iterable` to add to the `ImmutableSet`

            Returns
            - this `Builder` object

            Raises
            - NullPointerException: if `elements` is null or contains a
                null element
            """
            ...


        def addAll(self, elements: Iterator["E"]) -> "Builder"["E"]:
            """
            Adds each element of `elements` to the `ImmutableSet`,
            ignoring duplicate elements (only the first duplicate element is added).

            Arguments
            - elements: the elements to add to the `ImmutableSet`

            Returns
            - this `Builder` object

            Raises
            - NullPointerException: if `elements` is null or contains a
                null element
            """
            ...


        def build(self) -> "ImmutableSet"["E"]:
            """
            Returns a newly-created `ImmutableSet` based on the contents of
            the `Builder`.
            """
            ...
