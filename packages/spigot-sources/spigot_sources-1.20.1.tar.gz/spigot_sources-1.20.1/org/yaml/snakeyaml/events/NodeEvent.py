"""
Python module generated from Java source file org.yaml.snakeyaml.events.NodeEvent

Java source file obtained from artifact snakeyaml version 2.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.yaml.snakeyaml.error import Mark
from org.yaml.snakeyaml.events import *
from typing import Any, Callable, Iterable, Tuple


class NodeEvent(Event):
    """
    Base class for all events that mark the beginning of a node.
    """

    def __init__(self, anchor: str, startMark: "Mark", endMark: "Mark"):
        ...


    def getAnchor(self) -> str:
        """
        Node anchor by which this node might later be referenced by a AliasEvent.
        
        Note that AliasEvents are by it self `NodeEvent`s and use this property to
        indicate the referenced anchor.

        Returns
        - Anchor of this node or `null` if no anchor is defined.
        """
        ...
