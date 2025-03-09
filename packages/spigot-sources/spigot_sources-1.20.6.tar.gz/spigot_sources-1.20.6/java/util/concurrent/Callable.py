"""
Python module generated from Java source file java.util.concurrent.Callable

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util.concurrent import *
from typing import Any, Callable, Iterable, Tuple


class Callable:
    """
    A task that returns a result and may throw an exception.
    Implementors define a single method with no arguments called
    `call`.
    
    The `Callable` interface is similar to java.lang.Runnable, in that both are designed for classes whose
    instances are potentially executed by another thread.  A
    `Runnable`, however, does not return a result and cannot
    throw a checked exception.
    
    The Executors class contains utility methods to
    convert from other common forms to `Callable` classes.
    
    Type `<V>`: the result type of method `call`

    Author(s)
    - Doug Lea

    See
    - Executor

    Since
    - 1.5
    """

    def call(self) -> "V":
        """
        Computes a result, or throws an exception if unable to do so.

        Returns
        - computed result

        Raises
        - Exception: if unable to compute a result
        """
        ...
