"""
Python module generated from Java source file com.google.common.collect.ImmutableMultiset

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import VisibleForTesting
from com.google.common.collect import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from com.google.errorprone.annotations import DoNotCall
from com.google.errorprone.annotations.concurrent import LazyInit
from com.google.j2objc.annotations import WeakOuter
from java.io import Serializable
from java.util import Arrays
from java.util import Collections
from java.util import Iterator
from java.util.function import Function
from java.util.function import ToIntFunction
from java.util.stream import Collector
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class ImmutableMultiset(ImmutableMultisetGwtSerializationDependencies, Multiset):
    """
    A Multiset whose contents will never change, with many other important properties
    detailed at ImmutableCollection.
    
    **Grouped iteration.** In all current implementations, duplicate elements always appear
    consecutively when iterating. Elements iterate in order by the *first* appearance of that
    element when the multiset was created.
    
    See the Guava User Guide article on <a href=
    "https://github.com/google/guava/wiki/ImmutableCollectionsExplained"> immutable collections</a>.

    Author(s)
    - Louis Wasserman

    Since
    - 2.0
    """

    @staticmethod
    def toImmutableMultiset() -> "Collector"["E", Any, "ImmutableMultiset"["E"]]:
        """
        Returns a `Collector` that accumulates the input elements into a new `ImmutableMultiset`. Elements iterate in order by the *first* appearance of that element in
        encounter order.

        Since
        - 21.0
        """
        ...


    @staticmethod
    def toImmutableMultiset(elementFunction: "Function"["T", "E"], countFunction: "ToIntFunction"["T"]) -> "Collector"["T", Any, "ImmutableMultiset"["E"]]:
        """
        Returns a `Collector` that accumulates elements into an `ImmutableMultiset` whose
        elements are the result of applying `elementFunction` to the inputs, with counts equal to
        the result of applying `countFunction` to the inputs.
        
        If the mapped elements contain duplicates (according to Object.equals), the first
        occurrence in encounter order appears in the resulting multiset, with count equal to the sum of
        the outputs of `countFunction.applyAsInt(t)` for each `t` mapped to that element.

        Since
        - 22.0
        """
        ...


    @staticmethod
    def of() -> "ImmutableMultiset"["E"]:
        """
        Returns the empty immutable multiset.
        
        **Performance note:** the instance returned is a singleton.
        """
        ...


    @staticmethod
    def of(element: "E") -> "ImmutableMultiset"["E"]:
        """
        Returns an immutable multiset containing a single element.

        Raises
        - NullPointerException: if `element` is null

        Since
        - 6.0 (source-compatible since 2.0)
        """
        ...


    @staticmethod
    def of(e1: "E", e2: "E") -> "ImmutableMultiset"["E"]:
        """
        Returns an immutable multiset containing the given elements, in order.

        Raises
        - NullPointerException: if any element is null

        Since
        - 6.0 (source-compatible since 2.0)
        """
        ...


    @staticmethod
    def of(e1: "E", e2: "E", e3: "E") -> "ImmutableMultiset"["E"]:
        """
        Returns an immutable multiset containing the given elements, in the "grouped iteration order"
        described in the class documentation.

        Raises
        - NullPointerException: if any element is null

        Since
        - 6.0 (source-compatible since 2.0)
        """
        ...


    @staticmethod
    def of(e1: "E", e2: "E", e3: "E", e4: "E") -> "ImmutableMultiset"["E"]:
        """
        Returns an immutable multiset containing the given elements, in the "grouped iteration order"
        described in the class documentation.

        Raises
        - NullPointerException: if any element is null

        Since
        - 6.0 (source-compatible since 2.0)
        """
        ...


    @staticmethod
    def of(e1: "E", e2: "E", e3: "E", e4: "E", e5: "E") -> "ImmutableMultiset"["E"]:
        """
        Returns an immutable multiset containing the given elements, in the "grouped iteration order"
        described in the class documentation.

        Raises
        - NullPointerException: if any element is null

        Since
        - 6.0 (source-compatible since 2.0)
        """
        ...


    @staticmethod
    def of(e1: "E", e2: "E", e3: "E", e4: "E", e5: "E", e6: "E", *others: Tuple["E", ...]) -> "ImmutableMultiset"["E"]:
        """
        Returns an immutable multiset containing the given elements, in the "grouped iteration order"
        described in the class documentation.

        Raises
        - NullPointerException: if any element is null

        Since
        - 6.0 (source-compatible since 2.0)
        """
        ...


    @staticmethod
    def copyOf(elements: list["E"]) -> "ImmutableMultiset"["E"]:
        """
        Returns an immutable multiset containing the given elements, in the "grouped iteration order"
        described in the class documentation.

        Raises
        - NullPointerException: if any of `elements` is null

        Since
        - 6.0
        """
        ...


    @staticmethod
    def copyOf(elements: Iterable["E"]) -> "ImmutableMultiset"["E"]:
        """
        Returns an immutable multiset containing the given elements, in the "grouped iteration order"
        described in the class documentation.

        Raises
        - NullPointerException: if any of `elements` is null
        """
        ...


    @staticmethod
    def copyOf(elements: Iterator["E"]) -> "ImmutableMultiset"["E"]:
        """
        Returns an immutable multiset containing the given elements, in the "grouped iteration order"
        described in the class documentation.

        Raises
        - NullPointerException: if any of `elements` is null
        """
        ...


    def iterator(self) -> "UnmodifiableIterator"["E"]:
        ...


    def asList(self) -> "ImmutableList"["E"]:
        ...


    def contains(self, object: "Object") -> bool:
        ...


    def add(self, element: "E", occurrences: int) -> int:
        """
        Guaranteed to throw an exception and leave the collection unmodified.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - Unsupported operation.
        """
        ...


    def remove(self, element: "Object", occurrences: int) -> int:
        """
        Guaranteed to throw an exception and leave the collection unmodified.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - Unsupported operation.
        """
        ...


    def setCount(self, element: "E", count: int) -> int:
        """
        Guaranteed to throw an exception and leave the collection unmodified.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - Unsupported operation.
        """
        ...


    def setCount(self, element: "E", oldCount: int, newCount: int) -> bool:
        """
        Guaranteed to throw an exception and leave the collection unmodified.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - Unsupported operation.
        """
        ...


    def equals(self, object: "Object") -> bool:
        ...


    def hashCode(self) -> int:
        ...


    def toString(self) -> str:
        ...


    def elementSet(self) -> "ImmutableSet"["E"]:
        """
        Since
        - 21.0 (present with return type `Set` since 2.0)
        """
        ...


    def entrySet(self) -> "ImmutableSet"["Entry"["E"]]:
        ...


    @staticmethod
    def builder() -> "Builder"["E"]:
        """
        Returns a new builder. The generated builder is equivalent to the builder created by the Builder constructor.
        """
        ...


    class Builder(Builder):
        """
        A builder for creating immutable multiset instances, especially `public static final`
        multisets ("constant multisets"). Example:
        
        ````public static final ImmutableMultiset<Bean> BEANS =
            new ImmutableMultiset.Builder<Bean>()
                .addCopies(Bean.COCOA, 4)
                .addCopies(Bean.GARDEN, 6)
                .addCopies(Bean.RED, 8)
                .addCopies(Bean.BLACK_EYED, 10)
                .build();````
        
        Builder instances can be reused; it is safe to call .build multiple times to build
        multiple multisets in series.

        Since
        - 2.0
        """

        def __init__(self):
            """
            Creates a new builder. The returned builder is equivalent to the builder generated by ImmutableMultiset.builder.
            """
            ...


        def add(self, element: "E") -> "Builder"["E"]:
            """
            Adds `element` to the `ImmutableMultiset`.

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
            Adds each element of `elements` to the `ImmutableMultiset`.

            Arguments
            - elements: the elements to add

            Returns
            - this `Builder` object

            Raises
            - NullPointerException: if `elements` is null or contains a null element
            """
            ...


        def addCopies(self, element: "E", occurrences: int) -> "Builder"["E"]:
            """
            Adds a number of occurrences of an element to this `ImmutableMultiset`.

            Arguments
            - element: the element to add
            - occurrences: the number of occurrences of the element to add. May be zero, in which
                case no change will be made.

            Returns
            - this `Builder` object

            Raises
            - NullPointerException: if `element` is null
            - IllegalArgumentException: if `occurrences` is negative, or if this operation
                would result in more than Integer.MAX_VALUE occurrences of the element
            """
            ...


        def setCount(self, element: "E", count: int) -> "Builder"["E"]:
            """
            Adds or removes the necessary occurrences of an element such that the element attains the
            desired count.

            Arguments
            - element: the element to add or remove occurrences of
            - count: the desired count of the element in this multiset

            Returns
            - this `Builder` object

            Raises
            - NullPointerException: if `element` is null
            - IllegalArgumentException: if `count` is negative
            """
            ...


        def addAll(self, elements: Iterable["E"]) -> "Builder"["E"]:
            """
            Adds each element of `elements` to the `ImmutableMultiset`.

            Arguments
            - elements: the `Iterable` to add to the `ImmutableMultiset`

            Returns
            - this `Builder` object

            Raises
            - NullPointerException: if `elements` is null or contains a null element
            """
            ...


        def addAll(self, elements: Iterator["E"]) -> "Builder"["E"]:
            """
            Adds each element of `elements` to the `ImmutableMultiset`.

            Arguments
            - elements: the elements to add to the `ImmutableMultiset`

            Returns
            - this `Builder` object

            Raises
            - NullPointerException: if `elements` is null or contains a null element
            """
            ...


        def build(self) -> "ImmutableMultiset"["E"]:
            """
            Returns a newly-created `ImmutableMultiset` based on the contents of the `Builder`.
            """
            ...
