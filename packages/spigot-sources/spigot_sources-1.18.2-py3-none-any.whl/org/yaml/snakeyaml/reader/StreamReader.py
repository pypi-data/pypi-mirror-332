"""
Python module generated from Java source file org.yaml.snakeyaml.reader.StreamReader

Java source file obtained from artifact snakeyaml version 1.30

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import IOException
from java.io import Reader
from java.io import StringReader
from java.util import Arrays
from org.yaml.snakeyaml.error import Mark
from org.yaml.snakeyaml.error import YAMLException
from org.yaml.snakeyaml.reader import *
from org.yaml.snakeyaml.scanner import Constant
from typing import Any, Callable, Iterable, Tuple


class StreamReader:
    """
    Reader: checks if code points are in allowed range. Returns '\0' when end of
    data has been reached.
    """

    def __init__(self, stream: str):
        ...


    def __init__(self, reader: "Reader"):
        ...


    @staticmethod
    def isPrintable(data: str) -> bool:
        ...


    @staticmethod
    def isPrintable(c: int) -> bool:
        ...


    def getMark(self) -> "Mark":
        ...


    def forward(self) -> None:
        ...


    def forward(self, length: int) -> None:
        """
        read the next length characters and move the pointer.
        if the last character is high surrogate one more character will be read

        Arguments
        - length: amount of characters to move forward
        """
        ...


    def peek(self) -> int:
        ...


    def peek(self, index: int) -> int:
        """
        Peek the next index-th code point

        Arguments
        - index: to peek

        Returns
        - the next index-th code point
        """
        ...


    def prefix(self, length: int) -> str:
        """
        peek the next length code points

        Arguments
        - length: amount of the characters to peek

        Returns
        - the next length code points
        """
        ...


    def prefixForward(self, length: int) -> str:
        """
        prefix(length) immediately followed by forward(length)

        Arguments
        - length: amount of characters to get

        Returns
        - the next length code points
        """
        ...


    def getColumn(self) -> int:
        ...


    def getIndex(self) -> int:
        """
        Returns
        - current position as number (in characters) from the beginning of the stream
        """
        ...


    def getLine(self) -> int:
        ...
