"""
Python module generated from Java source file java.security.PrivilegedAction

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.security import *
from typing import Any, Callable, Iterable, Tuple


class PrivilegedAction:
    """
    A computation to be performed with privileges enabled.  The computation is
    performed by invoking `AccessController.doPrivileged` on the
    `PrivilegedAction` object.  This interface is used only for
    computations that do not throw checked exceptions; computations that
    throw checked exceptions must use `PrivilegedExceptionAction`
    instead.

    See
    - PrivilegedExceptionAction

    Since
    - 1.2
    """

    def run(self) -> "T":
        """
        Performs the computation.  This method will be called by
        `AccessController.doPrivileged` after enabling privileges.

        Returns
        - a class-dependent value that may represent the results of the
                computation. Each class that implements
                `PrivilegedAction`
                should document what (if anything) this value represents.

        See
        - AccessController.doPrivileged(PrivilegedAction,
                                            AccessControlContext)
        """
        ...
