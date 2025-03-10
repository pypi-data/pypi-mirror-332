"""
Python module generated from Java source file java.util.function.Predicate

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import Objects
from java.util.function import *
from typing import Any, Callable, Iterable, Tuple


class Predicate:
    """
    Represents a predicate (boolean-valued function) of one argument.
    
    This is a <a href="package-summary.html">functional interface</a>
    whose functional method is .test(Object).
    
    Type `<T>`: the type of the input to the predicate

    Since
    - 1.8
    """

    def test(self, t: "T") -> bool:
        """
        Evaluates this predicate on the given argument.

        Arguments
        - t: the input argument

        Returns
        - `True` if the input argument matches the predicate,
        otherwise `False`
        """
        ...


    def and(self, other: "Predicate"["T"]) -> "Predicate"["T"]:
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


    def negate(self) -> "Predicate"["T"]:
        """
        Returns a predicate that represents the logical negation of this
        predicate.

        Returns
        - a predicate that represents the logical negation of this
        predicate
        """
        ...


    def or(self, other: "Predicate"["T"]) -> "Predicate"["T"]:
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


    @staticmethod
    def isEqual(targetRef: "Object") -> "Predicate"["T"]:
        """
        Returns a predicate that tests if two arguments are equal according
        to Objects.equals(Object, Object).
        
        Type `<T>`: the type of arguments to the predicate

        Arguments
        - targetRef: the object reference with which to compare for equality,
                      which may be `null`

        Returns
        - a predicate that tests if two arguments are equal according
        to Objects.equals(Object, Object)
        """
        ...


    @staticmethod
    def not(target: "Predicate"["T"]) -> "Predicate"["T"]:
        """
        Returns a predicate that is the negation of the supplied predicate.
        This is accomplished by returning result of the calling
        `target.negate()`.
        
        Type `<T>`: the type of arguments to the specified predicate

        Arguments
        - target: predicate to negate

        Returns
        - a predicate that negates the results of the supplied
                predicate

        Raises
        - NullPointerException: if target is null

        Since
        - 11
        """
        ...
