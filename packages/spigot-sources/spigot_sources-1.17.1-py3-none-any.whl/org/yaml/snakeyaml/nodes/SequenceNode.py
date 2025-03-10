"""
Python module generated from Java source file org.yaml.snakeyaml.nodes.SequenceNode

Java source file obtained from artifact snakeyaml version 1.28

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.yaml.snakeyaml import DumperOptions
from org.yaml.snakeyaml.error import Mark
from org.yaml.snakeyaml.nodes import *
from typing import Any, Callable, Iterable, Tuple


class SequenceNode(CollectionNode):
    """
    Represents a sequence.
    
    A sequence is a ordered collection of nodes.
    """

    def __init__(self, tag: "Tag", resolved: bool, value: list["Node"], startMark: "Mark", endMark: "Mark", flowStyle: "DumperOptions.FlowStyle"):
        ...


    def __init__(self, tag: "Tag", value: list["Node"], flowStyle: "DumperOptions.FlowStyle"):
        ...


    def __init__(self, tag: "Tag", value: list["Node"], style: "Boolean"):
        ...


    def __init__(self, tag: "Tag", resolved: bool, value: list["Node"], startMark: "Mark", endMark: "Mark", style: "Boolean"):
        ...


    def getNodeId(self) -> "NodeId":
        ...


    def getValue(self) -> list["Node"]:
        """
        Returns the elements in this sequence.

        Returns
        - Nodes in the specified order.
        """
        ...


    def setListType(self, listType: type["Object"]) -> None:
        ...


    def toString(self) -> str:
        ...
