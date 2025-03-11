"""
Python module generated from Java source file com.google.common.graph.ForwardingGraph

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.graph import *
from typing import Any, Callable, Iterable, Tuple


class ForwardingGraph(AbstractGraph):
    """
    A class to allow Graph implementations to be backed by a BaseGraph. This is not
    currently planned to be released as a general-purpose forwarding class.

    Author(s)
    - James Sexton
    """

    def nodes(self) -> set["N"]:
        ...


    def isDirected(self) -> bool:
        ...


    def allowsSelfLoops(self) -> bool:
        ...


    def nodeOrder(self) -> "ElementOrder"["N"]:
        ...


    def incidentEdgeOrder(self) -> "ElementOrder"["N"]:
        ...


    def adjacentNodes(self, node: "N") -> set["N"]:
        ...


    def predecessors(self, node: "N") -> set["N"]:
        ...


    def successors(self, node: "N") -> set["N"]:
        ...


    def incidentEdges(self, node: "N") -> set["EndpointPair"["N"]]:
        ...


    def degree(self, node: "N") -> int:
        ...


    def inDegree(self, node: "N") -> int:
        ...


    def outDegree(self, node: "N") -> int:
        ...


    def hasEdgeConnecting(self, nodeU: "N", nodeV: "N") -> bool:
        ...


    def hasEdgeConnecting(self, endpoints: "EndpointPair"["N"]) -> bool:
        ...
