"""
Python module generated from Java source file com.google.common.util.concurrent.ExecutionError

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.util.concurrent import *
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class ExecutionError(Error):
    """
    Error variant of java.util.concurrent.ExecutionException. As with `ExecutionException`, the error's .getCause() cause comes from a failed task,
    possibly run in another thread. That cause should itself be an `Error`; if not, use `ExecutionException` or UncheckedExecutionException. This allows the client code to
    continue to distinguish between exceptions and errors, even when they come from other threads.

    Author(s)
    - Chris Povirk

    Since
    - 10.0
    """

    def __init__(self, message: str, cause: "Error"):
        """
        Creates a new instance with the given detail message and cause.
        """
        ...


    def __init__(self, cause: "Error"):
        """
        Creates a new instance with the given cause.
        """
        ...
