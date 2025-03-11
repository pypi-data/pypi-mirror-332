"""
Python module generated from Java source file java.util.function.LongBinaryOperator

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util.function import *
from typing import Any, Callable, Iterable, Tuple


class LongBinaryOperator:
    """
    Represents an operation upon two `long`-valued operands and producing a
    `long`-valued result.   This is the primitive type specialization of
    BinaryOperator for `long`.
    
    This is a <a href="package-summary.html">functional interface</a>
    whose functional method is .applyAsLong(long, long).

    See
    - LongUnaryOperator

    Since
    - 1.8
    """

    def applyAsLong(self, left: int, right: int) -> int:
        """
        Applies this operator to the given operands.

        Arguments
        - left: the first operand
        - right: the second operand

        Returns
        - the operator result
        """
        ...
