"""
Python module generated from Java source file java.text.ParseException

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.text import *
from typing import Any, Callable, Iterable, Tuple


class ParseException(Exception):
    """
    Signals that an error has been reached unexpectedly
    while parsing.

    Author(s)
    - Mark Davis

    See
    - java.text.FieldPosition

    Since
    - 1.1
    """

    def __init__(self, s: str, errorOffset: int):
        """
        Constructs a ParseException with the specified detail message and
        offset.
        A detail message is a String that describes this particular exception.

        Arguments
        - s: the detail message
        - errorOffset: the position where the error is found while parsing.
        """
        ...


    def getErrorOffset(self) -> int:
        """
        Returns the position where the error was found.

        Returns
        - the position where the error was found
        """
        ...
