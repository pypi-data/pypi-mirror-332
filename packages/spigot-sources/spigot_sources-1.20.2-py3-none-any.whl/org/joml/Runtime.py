"""
Python module generated from Java source file org.joml.Runtime

Java source file obtained from artifact joml version 1.10.5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.text import NumberFormat
from org.joml import *
from typing import Any, Callable, Iterable, Tuple


class Runtime:
    """
    Internal class to detect features of the runtime.

    Author(s)
    - Kai Burjack
    """

    HAS_floatToRawIntBits = hasFloatToRawIntBits()
    HAS_doubleToRawLongBits = hasDoubleToRawLongBits()
    HAS_Long_rotateLeft = hasLongRotateLeft()
    HAS_Math_fma = Options.USE_MATH_FMA && hasMathFma()


    @staticmethod
    def floatToIntBits(flt: float) -> int:
        ...


    @staticmethod
    def doubleToLongBits(dbl: float) -> int:
        ...


    @staticmethod
    def formatNumbers(str: str) -> str:
        ...


    @staticmethod
    def format(number: float, format: "NumberFormat") -> str:
        ...


    @staticmethod
    def equals(a: float, b: float, delta: float) -> bool:
        ...


    @staticmethod
    def equals(a: float, b: float, delta: float) -> bool:
        ...
