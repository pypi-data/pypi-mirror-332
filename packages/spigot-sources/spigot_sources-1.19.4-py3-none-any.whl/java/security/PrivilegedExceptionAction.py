"""
Python module generated from Java source file java.security.PrivilegedExceptionAction

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.security import *
from typing import Any, Callable, Iterable, Tuple


class PrivilegedExceptionAction:
    """
    A computation to be performed with privileges enabled, that throws one or
    more checked exceptions.  The computation is performed by invoking
    `AccessController.doPrivileged` on the
    `PrivilegedExceptionAction` object.  This interface is
    used only for computations that throw checked exceptions;
    computations that do not throw
    checked exceptions should use `PrivilegedAction` instead.

    See
    - PrivilegedAction

    Since
    - 1.2
    """

    def run(self) -> "T":
        ...
