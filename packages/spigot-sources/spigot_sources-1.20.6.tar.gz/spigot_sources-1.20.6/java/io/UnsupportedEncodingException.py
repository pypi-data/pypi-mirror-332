"""
Python module generated from Java source file java.io.UnsupportedEncodingException

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import *
from typing import Any, Callable, Iterable, Tuple


class UnsupportedEncodingException(IOException):
    """
    The Character Encoding is not supported.

    Author(s)
    - Asmus Freytag

    Since
    - 1.1
    """

    def __init__(self):
        """
        Constructs an UnsupportedEncodingException without a detail message.
        """
        ...


    def __init__(self, s: str):
        """
        Constructs an UnsupportedEncodingException with a detail message.

        Arguments
        - s: Describes the reason for the exception.
        """
        ...
