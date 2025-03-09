"""
Python module generated from Java source file java.util.NavigableSet

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import *
from typing import Any, Callable, Iterable, Tuple


class NavigableSet(SortedSet):
    """
    A SortedSet extended with navigation methods reporting
    closest matches for given search targets. Methods .lower,
    .floor, .ceiling, and .higher return elements
    respectively less than, less than or equal, greater than or equal,
    and greater than a given element, returning `null` if there
    is no such element.
    
    A `NavigableSet` may be accessed and traversed in either
    ascending or descending order.  The .descendingSet method
    returns a view of the set with the senses of all relational and
    directional methods inverted. The performance of ascending
    operations and views is likely to be faster than that of descending
    ones.  This interface additionally defines methods .pollFirst and .pollLast that return and remove the lowest
    and highest element, if one exists, else returning `null`.
    Methods
    .subSet(Object, boolean, Object, boolean) subSet(E, boolean, E, boolean),
    .headSet(Object, boolean) headSet(E, boolean), and
    .tailSet(Object, boolean) tailSet(E, boolean)
    differ from the like-named `SortedSet` methods in accepting
    additional arguments describing whether lower and upper bounds are
    inclusive versus exclusive.  Subsets of any `NavigableSet`
    must implement the `NavigableSet` interface.
    
    The return values of navigation methods may be ambiguous in
    implementations that permit `null` elements. However, even
    in this case the result can be disambiguated by checking
    `contains(null)`. To avoid such issues, implementations of
    this interface are encouraged to *not* permit insertion of
    `null` elements. (Note that sorted sets of Comparable elements intrinsically do not permit `null`.)
    
    Methods
    .subSet(Object, Object) subSet(E, E),
    .headSet(Object) headSet(E), and
    .tailSet(Object) tailSet(E)
    are specified to return `SortedSet` to allow existing
    implementations of `SortedSet` to be compatibly retrofitted to
    implement `NavigableSet`, but extensions and implementations
    of this interface are encouraged to override these methods to return
    `NavigableSet`.
    
    This interface is a member of the
    <a href="/java.base/java/util/package-summary.html#CollectionsFramework">
    Java Collections Framework</a>.
    
    Type `<E>`: the type of elements maintained by this set

    Author(s)
    - Josh Bloch

    Since
    - 1.6
    """

    def lower(self, e: "E") -> "E":
        """
        Returns the greatest element in this set strictly less than the
        given element, or `null` if there is no such element.

        Arguments
        - e: the value to match

        Returns
        - the greatest element less than `e`,
                or `null` if there is no such element

        Raises
        - ClassCastException: if the specified element cannot be
                compared with the elements currently in the set
        - NullPointerException: if the specified element is null
                and this set does not permit null elements
        """
        ...


    def floor(self, e: "E") -> "E":
        """
        Returns the greatest element in this set less than or equal to
        the given element, or `null` if there is no such element.

        Arguments
        - e: the value to match

        Returns
        - the greatest element less than or equal to `e`,
                or `null` if there is no such element

        Raises
        - ClassCastException: if the specified element cannot be
                compared with the elements currently in the set
        - NullPointerException: if the specified element is null
                and this set does not permit null elements
        """
        ...


    def ceiling(self, e: "E") -> "E":
        """
        Returns the least element in this set greater than or equal to
        the given element, or `null` if there is no such element.

        Arguments
        - e: the value to match

        Returns
        - the least element greater than or equal to `e`,
                or `null` if there is no such element

        Raises
        - ClassCastException: if the specified element cannot be
                compared with the elements currently in the set
        - NullPointerException: if the specified element is null
                and this set does not permit null elements
        """
        ...


    def higher(self, e: "E") -> "E":
        """
        Returns the least element in this set strictly greater than the
        given element, or `null` if there is no such element.

        Arguments
        - e: the value to match

        Returns
        - the least element greater than `e`,
                or `null` if there is no such element

        Raises
        - ClassCastException: if the specified element cannot be
                compared with the elements currently in the set
        - NullPointerException: if the specified element is null
                and this set does not permit null elements
        """
        ...


    def pollFirst(self) -> "E":
        """
        Retrieves and removes the first (lowest) element,
        or returns `null` if this set is empty.

        Returns
        - the first element, or `null` if this set is empty
        """
        ...


    def pollLast(self) -> "E":
        """
        Retrieves and removes the last (highest) element,
        or returns `null` if this set is empty.

        Returns
        - the last element, or `null` if this set is empty
        """
        ...


    def iterator(self) -> Iterator["E"]:
        """
        Returns an iterator over the elements in this set, in ascending order.

        Returns
        - an iterator over the elements in this set, in ascending order
        """
        ...


    def descendingSet(self) -> "NavigableSet"["E"]:
        """
        Returns a reverse order view of the elements contained in this set.
        The descending set is backed by this set, so changes to the set are
        reflected in the descending set, and vice-versa.  If either set is
        modified while an iteration over either set is in progress (except
        through the iterator's own `remove` operation), the results of
        the iteration are undefined.
        
        The returned set has an ordering equivalent to
        Collections.reverseOrder(Comparator) Collections.reverseOrder`(comparator())`.
        The expression `s.descendingSet().descendingSet()` returns a
        view of `s` essentially equivalent to `s`.

        Returns
        - a reverse order view of this set
        """
        ...


    def descendingIterator(self) -> Iterator["E"]:
        """
        Returns an iterator over the elements in this set, in descending order.
        Equivalent in effect to `descendingSet().iterator()`.

        Returns
        - an iterator over the elements in this set, in descending order
        """
        ...


    def subSet(self, fromElement: "E", fromInclusive: bool, toElement: "E", toInclusive: bool) -> "NavigableSet"["E"]:
        """
        Returns a view of the portion of this set whose elements range from
        `fromElement` to `toElement`.  If `fromElement` and
        `toElement` are equal, the returned set is empty unless `fromInclusive` and `toInclusive` are both True.  The returned set
        is backed by this set, so changes in the returned set are reflected in
        this set, and vice-versa.  The returned set supports all optional set
        operations that this set supports.
        
        The returned set will throw an `IllegalArgumentException`
        on an attempt to insert an element outside its range.

        Arguments
        - fromElement: low endpoint of the returned set
        - fromInclusive: `True` if the low endpoint
               is to be included in the returned view
        - toElement: high endpoint of the returned set
        - toInclusive: `True` if the high endpoint
               is to be included in the returned view

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
                `toElement` is null and this set does
                not permit null elements
        - IllegalArgumentException: if `fromElement` is
                greater than `toElement`; or if this set itself
                has a restricted range, and `fromElement` or
                `toElement` lies outside the bounds of the range.
        """
        ...


    def headSet(self, toElement: "E", inclusive: bool) -> "NavigableSet"["E"]:
        """
        Returns a view of the portion of this set whose elements are less than
        (or equal to, if `inclusive` is True) `toElement`.  The
        returned set is backed by this set, so changes in the returned set are
        reflected in this set, and vice-versa.  The returned set supports all
        optional set operations that this set supports.
        
        The returned set will throw an `IllegalArgumentException`
        on an attempt to insert an element outside its range.

        Arguments
        - toElement: high endpoint of the returned set
        - inclusive: `True` if the high endpoint
               is to be included in the returned view

        Returns
        - a view of the portion of this set whose elements are less than
                (or equal to, if `inclusive` is True) `toElement`

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


    def tailSet(self, fromElement: "E", inclusive: bool) -> "NavigableSet"["E"]:
        """
        Returns a view of the portion of this set whose elements are greater
        than (or equal to, if `inclusive` is True) `fromElement`.
        The returned set is backed by this set, so changes in the returned set
        are reflected in this set, and vice-versa.  The returned set supports
        all optional set operations that this set supports.
        
        The returned set will throw an `IllegalArgumentException`
        on an attempt to insert an element outside its range.

        Arguments
        - fromElement: low endpoint of the returned set
        - inclusive: `True` if the low endpoint
               is to be included in the returned view

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


    def subSet(self, fromElement: "E", toElement: "E") -> "SortedSet"["E"]:
        """
        
        
        Equivalent to `subSet(fromElement, True, toElement, False)`.

        Raises
        - ClassCastException: 
        - NullPointerException: 
        - IllegalArgumentException: 
        """
        ...


    def headSet(self, toElement: "E") -> "SortedSet"["E"]:
        """
        
        
        Equivalent to `headSet(toElement, False)`.

        Raises
        - ClassCastException: 
        - NullPointerException: 
        - IllegalArgumentException: 
        """
        ...


    def tailSet(self, fromElement: "E") -> "SortedSet"["E"]:
        """
        
        
        Equivalent to `tailSet(fromElement, True)`.

        Raises
        - ClassCastException: 
        - NullPointerException: 
        - IllegalArgumentException: 
        """
        ...
