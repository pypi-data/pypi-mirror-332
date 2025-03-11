"""
Python module generated from Java source file com.google.common.collect.BoundType

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.collect import *
from enum import Enum
from typing import Any, Callable, Iterable, Tuple


class BoundType(Enum):
    """
    Indicates whether an endpoint of some range is contained in the range itself ("closed") or not
    ("open"). If a range is unbounded on a side, it is neither open nor closed on that side; the
    bound simply does not exist.

    Since
    - 10.0
    """

    OPEN = (False)
    """
    The endpoint value *is not* considered part of the set ("exclusive").
    """
    CLOSED = (True)
