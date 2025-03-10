"""
Python module generated from Java source file com.google.common.cache.LongAddable

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.cache import *
from typing import Any, Callable, Iterable, Tuple


class LongAddable:
    """
    Abstract interface for objects that can concurrently add longs.

    Author(s)
    - Louis Wasserman
    """

    def increment(self) -> None:
        ...


    def add(self, x: int) -> None:
        ...


    def sum(self) -> int:
        ...
