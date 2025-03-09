"""
Python module generated from Java source file java.lang.reflect.InvocationTargetException

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.lang.reflect import *
from typing import Any, Callable, Iterable, Tuple


class InvocationTargetException(ReflectiveOperationException):
    """
    InvocationTargetException is a checked exception that wraps
    an exception thrown by an invoked method or constructor.

    See
    - Constructor

    Since
    - 1.1
    """

    def __init__(self, target: "Throwable"):
        """
        Constructs a InvocationTargetException with a target exception.

        Arguments
        - target: the target exception
        """
        ...


    def __init__(self, target: "Throwable", s: str):
        """
        Constructs a InvocationTargetException with a target exception
        and a detail message.

        Arguments
        - target: the target exception
        - s: the detail message
        """
        ...


    def getTargetException(self) -> "Throwable":
        """
        Get the thrown target exception.

        Returns
        - the thrown target exception (cause of this exception).

        Unknown Tags
        - This method predates the general-purpose exception chaining facility.
        The Throwable.getCause() method is now the preferred means of
        obtaining this information.
        """
        ...


    def getCause(self) -> "Throwable":
        """
        Returns the cause of this exception (the thrown target exception,
        which may be `null`).

        Returns
        - the cause of this exception.

        Since
        - 1.4
        """
        ...
