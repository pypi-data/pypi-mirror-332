"""
Python module generated from Java source file java.util.NoSuchElementException

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import *
from typing import Any, Callable, Iterable, Tuple


class NoSuchElementException(RuntimeException):
    """
    Thrown by various accessor methods to indicate that the element being requested
    does not exist.

    See
    - java.util.Iterator.next()

    Since
    - 1.0
    """

    def __init__(self):
        """
        Constructs a `NoSuchElementException` with `null`
        as its error message string.
        """
        ...


    def __init__(self, s: str, cause: "Throwable"):
        """
        Constructs a `NoSuchElementException` with the specified detail
        message and cause.

        Arguments
        - s: the detail message, or null
        - cause: the cause (which is saved for later retrieval by the
                     .getCause() method), or null

        Since
        - 15
        """
        ...


    def __init__(self, cause: "Throwable"):
        """
        Constructs a `NoSuchElementException` with the specified cause.
        The detail message is set to `(cause == null ? null :
        cause.toString())` (which typically contains the class and
        detail message of `cause`).

        Arguments
        - cause: the cause (which is saved for later retrieval by the
                     .getCause() method)

        Since
        - 15
        """
        ...


    def __init__(self, s: str):
        """
        Constructs a `NoSuchElementException`, saving a reference
        to the error message string `s` for later retrieval by the
        `getMessage` method.

        Arguments
        - s: the detail message.
        """
        ...
