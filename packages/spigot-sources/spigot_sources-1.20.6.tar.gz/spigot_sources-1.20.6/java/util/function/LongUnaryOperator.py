"""
Python module generated from Java source file java.util.function.LongUnaryOperator

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import Objects
from java.util.function import *
from typing import Any, Callable, Iterable, Tuple


class LongUnaryOperator:
    """
    Represents an operation on a single `long`-valued operand that produces
    a `long`-valued result.  This is the primitive type specialization of
    UnaryOperator for `long`.
    
    This is a <a href="package-summary.html">functional interface</a>
    whose functional method is .applyAsLong(long).

    See
    - UnaryOperator

    Since
    - 1.8
    """

    def applyAsLong(self, operand: int) -> int:
        """
        Applies this operator to the given operand.

        Arguments
        - operand: the operand

        Returns
        - the operator result
        """
        ...


    def compose(self, before: "LongUnaryOperator") -> "LongUnaryOperator":
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
        - .andThen(LongUnaryOperator)
        """
        ...


    def andThen(self, after: "LongUnaryOperator") -> "LongUnaryOperator":
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
        - .compose(LongUnaryOperator)
        """
        ...


    @staticmethod
    def identity() -> "LongUnaryOperator":
        """
        Returns a unary operator that always returns its input argument.

        Returns
        - a unary operator that always returns its input argument
        """
        ...
