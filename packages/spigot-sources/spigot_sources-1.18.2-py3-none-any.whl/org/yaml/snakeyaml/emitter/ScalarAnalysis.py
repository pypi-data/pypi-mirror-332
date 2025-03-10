"""
Python module generated from Java source file org.yaml.snakeyaml.emitter.ScalarAnalysis

Java source file obtained from artifact snakeyaml version 1.30

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.yaml.snakeyaml.emitter import *
from typing import Any, Callable, Iterable, Tuple


class ScalarAnalysis:
    """
    Accumulate information to choose the scalar style
    """

    def __init__(self, scalar: str, empty: bool, multiline: bool, allowFlowPlain: bool, allowBlockPlain: bool, allowSingleQuoted: bool, allowBlock: bool):
        ...


    def getScalar(self) -> str:
        ...


    def isEmpty(self) -> bool:
        ...


    def isMultiline(self) -> bool:
        ...


    def isAllowFlowPlain(self) -> bool:
        ...


    def isAllowBlockPlain(self) -> bool:
        ...


    def isAllowSingleQuoted(self) -> bool:
        ...


    def isAllowBlock(self) -> bool:
        ...
