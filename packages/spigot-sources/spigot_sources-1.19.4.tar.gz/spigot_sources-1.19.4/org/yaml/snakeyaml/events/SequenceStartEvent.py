"""
Python module generated from Java source file org.yaml.snakeyaml.events.SequenceStartEvent

Java source file obtained from artifact snakeyaml version 1.33

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.yaml.snakeyaml import DumperOptions
from org.yaml.snakeyaml.error import Mark
from org.yaml.snakeyaml.events import *
from typing import Any, Callable, Iterable, Tuple


class SequenceStartEvent(CollectionStartEvent):
    """
    Marks the beginning of a sequence node.
    
    This event is followed by the elements contained in the sequence, and a SequenceEndEvent.

    See
    - SequenceEndEvent
    """

    def __init__(self, anchor: str, tag: str, implicit: bool, startMark: "Mark", endMark: "Mark", flowStyle: "DumperOptions.FlowStyle"):
        ...


    def __init__(self, anchor: str, tag: str, implicit: bool, startMark: "Mark", endMark: "Mark", flowStyle: "Boolean"):
        ...


    def getEventId(self) -> "Event.ID":
        ...
