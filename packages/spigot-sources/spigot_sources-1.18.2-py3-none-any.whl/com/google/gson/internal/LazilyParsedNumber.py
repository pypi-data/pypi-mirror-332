"""
Python module generated from Java source file com.google.gson.internal.LazilyParsedNumber

Java source file obtained from artifact gson version 2.8.9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson.internal import *
from java.io import IOException
from java.io import InvalidObjectException
from java.io import ObjectInputStream
from java.io import ObjectStreamException
from java.math import BigDecimal
from typing import Any, Callable, Iterable, Tuple


class LazilyParsedNumber(Number):
    """
    This class holds a number value that is lazily converted to a specific number type

    Author(s)
    - Inderjeet Singh
    """

    def __init__(self, value: str):
        """
        Arguments
        - value: must not be null
        """
        ...


    def intValue(self) -> int:
        ...


    def longValue(self) -> int:
        ...


    def floatValue(self) -> float:
        ...


    def doubleValue(self) -> float:
        ...


    def toString(self) -> str:
        ...


    def hashCode(self) -> int:
        ...


    def equals(self, obj: "Object") -> bool:
        ...
