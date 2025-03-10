"""
Python module generated from Java source file com.google.common.math.BigDecimalMath

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.math import *
from java.math import BigDecimal
from java.math import RoundingMode
from typing import Any, Callable, Iterable, Tuple


class BigDecimalMath:
    """
    A class for arithmetic on BigDecimal that is not covered by its built-in methods.

    Author(s)
    - Louis Wasserman

    Since
    - 30.0
    """

    @staticmethod
    def roundToDouble(x: "BigDecimal", mode: "RoundingMode") -> float:
        """
        Returns `x`, rounded to a `double` with the specified rounding mode. If `x`
        is precisely representable as a `double`, its `double` value will be returned;
        otherwise, the rounding will choose between the two nearest representable values with `mode`.
        
        For the case of RoundingMode.HALF_DOWN, `HALF_UP`, and `HALF_EVEN`,
        infinite `double` values are considered infinitely far away. For example, 2^2000 is not
        representable as a double, but `roundToDouble(BigDecimal.valueOf(2).pow(2000), HALF_UP)`
        will return `Double.MAX_VALUE`, not `Double.POSITIVE_INFINITY`.
        
        For the case of RoundingMode.HALF_EVEN, this implementation uses the IEEE 754
        default rounding mode: if the two nearest representable values are equally near, the one with
        the least significant bit zero is chosen. (In such cases, both of the nearest representable
        values are even integers; this method returns the one that is a multiple of a greater power of
        two.)

        Raises
        - ArithmeticException: if `mode` is RoundingMode.UNNECESSARY and `x`
            is not precisely representable as a `double`

        Since
        - 30.0
        """
        ...
