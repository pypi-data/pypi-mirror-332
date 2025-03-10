"""
Python module generated from Java source file org.yaml.snakeyaml.tokens.AnchorToken

Java source file obtained from artifact snakeyaml version 1.33

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.yaml.snakeyaml.error import Mark
from org.yaml.snakeyaml.tokens import *
from typing import Any, Callable, Iterable, Tuple


class AnchorToken(Token):
    """
    Anchor
    """

    def __init__(self, value: str, startMark: "Mark", endMark: "Mark"):
        """
        Anchor

        Arguments
        - value: - anchor
        - startMark: - start
        - endMark: - end
        """
        ...


    def getValue(self) -> str:
        """
        getter

        Returns
        - anchor
        """
        ...


    def getTokenId(self) -> "Token.ID":
        """
        getter

        Returns
        - the identity
        """
        ...
