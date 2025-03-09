"""
Python module generated from Java source file java.util.concurrent.TimeoutException

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util.concurrent import *
from typing import Any, Callable, Iterable, Tuple


class TimeoutException(Exception):
    """
    Exception thrown when a blocking operation times out.  Blocking
    operations for which a timeout is specified need a means to
    indicate that the timeout has occurred. For many such operations it
    is possible to return a value that indicates timeout; when that is
    not possible or desirable then `TimeoutException` should be
    declared and thrown.

    Author(s)
    - Doug Lea

    Since
    - 1.5
    """

    def __init__(self):
        """
        Constructs a `TimeoutException` with no specified detail
        message.
        """
        ...


    def __init__(self, message: str):
        """
        Constructs a `TimeoutException` with the specified detail
        message.

        Arguments
        - message: the detail message
        """
        ...
