"""
Python module generated from Java source file java.security.PrivilegedActionException

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import IOException
from java.io import ObjectInputStream
from java.io import ObjectOutputStream
from java.io import ObjectStreamField
from java.security import *
from jdk.internal.access import SharedSecrets
from typing import Any, Callable, Iterable, Tuple


class PrivilegedActionException(Exception):
    """
    This exception is thrown by
    `doPrivileged(PrivilegedExceptionAction)` and
    `doPrivileged(PrivilegedExceptionAction,
    AccessControlContext context)` to indicate
    that the action being performed threw a checked exception.  The exception
    thrown by the action can be obtained by calling the
    `getException` method.  In effect, an
    `PrivilegedActionException` is a "wrapper"
    for an exception thrown by a privileged action.

    See
    - AccessController.doPrivileged(PrivilegedExceptionAction,AccessControlContext)

    Since
    - 1.2
    """

    def __init__(self, exception: "Exception"):
        """
        Constructs a new PrivilegedActionException &quot;wrapping&quot;
        the specific Exception.

        Arguments
        - exception: The exception thrown
        """
        ...


    def getException(self) -> "Exception":
        """
        Returns the exception thrown by the privileged computation that
        resulted in this `PrivilegedActionException`.

        Returns
        - the exception thrown by the privileged computation that
                resulted in this `PrivilegedActionException`.

        See
        - AccessController.doPrivileged(PrivilegedExceptionAction,
                                                   AccessControlContext)

        Unknown Tags
        - This method predates the general-purpose exception chaining facility.
        The Throwable.getCause() method is now the preferred means of
        obtaining this information.
        """
        ...


    def toString(self) -> str:
        ...
