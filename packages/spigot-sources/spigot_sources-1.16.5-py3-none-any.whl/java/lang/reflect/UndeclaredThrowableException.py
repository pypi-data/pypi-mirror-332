"""
Python module generated from Java source file java.lang.reflect.UndeclaredThrowableException

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import IOException
from java.io import ObjectInputStream
from java.io import ObjectOutputStream
from java.io import ObjectStreamField
from java.lang.reflect import *
from jdk.internal.access import SharedSecrets
from typing import Any, Callable, Iterable, Tuple


class UndeclaredThrowableException(RuntimeException):
    """
    Thrown by a method invocation on a proxy instance if its invocation
    handler's InvocationHandler.invoke invoke method throws a
    checked exception (a `Throwable` that is not assignable
    to `RuntimeException` or `Error`) that
    is not assignable to any of the exception types declared in the
    `throws` clause of the method that was invoked on the
    proxy instance and dispatched to the invocation handler.
    
    An `UndeclaredThrowableException` instance contains
    the undeclared checked exception that was thrown by the invocation
    handler, and it can be retrieved with the
    `getUndeclaredThrowable()` method.
    `UndeclaredThrowableException` extends
    `RuntimeException`, so it is an unchecked exception
    that wraps a checked exception.

    Author(s)
    - Peter Jones

    See
    - InvocationHandler

    Since
    - 1.3
    """

    def __init__(self, undeclaredThrowable: "Throwable"):
        """
        Constructs an `UndeclaredThrowableException` with the
        specified `Throwable`.

        Arguments
        - undeclaredThrowable: the undeclared checked exception
                 that was thrown
        """
        ...


    def __init__(self, undeclaredThrowable: "Throwable", s: str):
        """
        Constructs an `UndeclaredThrowableException` with the
        specified `Throwable` and a detail message.

        Arguments
        - undeclaredThrowable: the undeclared checked exception
                 that was thrown
        - s: the detail message
        """
        ...


    def getUndeclaredThrowable(self) -> "Throwable":
        """
        Returns the `Throwable` instance wrapped in this
        `UndeclaredThrowableException`, which may be `null`.

        Returns
        - the undeclared checked exception that was thrown

        Unknown Tags
        - This method predates the general-purpose exception chaining facility.
        The Throwable.getCause() method is now the preferred means of
        obtaining this information.
        """
        ...
