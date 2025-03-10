"""
Python module generated from Java source file org.yaml.snakeyaml.error.Mark

Java source file obtained from artifact snakeyaml version 1.28

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import Serializable
from org.yaml.snakeyaml.error import *
from org.yaml.snakeyaml.scanner import Constant
from typing import Any, Callable, Iterable, Tuple


class Mark(Serializable):
    """
    It's just a record and its only use is producing nice error messages. Parser
    does not use it for any other purposes.
    """

    def __init__(self, name: str, index: int, line: int, column: int, str: list[str], pointer: int):
        ...


    def __init__(self, name: str, index: int, line: int, column: int, buffer: str, pointer: int):
        ...


    def __init__(self, name: str, index: int, line: int, column: int, buffer: list[int], pointer: int):
        ...


    def get_snippet(self, indent: int, max_length: int) -> str:
        ...


    def get_snippet(self) -> str:
        ...


    def toString(self) -> str:
        ...


    def getName(self) -> str:
        ...


    def getLine(self) -> int:
        """
        starts with 0

        Returns
        - line number
        """
        ...


    def getColumn(self) -> int:
        """
        starts with 0

        Returns
        - column number
        """
        ...


    def getIndex(self) -> int:
        """
        starts with 0

        Returns
        - character number
        """
        ...


    def getBuffer(self) -> list[int]:
        ...


    def getPointer(self) -> int:
        ...
