"""
Python module generated from Java source file java.util.concurrent.ExecutionException

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util.concurrent import *
from typing import Any, Callable, Iterable, Tuple


class ExecutionException(Exception):
    """
    Exception thrown when attempting to retrieve the result of a task
    that aborted by throwing an exception. This exception can be
    inspected using the .getCause() method.

    Author(s)
    - Doug Lea

    See
    - Future

    Since
    - 1.5
    """

    def __init__(self, message: str, cause: "Throwable"):
        """
        Constructs an `ExecutionException` with the specified detail
        message and cause.

        Arguments
        - message: the detail message
        - cause: the cause (which is saved for later retrieval by the
                .getCause() method)
        """
        ...


    def __init__(self, cause: "Throwable"):
        """
        Constructs an `ExecutionException` with the specified cause.
        The detail message is set to `(cause == null ? null :
        cause.toString())` (which typically contains the class and
        detail message of `cause`).

        Arguments
        - cause: the cause (which is saved for later retrieval by the
                .getCause() method)
        """
        ...
