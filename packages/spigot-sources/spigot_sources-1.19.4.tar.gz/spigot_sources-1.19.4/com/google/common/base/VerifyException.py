"""
Python module generated from Java source file com.google.common.base.VerifyException

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.base import *
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class VerifyException(RuntimeException):
    """
    Exception thrown upon the failure of a <a
    href="https://github.com/google/guava/wiki/ConditionalFailuresExplained">verification check</a>,
    including those performed by the convenience methods of the Verify class.

    Since
    - 17.0
    """

    def __init__(self):
        """
        Constructs a `VerifyException` with no message.
        """
        ...


    def __init__(self, message: str):
        """
        Constructs a `VerifyException` with the message `message`.
        """
        ...


    def __init__(self, cause: "Throwable"):
        """
        Constructs a `VerifyException` with the cause `cause` and a message that is `null` if `cause` is null, and `cause.toString()` otherwise.

        Since
        - 19.0
        """
        ...


    def __init__(self, message: str, cause: "Throwable"):
        """
        Constructs a `VerifyException` with the message `message` and the cause `cause`.

        Since
        - 19.0
        """
        ...
