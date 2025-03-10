"""
Python module generated from Java source file org.yaml.snakeyaml.nodes.ScalarNode

Java source file obtained from artifact snakeyaml version 1.33

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.yaml.snakeyaml import DumperOptions
from org.yaml.snakeyaml.error import Mark
from org.yaml.snakeyaml.nodes import *
from typing import Any, Callable, Iterable, Tuple


class ScalarNode(Node):
    """
    Represents a scalar node.
    
    Scalar nodes form the leaves in the node graph.
    """

    def __init__(self, tag: "Tag", value: str, startMark: "Mark", endMark: "Mark", style: "DumperOptions.ScalarStyle"):
        ...


    def __init__(self, tag: "Tag", resolved: bool, value: str, startMark: "Mark", endMark: "Mark", style: "DumperOptions.ScalarStyle"):
        ...


    def __init__(self, tag: "Tag", value: str, startMark: "Mark", endMark: "Mark", style: "Character"):
        ...


    def __init__(self, tag: "Tag", resolved: bool, value: str, startMark: "Mark", endMark: "Mark", style: "Character"):
        ...


    def getStyle(self) -> "Character":
        """
        Get scalar style of this node.

        Returns
        - style of this scalar node

        See
        - <a href="http://yaml.org/spec/1.1/.id903915">Chapter 9. Scalar Styles</a>

        Deprecated
        - use getScalarStyle instead
        """
        ...


    def getScalarStyle(self) -> "DumperOptions.ScalarStyle":
        """
        Get scalar style of this node.

        Returns
        - style of this scalar node

        See
        - <a href="http://yaml.org/spec/1.1/.id903915">Chapter 9. Scalar Styles</a>
        """
        ...


    def getNodeId(self) -> "NodeId":
        ...


    def getValue(self) -> str:
        """
        Value of this scalar.

        Returns
        - Scalar's value.
        """
        ...


    def toString(self) -> str:
        ...


    def isPlain(self) -> bool:
        ...
