"""
Python module generated from Java source file java.nio.charset.IllegalCharsetNameException

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.nio.charset import *
from typing import Any, Callable, Iterable, Tuple


class IllegalCharsetNameException(IllegalArgumentException):

    def __init__(self, charsetName: str):
        """
        Constructs an instance of this class.

        Arguments
        - charsetName: The illegal charset name
        """
        ...


    def getCharsetName(self) -> str:
        """
        Retrieves the illegal charset name.

        Returns
        - The illegal charset name
        """
        ...
