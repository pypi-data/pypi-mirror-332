"""
Python module generated from Java source file com.google.common.graph.NetworkBuilder

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.base import Optional
from com.google.common.graph import *
from typing import Any, Callable, Iterable, Tuple


class NetworkBuilder(AbstractGraphBuilder):
    """
    A builder for constructing instances of MutableNetwork or ImmutableNetwork with
    user-defined properties.
    
    A network built by this class will have the following properties by default:
    
    
      - does not allow parallel edges
      - does not allow self-loops
      - orders Network.nodes() and Network.edges() in the order in which the
          elements were added
    
    
    Examples of use:
    
    ````// Building a mutable network
    MutableNetwork<String, Integer> network =
        NetworkBuilder.directed().allowsParallelEdges(True).build();
    flightNetwork.addEdge("LAX", "ATL", 3025);
    flightNetwork.addEdge("LAX", "ATL", 1598);
    flightNetwork.addEdge("ATL", "LAX", 2450);
    
    // Building a immutable network
    ImmutableNetwork<String, Integer> immutableNetwork =
        NetworkBuilder.directed()
            .allowsParallelEdges(True)
            .<String, Integer>immutable()
            .addEdge("LAX", "ATL", 3025)
            .addEdge("LAX", "ATL", 1598)
            .addEdge("ATL", "LAX", 2450)
            .build();````
    
    Type `<N>`: The most general node type this builder will support. This is normally `Object`
        unless it is constrained by using a method like .nodeOrder, or the builder is
        constructed based on an existing `Network` using .from(Network).
    
    Type `<E>`: The most general edge type this builder will support. This is normally `Object`
        unless it is constrained by using a method like .edgeOrder, or the builder is
        constructed based on an existing `Network` using .from(Network).

    Author(s)
    - Joshua O'Madadhain

    Since
    - 20.0
    """

    @staticmethod
    def directed() -> "NetworkBuilder"["Object", "Object"]:
        """
        Returns a NetworkBuilder for building directed networks.
        """
        ...


    @staticmethod
    def undirected() -> "NetworkBuilder"["Object", "Object"]:
        """
        Returns a NetworkBuilder for building undirected networks.
        """
        ...


    @staticmethod
    def from(network: "Network"["N", "E"]) -> "NetworkBuilder"["N", "E"]:
        """
        Returns a NetworkBuilder initialized with all properties queryable from `network`.
        
        The "queryable" properties are those that are exposed through the Network interface,
        such as Network.isDirected(). Other properties, such as .expectedNodeCount(int), are not set in the new builder.
        """
        ...


    def immutable(self) -> "ImmutableNetwork.Builder"["N1", "E1"]:
        """
        Returns an ImmutableNetwork.Builder with the properties of this NetworkBuilder.
        
        The returned builder can be used for populating an ImmutableNetwork.

        Since
        - 28.0
        """
        ...


    def allowsParallelEdges(self, allowsParallelEdges: bool) -> "NetworkBuilder"["N", "E"]:
        """
        Specifies whether the network will allow parallel edges. Attempting to add a parallel edge to a
        network that does not allow them will throw an UnsupportedOperationException.
        
        The default value is `False`.
        """
        ...


    def allowsSelfLoops(self, allowsSelfLoops: bool) -> "NetworkBuilder"["N", "E"]:
        """
        Specifies whether the network will allow self-loops (edges that connect a node to itself).
        Attempting to add a self-loop to a network that does not allow them will throw an UnsupportedOperationException.
        
        The default value is `False`.
        """
        ...


    def expectedNodeCount(self, expectedNodeCount: int) -> "NetworkBuilder"["N", "E"]:
        """
        Specifies the expected number of nodes in the network.

        Raises
        - IllegalArgumentException: if `expectedNodeCount` is negative
        """
        ...


    def expectedEdgeCount(self, expectedEdgeCount: int) -> "NetworkBuilder"["N", "E"]:
        """
        Specifies the expected number of edges in the network.

        Raises
        - IllegalArgumentException: if `expectedEdgeCount` is negative
        """
        ...


    def nodeOrder(self, nodeOrder: "ElementOrder"["N1"]) -> "NetworkBuilder"["N1", "E"]:
        """
        Specifies the order of iteration for the elements of Network.nodes().
        
        The default value is ElementOrder.insertion() insertion order.
        """
        ...


    def edgeOrder(self, edgeOrder: "ElementOrder"["E1"]) -> "NetworkBuilder"["N", "E1"]:
        """
        Specifies the order of iteration for the elements of Network.edges().
        
        The default value is ElementOrder.insertion() insertion order.
        """
        ...


    def build(self) -> "MutableNetwork"["N1", "E1"]:
        """
        Returns an empty MutableNetwork with the properties of this NetworkBuilder.
        """
        ...
