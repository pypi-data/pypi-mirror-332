"""
Python module generated from Java source file java.security.InvalidKeyException

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.security import *
from typing import Any, Callable, Iterable, Tuple


class InvalidKeyException(KeyException):

    def __init__(self):
        """
        Constructs an InvalidKeyException with no detail message. A
        detail message is a String that describes this particular
        exception.
        """
        ...


    def __init__(self, msg: str):
        """
        Constructs an InvalidKeyException with the specified detail
        message. A detail message is a String that describes this
        particular exception.

        Arguments
        - msg: the detail message.
        """
        ...


    def __init__(self, message: str, cause: "Throwable"):
        """
        Creates an `InvalidKeyException` with the specified
        detail message and cause.

        Arguments
        - message: the detail message (which is saved for later retrieval
               by the .getMessage() method).
        - cause: the cause (which is saved for later retrieval by the
               .getCause() method).  (A `null` value is permitted,
               and indicates that the cause is nonexistent or unknown.)

        Since
        - 1.5
        """
        ...


    def __init__(self, cause: "Throwable"):
        """
        Creates an `InvalidKeyException` with the specified cause
        and a detail message of `(cause==null ? null : cause.toString())`
        (which typically contains the class and detail message of
        `cause`).

        Arguments
        - cause: the cause (which is saved for later retrieval by the
               .getCause() method).  (A `null` value is permitted,
               and indicates that the cause is nonexistent or unknown.)

        Since
        - 1.5
        """
        ...
