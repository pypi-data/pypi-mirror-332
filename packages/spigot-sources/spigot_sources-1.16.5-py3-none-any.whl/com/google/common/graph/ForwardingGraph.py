"""
Python module generated from Java source file com.google.common.graph.ForwardingGraph

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.graph import *
from typing import Any, Callable, Iterable, Tuple


class ForwardingGraph(AbstractGraph):
    """
    A class to allow Graph implementations to be backed by ValueGraphs. This is not
    currently planned to be released as a general-purpose forwarding class.

    Author(s)
    - James Sexton
    """

    def nodes(self) -> set["N"]:
        ...


    def edges(self) -> set["EndpointPair"["N"]]:
        ...


    def isDirected(self) -> bool:
        ...


    def allowsSelfLoops(self) -> bool:
        ...


    def nodeOrder(self) -> "ElementOrder"["N"]:
        ...


    def adjacentNodes(self, node: "Object") -> set["N"]:
        ...


    def predecessors(self, node: "Object") -> set["N"]:
        ...


    def successors(self, node: "Object") -> set["N"]:
        ...


    def degree(self, node: "Object") -> int:
        ...


    def inDegree(self, node: "Object") -> int:
        ...


    def outDegree(self, node: "Object") -> int:
        ...
