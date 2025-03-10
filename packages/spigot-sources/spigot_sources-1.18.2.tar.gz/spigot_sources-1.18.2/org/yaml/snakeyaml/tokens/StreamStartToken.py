"""
Python module generated from Java source file org.yaml.snakeyaml.tokens.StreamStartToken

Java source file obtained from artifact snakeyaml version 1.30

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.yaml.snakeyaml.error import Mark
from org.yaml.snakeyaml.tokens import *
from typing import Any, Callable, Iterable, Tuple


class StreamStartToken(Token):

    def __init__(self, startMark: "Mark", endMark: "Mark"):
        ...


    def getTokenId(self) -> "Token.ID":
        ...
