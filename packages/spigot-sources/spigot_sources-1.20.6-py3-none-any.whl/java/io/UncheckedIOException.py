"""
Python module generated from Java source file java.io.UncheckedIOException

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import *
from java.util import Objects
from typing import Any, Callable, Iterable, Tuple


class UncheckedIOException(RuntimeException):
    """
    Wraps an IOException with an unchecked exception.

    Since
    - 1.8
    """

    def __init__(self, message: str, cause: "IOException"):
        """
        Constructs an instance of this class.

        Arguments
        - message: the detail message, can be null
        - cause: the `IOException`

        Raises
        - NullPointerException: if the cause is `null`
        """
        ...


    def __init__(self, cause: "IOException"):
        """
        Constructs an instance of this class.

        Arguments
        - cause: the `IOException`

        Raises
        - NullPointerException: if the cause is `null`
        """
        ...


    def getCause(self) -> "IOException":
        """
        Returns the cause of this exception.

        Returns
        - the `IOException` which is the cause of this exception.
        """
        ...
