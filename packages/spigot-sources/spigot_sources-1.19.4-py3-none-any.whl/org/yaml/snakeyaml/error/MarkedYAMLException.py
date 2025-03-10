"""
Python module generated from Java source file org.yaml.snakeyaml.error.MarkedYAMLException

Java source file obtained from artifact snakeyaml version 1.33

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.yaml.snakeyaml.error import *
from typing import Any, Callable, Iterable, Tuple


class MarkedYAMLException(YAMLException):

    def getMessage(self) -> str:
        ...


    def toString(self) -> str:
        ...


    def getContext(self) -> str:
        ...


    def getContextMark(self) -> "Mark":
        ...


    def getProblem(self) -> str:
        ...


    def getProblemMark(self) -> "Mark":
        ...
