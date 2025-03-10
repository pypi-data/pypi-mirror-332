"""
Python module generated from Java source file com.google.common.cache.Weigher

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.cache import *
from typing import Any, Callable, Iterable, Tuple


class Weigher:
    """
    Calculates the weights of cache entries.

    Author(s)
    - Charles Fry

    Since
    - 11.0
    """

    def weigh(self, key: "K", value: "V") -> int:
        """
        Returns the weight of a cache entry. There is no unit for entry weights; rather they are simply
        relative to each other.

        Returns
        - the weight of the entry; must be non-negative
        """
        ...
