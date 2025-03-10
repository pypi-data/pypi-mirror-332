"""
Python module generated from Java source file org.yaml.snakeyaml.events.AliasEvent

Java source file obtained from artifact snakeyaml version 1.27

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.yaml.snakeyaml.error import Mark
from org.yaml.snakeyaml.events import *
from typing import Any, Callable, Iterable, Tuple


class AliasEvent(NodeEvent):
    """
    Marks the inclusion of a previously anchored node.
    """

    def __init__(self, anchor: str, startMark: "Mark", endMark: "Mark"):
        ...


    def getEventId(self) -> "Event.ID":
        ...
