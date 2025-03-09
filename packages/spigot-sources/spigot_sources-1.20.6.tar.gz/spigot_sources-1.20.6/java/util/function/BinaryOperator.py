"""
Python module generated from Java source file java.util.function.BinaryOperator

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import Comparator
from java.util import Objects
from java.util.function import *
from typing import Any, Callable, Iterable, Tuple


class BinaryOperator(BiFunction):
    """
    Represents an operation upon two operands of the same type, producing a result
    of the same type as the operands.  This is a specialization of
    BiFunction for the case where the operands and the result are all of
    the same type.
    
    This is a <a href="package-summary.html">functional interface</a>
    whose functional method is .apply(Object, Object).
    
    Type `<T>`: the type of the operands and result of the operator

    See
    - UnaryOperator

    Since
    - 1.8
    """

    @staticmethod
    def minBy(comparator: "Comparator"["T"]) -> "BinaryOperator"["T"]:
        """
        Returns a BinaryOperator which returns the lesser of two elements
        according to the specified `Comparator`.
        
        Type `<T>`: the type of the input arguments of the comparator

        Arguments
        - comparator: a `Comparator` for comparing the two values

        Returns
        - a `BinaryOperator` which returns the lesser of its operands,
                according to the supplied `Comparator`

        Raises
        - NullPointerException: if the argument is null
        """
        ...


    @staticmethod
    def maxBy(comparator: "Comparator"["T"]) -> "BinaryOperator"["T"]:
        """
        Returns a BinaryOperator which returns the greater of two elements
        according to the specified `Comparator`.
        
        Type `<T>`: the type of the input arguments of the comparator

        Arguments
        - comparator: a `Comparator` for comparing the two values

        Returns
        - a `BinaryOperator` which returns the greater of its operands,
                according to the supplied `Comparator`

        Raises
        - NullPointerException: if the argument is null
        """
        ...
