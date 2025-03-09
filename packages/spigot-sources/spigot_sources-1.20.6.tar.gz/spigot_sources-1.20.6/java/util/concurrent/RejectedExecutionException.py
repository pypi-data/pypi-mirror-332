"""
Python module generated from Java source file java.util.concurrent.RejectedExecutionException

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util.concurrent import *
from typing import Any, Callable, Iterable, Tuple


class RejectedExecutionException(RuntimeException):
    """
    Exception thrown by an Executor when a task cannot be
    accepted for execution.

    Author(s)
    - Doug Lea

    Since
    - 1.5
    """

    def __init__(self):
        """
        Constructs a `RejectedExecutionException` with no detail message.
        The cause is not initialized, and may subsequently be
        initialized by a call to .initCause(Throwable) initCause.
        """
        ...


    def __init__(self, message: str):
        """
        Constructs a `RejectedExecutionException` with the
        specified detail message. The cause is not initialized, and may
        subsequently be initialized by a call to .initCause(Throwable) initCause.

        Arguments
        - message: the detail message
        """
        ...


    def __init__(self, message: str, cause: "Throwable"):
        """
        Constructs a `RejectedExecutionException` with the
        specified detail message and cause.

        Arguments
        - message: the detail message
        - cause: the cause (which is saved for later retrieval by the
                .getCause() method)
        """
        ...


    def __init__(self, cause: "Throwable"):
        """
        Constructs a `RejectedExecutionException` with the
        specified cause.  The detail message is set to `(cause ==
        null ? null : cause.toString())` (which typically contains
        the class and detail message of `cause`).

        Arguments
        - cause: the cause (which is saved for later retrieval by the
                .getCause() method)
        """
        ...
