"""
Python module generated from Java source file java.util.SortedSet

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import *
from typing import Any, Callable, Iterable, Tuple


class SortedSet(Set):

    def comparator(self) -> "Comparator"["E"]:
        """
        Returns the comparator used to order the elements in this set,
        or `null` if this set uses the Comparable
        natural ordering of its elements.

        Returns
        - the comparator used to order the elements in this set,
                or `null` if this set uses the natural ordering
                of its elements
        """
        ...


    def subSet(self, fromElement: "E", toElement: "E") -> "SortedSet"["E"]:
        """
        Returns a view of the portion of this set whose elements range
        from `fromElement`, inclusive, to `toElement`,
        exclusive.  (If `fromElement` and `toElement` are
        equal, the returned set is empty.)  The returned set is backed
        by this set, so changes in the returned set are reflected in
        this set, and vice-versa.  The returned set supports all
        optional set operations that this set supports.
        
        The returned set will throw an `IllegalArgumentException`
        on an attempt to insert an element outside its range.

        Arguments
        - fromElement: low endpoint (inclusive) of the returned set
        - toElement: high endpoint (exclusive) of the returned set

        Returns
        - a view of the portion of this set whose elements range from
                `fromElement`, inclusive, to `toElement`, exclusive

        Raises
        - ClassCastException: if `fromElement` and
                `toElement` cannot be compared to one another using this
                set's comparator (or, if the set has no comparator, using
                natural ordering).  Implementations may, but are not required
                to, throw this exception if `fromElement` or
                `toElement` cannot be compared to elements currently in
                the set.
        - NullPointerException: if `fromElement` or
                `toElement` is null and this set does not permit null
                elements
        - IllegalArgumentException: if `fromElement` is
                greater than `toElement`; or if this set itself
                has a restricted range, and `fromElement` or
                `toElement` lies outside the bounds of the range
        """
        ...


    def headSet(self, toElement: "E") -> "SortedSet"["E"]:
        """
        Returns a view of the portion of this set whose elements are
        strictly less than `toElement`.  The returned set is
        backed by this set, so changes in the returned set are
        reflected in this set, and vice-versa.  The returned set
        supports all optional set operations that this set supports.
        
        The returned set will throw an `IllegalArgumentException`
        on an attempt to insert an element outside its range.

        Arguments
        - toElement: high endpoint (exclusive) of the returned set

        Returns
        - a view of the portion of this set whose elements are strictly
                less than `toElement`

        Raises
        - ClassCastException: if `toElement` is not compatible
                with this set's comparator (or, if the set has no comparator,
                if `toElement` does not implement Comparable).
                Implementations may, but are not required to, throw this
                exception if `toElement` cannot be compared to elements
                currently in the set.
        - NullPointerException: if `toElement` is null and
                this set does not permit null elements
        - IllegalArgumentException: if this set itself has a
                restricted range, and `toElement` lies outside the
                bounds of the range
        """
        ...


    def tailSet(self, fromElement: "E") -> "SortedSet"["E"]:
        """
        Returns a view of the portion of this set whose elements are
        greater than or equal to `fromElement`.  The returned
        set is backed by this set, so changes in the returned set are
        reflected in this set, and vice-versa.  The returned set
        supports all optional set operations that this set supports.
        
        The returned set will throw an `IllegalArgumentException`
        on an attempt to insert an element outside its range.

        Arguments
        - fromElement: low endpoint (inclusive) of the returned set

        Returns
        - a view of the portion of this set whose elements are greater
                than or equal to `fromElement`

        Raises
        - ClassCastException: if `fromElement` is not compatible
                with this set's comparator (or, if the set has no comparator,
                if `fromElement` does not implement Comparable).
                Implementations may, but are not required to, throw this
                exception if `fromElement` cannot be compared to elements
                currently in the set.
        - NullPointerException: if `fromElement` is null
                and this set does not permit null elements
        - IllegalArgumentException: if this set itself has a
                restricted range, and `fromElement` lies outside the
                bounds of the range
        """
        ...


    def first(self) -> "E":
        """
        Returns the first (lowest) element currently in this set.

        Returns
        - the first (lowest) element currently in this set

        Raises
        - NoSuchElementException: if this set is empty
        """
        ...


    def last(self) -> "E":
        """
        Returns the last (highest) element currently in this set.

        Returns
        - the last (highest) element currently in this set

        Raises
        - NoSuchElementException: if this set is empty
        """
        ...


    def spliterator(self) -> "Spliterator"["E"]:
        """
        Creates a `Spliterator` over the elements in this sorted set.
        
        The `Spliterator` reports Spliterator.DISTINCT,
        Spliterator.SORTED and Spliterator.ORDERED.
        Implementations should document the reporting of additional
        characteristic values.
        
        The spliterator's comparator (see
        java.util.Spliterator.getComparator()) must be `null` if
        the sorted set's comparator (see .comparator()) is `null`.
        Otherwise, the spliterator's comparator must be the same as or impose the
        same total ordering as the sorted set's comparator.

        Returns
        - a `Spliterator` over the elements in this sorted set

        Since
        - 1.8

        Unknown Tags
        - The default implementation creates a
        *<a href="Spliterator.html#binding">late-binding</a>* spliterator
        from the sorted set's `Iterator`.  The spliterator inherits the
        *fail-fast* properties of the set's iterator.  The
        spliterator's comparator is the same as the sorted set's comparator.
        
        The created `Spliterator` additionally reports
        Spliterator.SIZED.
        - The created `Spliterator` additionally reports
        Spliterator.SUBSIZED.
        """
        ...
