"""
Python module generated from Java source file org.yaml.snakeyaml.scanner.SimpleKey

Java source file obtained from artifact snakeyaml version 1.33

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.yaml.snakeyaml.error import Mark
from org.yaml.snakeyaml.scanner import *
from typing import Any, Callable, Iterable, Tuple


class SimpleKey:
    """
    Simple keys treatment.
    
    Helper class for ScannerImpl.

    See
    - ScannerImpl
    """

    def __init__(self, tokenNumber: int, required: bool, index: int, line: int, column: int, mark: "Mark"):
        ...


    def getTokenNumber(self) -> int:
        ...


    def getColumn(self) -> int:
        ...


    def getMark(self) -> "Mark":
        ...


    def getIndex(self) -> int:
        ...


    def getLine(self) -> int:
        ...


    def isRequired(self) -> bool:
        ...


    def toString(self) -> str:
        ...
