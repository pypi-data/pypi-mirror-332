"""
Python module generated from Java source file java.util.regex.PatternSyntaxException

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util.regex import *
from typing import Any, Callable, Iterable, Tuple


class PatternSyntaxException(IllegalArgumentException):

    def __init__(self, desc: str, regex: str, index: int):
        """
        Constructs a new instance of this class.

        Arguments
        - desc: A description of the error
        - regex: The erroneous pattern
        - index: The approximate index in the pattern of the error,
                or `-1` if the index is not known
        """
        ...


    def getIndex(self) -> int:
        """
        Retrieves the error index.

        Returns
        - The approximate index in the pattern of the error,
                or `-1` if the index is not known
        """
        ...


    def getDescription(self) -> str:
        """
        Retrieves the description of the error.

        Returns
        - The description of the error
        """
        ...


    def getPattern(self) -> str:
        """
        Retrieves the erroneous regular-expression pattern.

        Returns
        - The erroneous pattern
        """
        ...


    def getMessage(self) -> str:
        """
        Returns a multi-line string containing the description of the syntax
        error and its index, the erroneous regular-expression pattern, and a
        visual indication of the error index within the pattern.

        Returns
        - The full detail message
        """
        ...
