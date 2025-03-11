"""
Python module generated from Java source file com.google.gson.ToNumberPolicy

Java source file obtained from artifact gson version 2.11.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson import *
from com.google.gson.internal import LazilyParsedNumber
from com.google.gson.internal import NumberLimits
from com.google.gson.stream import JsonReader
from com.google.gson.stream import MalformedJsonException
from enum import Enum
from java.io import IOException
from java.math import BigDecimal
from typing import Any, Callable, Iterable, Tuple


class ToNumberPolicy(Enum):
    """
    An enumeration that defines two standard number reading strategies and a couple of strategies to
    overcome some historical Gson limitations while deserializing numbers as Object and
    Number.

    See
    - ToNumberStrategy

    Since
    - 2.8.9
    """

    DOUBLE = 0
    """
    Using this policy will ensure that numbers will be read as Double values. This is the
    default strategy used during deserialization of numbers as Object.
    """
    LAZILY_PARSED_NUMBER = 1
    """
    Using this policy will ensure that numbers will be read as a lazily parsed number backed by a
    string. This is the default strategy used during deserialization of numbers as Number.
    """
    LONG_OR_DOUBLE = 2
    """
    Using this policy will ensure that numbers will be read as Long or Double
    values depending on how JSON numbers are represented: `Long` if the JSON number can be
    parsed as a `Long` value, or otherwise `Double` if it can be parsed as a `Double` value. If the parsed double-precision number results in a positive or negative infinity
    (Double.isInfinite()) or a NaN (Double.isNaN()) value and the `JsonReader` is not JsonReader.isLenient() lenient, a MalformedJsonException is
    thrown.
    """
    BIG_DECIMAL = 3
    """
    Using this policy will ensure that numbers will be read as numbers of arbitrary length using
    BigDecimal.
    """
