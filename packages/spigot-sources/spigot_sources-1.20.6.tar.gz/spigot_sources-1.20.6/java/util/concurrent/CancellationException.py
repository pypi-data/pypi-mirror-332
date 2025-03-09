"""
Python module generated from Java source file java.util.concurrent.CancellationException

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util.concurrent import *
from typing import Any, Callable, Iterable, Tuple


class CancellationException(IllegalStateException):
    """
    Exception indicating that the result of a value-producing task,
    such as a FutureTask, cannot be retrieved because the task
    was cancelled.

    Author(s)
    - Doug Lea

    Since
    - 1.5
    """

    def __init__(self):
        """
        Constructs a `CancellationException` with no detail message.
        """
        ...


    def __init__(self, message: str):
        """
        Constructs a `CancellationException` with the specified detail
        message.

        Arguments
        - message: the detail message
        """
        ...
