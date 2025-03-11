"""
Python module generated from Java source file java.io.InvalidObjectException

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import *
from typing import Any, Callable, Iterable, Tuple


class InvalidObjectException(ObjectStreamException):
    """
    Indicates that one or more deserialized objects failed validation
    tests.  The argument should provide the reason for the failure.

    See
    - ObjectInputValidation

    Since
    - 1.1
    """

    def __init__(self, reason: str):
        """
        Constructs an `InvalidObjectException`.

        Arguments
        - reason: Detailed message explaining the reason for the failure.

        See
        - ObjectInputValidation
        """
        ...
