"""
Python module generated from Java source file org.yaml.snakeyaml.tokens.ScalarToken

Java source file obtained from artifact snakeyaml version 2.2

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.yaml.snakeyaml import DumperOptions
from org.yaml.snakeyaml.error import Mark
from org.yaml.snakeyaml.tokens import *
from typing import Any, Callable, Iterable, Tuple


class ScalarToken(Token):

    def __init__(self, value: str, startMark: "Mark", endMark: "Mark", plain: bool):
        ...


    def __init__(self, value: str, plain: bool, startMark: "Mark", endMark: "Mark", style: "DumperOptions.ScalarStyle"):
        ...


    def getPlain(self) -> bool:
        ...


    def getValue(self) -> str:
        ...


    def getStyle(self) -> "DumperOptions.ScalarStyle":
        ...


    def getTokenId(self) -> "Token.ID":
        ...
