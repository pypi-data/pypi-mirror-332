"""
Python module generated from Java source file com.google.common.graph.SuccessorsFunction

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.graph import *
from com.google.errorprone.annotations import DoNotMock
from typing import Any, Callable, Iterable, Tuple


class SuccessorsFunction:
    """
    A functional interface for <a
    href="https://en.wikipedia.org/wiki/Graph_(discrete_mathematics)">graph</a>-structured data.
    
    This interface is meant to be used as the type of a parameter to graph algorithms (such as
    breadth first traversal) that only need a way of accessing the successors of a node in a graph.
    
    <h3>Usage</h3>
    
    Given an algorithm, for example:
    
    ````public <N> someGraphAlgorithm(N startNode, SuccessorsFunction<N> successorsFunction);````
    
    you will invoke it depending on the graph representation you're using.
    
    If you have an instance of one of the primary `common.graph` types (Graph,
    ValueGraph, and Network):
    
    ````someGraphAlgorithm(startNode, graph);````
    
    This works because those types each implement `SuccessorsFunction`. It will also work with
    any other implementation of this interface.
    
    If you have your own graph implementation based around a custom node type `MyNode`,
    which has a method `getChildren()` that retrieves its successors in a graph:
    
    ````someGraphAlgorithm(startNode, MyNode::getChildren);````
    
    If you have some other mechanism for returning the successors of a node, or one that doesn't
    return an `Iterable<? extends N>`, then you can use a lambda to perform a more general
    transformation:
    
    ````someGraphAlgorithm(startNode, node -> ImmutableList.of(node.leftChild(), node.rightChild()));````
    
    Graph algorithms that need additional capabilities (accessing both predecessors and
    successors, iterating over the edges, etc.) should declare their input to be of a type that
    provides those capabilities, such as Graph, ValueGraph, or Network.
    
    <h3>Additional documentation</h3>
    
    See the Guava User Guide for the `common.graph` package (<a
    href="https://github.com/google/guava/wiki/GraphsExplained">"Graphs Explained"</a>) for
    additional documentation, including <a
    href="https://github.com/google/guava/wiki/GraphsExplained#notes-for-implementors">notes for
    implementors</a>
    
    Type `<N>`: Node parameter type

    Author(s)
    - Jens Nyman

    Since
    - 23.0
    """

    def successors(self, node: "N") -> Iterable["N"]:
        """
        Returns all nodes in this graph adjacent to `node` which can be reached by traversing
        `node`'s outgoing edges in the direction (if any) of the edge.
        
        This is *not* the same as "all nodes reachable from `node` by following outgoing
        edges". For that functionality, see Graphs.reachableNodes(Graph, Object).
        
        Some algorithms that operate on a `SuccessorsFunction` may produce undesired results
        if the returned Iterable contains duplicate elements. Implementations of such
        algorithms should document their behavior in the presence of duplicates.
        
        The elements of the returned `Iterable` must each be:
        
        
          - Non-null
          - Usable as `Map` keys (see the Guava User Guide's section on <a
              href="https://github.com/google/guava/wiki/GraphsExplained#graph-elements-nodes-and-edges">
              graph elements</a> for details)

        Raises
        - IllegalArgumentException: if `node` is not an element of this graph
        """
        ...
