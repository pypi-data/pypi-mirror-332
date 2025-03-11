"""
Python module generated from Java source file java.util.function.DoubleBinaryOperator

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util.function import *
from typing import Any, Callable, Iterable, Tuple


class DoubleBinaryOperator:
    """
    Represents an operation upon two `double`-valued operands and producing a
    `double`-valued result.   This is the primitive type specialization of
    BinaryOperator for `double`.
    
    This is a <a href="package-summary.html">functional interface</a>
    whose functional method is .applyAsDouble(double, double).

    See
    - DoubleUnaryOperator

    Since
    - 1.8
    """

    def applyAsDouble(self, left: float, right: float) -> float:
        """
        Applies this operator to the given operands.

        Arguments
        - left: the first operand
        - right: the second operand

        Returns
        - the operator result
        """
        ...
