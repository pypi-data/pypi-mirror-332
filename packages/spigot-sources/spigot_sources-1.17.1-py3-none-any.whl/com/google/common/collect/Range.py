"""
Python module generated from Java source file com.google.common.collect.Range

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.base import Equivalence
from com.google.common.base import Function
from com.google.common.base import Predicate
from com.google.common.collect import *
from java.io import Serializable
from java.util import Comparator
from java.util import Iterator
from java.util import NoSuchElementException
from java.util import SortedSet
from javax.annotation import Nullable
from typing import Any, Callable, Iterable, Tuple


class Range(Predicate, Serializable):
    """
    A range (or "interval") defines the *boundaries* around a contiguous span of values of some
    `Comparable` type; for example, "integers from 1 to 100 inclusive." Note that it is not
    possible to *iterate* over these contained values. To do so, pass this range instance and
    an appropriate DiscreteDomain to ContiguousSet.create.
    
    <h3>Types of ranges</h3>
    
    Each end of the range may be bounded or unbounded. If bounded, there is an associated
    *endpoint* value, and the range is considered to be either *open* (does not include the
    endpoint) or *closed* (includes the endpoint) on that side. With three possibilities on each
    side, this yields nine basic types of ranges, enumerated below. (Notation: a square bracket
    (`[ ]`) indicates that the range is closed on that side; a parenthesis (`( )`) means
    it is either open or unbounded. The construct `{x | statement`} is read "the set of all
    *x* such that *statement*.")
    
    <blockquote>
    <table>
    <tr><th>Notation        <th>Definition               <th>Factory method
    <tr><td>`(a..b)`  <td>`{x | a < x < b`}  <td>Range.open open
    <tr><td>`[a..b]`  <td>`{x | a <= x <= b`}<td>Range.closed closed
    <tr><td>`(a..b]`  <td>`{x | a < x <= b`} <td>Range.openClosed openClosed
    <tr><td>`[a..b)`  <td>`{x | a <= x < b`} <td>Range.closedOpen closedOpen
    <tr><td>`(a..+∞)` <td>`{x | x > a`}      <td>Range.greaterThan greaterThan
    <tr><td>`[a..+∞)` <td>`{x | x >= a`}     <td>Range.atLeast atLeast
    <tr><td>`(-∞..b)` <td>`{x | x < b`}      <td>Range.lessThan lessThan
    <tr><td>`(-∞..b]` <td>`{x | x <= b`}     <td>Range.atMost atMost
    <tr><td>`(-∞..+∞)`<td>`{x`}              <td>Range.all all
    </table>
    </blockquote>
    
    When both endpoints exist, the upper endpoint may not be less than the lower. The endpoints
    may be equal only if at least one of the bounds is closed:
    
    
    - `[a..a]` : a singleton range
    - `[a..a); (a..a]` : .isEmpty empty ranges; also valid
    - `(a..a)` : **invalid**; an exception will be thrown
    
    
    <h3>Warnings</h3>
    
    
    - Use immutable value types only, if at all possible. If you must use a mutable type, **do
        not** allow the endpoint instances to mutate after the range is created!
    - Your value type's comparison method should be Comparable consistent with equals
        if at all possible. Otherwise, be aware that concepts used throughout this documentation such
        as "equal", "same", "unique" and so on actually refer to whether Comparable.compareTo
        compareTo returns zero, not whether Object.equals equals returns `True`.
    - A class which implements `Comparable<UnrelatedType>` is very broken, and will cause
        undefined horrible things to happen in `Range`. For now, the Range API does not prevent
        its use, because this would also rule out all ungenerified (pre-JDK1.5) data types. **This
        may change in the future.**
    
    
    <h3>Other notes</h3>
    
    
    - Instances of this type are obtained using the static factory methods in this class.
    - Ranges are *convex*: whenever two values are contained, all values in between them must
        also be contained. More formally, for any `c1 <= c2 <= c3` of type `C`, `r.contains(c1) && r.contains(c3)` implies `r.contains(c2)`). This means that a `Range<Integer>` can never be used to represent, say, "all *prime* numbers from 1 to
        100."
    - When evaluated as a Predicate, a range yields the same result as invoking .contains.
    - Terminology note: a range `a` is said to be the *maximal* range having property
        *P* if, for all ranges `b` also having property *P*, `a.encloses(b)`.
        Likewise, `a` is *minimal* when `b.encloses(a)` for all `b` having
        property *P*. See, for example, the definition of .intersection intersection.
    
    
    <h3>Further reading</h3>
    
    See the Guava User Guide article on
    <a href="https://github.com/google/guava/wiki/RangesExplained">`Range`</a>.

    Author(s)
    - Gregory Kick

    Since
    - 10.0
    """

    @staticmethod
    def open(lower: "C", upper: "C") -> "Range"["C"]:
        """
        Returns a range that contains all values strictly greater than `lower` and strictly less than `upper`.

        Raises
        - IllegalArgumentException: if `lower` is greater than *or
            equal to* `upper`

        Since
        - 14.0
        """
        ...


    @staticmethod
    def closed(lower: "C", upper: "C") -> "Range"["C"]:
        """
        Returns a range that contains all values greater than or equal to
        `lower` and less than or equal to `upper`.

        Raises
        - IllegalArgumentException: if `lower` is greater than `upper`

        Since
        - 14.0
        """
        ...


    @staticmethod
    def closedOpen(lower: "C", upper: "C") -> "Range"["C"]:
        """
        Returns a range that contains all values greater than or equal to
        `lower` and strictly less than `upper`.

        Raises
        - IllegalArgumentException: if `lower` is greater than `upper`

        Since
        - 14.0
        """
        ...


    @staticmethod
    def openClosed(lower: "C", upper: "C") -> "Range"["C"]:
        """
        Returns a range that contains all values strictly greater than `lower` and less than or equal to `upper`.

        Raises
        - IllegalArgumentException: if `lower` is greater than `upper`

        Since
        - 14.0
        """
        ...


    @staticmethod
    def range(lower: "C", lowerType: "BoundType", upper: "C", upperType: "BoundType") -> "Range"["C"]:
        """
        Returns a range that contains any value from `lower` to `upper`, where each endpoint may be either inclusive (closed) or exclusive
        (open).

        Raises
        - IllegalArgumentException: if `lower` is greater than `upper`

        Since
        - 14.0
        """
        ...


    @staticmethod
    def lessThan(endpoint: "C") -> "Range"["C"]:
        """
        Returns a range that contains all values strictly less than `endpoint`.

        Since
        - 14.0
        """
        ...


    @staticmethod
    def atMost(endpoint: "C") -> "Range"["C"]:
        """
        Returns a range that contains all values less than or equal to
        `endpoint`.

        Since
        - 14.0
        """
        ...


    @staticmethod
    def upTo(endpoint: "C", boundType: "BoundType") -> "Range"["C"]:
        """
        Returns a range with no lower bound up to the given endpoint, which may be
        either inclusive (closed) or exclusive (open).

        Since
        - 14.0
        """
        ...


    @staticmethod
    def greaterThan(endpoint: "C") -> "Range"["C"]:
        """
        Returns a range that contains all values strictly greater than `endpoint`.

        Since
        - 14.0
        """
        ...


    @staticmethod
    def atLeast(endpoint: "C") -> "Range"["C"]:
        """
        Returns a range that contains all values greater than or equal to
        `endpoint`.

        Since
        - 14.0
        """
        ...


    @staticmethod
    def downTo(endpoint: "C", boundType: "BoundType") -> "Range"["C"]:
        """
        Returns a range from the given endpoint, which may be either inclusive
        (closed) or exclusive (open), with no upper bound.

        Since
        - 14.0
        """
        ...


    @staticmethod
    def all() -> "Range"["C"]:
        """
        Returns a range that contains every value of type `C`.

        Since
        - 14.0
        """
        ...


    @staticmethod
    def singleton(value: "C") -> "Range"["C"]:
        """
        Returns a range that Range.contains(Comparable) contains only
        the given value. The returned range is BoundType.CLOSED closed
        on both ends.

        Since
        - 14.0
        """
        ...


    @staticmethod
    def encloseAll(values: Iterable["C"]) -> "Range"["C"]:
        """
        Returns the minimal range that
        Range.contains(Comparable) contains all of the given values.
        The returned range is BoundType.CLOSED closed on both ends.

        Raises
        - ClassCastException: if the parameters are not *mutually
            comparable*
        - NoSuchElementException: if `values` is empty
        - NullPointerException: if any of `values` is null

        Since
        - 14.0
        """
        ...


    def hasLowerBound(self) -> bool:
        """
        Returns `True` if this range has a lower endpoint.
        """
        ...


    def lowerEndpoint(self) -> "C":
        """
        Returns the lower endpoint of this range.

        Raises
        - IllegalStateException: if this range is unbounded below (that is, .hasLowerBound() returns `False`)
        """
        ...


    def lowerBoundType(self) -> "BoundType":
        """
        Returns the type of this range's lower bound: BoundType.CLOSED if the range includes
        its lower endpoint, BoundType.OPEN if it does not.

        Raises
        - IllegalStateException: if this range is unbounded below (that is, .hasLowerBound() returns `False`)
        """
        ...


    def hasUpperBound(self) -> bool:
        """
        Returns `True` if this range has an upper endpoint.
        """
        ...


    def upperEndpoint(self) -> "C":
        """
        Returns the upper endpoint of this range.

        Raises
        - IllegalStateException: if this range is unbounded above (that is, .hasUpperBound() returns `False`)
        """
        ...


    def upperBoundType(self) -> "BoundType":
        """
        Returns the type of this range's upper bound: BoundType.CLOSED if the range includes
        its upper endpoint, BoundType.OPEN if it does not.

        Raises
        - IllegalStateException: if this range is unbounded above (that is, .hasUpperBound() returns `False`)
        """
        ...


    def isEmpty(self) -> bool:
        """
        Returns `True` if this range is of the form `[v..v)` or `(v..v]`. (This does
        not encompass ranges of the form `(v..v)`, because such ranges are *invalid* and
        can't be constructed at all.)
        
        Note that certain discrete ranges such as the integer range `(3..4)` are **not**
        considered empty, even though they contain no actual values.  In these cases, it may be
        helpful to preprocess ranges with .canonical(DiscreteDomain).
        """
        ...


    def contains(self, value: "C") -> bool:
        """
        Returns `True` if `value` is within the bounds of this range. For example, on the
        range `[0..2)`, `contains(1)` returns `True`, while `contains(2)`
        returns `False`.
        """
        ...


    def apply(self, input: "C") -> bool:
        """
        Deprecated
        - Provided only to satisfy the Predicate interface; use .contains
            instead.
        """
        ...


    def containsAll(self, values: Iterable["C"]) -> bool:
        """
        Returns `True` if every element in `values` is .contains contained in
        this range.
        """
        ...


    def encloses(self, other: "Range"["C"]) -> bool:
        """
        Returns `True` if the bounds of `other` do not extend outside the bounds of this
        range. Examples:
        
        
        - `[3..6]` encloses `[4..5]`
        - `(3..6)` encloses `(3..6)`
        - `[3..6]` encloses `[4..4)` (even though the latter is empty)
        - `(3..6]` does not enclose `[3..6]`
        - `[4..5]` does not enclose `(3..6)` (even though it contains every value
            contained by the latter range)
        - `[3..6]` does not enclose `(1..1]` (even though it contains every value
            contained by the latter range)
        
        
        Note that if `a.encloses(b)`, then `b.contains(v)` implies
        `a.contains(v)`, but as the last two examples illustrate, the converse is not always
        True.
        
        Being reflexive, antisymmetric and transitive, the `encloses` relation defines a
        *partial order* over ranges. There exists a unique Range.all maximal range
        according to this relation, and also numerous .isEmpty minimal ranges. Enclosure
        also implies .isConnected connectedness.
        """
        ...


    def isConnected(self, other: "Range"["C"]) -> bool:
        """
        Returns `True` if there exists a (possibly empty) range which is .encloses
        enclosed by both this range and `other`.
        
        For example,
        
        - `[2, 4)` and `[5, 7)` are not connected
        - `[2, 4)` and `[3, 5)` are connected, because both enclose `[3, 4)`
        - `[2, 4)` and `[4, 6)` are connected, because both enclose the empty range
            `[4, 4)`
        
        
        Note that this range and `other` have a well-defined .span union and
        .intersection intersection (as a single, possibly-empty range) if and only if this
        method returns `True`.
        
        The connectedness relation is both reflexive and symmetric, but does not form an Equivalence equivalence relation as it is not transitive.
        
        Note that certain discrete ranges are not considered connected, even though there are no
        elements "between them."  For example, `[3, 5]` is not considered connected to `[6, 10]`.  In these cases, it may be desirable for both input ranges to be preprocessed with
        .canonical(DiscreteDomain) before testing for connectedness.
        """
        ...


    def intersection(self, connectedRange: "Range"["C"]) -> "Range"["C"]:
        """
        Returns the maximal range .encloses enclosed by both this range and `connectedRange`, if such a range exists.
        
        For example, the intersection of `[1..5]` and `(3..7)` is `(3..5]`. The
        resulting range may be empty; for example, `[1..5)` intersected with `[5..7)`
        yields the empty range `[5..5)`.
        
        The intersection exists if and only if the two ranges are .isConnected
        connected.
        
        The intersection operation is commutative, associative and idempotent, and its identity
        element is Range.all).

        Raises
        - IllegalArgumentException: if `isConnected(connectedRange)` is `False`
        """
        ...


    def span(self, other: "Range"["C"]) -> "Range"["C"]:
        """
        Returns the minimal range that .encloses encloses both this range and `other`. For example, the span of `[1..3]` and `(5..7)` is `[1..7)`.
        
        *If* the input ranges are .isConnected connected, the returned range can
        also be called their *union*. If they are not, note that the span might contain values
        that are not contained in either input range.
        
        Like .intersection(Range) intersection, this operation is commutative, associative
        and idempotent. Unlike it, it is always well-defined for any two input ranges.
        """
        ...


    def canonical(self, domain: "DiscreteDomain"["C"]) -> "Range"["C"]:
        """
        Returns the canonical form of this range in the given domain. The canonical form has the
        following properties:
        
        
        - equivalence: `a.canonical().contains(v) == a.contains(v)` for all `v` (in other
            words, `ContiguousSet.create(a.canonical(domain), domain).equals(
            ContiguousSet.create(a, domain))`
        - uniqueness: unless `a.isEmpty()`,
            `ContiguousSet.create(a, domain).equals(ContiguousSet.create(b, domain))` implies
            `a.canonical(domain).equals(b.canonical(domain))`
        - idempotence: `a.canonical(domain).canonical(domain).equals(a.canonical(domain))`
        
        
        Furthermore, this method guarantees that the range returned will be one of the following
        canonical forms:
        
        
        - [start..end)
        - [start..+∞)
        - (-∞..end) (only if type `C` is unbounded below)
        - (-∞..+∞) (only if type `C` is unbounded below)
        """
        ...


    def equals(self, object: "Object") -> bool:
        """
        Returns `True` if `object` is a range having the same endpoints and bound types as
        this range. Note that discrete ranges such as `(1..4)` and `[2..3]` are **not**
        equal to one another, despite the fact that they each contain precisely the same set of values.
        Similarly, empty ranges are not equal unless they have exactly the same representation, so
        `[3..3)`, `(3..3]`, `(4..4]` are all unequal.
        """
        ...


    def hashCode(self) -> int:
        """
        Returns a hash code for this range.
        """
        ...


    def toString(self) -> str:
        """
        Returns a string representation of this range, such as `"[3..5)"` (other examples are
        listed in the class documentation).
        """
        ...
