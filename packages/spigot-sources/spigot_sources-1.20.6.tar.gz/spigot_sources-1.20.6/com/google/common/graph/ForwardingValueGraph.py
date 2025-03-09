"""
Python module generated from Java source file com.google.common.graph.ForwardingValueGraph

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.graph import *
from java.util import Optional
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class ForwardingValueGraph(AbstractValueGraph):
    """
    A class to allow ValueGraph implementations to be backed by a provided delegate. This is
    not currently planned to be released as a general-purpose forwarding class.

    Author(s)
    - Joshua O'Madadhain
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


    def edgeValue(self, nodeU: "N", nodeV: "N") -> "Optional"["V"]:
        ...


    def edgeValue(self, endpoints: "EndpointPair"["N"]) -> "Optional"["V"]:
        ...


    def edgeValueOrDefault(self, nodeU: "N", nodeV: "N", defaultValue: "V") -> "V":
        ...


    def edgeValueOrDefault(self, endpoints: "EndpointPair"["N"], defaultValue: "V") -> "V":
        ...
