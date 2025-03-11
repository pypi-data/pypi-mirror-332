"""
Python module generated from Java source file com.google.common.util.concurrent.UncheckedTimeoutException

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import J2ktIncompatible
from com.google.common.util.concurrent import *
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class UncheckedTimeoutException(RuntimeException):
    """
    Unchecked version of java.util.concurrent.TimeoutException.

    Author(s)
    - Kevin Bourrillion

    Since
    - 1.0
    """

    def __init__(self):
        ...


    def __init__(self, message: str):
        ...


    def __init__(self, cause: "Throwable"):
        ...


    def __init__(self, message: str, cause: "Throwable"):
        ...
