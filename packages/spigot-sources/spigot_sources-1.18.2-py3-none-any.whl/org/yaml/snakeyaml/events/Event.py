"""
Python module generated from Java source file org.yaml.snakeyaml.events.Event

Java source file obtained from artifact snakeyaml version 1.30

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.yaml.snakeyaml.error import Mark
from org.yaml.snakeyaml.events import *
from typing import Any, Callable, Iterable, Tuple


class Event:
    """
    Basic unit of output from a org.yaml.snakeyaml.parser.Parser or input
    of a org.yaml.snakeyaml.emitter.Emitter.
    """

    def __init__(self, startMark: "Mark", endMark: "Mark"):
        ...


    def toString(self) -> str:
        ...


    def getStartMark(self) -> "Mark":
        ...


    def getEndMark(self) -> "Mark":
        ...


    def is(self, id: "Event.ID") -> bool:
        """
        Check if the Event is of the provided kind

        Arguments
        - id: - the Event.ID enum

        Returns
        - True then this Event of the provided type
        """
        ...


    def getEventId(self) -> "Event.ID":
        """
        Get the type (kind) if this Event

        Returns
        - the ID of this Event
        """
        ...


    def equals(self, obj: "Object") -> bool:
        ...


    def hashCode(self) -> int:
        ...


    class ID(Enum):

        Alias = 0
        Comment = 1
        DocumentEnd = 2
        DocumentStart = 3
        MappingEnd = 4
        MappingStart = 5
        Scalar = 6
        SequenceEnd = 7
        SequenceStart = 8
        StreamEnd = 9
        StreamStart = 10
