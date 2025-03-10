"""
Python module generated from Java source file com.google.common.graph.ValueGraph

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.graph import *
from com.google.errorprone.annotations import CompatibleWith
from javax.annotation import Nullable
from typing import Any, Callable, Iterable, Tuple


class ValueGraph(Graph):
    """
    An interface for <a
    href="https://en.wikipedia.org/wiki/Graph_(discrete_mathematics)">graph</a>-structured data,
    whose edges have associated non-unique values.
    
    A graph is composed of a set of nodes and a set of edges connecting pairs of nodes.
    
    There are three main interfaces provided to represent graphs. In order of increasing
    complexity they are: Graph, ValueGraph, and Network. You should generally
    prefer the simplest interface that satisfies your use case. See the <a
    href="https://github.com/google/guava/wiki/GraphsExplained#choosing-the-right-graph-type">
    "Choosing the right graph type"</a> section of the Guava User Guide for more details.
    
    <h3>Capabilities</h3>
    
    `ValueGraph` supports the following use cases (<a
    href="https://github.com/google/guava/wiki/GraphsExplained#definitions">definitions of
    terms</a>):
    
    
      - directed graphs
      - undirected graphs
      - graphs that do/don't allow self-loops
      - graphs whose nodes/edges are insertion-ordered, sorted, or unordered
      - graphs whose edges have associated values
    
    
    `ValueGraph`, as a subtype of `Graph`, explicitly does not support parallel edges,
    and forbids implementations or extensions with parallel edges. If you need parallel edges, use
    Network. (You can use a positive `Integer` edge value as a loose representation of
    edge multiplicity, but the `*degree()` and mutation methods will not reflect your
    interpretation of the edge value as its multiplicity.)
    
    <h3>Building a `ValueGraph`</h3>
    
    The implementation classes that `common.graph` provides are not public, by design. To create
    an instance of one of the built-in implementations of `ValueGraph`, use the ValueGraphBuilder class:
    
    ````MutableValueGraph<Integer, Double> graph = ValueGraphBuilder.directed().build();````
    
    ValueGraphBuilder.build() returns an instance of MutableValueGraph, which is a
    subtype of `ValueGraph` that provides methods for adding and removing nodes and edges. If
    you do not need to mutate a graph (e.g. if you write a method than runs a read-only algorithm on
    the graph), you should use the non-mutating ValueGraph interface, or an ImmutableValueGraph.
    
    You can create an immutable copy of an existing `ValueGraph` using ImmutableValueGraph.copyOf(ValueGraph):
    
    ````ImmutableValueGraph<Integer, Double> immutableGraph = ImmutableValueGraph.copyOf(graph);````
    
    Instances of ImmutableValueGraph do not implement MutableValueGraph
    (obviously!) and are contractually guaranteed to be unmodifiable and thread-safe.
    
    The Guava User Guide has <a
    href="https://github.com/google/guava/wiki/GraphsExplained#building-graph-instances">more
    information on (and examples of) building graphs</a>.
    
    <h3>Additional documentation</h3>
    
    See the Guava User Guide for the `common.graph` package (<a
    href="https://github.com/google/guava/wiki/GraphsExplained">"Graphs Explained"</a>) for
    additional documentation, including:
    
    
      - <a
          href="https://github.com/google/guava/wiki/GraphsExplained#equals-hashcode-and-graph-equivalence">
          `equals()`, `hashCode()`, and graph equivalence</a>
      - <a href="https://github.com/google/guava/wiki/GraphsExplained#synchronization">
          Synchronization policy</a>
      - <a href="https://github.com/google/guava/wiki/GraphsExplained#notes-for-implementors">Notes
          for implementors</a>
    
    
    Type `<N>`: Node parameter type
    
    Type `<V>`: Value parameter type

    Author(s)
    - Joshua O'Madadhain

    Since
    - 20.0
    """

    def edgeValue(self, nodeU: "Object", nodeV: "Object") -> "V":
        """
        If there is an edge connecting `nodeU` to `nodeV`, returns the non-null value
        associated with that edge.
        
        In an undirected graph, this is equal to `edgeValue(nodeV, nodeU)`.

        Raises
        - IllegalArgumentException: if there is no edge connecting `nodeU` to `nodeV`.
        """
        ...


    def edgeValueOrDefault(self, nodeU: "Object", nodeV: "Object", defaultValue: "V") -> "V":
        """
        If there is an edge connecting `nodeU` to `nodeV`, returns the non-null value
        associated with that edge; otherwise, returns `defaultValue`.
        
        In an undirected graph, this is equal to `edgeValueOrDefault(nodeV, nodeU,
        defaultValue)`.
        """
        ...


    def equals(self, object: "Object") -> bool:
        """
        For the default ValueGraph implementations, returns True if `this == object`
        (reference equality). External implementations are free to define this method as they see fit,
        as long as they satisfy the Object.equals(Object) contract.
        
        To compare two ValueGraphs based on their contents rather than their references, see
        Graphs.equivalent(ValueGraph, ValueGraph).
        """
        ...


    def hashCode(self) -> int:
        """
        For the default ValueGraph implementations, returns `System.identityHashCode(this)`. External implementations are free to define this method as they
        see fit, as long as they satisfy the Object.hashCode() contract.
        """
        ...
