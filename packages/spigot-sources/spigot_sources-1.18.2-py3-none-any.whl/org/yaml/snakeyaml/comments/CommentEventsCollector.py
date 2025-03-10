"""
Python module generated from Java source file org.yaml.snakeyaml.comments.CommentEventsCollector

Java source file obtained from artifact snakeyaml version 1.30

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import AbstractQueue
from java.util import Iterator
from java.util import Queue
from org.yaml.snakeyaml.comments import *
from org.yaml.snakeyaml.events import CommentEvent
from org.yaml.snakeyaml.events import Event
from org.yaml.snakeyaml.parser import Parser
from typing import Any, Callable, Iterable, Tuple


class CommentEventsCollector:
    """
    Used by the Composer and Emitter to collect comment events so that they can be used at a later point in the process.
    """

    def __init__(self, parser: "Parser", *expectedCommentTypes: Tuple["CommentType", ...]):
        """
        Constructor used to collect comment events emitted by a Parser.

        Arguments
        - parser: the event source.
        - expectedCommentTypes: the comment types expected. Any comment types not included are not collected.
        """
        ...


    def __init__(self, eventSource: "Queue"["Event"], *expectedCommentTypes: Tuple["CommentType", ...]):
        """
        Constructor used to collect events emitted by the Serializer.

        Arguments
        - eventSource: the event source.
        - expectedCommentTypes: the comment types expected. Any comment types not included are not collected.
        """
        ...


    def collectEvents(self) -> "CommentEventsCollector":
        """
        Collect all events of the expected type (set during construction) starting with the top event on the event source.
        Collection stops as soon as a non comment or comment of the unexpected type is encountered.

        Returns
        - this object.
        """
        ...


    def collectEvents(self, event: "Event") -> "Event":
        """
        Collect all events of the expected type (set during construction) starting with event provided as an argument and
        continuing with the top event on the event source. Collection stops as soon as a non comment or comment of the
        unexpected type is encountered.

        Arguments
        - event: the first event to attempt to collect.

        Returns
        - the event provided as an argument, if it is not collected; Otherwise, `null`
        """
        ...


    def collectEventsAndPoll(self, event: "Event") -> "Event":
        """
        Collect all events of the expected type (set during construction) starting with event provided as an argument and
        continuing with the top event on the event source. Collection stops as soon as a non comment or comment of the
        unexpected type is encountered.

        Arguments
        - event: the first event to attempt to collect.

        Returns
        - the event provided as an argument, if it is not collected; Otherwise, the first event that is not collected.
        """
        ...


    def consume(self) -> list["CommentLine"]:
        """
        Return the events collected and reset the colletor.

        Returns
        - the events collected.
        """
        ...


    def isEmpty(self) -> bool:
        """
        Test if the collector contains any collected events.

        Returns
        - `True` if it does; Otherwise, `False`
        """
        ...
