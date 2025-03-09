"""
Python module generated from Java source file java.util.function.BiPredicate

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import Objects
from java.util.function import *
from typing import Any, Callable, Iterable, Tuple


class BiPredicate:
    """
    Represents a predicate (boolean-valued function) of two arguments.  This is
    the two-arity specialization of Predicate.
    
    This is a <a href="package-summary.html">functional interface</a>
    whose functional method is .test(Object, Object).
    
    Type `<T>`: the type of the first argument to the predicate
    
    Type `<U>`: the type of the second argument the predicate

    See
    - Predicate

    Since
    - 1.8
    """

    def test(self, t: "T", u: "U") -> bool:
        """
        Evaluates this predicate on the given arguments.

        Arguments
        - t: the first input argument
        - u: the second input argument

        Returns
        - `True` if the input arguments match the predicate,
        otherwise `False`
        """
        ...


    def and(self, other: "BiPredicate"["T", "U"]) -> "BiPredicate"["T", "U"]:
        """
        Returns a composed predicate that represents a short-circuiting logical
        AND of this predicate and another.  When evaluating the composed
        predicate, if this predicate is `False`, then the `other`
        predicate is not evaluated.
        
        Any exceptions thrown during evaluation of either predicate are relayed
        to the caller; if evaluation of this predicate throws an exception, the
        `other` predicate will not be evaluated.

        Arguments
        - other: a predicate that will be logically-ANDed with this
                     predicate

        Returns
        - a composed predicate that represents the short-circuiting logical
        AND of this predicate and the `other` predicate

        Raises
        - NullPointerException: if other is null
        """
        ...


    def negate(self) -> "BiPredicate"["T", "U"]:
        """
        Returns a predicate that represents the logical negation of this
        predicate.

        Returns
        - a predicate that represents the logical negation of this
        predicate
        """
        ...


    def or(self, other: "BiPredicate"["T", "U"]) -> "BiPredicate"["T", "U"]:
        """
        Returns a composed predicate that represents a short-circuiting logical
        OR of this predicate and another.  When evaluating the composed
        predicate, if this predicate is `True`, then the `other`
        predicate is not evaluated.
        
        Any exceptions thrown during evaluation of either predicate are relayed
        to the caller; if evaluation of this predicate throws an exception, the
        `other` predicate will not be evaluated.

        Arguments
        - other: a predicate that will be logically-ORed with this
                     predicate

        Returns
        - a composed predicate that represents the short-circuiting logical
        OR of this predicate and the `other` predicate

        Raises
        - NullPointerException: if other is null
        """
        ...
