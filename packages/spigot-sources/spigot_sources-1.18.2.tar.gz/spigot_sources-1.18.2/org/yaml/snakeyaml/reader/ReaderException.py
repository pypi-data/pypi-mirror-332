"""
Python module generated from Java source file org.yaml.snakeyaml.reader.ReaderException

Java source file obtained from artifact snakeyaml version 1.30

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.yaml.snakeyaml.error import YAMLException
from org.yaml.snakeyaml.reader import *
from typing import Any, Callable, Iterable, Tuple


class ReaderException(YAMLException):

    def __init__(self, name: str, position: int, codePoint: int, message: str):
        ...


    def getName(self) -> str:
        ...


    def getCodePoint(self) -> int:
        ...


    def getPosition(self) -> int:
        ...


    def toString(self) -> str:
        ...
