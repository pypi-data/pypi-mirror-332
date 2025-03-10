"""
Python module generated from Java source file com.google.common.graph.ForwardingNetwork

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.graph import *
from java.util import Optional
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class ForwardingNetwork(AbstractNetwork):
    """
    A class to allow Network implementations to be backed by a provided delegate. This is not
    currently planned to be released as a general-purpose forwarding class.

    Author(s)
    - Joshua O'Madadhain
    """

    def nodes(self) -> set["N"]:
        ...


    def edges(self) -> set["E"]:
        ...


    def isDirected(self) -> bool:
        ...


    def allowsParallelEdges(self) -> bool:
        ...


    def allowsSelfLoops(self) -> bool:
        ...


    def nodeOrder(self) -> "ElementOrder"["N"]:
        ...


    def edgeOrder(self) -> "ElementOrder"["E"]:
        ...


    def adjacentNodes(self, node: "N") -> set["N"]:
        ...


    def predecessors(self, node: "N") -> set["N"]:
        ...


    def successors(self, node: "N") -> set["N"]:
        ...


    def incidentEdges(self, node: "N") -> set["E"]:
        ...


    def inEdges(self, node: "N") -> set["E"]:
        ...


    def outEdges(self, node: "N") -> set["E"]:
        ...


    def incidentNodes(self, edge: "E") -> "EndpointPair"["N"]:
        ...


    def adjacentEdges(self, edge: "E") -> set["E"]:
        ...


    def degree(self, node: "N") -> int:
        ...


    def inDegree(self, node: "N") -> int:
        ...


    def outDegree(self, node: "N") -> int:
        ...


    def edgesConnecting(self, nodeU: "N", nodeV: "N") -> set["E"]:
        ...


    def edgesConnecting(self, endpoints: "EndpointPair"["N"]) -> set["E"]:
        ...


    def edgeConnecting(self, nodeU: "N", nodeV: "N") -> "Optional"["E"]:
        ...


    def edgeConnecting(self, endpoints: "EndpointPair"["N"]) -> "Optional"["E"]:
        ...


    def edgeConnectingOrNull(self, nodeU: "N", nodeV: "N") -> "E":
        ...


    def edgeConnectingOrNull(self, endpoints: "EndpointPair"["N"]) -> "E":
        ...


    def hasEdgeConnecting(self, nodeU: "N", nodeV: "N") -> bool:
        ...


    def hasEdgeConnecting(self, endpoints: "EndpointPair"["N"]) -> bool:
        ...
