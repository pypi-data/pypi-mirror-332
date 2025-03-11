"""
Python module generated from Java source file com.google.common.graph.GraphsBridgeMethods

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.graph import *
from typing import Any, Callable, Iterable, Tuple


class GraphsBridgeMethods:
    """
    Supertype for Graphs, containing the old signatures of methods whose signatures we've
    changed. This provides binary compatibility for users who compiled against the old signatures.
    """

    @staticmethod
    def transitiveClosure(graph: "Graph"["N"]) -> "Graph"["N"]:
        ...


    @staticmethod
    def reachableNodes(graph: "Graph"["N"], node: "N") -> set["N"]:
        ...
