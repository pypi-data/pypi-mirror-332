"""
Python module generated from Java source file org.yaml.snakeyaml.comments.CommentLine

Java source file obtained from artifact snakeyaml version 1.33

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
    A comment line. It may be a block comment, blank line, or inline comment.
    """

    def __init__(self, event: "CommentEvent"):
        """
        Create

        Arguments
        - event: - the source
        """
        ...


    def __init__(self, startMark: "Mark", endMark: "Mark", value: str, commentType: "CommentType"):
        """
        Create

        Arguments
        - startMark: - start
        - endMark: - end
        - value: - text
        - commentType: - kind
        """
        ...


    def getEndMark(self) -> "Mark":
        """
        getter

        Returns
        - end
        """
        ...


    def getStartMark(self) -> "Mark":
        """
        getter

        Returns
        - start
        """
        ...


    def getCommentType(self) -> "CommentType":
        """
        Getter

        Returns
        - kind
        """
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
