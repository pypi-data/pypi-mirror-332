"""
Python module generated from Java source file org.yaml.snakeyaml.nodes.AnchorNode

Java source file obtained from artifact snakeyaml version 1.33

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.yaml.snakeyaml.nodes import *
from typing import Any, Callable, Iterable, Tuple


class AnchorNode(Node):
    """
    This class is only used during representation (dumping)
    """

    def __init__(self, realNode: "Node"):
        """
        Anchor

        Arguments
        - realNode: - the node which contains the referenced data
        """
        ...


    def getNodeId(self) -> "NodeId":
        ...


    def getRealNode(self) -> "Node":
        """
        Getter

        Returns
        - node with data
        """
        ...
