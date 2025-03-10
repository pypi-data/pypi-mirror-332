"""
Python module generated from Java source file java.util.Comparator

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import Serializable
from java.util import *
from java.util import Comparators
from java.util.function import Function
from java.util.function import ToDoubleFunction
from java.util.function import ToIntFunction
from java.util.function import ToLongFunction
from typing import Any, Callable, Iterable, Tuple


class Comparator:
    """
    A comparison function, which imposes a *total ordering* on
    some collection of objects.  Comparators can be passed to a sort
    method (such as Collections.sort(List,Comparator)
    Collections.sort or Arrays.sort(Object[],Comparator)
    Arrays.sort) to allow precise control over the sort order.
    Comparators can also be used to control the order of certain data
    structures (such as SortedSet sorted sets or
    SortedMap sorted maps), or to provide an ordering for
    collections of objects that don't have a Comparable
    natural ordering.
    
    The ordering imposed by a comparator `c` on a set of elements
    `S` is said to be *consistent with equals* if and only if
    `c.compare(e1, e2)==0` has the same boolean value as
    `e1.equals(e2)` for every `e1` and `e2` in
    `S`.
    
    Caution should be exercised when using a comparator capable of imposing an
    ordering inconsistent with equals to order a sorted set (or sorted map).
    Suppose a sorted set (or sorted map) with an explicit comparator `c`
    is used with elements (or keys) drawn from a set `S`.  If the
    ordering imposed by `c` on `S` is inconsistent with equals,
    the sorted set (or sorted map) will behave "strangely."  In particular the
    sorted set (or sorted map) will violate the general contract for set (or
    map), which is defined in terms of `equals`.
    
    For example, suppose one adds two elements `a` and `b` such that
    `(a.equals(b) && c.compare(a, b) != 0)`
    to an empty `TreeSet` with comparator `c`.
    The second `add` operation will return
    True (and the size of the tree set will increase) because `a` and
    `b` are not equivalent from the tree set's perspective, even though
    this is contrary to the specification of the
    Set.add Set.add method.
    
    Note: It is generally a good idea for comparators to also implement
    `java.io.Serializable`, as they may be used as ordering methods in
    serializable data structures (like TreeSet, TreeMap).  In
    order for the data structure to serialize successfully, the comparator (if
    provided) must implement `Serializable`.
    
    For the mathematically inclined, the *relation* that defines the
    *imposed ordering* that a given comparator `c` imposes on a
    given set of objects `S` is:```
          {(x, y) such that c.compare(x, y) &lt;= 0}.
    ``` The *quotient* for this total order is:```
          {(x, y) such that c.compare(x, y) == 0}.
    ```
    
    It follows immediately from the contract for `compare` that the
    quotient is an *equivalence relation* on `S`, and that the
    imposed ordering is a *total order* on `S`.  When we say that
    the ordering imposed by `c` on `S` is *consistent with
    equals*, we mean that the quotient for the ordering is the equivalence
    relation defined by the objects' Object.equals(Object)
    equals(Object) method(s):```
        {(x, y) such that x.equals(y)}. ```
    
    In other words, when the imposed ordering is consistent with
    equals, the equivalence classes defined by the equivalence relation
    of the `equals` method and the equivalence classes defined by
    the quotient of the `compare` method are the same.
    
    Unlike `Comparable`, a comparator may optionally permit
    comparison of null arguments, while maintaining the requirements for
    an equivalence relation.
    
    This interface is a member of the
    <a href="/java.base/java/util/package-summary.html#CollectionsFramework">
    Java Collections Framework</a>.
    
    Type `<T>`: the type of objects that may be compared by this comparator

    Author(s)
    - Neal Gafter

    See
    - java.io.Serializable

    Since
    - 1.2
    """

    def compare(self, o1: "T", o2: "T") -> int:
        """
        Compares its two arguments for order.  Returns a negative integer,
        zero, or a positive integer as the first argument is less than, equal
        to, or greater than the second.
        
        The implementor must ensure that Integer.signum
        signum`(compare(x, y)) == -signum(compare(y, x))` for
        all `x` and `y`.  (This implies that `compare(x, y)` must throw an exception if and only if `compare(y, x)` throws an exception.)
        
        The implementor must also ensure that the relation is transitive:
        `((compare(x, y)>0) && (compare(y, z)>0))` implies
        `compare(x, z)>0`.
        
        Finally, the implementor must ensure that `compare(x,
        y)==0` implies that `signum(compare(x,
        z))==signum(compare(y, z))` for all `z`.

        Arguments
        - o1: the first object to be compared.
        - o2: the second object to be compared.

        Returns
        - a negative integer, zero, or a positive integer as the
                first argument is less than, equal to, or greater than the
                second.

        Raises
        - NullPointerException: if an argument is null and this
                comparator does not permit null arguments
        - ClassCastException: if the arguments' types prevent them from
                being compared by this comparator.

        Unknown Tags
        - It is generally the case, but *not* strictly required that
        `(compare(x, y)==0) == (x.equals(y))`.  Generally speaking,
        any comparator that violates this condition should clearly indicate
        this fact.  The recommended language is "Note: this comparator
        imposes orderings that are inconsistent with equals."
        """
        ...


    def equals(self, obj: "Object") -> bool:
        """
        Indicates whether some other object is &quot;equal to&quot;
        this comparator.  This method must obey the general contract of
        Object.equals(Object).  Additionally, this method can
        return `True` *only* if the specified object is also
        a comparator and it imposes the same ordering as this
        comparator.  Thus, `comp1.equals(comp2)` implies that
        Integer.signum signum`(comp1.compare(o1,
        o2))==signum(comp2.compare(o1, o2))` for every object reference
        `o1` and `o2`.
        
        Note that it is *always* safe *not* to override
        `Object.equals(Object)`.  However, overriding this method may,
        in some cases, improve performance by allowing programs to determine
        that two distinct comparators impose the same order.

        Arguments
        - obj: the reference object with which to compare.

        Returns
        - `True` only if the specified object is also
                 a comparator and it imposes the same ordering as this
                 comparator.

        See
        - Object.hashCode()
        """
        ...


    def reversed(self) -> "Comparator"["T"]:
        """
        Returns a comparator that imposes the reverse ordering of this
        comparator.

        Returns
        - a comparator that imposes the reverse ordering of this
                comparator.

        Since
        - 1.8
        """
        ...


    def thenComparing(self, other: "Comparator"["T"]) -> "Comparator"["T"]:
        """
        Returns a lexicographic-order comparator with another comparator.
        If this `Comparator` considers two elements equal, i.e.
        `compare(a, b) == 0`, `other` is used to determine the order.
        
        The returned comparator is serializable if the specified comparator
        is also serializable.

        Arguments
        - other: the other comparator to be used when this comparator
                compares two objects that are equal.

        Returns
        - a lexicographic-order comparator composed of this and then the
                other comparator

        Raises
        - NullPointerException: if the argument is null.

        Since
        - 1.8

        Unknown Tags
        - For example, to sort a collection of `String` based on the length
        and then case-insensitive natural ordering, the comparator can be
        composed using following code,
        
        ````Comparator<String> cmp = Comparator.comparingInt(String::length)
                    .thenComparing(String.CASE_INSENSITIVE_ORDER);````
        """
        ...


    def thenComparing(self, keyExtractor: "Function"["T", "U"], keyComparator: "Comparator"["U"]) -> "Comparator"["T"]:
        """
        Returns a lexicographic-order comparator with a function that
        extracts a key to be compared with the given `Comparator`.
        
        Type `<U>`: the type of the sort key

        Arguments
        - keyExtractor: the function used to extract the sort key
        - keyComparator: the `Comparator` used to compare the sort key

        Returns
        - a lexicographic-order comparator composed of this comparator
                and then comparing on the key extracted by the keyExtractor function

        Raises
        - NullPointerException: if either argument is null.

        See
        - .thenComparing(Comparator)

        Since
        - 1.8

        Unknown Tags
        - This default implementation behaves as if `thenComparing(comparing(keyExtractor, cmp))`.
        """
        ...


    def thenComparing(self, keyExtractor: "Function"["T", "U"]) -> "Comparator"["T"]:
        """
        Returns a lexicographic-order comparator with a function that
        extracts a `Comparable` sort key.
        
        Type `<U>`: the type of the Comparable sort key

        Arguments
        - keyExtractor: the function used to extract the Comparable sort key

        Returns
        - a lexicographic-order comparator composed of this and then the
                Comparable sort key.

        Raises
        - NullPointerException: if the argument is null.

        See
        - .thenComparing(Comparator)

        Since
        - 1.8

        Unknown Tags
        - This default implementation behaves as if `thenComparing(comparing(keyExtractor))`.
        """
        ...


    def thenComparingInt(self, keyExtractor: "ToIntFunction"["T"]) -> "Comparator"["T"]:
        """
        Returns a lexicographic-order comparator with a function that
        extracts an `int` sort key.

        Arguments
        - keyExtractor: the function used to extract the integer sort key

        Returns
        - a lexicographic-order comparator composed of this and then the
                `int` sort key

        Raises
        - NullPointerException: if the argument is null.

        See
        - .thenComparing(Comparator)

        Since
        - 1.8

        Unknown Tags
        - This default implementation behaves as if `thenComparing(comparingInt(keyExtractor))`.
        """
        ...


    def thenComparingLong(self, keyExtractor: "ToLongFunction"["T"]) -> "Comparator"["T"]:
        """
        Returns a lexicographic-order comparator with a function that
        extracts a `long` sort key.

        Arguments
        - keyExtractor: the function used to extract the long sort key

        Returns
        - a lexicographic-order comparator composed of this and then the
                `long` sort key

        Raises
        - NullPointerException: if the argument is null.

        See
        - .thenComparing(Comparator)

        Since
        - 1.8

        Unknown Tags
        - This default implementation behaves as if `thenComparing(comparingLong(keyExtractor))`.
        """
        ...


    def thenComparingDouble(self, keyExtractor: "ToDoubleFunction"["T"]) -> "Comparator"["T"]:
        """
        Returns a lexicographic-order comparator with a function that
        extracts a `double` sort key.

        Arguments
        - keyExtractor: the function used to extract the double sort key

        Returns
        - a lexicographic-order comparator composed of this and then the
                `double` sort key

        Raises
        - NullPointerException: if the argument is null.

        See
        - .thenComparing(Comparator)

        Since
        - 1.8

        Unknown Tags
        - This default implementation behaves as if `thenComparing(comparingDouble(keyExtractor))`.
        """
        ...


    @staticmethod
    def reverseOrder() -> "Comparator"["T"]:
        """
        Returns a comparator that imposes the reverse of the *natural
        ordering*.
        
        The returned comparator is serializable and throws NullPointerException when comparing `null`.
        
        Type `<T>`: the Comparable type of element to be compared

        Returns
        - a comparator that imposes the reverse of the *natural
                ordering* on `Comparable` objects.

        See
        - Comparable

        Since
        - 1.8
        """
        ...


    @staticmethod
    def naturalOrder() -> "Comparator"["T"]:
        """
        Returns a comparator that compares Comparable objects in natural
        order.
        
        The returned comparator is serializable and throws NullPointerException when comparing `null`.
        
        Type `<T>`: the Comparable type of element to be compared

        Returns
        - a comparator that imposes the *natural ordering* on `Comparable` objects.

        See
        - Comparable

        Since
        - 1.8
        """
        ...


    @staticmethod
    def nullsFirst(comparator: "Comparator"["T"]) -> "Comparator"["T"]:
        """
        Returns a null-friendly comparator that considers `null` to be
        less than non-null. When both are `null`, they are considered
        equal. If both are non-null, the specified `Comparator` is used
        to determine the order. If the specified comparator is `null`,
        then the returned comparator considers all non-null values to be equal.
        
        The returned comparator is serializable if the specified comparator
        is serializable.
        
        Type `<T>`: the type of the elements to be compared

        Arguments
        - comparator: a `Comparator` for comparing non-null values

        Returns
        - a comparator that considers `null` to be less than
                non-null, and compares non-null objects with the supplied
                `Comparator`.

        Since
        - 1.8
        """
        ...


    @staticmethod
    def nullsLast(comparator: "Comparator"["T"]) -> "Comparator"["T"]:
        """
        Returns a null-friendly comparator that considers `null` to be
        greater than non-null. When both are `null`, they are considered
        equal. If both are non-null, the specified `Comparator` is used
        to determine the order. If the specified comparator is `null`,
        then the returned comparator considers all non-null values to be equal.
        
        The returned comparator is serializable if the specified comparator
        is serializable.
        
        Type `<T>`: the type of the elements to be compared

        Arguments
        - comparator: a `Comparator` for comparing non-null values

        Returns
        - a comparator that considers `null` to be greater than
                non-null, and compares non-null objects with the supplied
                `Comparator`.

        Since
        - 1.8
        """
        ...


    @staticmethod
    def comparing(keyExtractor: "Function"["T", "U"], keyComparator: "Comparator"["U"]) -> "Comparator"["T"]:
        """
        Accepts a function that extracts a sort key from a type `T`, and
        returns a `Comparator<T>` that compares by that sort key using
        the specified Comparator.
        
        The returned comparator is serializable if the specified function
        and comparator are both serializable.
        
        Type `<T>`: the type of element to be compared
        
        Type `<U>`: the type of the sort key

        Arguments
        - keyExtractor: the function used to extract the sort key
        - keyComparator: the `Comparator` used to compare the sort key

        Returns
        - a comparator that compares by an extracted key using the
                specified `Comparator`

        Raises
        - NullPointerException: if either argument is null

        Since
        - 1.8

        Unknown Tags
        - For example, to obtain a `Comparator` that compares `Person` objects by their last name ignoring case differences,
        
        ````Comparator<Person> cmp = Comparator.comparing(
                    Person::getLastName,
                    String.CASE_INSENSITIVE_ORDER);````
        """
        ...


    @staticmethod
    def comparing(keyExtractor: "Function"["T", "U"]) -> "Comparator"["T"]:
        """
        Accepts a function that extracts a java.lang.Comparable
        Comparable sort key from a type `T`, and returns a `Comparator<T>` that compares by that sort key.
        
        The returned comparator is serializable if the specified function
        is also serializable.
        
        Type `<T>`: the type of element to be compared
        
        Type `<U>`: the type of the `Comparable` sort key

        Arguments
        - keyExtractor: the function used to extract the Comparable sort key

        Returns
        - a comparator that compares by an extracted key

        Raises
        - NullPointerException: if the argument is null

        Since
        - 1.8

        Unknown Tags
        - For example, to obtain a `Comparator` that compares `Person` objects by their last name,
        
        ````Comparator<Person> byLastName = Comparator.comparing(Person::getLastName);````
        """
        ...


    @staticmethod
    def comparingInt(keyExtractor: "ToIntFunction"["T"]) -> "Comparator"["T"]:
        """
        Accepts a function that extracts an `int` sort key from a type
        `T`, and returns a `Comparator<T>` that compares by that
        sort key.
        
        The returned comparator is serializable if the specified function
        is also serializable.
        
        Type `<T>`: the type of element to be compared

        Arguments
        - keyExtractor: the function used to extract the integer sort key

        Returns
        - a comparator that compares by an extracted key

        Raises
        - NullPointerException: if the argument is null

        See
        - .comparing(Function)

        Since
        - 1.8
        """
        ...


    @staticmethod
    def comparingLong(keyExtractor: "ToLongFunction"["T"]) -> "Comparator"["T"]:
        """
        Accepts a function that extracts a `long` sort key from a type
        `T`, and returns a `Comparator<T>` that compares by that
        sort key.
        
        The returned comparator is serializable if the specified function is
        also serializable.
        
        Type `<T>`: the type of element to be compared

        Arguments
        - keyExtractor: the function used to extract the long sort key

        Returns
        - a comparator that compares by an extracted key

        Raises
        - NullPointerException: if the argument is null

        See
        - .comparing(Function)

        Since
        - 1.8
        """
        ...


    @staticmethod
    def comparingDouble(keyExtractor: "ToDoubleFunction"["T"]) -> "Comparator"["T"]:
        """
        Accepts a function that extracts a `double` sort key from a type
        `T`, and returns a `Comparator<T>` that compares by that
        sort key.
        
        The returned comparator is serializable if the specified function
        is also serializable.
        
        Type `<T>`: the type of element to be compared

        Arguments
        - keyExtractor: the function used to extract the double sort key

        Returns
        - a comparator that compares by an extracted key

        Raises
        - NullPointerException: if the argument is null

        See
        - .comparing(Function)

        Since
        - 1.8
        """
        ...
