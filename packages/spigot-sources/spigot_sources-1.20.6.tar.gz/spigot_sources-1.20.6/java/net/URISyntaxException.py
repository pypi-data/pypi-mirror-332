"""
Python module generated from Java source file java.net.URISyntaxException

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.net import *
from typing import Any, Callable, Iterable, Tuple


class URISyntaxException(Exception):

    def __init__(self, input: str, reason: str, index: int):
        """
        Constructs an instance from the given input string, reason, and error
        index.

        Arguments
        - input: The input string
        - reason: A string explaining why the input could not be parsed
        - index: The index at which the parse error occurred,
                        or `-1` if the index is not known

        Raises
        - NullPointerException: If either the input or reason strings are `null`
        - IllegalArgumentException: If the error index is less than `-1`
        """
        ...


    def __init__(self, input: str, reason: str):
        """
        Constructs an instance from the given input string and reason.  The
        resulting object will have an error index of `-1`.

        Arguments
        - input: The input string
        - reason: A string explaining why the input could not be parsed

        Raises
        - NullPointerException: If either the input or reason strings are `null`
        """
        ...


    def getInput(self) -> str:
        """
        Returns the input string.

        Returns
        - The input string
        """
        ...


    def getReason(self) -> str:
        """
        Returns a string explaining why the input string could not be parsed.

        Returns
        - The reason string
        """
        ...


    def getIndex(self) -> int:
        """
        Returns an index into the input string of the position at which the
        parse error occurred, or `-1` if this position is not known.

        Returns
        - The error index
        """
        ...


    def getMessage(self) -> str:
        """
        Returns a string describing the parse error.  The resulting string
        consists of the reason string followed by a colon character
        (`':'`), a space, and the input string.  If the error index is
        defined then the string `" at index "` followed by the index, in
        decimal, is inserted after the reason string and before the colon
        character.

        Returns
        - A string describing the parse error
        """
        ...
