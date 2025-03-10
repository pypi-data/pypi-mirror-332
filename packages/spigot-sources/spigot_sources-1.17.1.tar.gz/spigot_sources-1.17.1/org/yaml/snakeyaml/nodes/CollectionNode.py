"""
Python module generated from Java source file org.yaml.snakeyaml.nodes.CollectionNode

Java source file obtained from artifact snakeyaml version 1.28

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.yaml.snakeyaml import DumperOptions
from org.yaml.snakeyaml.error import Mark
from org.yaml.snakeyaml.nodes import *
from typing import Any, Callable, Iterable, Tuple


class CollectionNode(Node):
    """
    Base class for the two collection types MappingNode mapping and
    SequenceNode collection.
    """

    def __init__(self, tag: "Tag", startMark: "Mark", endMark: "Mark", flowStyle: "DumperOptions.FlowStyle"):
        ...


    def __init__(self, tag: "Tag", startMark: "Mark", endMark: "Mark", flowStyle: "Boolean"):
        ...


    def getValue(self) -> list["T"]:
        """
        Returns the elements in this sequence.

        Returns
        - Nodes in the specified order.
        """
        ...


    def getFlowStyle(self) -> "DumperOptions.FlowStyle":
        """
        Serialization style of this collection.

        Returns
        - `True` for flow style, `False` for block
                style.
        """
        ...


    def setFlowStyle(self, flowStyle: "DumperOptions.FlowStyle") -> None:
        ...


    def setFlowStyle(self, flowStyle: "Boolean") -> None:
        ...


    def setEndMark(self, endMark: "Mark") -> None:
        ...
