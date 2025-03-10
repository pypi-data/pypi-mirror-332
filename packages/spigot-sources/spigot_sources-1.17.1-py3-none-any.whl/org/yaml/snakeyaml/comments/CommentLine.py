"""
Python module generated from Java source file org.yaml.snakeyaml.comments.CommentLine

Java source file obtained from artifact snakeyaml version 1.28

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.yaml.snakeyaml.comments import *
from org.yaml.snakeyaml.error import Mark
from org.yaml.snakeyaml.events import CommentEvent
from typing import Any, Callable, Iterable, Tuple


class CommentLine:
    """
    A comment line. May be a block comment, blank line, or inline comment.
    """

    def __init__(self, event: "CommentEvent"):
        ...


    def __init__(self, startMark: "Mark", endMark: "Mark", value: str, commentType: "CommentType"):
        ...


    def getEndMark(self) -> "Mark":
        ...


    def getStartMark(self) -> "Mark":
        ...


    def getCommentType(self) -> "CommentType":
        ...


    def getValue(self) -> str:
        """
        Value of this comment.

        Returns
        - comment's value.
        """
        ...


    def toString(self) -> str:
        ...
