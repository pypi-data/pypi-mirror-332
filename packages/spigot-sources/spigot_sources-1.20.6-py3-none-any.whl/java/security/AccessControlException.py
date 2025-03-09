"""
Python module generated from Java source file java.security.AccessControlException

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.security import *
from typing import Any, Callable, Iterable, Tuple


class AccessControlException(SecurityException):

    def __init__(self, s: str):
        """
        Constructs an `AccessControlException` with the
        specified, detailed message.

        Arguments
        - s: the detail message.
        """
        ...


    def __init__(self, s: str, p: "Permission"):
        """
        Constructs an `AccessControlException` with the
        specified, detailed message, and the requested permission that caused
        the exception.

        Arguments
        - s: the detail message.
        - p: the permission that caused the exception.
        """
        ...


    def getPermission(self) -> "Permission":
        """
        Gets the Permission object associated with this exception, or
        null if there was no corresponding Permission object.

        Returns
        - the Permission object.
        """
        ...
