"""
Python module generated from Java source file org.yaml.snakeyaml.events.CollectionStartEvent

Java source file obtained from artifact snakeyaml version 1.27

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.yaml.snakeyaml import DumperOptions
from org.yaml.snakeyaml.error import Mark
from org.yaml.snakeyaml.events import *
from typing import Any, Callable, Iterable, Tuple


class CollectionStartEvent(NodeEvent):
    """
    Base class for the start events of the collection nodes.
    """

    def __init__(self, anchor: str, tag: str, implicit: bool, startMark: "Mark", endMark: "Mark", flowStyle: "DumperOptions.FlowStyle"):
        ...


    def __init__(self, anchor: str, tag: str, implicit: bool, startMark: "Mark", endMark: "Mark", flowStyle: "Boolean"):
        ...


    def getTag(self) -> str:
        """
        Tag of this collection.

        Returns
        - The tag of this collection, or `null` if no explicit
                tag is available.
        """
        ...


    def getImplicit(self) -> bool:
        """
        `True` if the tag can be omitted while this collection is
        emitted.

        Returns
        - True if the tag can be omitted while this collection is emitted.
        """
        ...


    def getFlowStyle(self) -> "DumperOptions.FlowStyle":
        """
        `True` if this collection is in flow style, `False`
        for block style.

        Returns
        - If this collection is in flow style.
        """
        ...


    def isFlow(self) -> bool:
        ...
