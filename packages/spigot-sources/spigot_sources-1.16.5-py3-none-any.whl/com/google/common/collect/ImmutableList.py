"""
Python module generated from Java source file com.google.common.collect.ImmutableList

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtCompatible
from com.google.common.collect import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.io import InvalidObjectException
from java.io import ObjectInputStream
from java.io import Serializable
from java.util import Arrays
from java.util import Collections
from java.util import Comparator
from java.util import Iterator
from java.util import RandomAccess
from java.util import Spliterator
from java.util.function import Consumer
from java.util.function import UnaryOperator
from java.util.stream import Collector
from javax.annotation import Nullable
from typing import Any, Callable, Iterable, Tuple


class ImmutableList(ImmutableCollection, List, RandomAccess):
    """
    A List whose contents will never change, with many other important properties detailed at
    ImmutableCollection.
    
    See the Guava User Guide article on <a href=
    "https://github.com/google/guava/wiki/ImmutableCollectionsExplained">
    immutable collections</a>.

    Author(s)
    - Kevin Bourrillion

    See
    - ImmutableSet

    Since
    - 2.0
    """

    @staticmethod
    def toImmutableList() -> "Collector"["E", Any, "ImmutableList"["E"]]:
        """
        Returns a `Collector` that accumulates the input elements into a new
        `ImmutableList`, in encounter order.

        Since
        - 21.0
        """
        ...


    @staticmethod
    def of() -> "ImmutableList"["E"]:
        ...


    @staticmethod
    def of(element: "E") -> "ImmutableList"["E"]:
        """
        Returns an immutable list containing a single element. This list behaves
        and performs comparably to Collections.singleton, but will not
        accept a null element. It is preferable mainly for consistency and
        maintainability of your code.

        Raises
        - NullPointerException: if `element` is null
        """
        ...


    @staticmethod
    def of(e1: "E", e2: "E") -> "ImmutableList"["E"]:
        """
        Returns an immutable list containing the given elements, in order.

        Raises
        - NullPointerException: if any element is null
        """
        ...


    @staticmethod
    def of(e1: "E", e2: "E", e3: "E") -> "ImmutableList"["E"]:
        """
        Returns an immutable list containing the given elements, in order.

        Raises
        - NullPointerException: if any element is null
        """
        ...


    @staticmethod
    def of(e1: "E", e2: "E", e3: "E", e4: "E") -> "ImmutableList"["E"]:
        """
        Returns an immutable list containing the given elements, in order.

        Raises
        - NullPointerException: if any element is null
        """
        ...


    @staticmethod
    def of(e1: "E", e2: "E", e3: "E", e4: "E", e5: "E") -> "ImmutableList"["E"]:
        """
        Returns an immutable list containing the given elements, in order.

        Raises
        - NullPointerException: if any element is null
        """
        ...


    @staticmethod
    def of(e1: "E", e2: "E", e3: "E", e4: "E", e5: "E", e6: "E") -> "ImmutableList"["E"]:
        """
        Returns an immutable list containing the given elements, in order.

        Raises
        - NullPointerException: if any element is null
        """
        ...


    @staticmethod
    def of(e1: "E", e2: "E", e3: "E", e4: "E", e5: "E", e6: "E", e7: "E") -> "ImmutableList"["E"]:
        """
        Returns an immutable list containing the given elements, in order.

        Raises
        - NullPointerException: if any element is null
        """
        ...


    @staticmethod
    def of(e1: "E", e2: "E", e3: "E", e4: "E", e5: "E", e6: "E", e7: "E", e8: "E") -> "ImmutableList"["E"]:
        """
        Returns an immutable list containing the given elements, in order.

        Raises
        - NullPointerException: if any element is null
        """
        ...


    @staticmethod
    def of(e1: "E", e2: "E", e3: "E", e4: "E", e5: "E", e6: "E", e7: "E", e8: "E", e9: "E") -> "ImmutableList"["E"]:
        """
        Returns an immutable list containing the given elements, in order.

        Raises
        - NullPointerException: if any element is null
        """
        ...


    @staticmethod
    def of(e1: "E", e2: "E", e3: "E", e4: "E", e5: "E", e6: "E", e7: "E", e8: "E", e9: "E", e10: "E") -> "ImmutableList"["E"]:
        """
        Returns an immutable list containing the given elements, in order.

        Raises
        - NullPointerException: if any element is null
        """
        ...


    @staticmethod
    def of(e1: "E", e2: "E", e3: "E", e4: "E", e5: "E", e6: "E", e7: "E", e8: "E", e9: "E", e10: "E", e11: "E") -> "ImmutableList"["E"]:
        """
        Returns an immutable list containing the given elements, in order.

        Raises
        - NullPointerException: if any element is null
        """
        ...


    @staticmethod
    def of(e1: "E", e2: "E", e3: "E", e4: "E", e5: "E", e6: "E", e7: "E", e8: "E", e9: "E", e10: "E", e11: "E", e12: "E", *others: Tuple["E", ...]) -> "ImmutableList"["E"]:
        """
        Returns an immutable list containing the given elements, in order.

        Raises
        - NullPointerException: if any element is null

        Since
        - 3.0 (source-compatible since 2.0)
        """
        ...


    @staticmethod
    def copyOf(elements: Iterable["E"]) -> "ImmutableList"["E"]:
        """
        Returns an immutable list containing the given elements, in order. If
        `elements` is a Collection, this method behaves exactly as
        .copyOf(Collection); otherwise, it behaves exactly as `copyOf(elements.iterator()`.

        Raises
        - NullPointerException: if any of `elements` is null
        """
        ...


    @staticmethod
    def copyOf(elements: Iterable["E"]) -> "ImmutableList"["E"]:
        """
        Returns an immutable list containing the given elements, in order.
        
        Despite the method name, this method attempts to avoid actually copying
        the data when it is safe to do so. The exact circumstances under which a
        copy will or will not be performed are undocumented and subject to change.
        
        Note that if `list` is a `List<String>`, then `ImmutableList.copyOf(list)` returns an `ImmutableList<String>`
        containing each of the strings in `list`, while
        ImmutableList.of(list)} returns an `ImmutableList<List<String>>`
        containing one element (the given list itself).
        
        This method is safe to use even when `elements` is a synchronized
        or concurrent collection that is currently being modified by another
        thread.

        Raises
        - NullPointerException: if any of `elements` is null
        """
        ...


    @staticmethod
    def copyOf(elements: Iterator["E"]) -> "ImmutableList"["E"]:
        """
        Returns an immutable list containing the given elements, in order.

        Raises
        - NullPointerException: if any of `elements` is null
        """
        ...


    @staticmethod
    def copyOf(elements: list["E"]) -> "ImmutableList"["E"]:
        """
        Returns an immutable list containing the given elements, in order.

        Raises
        - NullPointerException: if any of `elements` is null

        Since
        - 3.0
        """
        ...


    @staticmethod
    def sortedCopyOf(elements: Iterable["E"]) -> "ImmutableList"["E"]:
        """
        Returns an immutable list containing the given elements, sorted according to their natural
        order. The sorting algorithm used is stable, so elements that compare as equal will stay in the
        order in which they appear in the input.
        
        If your data has no duplicates, or you wish to deduplicate elements, use `ImmutableSortedSet.copyOf(elements)`; if you want a `List` you can use its `asList()` view.
        
        **Java 8 users:** If you want to convert a java.util.stream.Stream to a sorted
        `ImmutableList`, use `stream.sorted().collect(toImmutableList())`.

        Raises
        - NullPointerException: if any element in the input is null

        Since
        - 21.0
        """
        ...


    @staticmethod
    def sortedCopyOf(comparator: "Comparator"["E"], elements: Iterable["E"]) -> "ImmutableList"["E"]:
        """
        Returns an immutable list containing the given elements, in sorted order relative to the
        specified comparator. The sorting algorithm used is stable, so elements that compare as equal
        will stay in the order in which they appear in the input.
        
        If your data has no duplicates, or you wish to deduplicate elements, use `ImmutableSortedSet.copyOf(comparator, elements)`; if you want a `List` you can use its
        `asList()` view.
        
        **Java 8 users:** If you want to convert a java.util.stream.Stream to a sorted
        `ImmutableList`, use `stream.sorted(comparator).collect(toImmutableList())`.

        Raises
        - NullPointerException: if any element in the input is null

        Since
        - 21.0
        """
        ...


    def iterator(self) -> "UnmodifiableIterator"["E"]:
        ...


    def listIterator(self) -> "UnmodifiableListIterator"["E"]:
        ...


    def listIterator(self, index: int) -> "UnmodifiableListIterator"["E"]:
        ...


    def forEach(self, consumer: "Consumer"["E"]) -> None:
        ...


    def indexOf(self, object: "Object") -> int:
        ...


    def lastIndexOf(self, object: "Object") -> int:
        ...


    def contains(self, object: "Object") -> bool:
        ...


    def subList(self, fromIndex: int, toIndex: int) -> "ImmutableList"["E"]:
        """
        Returns an immutable list of the elements between the specified `fromIndex`, inclusive, and `toIndex`, exclusive. (If `fromIndex` and `toIndex` are equal, the empty immutable list is
        returned.)
        """
        ...


    def addAll(self, index: int, newElements: Iterable["E"]) -> bool:
        """
        Guaranteed to throw an exception and leave the list unmodified.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - Unsupported operation.
        """
        ...


    def set(self, index: int, element: "E") -> "E":
        """
        Guaranteed to throw an exception and leave the list unmodified.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - Unsupported operation.
        """
        ...


    def add(self, index: int, element: "E") -> None:
        """
        Guaranteed to throw an exception and leave the list unmodified.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - Unsupported operation.
        """
        ...


    def remove(self, index: int) -> "E":
        """
        Guaranteed to throw an exception and leave the list unmodified.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - Unsupported operation.
        """
        ...


    def replaceAll(self, operator: "UnaryOperator"["E"]) -> None:
        """
        Guaranteed to throw an exception and leave the list unmodified.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - Unsupported operation.
        """
        ...


    def sort(self, c: "Comparator"["E"]) -> None:
        """
        Guaranteed to throw an exception and leave the list unmodified.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - Unsupported operation.
        """
        ...


    def asList(self) -> "ImmutableList"["E"]:
        """
        Returns this list instance.

        Since
        - 2.0
        """
        ...


    def spliterator(self) -> "Spliterator"["E"]:
        ...


    def reverse(self) -> "ImmutableList"["E"]:
        """
        Returns a view of this immutable list in reverse order. For example, `ImmutableList.of(1, 2, 3).reverse()` is equivalent to `ImmutableList.of(3, 2, 1)`.

        Returns
        - a view of this immutable list in reverse order

        Since
        - 7.0
        """
        ...


    def equals(self, obj: "Object") -> bool:
        ...


    def hashCode(self) -> int:
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
        A builder for creating immutable list instances, especially `public
        static final` lists ("constant lists"). Example: ```   `public static final ImmutableList<Color> GOOGLE_COLORS
              = new ImmutableList.Builder<Color>()
                  .addAll(WEBSAFE_COLORS)
                  .add(new Color(0, 191, 255))
                  .build();````
        
        Builder instances can be reused; it is safe to call .build multiple
        times to build multiple lists in series. Each new list contains all the
        elements of the ones created before it.

        Since
        - 2.0
        """

        def __init__(self):
            """
            Creates a new builder. The returned builder is equivalent to the builder
            generated by ImmutableList.builder.
            """
            ...


        def add(self, element: "E") -> "Builder"["E"]:
            """
            Adds `element` to the `ImmutableList`.

            Arguments
            - element: the element to add

            Returns
            - this `Builder` object

            Raises
            - NullPointerException: if `element` is null
            """
            ...


        def addAll(self, elements: Iterable["E"]) -> "Builder"["E"]:
            """
            Adds each element of `elements` to the `ImmutableList`.

            Arguments
            - elements: the `Iterable` to add to the `ImmutableList`

            Returns
            - this `Builder` object

            Raises
            - NullPointerException: if `elements` is null or contains a
                null element
            """
            ...


        def add(self, *elements: Tuple["E", ...]) -> "Builder"["E"]:
            """
            Adds each element of `elements` to the `ImmutableList`.

            Arguments
            - elements: the `Iterable` to add to the `ImmutableList`

            Returns
            - this `Builder` object

            Raises
            - NullPointerException: if `elements` is null or contains a
                null element
            """
            ...


        def addAll(self, elements: Iterator["E"]) -> "Builder"["E"]:
            """
            Adds each element of `elements` to the `ImmutableList`.

            Arguments
            - elements: the `Iterable` to add to the `ImmutableList`

            Returns
            - this `Builder` object

            Raises
            - NullPointerException: if `elements` is null or contains a
                null element
            """
            ...


        def build(self) -> "ImmutableList"["E"]:
            """
            Returns a newly-created `ImmutableList` based on the contents of
            the `Builder`.
            """
            ...
