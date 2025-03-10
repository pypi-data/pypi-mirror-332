"""
Python module generated from Java source file org.yaml.snakeyaml.nodes.AnchorNode

Java source file obtained from artifact snakeyaml version 1.28

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
        ...


    def getNodeId(self) -> "NodeId":
        ...


    def getRealNode(self) -> "Node":
        ...
