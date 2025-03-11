"""
Python module generated from Java source file com.google.common.util.concurrent.UncheckedExecutionException

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.util.concurrent import *
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class UncheckedExecutionException(RuntimeException):
    """
    Unchecked variant of java.util.concurrent.ExecutionException. As with `ExecutionException`, the exception's .getCause() cause comes from a failed task,
    possibly run in another thread.
    
    `UncheckedExecutionException` is intended as an alternative to `ExecutionException` when the exception thrown by a task is an unchecked exception. However, it
    may also wrap a checked exception in some cases.
    
    When wrapping an `Error` from another thread, prefer ExecutionError. When
    wrapping a checked exception, prefer `ExecutionException`.

    Author(s)
    - Charles Fry

    Since
    - 10.0
    """

    def __init__(self, message: str, cause: "Throwable"):
        """
        Creates a new instance with the given detail message and cause. Prefer to provide a
        non-nullable `cause`, as many users expect to find one.
        """
        ...


    def __init__(self, cause: "Throwable"):
        """
        Creates a new instance with `null` as its detail message and the given cause. Prefer to
        provide a non-nullable `cause`, as many users expect to find one.
        """
        ...
