"""
Python module generated from Java source file com.google.common.cache.LongAddables

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.base import Supplier
from com.google.common.cache import *
from java.util.concurrent.atomic import AtomicLong
from typing import Any, Callable, Iterable, Tuple


class LongAddables:
    """
    Source of LongAddable objects that deals with GWT, Unsafe, and all that.

    Author(s)
    - Louis Wasserman
    """

    @staticmethod
    def create() -> "LongAddable":
        ...
