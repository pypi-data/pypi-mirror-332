"""
Python module generated from Java source file com.google.common.collect.Lists

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import VisibleForTesting
from com.google.common.base import Function
from com.google.common.base import Objects
from com.google.common.collect import *
from com.google.common.math import IntMath
from com.google.common.primitives import Ints
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.io import Serializable
from java.math import RoundingMode
from java.util import AbstractList
from java.util import AbstractSequentialList
from java.util import Arrays
from java.util import Collections
from java.util import Iterator
from java.util import ListIterator
from java.util import NoSuchElementException
from java.util import RandomAccess
from java.util.concurrent import CopyOnWriteArrayList
from java.util.function import Predicate
from javax.annotation import Nullable
from typing import Any, Callable, Iterable, Tuple


class Lists:
    """
    Static utility methods pertaining to List instances. Also see this
    class's counterparts Sets, Maps and Queues.
    
    See the Guava User Guide article on <a href=
    "https://github.com/google/guava/wiki/CollectionUtilitiesExplained#lists">
    `Lists`</a>.

    Author(s)
    - Louis Wasserman

    Since
    - 2.0
    """

    @staticmethod
    def newArrayList() -> list["E"]:
        """
        Creates a *mutable*, empty `ArrayList` instance (for Java 6 and
        earlier).
        
        **Note:** if mutability is not required, use ImmutableList.of() instead.
        
        **Note for Java 7 and later:** this method is now unnecessary and
        should be treated as deprecated. Instead, use the `ArrayList`
        ArrayList.ArrayList() constructor directly, taking advantage
        of the new <a href="http://goo.gl/iz2Wi">"diamond" syntax</a>.
        """
        ...


    @staticmethod
    def newArrayList(*elements: Tuple["E", ...]) -> list["E"]:
        """
        Creates a *mutable* `ArrayList` instance containing the given
        elements.
        
        **Note:** essentially the only reason to use this method is when you
        will need to add or remove elements later. Otherwise, for non-null elements
        use ImmutableList.of() (for varargs) or ImmutableList.copyOf(Object[]) (for an array) instead. If any elements
        might be null, or you need support for List.set(int, Object), use
        Arrays.asList.
        
        Note that even when you do need the ability to add or remove, this method
        provides only a tiny bit of syntactic sugar for `newArrayList(`Arrays.asList asList`(...))`, or for creating an empty list then
        calling Collections.addAll. This method is not actually very useful
        and will likely be deprecated in the future.
        """
        ...


    @staticmethod
    def newArrayList(elements: Iterable["E"]) -> list["E"]:
        """
        Creates a *mutable* `ArrayList` instance containing the given
        elements; a very thin shortcut for creating an empty list then calling
        Iterables.addAll.
        
        **Note:** if mutability is not required and the elements are
        non-null, use ImmutableList.copyOf(Iterable) instead. (Or, change
        `elements` to be a FluentIterable and call
        `elements.toList()`.)
        
        **Note for Java 7 and later:** if `elements` is a Collection, you don't need this method. Use the `ArrayList`
        ArrayList.ArrayList(Collection) constructor directly, taking
        advantage of the new <a href="http://goo.gl/iz2Wi">"diamond" syntax</a>.
        """
        ...


    @staticmethod
    def newArrayList(elements: Iterator["E"]) -> list["E"]:
        """
        Creates a *mutable* `ArrayList` instance containing the given
        elements; a very thin shortcut for creating an empty list and then calling
        Iterators.addAll.
        
        **Note:** if mutability is not required and the elements are
        non-null, use ImmutableList.copyOf(Iterator) instead.
        """
        ...


    @staticmethod
    def newArrayListWithCapacity(initialArraySize: int) -> list["E"]:
        """
        Creates an `ArrayList` instance backed by an array with the specified
        initial size; simply delegates to ArrayList.ArrayList(int).
        
        **Note for Java 7 and later:** this method is now unnecessary and
        should be treated as deprecated. Instead, use `new`ArrayList.ArrayList(int) ArrayList`<>(int)` directly, taking
        advantage of the new <a href="http://goo.gl/iz2Wi">"diamond" syntax</a>.
        (Unlike here, there is no risk of overload ambiguity, since the `ArrayList` constructors very wisely did not accept varargs.)

        Arguments
        - initialArraySize: the exact size of the initial backing array for
            the returned array list (`ArrayList` documentation calls this
            value the "capacity")

        Returns
        - a new, empty `ArrayList` which is guaranteed not to resize
            itself unless its size reaches `initialArraySize + 1`

        Raises
        - IllegalArgumentException: if `initialArraySize` is negative
        """
        ...


    @staticmethod
    def newArrayListWithExpectedSize(estimatedSize: int) -> list["E"]:
        """
        Creates an `ArrayList` instance to hold `estimatedSize`
        elements, *plus* an unspecified amount of padding; you almost
        certainly mean to call .newArrayListWithCapacity (see that method
        for further advice on usage).
        
        **Note:** This method will soon be deprecated. Even in the rare case
        that you do want some amount of padding, it's best if you choose your
        desired amount explicitly.

        Arguments
        - estimatedSize: an estimate of the eventual List.size() of
            the new list

        Returns
        - a new, empty `ArrayList`, sized appropriately to hold the
            estimated number of elements

        Raises
        - IllegalArgumentException: if `estimatedSize` is negative
        """
        ...


    @staticmethod
    def newLinkedList() -> list["E"]:
        """
        Creates a *mutable*, empty `LinkedList` instance (for Java 6 and
        earlier).
        
        **Note:** if you won't be adding any elements to the list, use ImmutableList.of() instead.
        
        **Performance note:** ArrayList and java.util.ArrayDeque consistently outperform `LinkedList` except in
        certain rare and specific situations. Unless you have spent a lot of time
        benchmarking your specific needs, use one of those instead.
        
        **Note for Java 7 and later:** this method is now unnecessary and
        should be treated as deprecated. Instead, use the `LinkedList`
        LinkedList.LinkedList() constructor directly, taking advantage
        of the new <a href="http://goo.gl/iz2Wi">"diamond" syntax</a>.
        """
        ...


    @staticmethod
    def newLinkedList(elements: Iterable["E"]) -> list["E"]:
        """
        Creates a *mutable* `LinkedList` instance containing the given
        elements; a very thin shortcut for creating an empty list then calling
        Iterables.addAll.
        
        **Note:** if mutability is not required and the elements are
        non-null, use ImmutableList.copyOf(Iterable) instead. (Or, change
        `elements` to be a FluentIterable and call
        `elements.toList()`.)
        
        **Performance note:** ArrayList and java.util.ArrayDeque consistently outperform `LinkedList` except in
        certain rare and specific situations. Unless you have spent a lot of time
        benchmarking your specific needs, use one of those instead.
        
        **Note for Java 7 and later:** if `elements` is a Collection, you don't need this method. Use the `LinkedList`
        LinkedList.LinkedList(Collection) constructor directly, taking
        advantage of the new <a href="http://goo.gl/iz2Wi">"diamond" syntax</a>.
        """
        ...


    @staticmethod
    def newCopyOnWriteArrayList() -> "CopyOnWriteArrayList"["E"]:
        """
        Creates an empty `CopyOnWriteArrayList` instance.
        
        **Note:** if you need an immutable empty List, use
        Collections.emptyList instead.

        Returns
        - a new, empty `CopyOnWriteArrayList`

        Since
        - 12.0
        """
        ...


    @staticmethod
    def newCopyOnWriteArrayList(elements: Iterable["E"]) -> "CopyOnWriteArrayList"["E"]:
        """
        Creates a `CopyOnWriteArrayList` instance containing the given elements.

        Arguments
        - elements: the elements that the list should contain, in order

        Returns
        - a new `CopyOnWriteArrayList` containing those elements

        Since
        - 12.0
        """
        ...


    @staticmethod
    def asList(first: "E", rest: list["E"]) -> list["E"]:
        """
        Returns an unmodifiable list containing the specified first element and
        backed by the specified array of additional elements. Changes to the `rest` array will be reflected in the returned list. Unlike Arrays.asList, the returned list is unmodifiable.
        
        This is useful when a varargs method needs to use a signature such as
        `(Foo firstFoo, Foo... moreFoos)`, in order to avoid overload
        ambiguity or to enforce a minimum argument count.
        
        The returned list is serializable and implements RandomAccess.

        Arguments
        - first: the first element
        - rest: an array of additional elements, possibly empty

        Returns
        - an unmodifiable list containing the specified elements
        """
        ...


    @staticmethod
    def asList(first: "E", second: "E", rest: list["E"]) -> list["E"]:
        """
        Returns an unmodifiable list containing the specified first and second
        element, and backed by the specified array of additional elements. Changes
        to the `rest` array will be reflected in the returned list. Unlike
        Arrays.asList, the returned list is unmodifiable.
        
        This is useful when a varargs method needs to use a signature such as
        `(Foo firstFoo, Foo secondFoo, Foo... moreFoos)`, in order to avoid
        overload ambiguity or to enforce a minimum argument count.
        
        The returned list is serializable and implements RandomAccess.

        Arguments
        - first: the first element
        - second: the second element
        - rest: an array of additional elements, possibly empty

        Returns
        - an unmodifiable list containing the specified elements
        """
        ...


    @staticmethod
    def cartesianProduct(lists: list[list["B"]]) -> list[list["B"]]:
        """
        Returns every possible list that can be formed by choosing one element
        from each of the given lists in order; the "n-ary
        <a href="http://en.wikipedia.org/wiki/Cartesian_product">Cartesian
        product</a>" of the lists. For example: ```   `Lists.cartesianProduct(ImmutableList.of(
              ImmutableList.of(1, 2),
              ImmutableList.of("A", "B", "C")))````
        
        returns a list containing six lists in the following order:
        
        
        - `ImmutableList.of(1, "A")`
        - `ImmutableList.of(1, "B")`
        - `ImmutableList.of(1, "C")`
        - `ImmutableList.of(2, "A")`
        - `ImmutableList.of(2, "B")`
        - `ImmutableList.of(2, "C")`
        
        
        The result is guaranteed to be in the "traditional", lexicographical
        order for Cartesian products that you would get from nesting for loops:
        ```   `for (B b0 : lists.get(0)) {
            for (B b1 : lists.get(1)) {
              ...
              ImmutableList<B> tuple = ImmutableList.of(b0, b1, ...);
              // operate on tuple`
          }}```
        
        Note that if any input list is empty, the Cartesian product will also be
        empty. If no lists at all are provided (an empty list), the resulting
        Cartesian product has one element, an empty list (counter-intuitive, but
        mathematically consistent).
        
        *Performance notes:* while the cartesian product of lists of size
        `m, n, p` is a list of size `m x n x p`, its actual memory
        consumption is much smaller. When the cartesian product is constructed, the
        input lists are merely copied. Only as the resulting list is iterated are
        the individual lists created, and these are not retained after iteration.
        
        Type `<B>`: any common base class shared by all axes (often just Object)

        Arguments
        - lists: the lists to choose elements from, in the order that
            the elements chosen from those lists should appear in the resulting
            lists

        Returns
        - the Cartesian product, as an immutable list containing immutable
            lists

        Raises
        - IllegalArgumentException: if the size of the cartesian product would
            be greater than Integer.MAX_VALUE
        - NullPointerException: if `lists`, any one of the `lists`,
            or any element of a provided list is null

        Since
        - 19.0
        """
        ...


    @staticmethod
    def cartesianProduct(*lists: Tuple[list["B"], ...]) -> list[list["B"]]:
        """
        Returns every possible list that can be formed by choosing one element
        from each of the given lists in order; the "n-ary
        <a href="http://en.wikipedia.org/wiki/Cartesian_product">Cartesian
        product</a>" of the lists. For example: ```   `Lists.cartesianProduct(ImmutableList.of(
              ImmutableList.of(1, 2),
              ImmutableList.of("A", "B", "C")))````
        
        returns a list containing six lists in the following order:
        
        
        - `ImmutableList.of(1, "A")`
        - `ImmutableList.of(1, "B")`
        - `ImmutableList.of(1, "C")`
        - `ImmutableList.of(2, "A")`
        - `ImmutableList.of(2, "B")`
        - `ImmutableList.of(2, "C")`
        
        
        The result is guaranteed to be in the "traditional", lexicographical
        order for Cartesian products that you would get from nesting for loops:
        ```   `for (B b0 : lists.get(0)) {
            for (B b1 : lists.get(1)) {
              ...
              ImmutableList<B> tuple = ImmutableList.of(b0, b1, ...);
              // operate on tuple`
          }}```
        
        Note that if any input list is empty, the Cartesian product will also be
        empty. If no lists at all are provided (an empty list), the resulting
        Cartesian product has one element, an empty list (counter-intuitive, but
        mathematically consistent).
        
        *Performance notes:* while the cartesian product of lists of size
        `m, n, p` is a list of size `m x n x p`, its actual memory
        consumption is much smaller. When the cartesian product is constructed, the
        input lists are merely copied. Only as the resulting list is iterated are
        the individual lists created, and these are not retained after iteration.
        
        Type `<B>`: any common base class shared by all axes (often just Object)

        Arguments
        - lists: the lists to choose elements from, in the order that
            the elements chosen from those lists should appear in the resulting
            lists

        Returns
        - the Cartesian product, as an immutable list containing immutable
            lists

        Raises
        - IllegalArgumentException: if the size of the cartesian product would
            be greater than Integer.MAX_VALUE
        - NullPointerException: if `lists`, any one of the
            `lists`, or any element of a provided list is null

        Since
        - 19.0
        """
        ...


    @staticmethod
    def transform(fromList: list["F"], function: "Function"["F", "T"]) -> list["T"]:
        """
        Returns a list that applies `function` to each element of `fromList`. The returned list is a transformed view of `fromList`;
        changes to `fromList` will be reflected in the returned list and vice
        versa.
        
        Since functions are not reversible, the transform is one-way and new
        items cannot be stored in the returned list. The `add`,
        `addAll` and `set` methods are unsupported in the returned
        list.
        
        The function is applied lazily, invoked when needed. This is necessary
        for the returned list to be a view, but it means that the function will be
        applied many times for bulk operations like List.contains and
        List.hashCode. For this to perform well, `function` should be
        fast. To avoid lazy evaluation when the returned list doesn't need to be a
        view, copy the returned list into a new list of your choosing.
        
        If `fromList` implements RandomAccess, so will the
        returned list. The returned list is threadsafe if the supplied list and
        function are.
        
        If only a `Collection` or `Iterable` input is available, use
        Collections2.transform or Iterables.transform.
        
        **Note:** serializing the returned list is implemented by serializing
        `fromList`, its contents, and `function` -- *not* by
        serializing the transformed values. This can lead to surprising behavior,
        so serializing the returned list is **not recommended**. Instead,
        copy the list using ImmutableList.copyOf(Collection) (for example),
        then serialize the copy. Other methods similar to this do not implement
        serialization at all for this reason.
        
        **Java 8 users:** many use cases for this method are better addressed
         by java.util.stream.Stream.map. This method is not being
        deprecated, but we gently encourage you to migrate to streams.
        """
        ...


    @staticmethod
    def partition(list: list["T"], size: int) -> list[list["T"]]:
        """
        Returns consecutive List.subList(int, int) sublists of a list,
        each of the same size (the final list may be smaller). For example,
        partitioning a list containing `[a, b, c, d, e]` with a partition
        size of 3 yields `[[a, b, c], [d, e]]` -- an outer list containing
        two inner lists of three and two elements, all in the original order.
        
        The outer list is unmodifiable, but reflects the latest state of the
        source list. The inner lists are sublist views of the original list,
        produced on demand using List.subList(int, int), and are subject
        to all the usual caveats about modification as explained in that API.

        Arguments
        - list: the list to return consecutive sublists of
        - size: the desired size of each sublist (the last may be
            smaller)

        Returns
        - a list of consecutive sublists

        Raises
        - IllegalArgumentException: if `partitionSize` is nonpositive
        """
        ...


    @staticmethod
    def charactersOf(string: str) -> "ImmutableList"["Character"]:
        """
        Returns a view of the specified string as an immutable list of `Character` values.

        Since
        - 7.0
        """
        ...


    @staticmethod
    def charactersOf(sequence: "CharSequence") -> list["Character"]:
        """
        Returns a view of the specified `CharSequence` as a `List<Character>`, viewing `sequence` as a sequence of Unicode code
        units. The view does not support any modification operations, but reflects
        any changes to the underlying character sequence.

        Arguments
        - sequence: the character sequence to view as a `List` of
               characters

        Returns
        - an `List<Character>` view of the character sequence

        Since
        - 7.0
        """
        ...


    @staticmethod
    def reverse(list: list["T"]) -> list["T"]:
        """
        Returns a reversed view of the specified list. For example, `Lists.reverse(Arrays.asList(1, 2, 3))` returns a list containing `3,
        2, 1`. The returned list is backed by this list, so changes in the returned
        list are reflected in this list, and vice-versa. The returned list supports
        all of the optional list operations supported by this list.
        
        The returned list is random-access if the specified list is random
        access.

        Since
        - 7.0
        """
        ...
