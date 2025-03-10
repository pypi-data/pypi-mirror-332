"""
Python module generated from Java source file com.google.common.collect.ComputationException

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.collect import *
from javax.annotation import Nullable
from typing import Any, Callable, Iterable, Tuple


class ComputationException(RuntimeException):
    """
    Wraps an exception that occurred during a computation.

    Author(s)
    - Bob Lee

    Since
    - 2.0
    """

    def __init__(self, cause: "Throwable"):
        """
        Creates a new instance with the given cause.
        """
        ...
