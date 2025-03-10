"""
Python module generated from Java source file java.nio.file.DirectoryIteratorException

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import IOException
from java.io import InvalidObjectException
from java.io import ObjectInputStream
from java.nio.file import *
from java.util import ConcurrentModificationException
from java.util import Objects
from typing import Any, Callable, Iterable, Tuple


class DirectoryIteratorException(ConcurrentModificationException):

    def __init__(self, cause: "IOException"):
        """
        Constructs an instance of this class.

        Arguments
        - cause: the `IOException` that caused the directory iteration
                 to fail

        Raises
        - NullPointerException: if the cause is `null`
        """
        ...


    def getCause(self) -> "IOException":
        """
        Returns the cause of this exception.

        Returns
        - the cause
        """
        ...
