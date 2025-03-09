"""
Python module generated from Java source file com.google.common.collect.ComputationException

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.collect import *
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class ComputationException(RuntimeException):
    """
    Wraps an exception that occurred during a computation.

    Author(s)
    - Bob Lee

    Since
    - 2.0

    Deprecated
    - This exception is no longer thrown by `com.google.common`. Previously, it was
        thrown by MapMaker computing maps. When support for computing maps was removed from
        `MapMaker`, it was added to `CacheBuilder`, which throws `ExecutionException`, `UncheckedExecutionException`, and `ExecutionError`. Any
        code that is still catching `ComputationException` may need to be updated to catch some
        of those types instead. (Note that this type, though deprecated, is not planned to be removed
        from Guava.)
    """

    def __init__(self, cause: "Throwable"):
        """
        Creates a new instance with the given cause.
        """
        ...
