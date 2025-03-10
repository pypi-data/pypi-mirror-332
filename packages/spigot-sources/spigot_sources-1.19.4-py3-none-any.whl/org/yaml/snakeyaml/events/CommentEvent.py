"""
Python module generated from Java source file org.yaml.snakeyaml.events.CommentEvent

Java source file obtained from artifact snakeyaml version 1.33

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.yaml.snakeyaml.comments import CommentType
from org.yaml.snakeyaml.error import Mark
from org.yaml.snakeyaml.events import *
from typing import Any, Callable, Iterable, Tuple


class CommentEvent(Event):
    """
    Marks a comment block value.
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


    def getValue(self) -> str:
        """
        String representation of the value.
        
        Without quotes and escaping.

        Returns
        - Value a comment line string without the leading '#' or a blank line.
        """
        ...


    def getCommentType(self) -> "CommentType":
        """
        The comment type.

        Returns
        - the commentType.
        """
        ...


    def getEventId(self) -> "Event.ID":
        ...
