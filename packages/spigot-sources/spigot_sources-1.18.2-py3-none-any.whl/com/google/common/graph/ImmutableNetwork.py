"""
Python module generated from Java source file com.google.common.graph.ImmutableNetwork

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.base import Function
from com.google.common.collect import ImmutableMap
from com.google.common.collect import Maps
from com.google.common.graph import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from com.google.errorprone.annotations import Immutable
from typing import Any, Callable, Iterable, Tuple


class ImmutableNetwork(StandardNetwork):
    """
    A Network whose elements and structural relationships will never change. Instances of
    this class may be obtained with .copyOf(Network).
    
    See the Guava User's Guide's <a
    href="https://github.com/google/guava/wiki/GraphsExplained#immutable-implementations">discussion
    of the `Immutable*` types</a> for more information on the properties and guarantees
    provided by this class.
    
    Type `<N>`: Node parameter type
    
    Type `<E>`: Edge parameter type

    Author(s)
    - Jens Nyman

    Since
    - 20.0
    """

    @staticmethod
    def copyOf(network: "Network"["N", "E"]) -> "ImmutableNetwork"["N", "E"]:
        """
        Returns an immutable copy of `network`.
        """
        ...


    @staticmethod
    def copyOf(network: "ImmutableNetwork"["N", "E"]) -> "ImmutableNetwork"["N", "E"]:
        """
        Simply returns its argument.

        Deprecated
        - no need to use this
        """
        ...


    def asGraph(self) -> "ImmutableGraph"["N"]:
        ...


    class Builder:
        """
        A builder for creating ImmutableNetwork instances, especially `static final`
        networks. Example:
        
        ````static final ImmutableNetwork<City, Train> TRAIN_NETWORK =
            NetworkBuilder.undirected()
                .allowsParallelEdges(True)
                .<City, Train>immutable()
                .addEdge(PARIS, BRUSSELS, Thalys.trainNumber("1111"))
                .addEdge(PARIS, BRUSSELS, RegionalTrain.trainNumber("2222"))
                .addEdge(LONDON, PARIS, Eurostar.trainNumber("3333"))
                .addEdge(LONDON, BRUSSELS, Eurostar.trainNumber("4444"))
                .addNode(REYKJAVIK)
                .build();````
        
        Builder instances can be reused; it is safe to call .build multiple times to build
        multiple networks in series. Each new network contains all the elements of the ones created
        before it.

        Since
        - 28.0
        """

        def addNode(self, node: "N") -> "ImmutableNetwork.Builder"["N", "E"]:
            """
            Adds `node` if it is not already present.
            
            **Nodes must be unique**, just as `Map` keys must be. They must also be non-null.

            Returns
            - this `Builder` object
            """
            ...


        def addEdge(self, nodeU: "N", nodeV: "N", edge: "E") -> "ImmutableNetwork.Builder"["N", "E"]:
            """
            Adds `edge` connecting `nodeU` to `nodeV`.
            
            If the network is directed, `edge` will be directed in this network; otherwise, it
            will be undirected.
            
            **`edge` must be unique to this network**, just as a `Map` key must be. It
            must also be non-null.
            
            If `nodeU` and `nodeV` are not already present in this network, this method
            will silently .addNode(Object) add `nodeU` and `nodeV` to the network.
            
            If `edge` already connects `nodeU` to `nodeV` (in the specified order if
            this network .isDirected(), else in any order), then this method will have no effect.

            Returns
            - this `Builder` object

            Raises
            - IllegalArgumentException: if `edge` already exists in the network and does not
                connect `nodeU` to `nodeV`
            - IllegalArgumentException: if the introduction of the edge would violate .allowsParallelEdges() or .allowsSelfLoops()
            """
            ...


        def addEdge(self, endpoints: "EndpointPair"["N"], edge: "E") -> "ImmutableNetwork.Builder"["N", "E"]:
            """
            Adds `edge` connecting `endpoints`. In an undirected network, `edge` will
            also connect `nodeV` to `nodeU`.
            
            If this network is directed, `edge` will be directed in this network; if it is
            undirected, `edge` will be undirected in this network.
            
            If this network is directed, `endpoints` must be ordered.
            
            **`edge` must be unique to this network**, just as a `Map` key must be. It
            must also be non-null.
            
            If either or both endpoints are not already present in this network, this method will
            silently .addNode(Object) add each missing endpoint to the network.
            
            If `edge` already connects an endpoint pair equal to `endpoints`, then this
            method will have no effect.

            Returns
            - this `Builder` object

            Raises
            - IllegalArgumentException: if `edge` already exists in the network and connects
                some other endpoint pair that is not equal to `endpoints`
            - IllegalArgumentException: if the introduction of the edge would violate .allowsParallelEdges() or .allowsSelfLoops()
            - IllegalArgumentException: if the endpoints are unordered and the network is directed
            """
            ...


        def build(self) -> "ImmutableNetwork"["N", "E"]:
            """
            Returns a newly-created `ImmutableNetwork` based on the contents of this `Builder`.
            """
            ...
