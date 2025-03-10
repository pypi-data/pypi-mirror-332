"""
Python module generated from Java source file org.yaml.snakeyaml.nodes.NodeTuple

Java source file obtained from artifact snakeyaml version 1.33

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.yaml.snakeyaml.nodes import *
from typing import Any, Callable, Iterable, Tuple


class NodeTuple:
    """
    Stores one key value pair used in a map.
    """

    def __init__(self, keyNode: "Node", valueNode: "Node"):
        ...


    def getKeyNode(self) -> "Node":
        """
        Key node.

        Returns
        - the node used as key
        """
        ...


    def getValueNode(self) -> "Node":
        """
        Value node.

        Returns
        - node used as value
        """
        ...


    def toString(self) -> str:
        ...
