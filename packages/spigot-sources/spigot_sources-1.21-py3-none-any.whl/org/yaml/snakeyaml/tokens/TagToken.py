"""
Python module generated from Java source file org.yaml.snakeyaml.tokens.TagToken

Java source file obtained from artifact snakeyaml version 2.2

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.yaml.snakeyaml.error import Mark
from org.yaml.snakeyaml.tokens import *
from typing import Any, Callable, Iterable, Tuple


class TagToken(Token):

    def __init__(self, value: "TagTuple", startMark: "Mark", endMark: "Mark"):
        ...


    def getValue(self) -> "TagTuple":
        ...


    def getTokenId(self) -> "Token.ID":
        ...
