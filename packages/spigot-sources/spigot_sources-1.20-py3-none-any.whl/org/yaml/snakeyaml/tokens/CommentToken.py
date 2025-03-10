"""
Python module generated from Java source file org.yaml.snakeyaml.tokens.CommentToken

Java source file obtained from artifact snakeyaml version 2.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import Objects
from org.yaml.snakeyaml.comments import CommentType
from org.yaml.snakeyaml.error import Mark
from org.yaml.snakeyaml.tokens import *
from typing import Any, Callable, Iterable, Tuple


class CommentToken(Token):
    """
    Comment for humans
    """

    def __init__(self, type: "CommentType", value: str, startMark: "Mark", endMark: "Mark"):
        """
        Create

        Arguments
        - type: - kind
        - value: - text
        - startMark: - start
        - endMark: - end
        """
        ...


    def getCommentType(self) -> "CommentType":
        """
        getter

        Returns
        - the kind
        """
        ...


    def getValue(self) -> str:
        """
        getter

        Returns
        - text
        """
        ...


    def getTokenId(self) -> "Token.ID":
        ...
