"""
Python module generated from Java source file com.google.common.collect.Ordering

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import VisibleForTesting
from com.google.common.base import Function
from com.google.common.collect import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.util import Arrays
from java.util import Collections
from java.util import Comparator
from java.util import Iterator
from java.util import NoSuchElementException
from java.util import SortedMap
from java.util import SortedSet
from java.util.concurrent import ConcurrentMap
from java.util.concurrent.atomic import AtomicInteger
from javax.annotation import Nullable
from typing import Any, Callable, Iterable, Tuple


class Ordering(Comparator):
    """
    A comparator, with additional methods to support common operations. This is an "enriched" version
    of `Comparator` for pre-Java-8 users, in the same sense that FluentIterable is an
    enriched Iterable for pre-Java-8 users.
    
    <h3>Three types of methods</h3>
    
    Like other fluent types, there are three types of methods present: methods for *acquiring*,
    *chaining*, and *using*.
    
    <h4>Acquiring</h4>
    
    The common ways to get an instance of `Ordering` are:
    
    
    - Subclass it and implement .compare instead of implementing Comparator
        directly
    - Pass a *pre-existing* Comparator instance to .from(Comparator)
    - Use the natural ordering, Ordering.natural
    
    
    <h4>Chaining</h4>
    
    Then you can use the *chaining* methods to get an altered version of that `Ordering`, including:
    
    
    - .reverse
    - .compound(Comparator)
    - .onResultOf(Function)
    - .nullsFirst / .nullsLast
    
    
    <h4>Using</h4>
    
    Finally, use the resulting `Ordering` anywhere a Comparator is required, or use
    any of its special operations, such as:
    
    
    - .immutableSortedCopy
    - .isOrdered / .isStrictlyOrdered
    - .min / .max
    
    
    <h3>Understanding complex orderings</h3>
    
    Complex chained orderings like the following example can be challenging to understand.
    
    ````Ordering<Foo> ordering =
        Ordering.natural()
            .nullsFirst()
            .onResultOf(getBarFunction)
            .nullsLast();````
    
    Note that each chaining method returns a new ordering instance which is backed by the previous
    instance, but has the chance to act on values *before* handing off to that backing instance.
    As a result, it usually helps to read chained ordering expressions *backwards*. For example,
    when `compare` is called on the above ordering:
    
    <ol>
    - First, if only one `Foo` is null, that null value is treated as *greater*
    - Next, non-null `Foo` values are passed to `getBarFunction` (we will be comparing
        `Bar` values from now on)
    - Next, if only one `Bar` is null, that null value is treated as *lesser*
    - Finally, natural ordering is used (i.e. the result of `Bar.compareTo(Bar)` is returned)
    </ol>
    
    Alas, .reverse is a little different. As you read backwards through a chain and
    encounter a call to `reverse`, continue working backwards until a result is determined, and
    then reverse that result.
    
    <h3>Additional notes</h3>
    
    Except as noted, the orderings returned by the factory methods of this class are serializable
    if and only if the provided instances that back them are. For example, if `ordering` and
    `function` can themselves be serialized, then `ordering.onResultOf(function)` can as
    well.
    
    <h3>For Java 8 users</h3>
    
    If you are using Java 8, this class is now obsolete *(pending a few August 2016
    updates)*. Most of its functionality is now provided by Stream and by Comparator itself, and the rest can now be found as static methods in our new Comparators class. See each method below for further instructions. Whenever possible, you should
    change any references of type `Ordering` to be of type `Comparator` instead. However,
    at this time we have no plan to *deprecate* this class.
    
    Many replacements involve adopting `Stream`, and these changes can sometimes make your
    code verbose. Whenever following this advice, you should check whether `Stream` could be
    adopted more comprehensively in your code; the end result may be quite a bit simpler.
    
    <h3>See also</h3>
    
    See the Guava User Guide article on <a href=
    "https://github.com/google/guava/wiki/OrderingExplained">`Ordering`</a>.

    Author(s)
    - Kevin Bourrillion

    Since
    - 2.0
    """

    @staticmethod
    def natural() -> "Ordering"["C"]:
        """
        Returns a serializable ordering that uses the natural order of the values. The ordering throws
        a NullPointerException when passed a null parameter.
        
        The type specification is `<C extends Comparable>`, instead of the technically correct
        `<C extends Comparable<? super C>>`, to support legacy types from before Java 5.
        
        **Java 8 users:** use Comparator.naturalOrder instead.
        """
        ...


    @staticmethod
    def from(comparator: "Comparator"["T"]) -> "Ordering"["T"]:
        """
        Returns an ordering based on an *existing* comparator instance. Note that it is
        unnecessary to create a *new* anonymous inner class implementing `Comparator` just
        to pass it in here. Instead, simply subclass `Ordering` and implement its `compare`
        method directly.
        
        **Java 8 users:** this class is now obsolete as explained in the class documentation, so
        there is no need to use this method.

        Arguments
        - comparator: the comparator that defines the order

        Returns
        - comparator itself if it is already an `Ordering`; otherwise an ordering that
            wraps that comparator
        """
        ...


    @staticmethod
    def from(ordering: "Ordering"["T"]) -> "Ordering"["T"]:
        """
        Simply returns its argument.

        Deprecated
        - no need to use this
        """
        ...


    @staticmethod
    def explicit(valuesInOrder: list["T"]) -> "Ordering"["T"]:
        ...


    @staticmethod
    def explicit(leastValue: "T", *remainingValuesInOrder: Tuple["T", ...]) -> "Ordering"["T"]:
        ...


    @staticmethod
    def allEqual() -> "Ordering"["Object"]:
        """
        Returns an ordering which treats all values as equal, indicating "no ordering." Passing this
        ordering to any *stable* sort algorithm results in no change to the order of elements.
        Note especially that .sortedCopy and .immutableSortedCopy are stable, and in
        the returned instance these are implemented by simply copying the source list.
        
        Example:
        
        ````Ordering.allEqual().nullsLast().sortedCopy(
            asList(t, null, e, s, null, t, null))````
        
        Assuming `t`, `e` and `s` are non-null, this returns `[t, e, s, t,
        null, null, null]` regardless of the True comparison order of those three values (which might
        not even implement Comparable at all).
        
        **Warning:** by definition, this comparator is not *consistent with equals* (as
        defined Comparator here). Avoid its use in APIs, such as TreeSet.TreeSet(Comparator), where such consistency is expected.
        
        The returned comparator is serializable.
        
        **Java 8 users:** Use the lambda expression `(a, b) -> 0` instead (in certain cases
        you may need to cast that to `Comparator<YourType>`).

        Since
        - 13.0
        """
        ...


    @staticmethod
    def usingToString() -> "Ordering"["Object"]:
        """
        Returns an ordering that compares objects by the natural ordering of their string
        representations as returned by `toString()`. It does not support null values.
        
        The comparator is serializable.
        
        **Java 8 users:** Use `Comparator.comparing(Object::toString)` instead.
        """
        ...


    @staticmethod
    def arbitrary() -> "Ordering"["Object"]:
        ...


    def reverse(self) -> "Ordering"["S"]:
        ...


    def nullsFirst(self) -> "Ordering"["S"]:
        ...


    def nullsLast(self) -> "Ordering"["S"]:
        ...


    def onResultOf(self, function: "Function"["F", "T"]) -> "Ordering"["F"]:
        """
        Returns a new ordering on `F` which orders elements by first applying a function to them,
        then comparing those results using `this`. For example, to compare objects by their
        string forms, in a case-insensitive manner, use:
        
        ````Ordering.from(String.CASE_INSENSITIVE_ORDER)
            .onResultOf(Functions.toStringFunction())````
        
        **Java 8 users:** Use `Comparator.comparing(function, thisComparator)` instead (you
        can omit the comparator if it is the natural order).
        """
        ...


    def compound(self, secondaryComparator: "Comparator"["U"]) -> "Ordering"["U"]:
        """
        Returns an ordering which first uses the ordering `this`, but which in the event of a
        "tie", then delegates to `secondaryComparator`. For example, to sort a bug list first by
        status and second by priority, you might use `byStatus.compound(byPriority)`. For a
        compound ordering with three or more components, simply chain multiple calls to this method.
        
        An ordering produced by this method, or a chain of calls to this method, is equivalent to
        one created using Ordering.compound(Iterable) on the same component comparators.
        
        **Java 8 users:** Use `thisComparator.thenComparing(secondaryComparator)` instead.
        Depending on what `secondaryComparator` is, one of the other overloads of `thenComparing` may be even more useful.
        """
        ...


    @staticmethod
    def compound(comparators: Iterable["Comparator"["T"]]) -> "Ordering"["T"]:
        """
        Returns an ordering which tries each given comparator in order until a non-zero result is
        found, returning that result, and returning zero only if all comparators return zero. The
        returned ordering is based on the state of the `comparators` iterable at the time it was
        provided to this method.
        
        The returned ordering is equivalent to that produced using `Ordering.from(comp1).compound(comp2).compound(comp3) . . .`.
        
        **Warning:** Supplying an argument with undefined iteration order, such as a HashSet, will produce non-deterministic results.
        
        **Java 8 users:** Use a chain of calls to Comparator.thenComparing(Comparator),
        or `comparatorCollection.stream().reduce(Comparator::thenComparing).get()` (if the
        collection might be empty, also provide a default comparator as the `identity` parameter
        to `reduce`).

        Arguments
        - comparators: the comparators to try in order
        """
        ...


    def lexicographical(self) -> "Ordering"[Iterable["S"]]:
        """
        Returns a new ordering which sorts iterables by comparing corresponding elements pairwise until
        a nonzero result is found; imposes "dictionary order". If the end of one iterable is reached,
        but not the other, the shorter iterable is considered to be less than the longer one. For
        example, a lexicographical natural ordering over integers considers `[] < [1] < [1, 1] <
        [1, 2] < [2]`.
        
        Note that `ordering.lexicographical().reverse()` is not equivalent to `ordering.reverse().lexicographical()` (consider how each would order `[1]` and `[1,
        1]`).
        
        **Java 8 users:** Use Comparators.lexicographical(Comparator) instead.

        Since
        - 2.0
        """
        ...


    def compare(self, left: "T", right: "T") -> int:
        ...


    def min(self, iterator: Iterator["E"]) -> "E":
        """
        Returns the least of the specified values according to this ordering. If there are multiple
        least values, the first of those is returned. The iterator will be left exhausted: its `hasNext()` method will return `False`.
        
        **Java 8 users:** Continue to use this method for now. After the next release of Guava,
        use `Streams.stream(iterator).min(thisComparator).get()` instead (but note that it does
        not guarantee which tied minimum element is returned).

        Arguments
        - iterator: the iterator whose minimum element is to be determined

        Raises
        - NoSuchElementException: if `iterator` is empty
        - ClassCastException: if the parameters are not *mutually comparable* under this
            ordering.

        Since
        - 11.0
        """
        ...


    def min(self, iterable: Iterable["E"]) -> "E":
        """
        Returns the least of the specified values according to this ordering. If there are multiple
        least values, the first of those is returned.
        
        **Java 8 users:** If `iterable` is a Collection, use `Collections.min(collection, thisComparator)` instead. Otherwise, continue to use this method
        for now. After the next release of Guava, use `Streams.stream(iterable).min(thisComparator).get()` instead. Note that these alternatives do
        not guarantee which tied minimum element is returned)

        Arguments
        - iterable: the iterable whose minimum element is to be determined

        Raises
        - NoSuchElementException: if `iterable` is empty
        - ClassCastException: if the parameters are not *mutually comparable* under this
            ordering.
        """
        ...


    def min(self, a: "E", b: "E") -> "E":
        """
        Returns the lesser of the two values according to this ordering. If the values compare as 0,
        the first is returned.
        
        **Implementation note:** this method is invoked by the default implementations of the
        other `min` overloads, so overriding it will affect their behavior.
        
        **Java 8 users:** Use `Collections.min(Arrays.asList(a, b), thisComparator)`
        instead (but note that it does not guarantee which tied maximum element is returned).

        Arguments
        - a: value to compare, returned if less than or equal to b.
        - b: value to compare.

        Raises
        - ClassCastException: if the parameters are not *mutually comparable* under this
            ordering.
        """
        ...


    def min(self, a: "E", b: "E", c: "E", *rest: Tuple["E", ...]) -> "E":
        """
        Returns the least of the specified values according to this ordering. If there are multiple
        least values, the first of those is returned.
        
        **Java 8 users:** Use `Collections.min(Arrays.asList(a, b, c...), thisComparator)`
        instead (but note that it does not guarantee which tied maximum element is returned).

        Arguments
        - a: value to compare, returned if less than or equal to the rest.
        - b: value to compare
        - c: value to compare
        - rest: values to compare

        Raises
        - ClassCastException: if the parameters are not *mutually comparable* under this
            ordering.
        """
        ...


    def max(self, iterator: Iterator["E"]) -> "E":
        """
        Returns the greatest of the specified values according to this ordering. If there are multiple
        greatest values, the first of those is returned. The iterator will be left exhausted: its
        `hasNext()` method will return `False`.
        
        **Java 8 users:** Continue to use this method for now. After the next release of Guava,
        use `Streams.stream(iterator).max(thisComparator).get()` instead (but note that it does
        not guarantee which tied maximum element is returned).

        Arguments
        - iterator: the iterator whose maximum element is to be determined

        Raises
        - NoSuchElementException: if `iterator` is empty
        - ClassCastException: if the parameters are not *mutually comparable* under this
            ordering.

        Since
        - 11.0
        """
        ...


    def max(self, iterable: Iterable["E"]) -> "E":
        """
        Returns the greatest of the specified values according to this ordering. If
        there are multiple greatest values, the first of those is returned.
        
        **Java 8 users:** If `iterable` is a Collection, use `Collections.max(collection, thisComparator)` instead. Otherwise, continue to use this method
        for now. After the next release of Guava, use `Streams.stream(iterable).max(thisComparator).get()` instead. Note that these alternatives do
        not guarantee which tied maximum element is returned)

        Arguments
        - iterable: the iterable whose maximum element is to be determined

        Raises
        - NoSuchElementException: if `iterable` is empty
        - ClassCastException: if the parameters are not *mutually
            comparable* under this ordering.
        """
        ...


    def max(self, a: "E", b: "E") -> "E":
        """
        Returns the greater of the two values according to this ordering. If the values compare as 0,
        the first is returned.
        
        **Implementation note:** this method is invoked by the default implementations of the
        other `max` overloads, so overriding it will affect their behavior.
        
        **Java 8 users:** Use `Collections.max(Arrays.asList(a, b), thisComparator)`
        instead (but note that it does not guarantee which tied maximum element is returned).

        Arguments
        - a: value to compare, returned if greater than or equal to b.
        - b: value to compare.

        Raises
        - ClassCastException: if the parameters are not *mutually comparable* under this
            ordering.
        """
        ...


    def max(self, a: "E", b: "E", c: "E", *rest: Tuple["E", ...]) -> "E":
        """
        Returns the greatest of the specified values according to this ordering. If there are multiple
        greatest values, the first of those is returned.
        
        **Java 8 users:** Use `Collections.max(Arrays.asList(a, b, c...), thisComparator)`
        instead (but note that it does not guarantee which tied maximum element is returned).

        Arguments
        - a: value to compare, returned if greater than or equal to the rest.
        - b: value to compare
        - c: value to compare
        - rest: values to compare

        Raises
        - ClassCastException: if the parameters are not *mutually comparable* under this
            ordering.
        """
        ...


    def leastOf(self, iterable: Iterable["E"], k: int) -> list["E"]:
        """
        Returns the `k` least elements of the given iterable according to this ordering, in order
        from least to greatest. If there are fewer than `k` elements present, all will be
        included.
        
        The implementation does not necessarily use a *stable* sorting algorithm; when multiple
        elements are equivalent, it is undefined which will come first.
        
        **Java 8 users:** Use `Streams.stream(iterable).collect(Comparators.least(k,
        thisComparator))` instead.

        Returns
        - an immutable `RandomAccess` list of the `k` least elements in ascending
            order

        Raises
        - IllegalArgumentException: if `k` is negative

        Since
        - 8.0
        """
        ...


    def leastOf(self, iterator: Iterator["E"], k: int) -> list["E"]:
        """
        Returns the `k` least elements from the given iterator according to this ordering, in
        order from least to greatest. If there are fewer than `k` elements present, all will be
        included.
        
        The implementation does not necessarily use a *stable* sorting algorithm; when multiple
        elements are equivalent, it is undefined which will come first.
        
        **Java 8 users:** Continue to use this method for now. After the next release of Guava,
        use `Streams.stream(iterator).collect(Comparators.least(k, thisComparator))` instead.

        Returns
        - an immutable `RandomAccess` list of the `k` least elements in ascending
            order

        Raises
        - IllegalArgumentException: if `k` is negative

        Since
        - 14.0
        """
        ...


    def greatestOf(self, iterable: Iterable["E"], k: int) -> list["E"]:
        """
        Returns the `k` greatest elements of the given iterable according to this ordering, in
        order from greatest to least. If there are fewer than `k` elements present, all will be
        included.
        
        The implementation does not necessarily use a *stable* sorting algorithm; when multiple
        elements are equivalent, it is undefined which will come first.
        
        **Java 8 users:** Use `Streams.stream(iterable).collect(Comparators.greatest(k,
        thisComparator))` instead.

        Returns
        - an immutable `RandomAccess` list of the `k` greatest elements in
            *descending order*

        Raises
        - IllegalArgumentException: if `k` is negative

        Since
        - 8.0
        """
        ...


    def greatestOf(self, iterator: Iterator["E"], k: int) -> list["E"]:
        """
        Returns the `k` greatest elements from the given iterator according to this ordering, in
        order from greatest to least. If there are fewer than `k` elements present, all will be
        included.
        
        The implementation does not necessarily use a *stable* sorting algorithm; when multiple
        elements are equivalent, it is undefined which will come first.
        
        **Java 8 users:** Continue to use this method for now. After the next release of Guava,
        use `Streams.stream(iterator).collect(Comparators.greatest(k, thisComparator))` instead.

        Returns
        - an immutable `RandomAccess` list of the `k` greatest elements in
            *descending order*

        Raises
        - IllegalArgumentException: if `k` is negative

        Since
        - 14.0
        """
        ...


    def sortedCopy(self, elements: Iterable["E"]) -> list["E"]:
        ...


    def immutableSortedCopy(self, elements: Iterable["E"]) -> "ImmutableList"["E"]:
        ...


    def isOrdered(self, iterable: Iterable["T"]) -> bool:
        """
        Returns `True` if each element in `iterable` after the first is greater than or
        equal to the element that preceded it, according to this ordering. Note that this is always
        True when the iterable has fewer than two elements.
        
        **Java 8 users:** Use the equivalent Comparators.isInOrder(Iterable) instead,
        since the rest of `Ordering` is mostly obsolete (as explained in the class
        documentation).
        """
        ...


    def isStrictlyOrdered(self, iterable: Iterable["T"]) -> bool:
        """
        Returns `True` if each element in `iterable` after the first is *strictly*
        greater than the element that preceded it, according to this ordering. Note that this is always
        True when the iterable has fewer than two elements.
        
        **Java 8 users:** Use the equivalent Comparators.isInStrictOrder(Iterable)
        instead, since the rest of `Ordering` is mostly obsolete (as explained in the class
        documentation).
        """
        ...


    def binarySearch(self, sortedList: list["T"], key: "T") -> int:
        """
        Collections.binarySearch(List, Object, Comparator) Searches
        `sortedList` for `key` using the binary search algorithm. The
        list must be sorted using this ordering.

        Arguments
        - sortedList: the list to be searched
        - key: the key to be searched for

        Deprecated
        - Use Collections.binarySearch(List, Object, Comparator) directly. This
        method is scheduled for deletion in June 2018.
        """
        ...
