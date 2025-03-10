"""
Python module generated from Java source file com.google.common.base.Equivalence

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.base import *
from com.google.errorprone.annotations import ForOverride
from java.io import Serializable
from java.util.function import BiPredicate
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class Equivalence(BiPredicate):
    """
    A strategy for determining whether two instances are considered equivalent, and for computing
    hash codes in a manner consistent with that equivalence. Two examples of equivalences are the
    .identity() identity equivalence and the .equals "equals" equivalence.

    Author(s)
    - Gregory Kick

    Since
    - 10.0 (<a href="https://github.com/google/guava/wiki/Compatibility">mostly
        source-compatible</a> since 4.0)
    """

    def equivalent(self, a: "T", b: "T") -> bool:
        """
        Returns `True` if the given objects are considered equivalent.
        
        This method describes an *equivalence relation* on object references, meaning that for
        all references `x`, `y`, and `z` (any of which may be null):
        
        
          - `equivalent(x, x)` is True (*reflexive* property)
          - `equivalent(x, y)` and `equivalent(y, x)` each return the same result
              (*symmetric* property)
          - If `equivalent(x, y)` and `equivalent(y, z)` are both True, then `equivalent(x, z)` is also True (*transitive* property)
        
        
        Note that all calls to `equivalent(x, y)` are expected to return the same result as
        long as neither `x` nor `y` is modified.
        """
        ...


    def test(self, t: "T", u: "T") -> bool:
        """
        Since
        - 21.0

        Deprecated
        - Provided only to satisfy the BiPredicate interface; use .equivalent
            instead.
        """
        ...


    def hash(self, t: "T") -> int:
        """
        Returns a hash code for `t`.
        
        The `hash` has the following properties:
        
        
          - It is *consistent*: for any reference `x`, multiple invocations of `hash(x`} consistently return the same value provided `x` remains unchanged
              according to the definition of the equivalence. The hash need not remain consistent from
              one execution of an application to another execution of the same application.
          - It is *distributable across equivalence*: for any references `x` and `y`, if `equivalent(x, y)`, then `hash(x) == hash(y)`. It is *not*
              necessary that the hash be distributable across *inequivalence*. If `equivalence(x, y)` is False, `hash(x) == hash(y)` may still be True.
          - `hash(null)` is `0`.
        """
        ...


    def onResultOf(self, function: "Function"["F", "T"]) -> "Equivalence"["F"]:
        """
        Returns a new equivalence relation for `F` which evaluates equivalence by first applying
        `function` to the argument, then evaluating using `this`. That is, for any pair of
        non-null objects `x` and `y`, `equivalence.onResultOf(function).equivalent(a,
        b)` is True if and only if `equivalence.equivalent(function.apply(a), function.apply(b))`
        is True.
        
        For example:
        
        ````Equivalence<Person> SAME_AGE = Equivalence.equals().onResultOf(GET_PERSON_AGE);````
        
        `function` will never be invoked with a null value.
        
        Note that `function` must be consistent according to `this` equivalence
        relation. That is, invoking Function.apply multiple times for a given value must return
        equivalent results. For example, `Equivalence.identity().onResultOf(Functions.toStringFunction())` is broken because it's not
        guaranteed that Object.toString) always returns the same string instance.

        Since
        - 10.0
        """
        ...


    def wrap(self, reference: "S") -> "Wrapper"["S"]:
        """
        Returns a wrapper of `reference` that implements Wrapper.equals(Object)
        Object.equals() such that `wrap(a).equals(wrap(b))` if and only if `equivalent(a,
        b)`.

        Since
        - 10.0
        """
        ...


    def pairwise(self) -> "Equivalence"[Iterable["S"]]:
        """
        Returns an equivalence over iterables based on the equivalence of their elements. More
        specifically, two iterables are considered equivalent if they both contain the same number of
        elements, and each pair of corresponding elements is equivalent according to `this`. Null
        iterables are equivalent to one another.
        
        Note that this method performs a similar function for equivalences as com.google.common.collect.Ordering.lexicographical does for orderings.

        Since
        - 10.0
        """
        ...


    def equivalentTo(self, target: "T") -> "Predicate"["T"]:
        """
        Returns a predicate that evaluates to True if and only if the input is equivalent to `target` according to this equivalence relation.

        Since
        - 10.0
        """
        ...


    @staticmethod
    def equals() -> "Equivalence"["Object"]:
        """
        Returns an equivalence that delegates to Object.equals and Object.hashCode.
        Equivalence.equivalent returns `True` if both values are null, or if neither
        value is null and Object.equals returns `True`. Equivalence.hash returns
        `0` if passed a null value.

        Since
        - 4.0 (in Equivalences)
        """
        ...


    @staticmethod
    def identity() -> "Equivalence"["Object"]:
        """
        Returns an equivalence that uses `==` to compare values and System.identityHashCode(Object) to compute the hash code. Equivalence.equivalent
        returns `True` if `a == b`, including in the case that a and b are both null.

        Since
        - 4.0 (in Equivalences)
        """
        ...


    class Wrapper(Serializable):
        """
        Wraps an object so that .equals(Object) and .hashCode() delegate to an Equivalence.
        
        For example, given an Equivalence for String strings named `equiv`
        that tests equivalence using their lengths:
        
        ````equiv.wrap("a").equals(equiv.wrap("b")) // True
        equiv.wrap("a").equals(equiv.wrap("hello")) // False````
        
        Note in particular that an equivalence wrapper is never equal to the object it wraps.
        
        ````equiv.wrap(obj).equals(obj) // always False````

        Since
        - 10.0
        """

        def get(self) -> "T":
            """
            Returns the (possibly null) reference wrapped by this instance.
            """
            ...


        def equals(self, obj: "Object") -> bool:
            """
            Returns `True` if Equivalence.equivalent(Object, Object) applied to the wrapped
            references is `True` and both wrappers use the Object.equals(Object) same
            equivalence.
            """
            ...


        def hashCode(self) -> int:
            """
            Returns the result of Equivalence.hash(Object) applied to the wrapped reference.
            """
            ...


        def toString(self) -> str:
            """
            Returns a string representation for this equivalence wrapper. The form of this string
            representation is not specified.
            """
            ...
