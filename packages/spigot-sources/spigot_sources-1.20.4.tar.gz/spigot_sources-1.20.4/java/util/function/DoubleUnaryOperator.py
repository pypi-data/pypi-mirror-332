"""
Python module generated from Java source file java.util.function.DoubleUnaryOperator

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import Objects
from java.util.function import *
from typing import Any, Callable, Iterable, Tuple


class DoubleUnaryOperator:
    """
    Represents an operation on a single `double`-valued operand that produces
    a `double`-valued result.  This is the primitive type specialization of
    UnaryOperator for `double`.
    
    This is a <a href="package-summary.html">functional interface</a>
    whose functional method is .applyAsDouble(double).

    See
    - UnaryOperator

    Since
    - 1.8
    """

    def applyAsDouble(self, operand: float) -> float:
        """
        Applies this operator to the given operand.

        Arguments
        - operand: the operand

        Returns
        - the operator result
        """
        ...


    def compose(self, before: "DoubleUnaryOperator") -> "DoubleUnaryOperator":
        """
        Returns a composed operator that first applies the `before`
        operator to its input, and then applies this operator to the result.
        If evaluation of either operator throws an exception, it is relayed to
        the caller of the composed operator.

        Arguments
        - before: the operator to apply before this operator is applied

        Returns
        - a composed operator that first applies the `before`
        operator and then applies this operator

        Raises
        - NullPointerException: if before is null

        See
        - .andThen(DoubleUnaryOperator)
        """
        ...


    def andThen(self, after: "DoubleUnaryOperator") -> "DoubleUnaryOperator":
        """
        Returns a composed operator that first applies this operator to
        its input, and then applies the `after` operator to the result.
        If evaluation of either operator throws an exception, it is relayed to
        the caller of the composed operator.

        Arguments
        - after: the operator to apply after this operator is applied

        Returns
        - a composed operator that first applies this operator and then
        applies the `after` operator

        Raises
        - NullPointerException: if after is null

        See
        - .compose(DoubleUnaryOperator)
        """
        ...


    @staticmethod
    def identity() -> "DoubleUnaryOperator":
        """
        Returns a unary operator that always returns its input argument.

        Returns
        - a unary operator that always returns its input argument
        """
        ...
