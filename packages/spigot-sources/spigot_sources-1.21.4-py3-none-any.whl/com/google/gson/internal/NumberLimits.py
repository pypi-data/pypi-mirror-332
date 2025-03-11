"""
Python module generated from Java source file com.google.gson.internal.NumberLimits

Java source file obtained from artifact gson version 2.11.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson.internal import *
from java.math import BigDecimal
from java.math import BigInteger
from typing import Any, Callable, Iterable, Tuple


class NumberLimits:
    """
    This class enforces limits on numbers parsed from JSON to avoid potential performance problems
    when extremely large numbers are used.
    """

    @staticmethod
    def parseBigDecimal(s: str) -> "BigDecimal":
        ...


    @staticmethod
    def parseBigInteger(s: str) -> "BigInteger":
        ...
