"""
Python module generated from Java source file java.text.ParsePosition

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.text import *
from typing import Any, Callable, Iterable, Tuple


class ParsePosition:

    def __init__(self, index: int):
        """
        Create a new ParsePosition with the given initial index.

        Arguments
        - index: initial index
        """
        ...


    def getIndex(self) -> int:
        """
        Retrieve the current parse position.  On input to a parse method, this
        is the index of the character at which parsing will begin; on output, it
        is the index of the character following the last character parsed.

        Returns
        - the current parse position
        """
        ...


    def setIndex(self, index: int) -> None:
        """
        Set the current parse position.

        Arguments
        - index: the current parse position
        """
        ...


    def setErrorIndex(self, ei: int) -> None:
        """
        Set the index at which a parse error occurred.  Formatters
        should set this before returning an error code from their
        parseObject method.  The default value is -1 if this is not set.

        Arguments
        - ei: the index at which an error occurred

        Since
        - 1.2
        """
        ...


    def getErrorIndex(self) -> int:
        """
        Retrieve the index at which an error occurred, or -1 if the
        error index has not been set.

        Returns
        - the index at which an error occurred

        Since
        - 1.2
        """
        ...


    def equals(self, obj: "Object") -> bool:
        """
        Overrides equals
        """
        ...


    def hashCode(self) -> int:
        """
        Returns a hash code for this ParsePosition.

        Returns
        - a hash code value for this object
        """
        ...


    def toString(self) -> str:
        """
        Return a string representation of this ParsePosition.

        Returns
        - a string representation of this object
        """
        ...
