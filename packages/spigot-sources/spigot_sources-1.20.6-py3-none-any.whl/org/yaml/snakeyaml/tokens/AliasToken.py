"""
Python module generated from Java source file org.yaml.snakeyaml.tokens.AliasToken

Java source file obtained from artifact snakeyaml version 2.2

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.yaml.snakeyaml.error import Mark
from org.yaml.snakeyaml.tokens import *
from typing import Any, Callable, Iterable, Tuple


class AliasToken(Token):
    """
    Alias
    """

    def __init__(self, value: str, startMark: "Mark", endMark: "Mark"):
        """
        Alias

        Arguments
        - value: - alias
        - startMark: - start
        - endMark: - end
        """
        ...


    def getValue(self) -> str:
        """
        getter

        Returns
        - alias
        """
        ...


    def getTokenId(self) -> "Token.ID":
        ...
