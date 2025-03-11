"""
Python module generated from Java source file java.io.IOException

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import *
from typing import Any, Callable, Iterable, Tuple


class IOException(Exception):
    """
    Signals that an I/O exception of some sort has occurred. This
    class is the general class of exceptions produced by failed or
    interrupted I/O operations.

    See
    - java.io.OutputStream

    Since
    - 1.0
    """

    def __init__(self):
        """
        Constructs an `IOException` with `null`
        as its error detail message.
        """
        ...


    def __init__(self, message: str):
        """
        Constructs an `IOException` with the specified detail message.

        Arguments
        - message: The detail message (which is saved for later retrieval
               by the .getMessage() method)
        """
        ...


    def __init__(self, message: str, cause: "Throwable"):
        """
        Constructs an `IOException` with the specified detail message
        and cause.
        
         Note that the detail message associated with `cause` is
        *not* automatically incorporated into this exception's detail
        message.

        Arguments
        - message: The detail message (which is saved for later retrieval
               by the .getMessage() method)
        - cause: The cause (which is saved for later retrieval by the
               .getCause() method).  (A null value is permitted,
               and indicates that the cause is nonexistent or unknown.)

        Since
        - 1.6
        """
        ...


    def __init__(self, cause: "Throwable"):
        """
        Constructs an `IOException` with the specified cause and a
        detail message of `(cause==null ? null : cause.toString())`
        (which typically contains the class and detail message of `cause`).
        This constructor is useful for IO exceptions that are little more
        than wrappers for other throwables.

        Arguments
        - cause: The cause (which is saved for later retrieval by the
               .getCause() method).  (A null value is permitted,
               and indicates that the cause is nonexistent or unknown.)

        Since
        - 1.6
        """
        ...
