"""
Python module generated from Java source file org.yaml.snakeyaml.events.SequenceEndEvent

Java source file obtained from artifact snakeyaml version 1.27

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.yaml.snakeyaml.error import Mark
from org.yaml.snakeyaml.events import *
from typing import Any, Callable, Iterable, Tuple


class SequenceEndEvent(CollectionEndEvent):
    """
    Marks the end of a sequence.

    See
    - SequenceStartEvent
    """

    def __init__(self, startMark: "Mark", endMark: "Mark"):
        ...


    def getEventId(self) -> "Event.ID":
        ...
