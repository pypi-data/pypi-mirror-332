"""
Python module generated from Java source file org.yaml.snakeyaml.nodes.MappingNode

Java source file obtained from artifact snakeyaml version 1.30

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.yaml.snakeyaml import DumperOptions
from org.yaml.snakeyaml.error import Mark
from org.yaml.snakeyaml.nodes import *
from typing import Any, Callable, Iterable, Tuple


class MappingNode(CollectionNode):
    """
    Represents a map.
    
    A map is a collection of unsorted key-value pairs.
    """

    def __init__(self, tag: "Tag", resolved: bool, value: list["NodeTuple"], startMark: "Mark", endMark: "Mark", flowStyle: "DumperOptions.FlowStyle"):
        ...


    def __init__(self, tag: "Tag", value: list["NodeTuple"], flowStyle: "DumperOptions.FlowStyle"):
        ...


    def __init__(self, tag: "Tag", resolved: bool, value: list["NodeTuple"], startMark: "Mark", endMark: "Mark", flowStyle: "Boolean"):
        ...


    def __init__(self, tag: "Tag", value: list["NodeTuple"], flowStyle: "Boolean"):
        ...


    def getNodeId(self) -> "NodeId":
        ...


    def getValue(self) -> list["NodeTuple"]:
        """
        Returns the entries of this map.

        Returns
        - List of entries.
        """
        ...


    def setValue(self, mergedValue: list["NodeTuple"]) -> None:
        ...


    def setOnlyKeyType(self, keyType: type["Object"]) -> None:
        ...


    def setTypes(self, keyType: type["Object"], valueType: type["Object"]) -> None:
        ...


    def toString(self) -> str:
        ...


    def setMerged(self, merged: bool) -> None:
        """
        Arguments
        - merged: - True if map contains merge node
        """
        ...


    def isMerged(self) -> bool:
        """
        Returns
        - True if map contains merge node
        """
        ...
