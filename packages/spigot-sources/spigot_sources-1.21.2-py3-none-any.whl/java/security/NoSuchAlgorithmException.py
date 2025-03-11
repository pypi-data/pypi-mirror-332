"""
Python module generated from Java source file java.security.NoSuchAlgorithmException

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.security import *
from typing import Any, Callable, Iterable, Tuple


class NoSuchAlgorithmException(GeneralSecurityException):

    def __init__(self):
        """
        Constructs a NoSuchAlgorithmException with no detail
        message. A detail message is a String that describes this
        particular exception.
        """
        ...


    def __init__(self, msg: str):
        """
        Constructs a NoSuchAlgorithmException with the specified
        detail message. A detail message is a String that describes
        this particular exception, which may, for example, specify which
        algorithm is not available.

        Arguments
        - msg: the detail message.
        """
        ...


    def __init__(self, message: str, cause: "Throwable"):
        """
        Creates a `NoSuchAlgorithmException` with the specified
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
        Creates a `NoSuchAlgorithmException` with the specified cause
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
