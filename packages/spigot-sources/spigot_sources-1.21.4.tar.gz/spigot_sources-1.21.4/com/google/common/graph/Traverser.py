"""
Python module generated from Java source file com.google.common.graph.Traverser

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.collect import AbstractIterator
from com.google.common.collect import ImmutableSet
from com.google.common.graph import *
from com.google.errorprone.annotations import DoNotMock
from java.util import ArrayDeque
from java.util import Deque
from java.util import Iterator
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class Traverser:
    """
    An object that can traverse the nodes that are reachable from a specified (set of) start node(s)
    using a specified SuccessorsFunction.
    
    There are two entry points for creating a `Traverser`: .forTree(SuccessorsFunction) and .forGraph(SuccessorsFunction). You should choose one
    based on your answers to the following questions:
    
    <ol>
      - Is there only one path to any node that's reachable from any start node? (If so, the graph
          to be traversed is a tree or forest even if it is a subgraph of a graph which is neither.)
      - Are the node objects' implementations of `equals()`/`hashCode()` <a
          href="https://github.com/google/guava/wiki/GraphsExplained#non-recursiveness">recursive</a>?
    </ol>
    
    If your answers are:
    
    
      - (1) "no" and (2) "no", use .forGraph(SuccessorsFunction).
      - (1) "yes" and (2) "yes", use .forTree(SuccessorsFunction).
      - (1) "yes" and (2) "no", you can use either, but `forTree()` will be more efficient.
      - (1) "no" and (2) "yes", ***neither will work***, but if you transform your node
          objects into a non-recursive form, you can use `forGraph()`.
    
    
    Type `<N>`: Node parameter type

    Author(s)
    - Jens Nyman

    Since
    - 23.1
    """

    @staticmethod
    def forGraph(graph: "SuccessorsFunction"["N"]) -> "Traverser"["N"]:
        """
        Creates a new traverser for the given general `graph`.
        
        Traversers created using this method are guaranteed to visit each node reachable from the
        start node(s) at most once.
        
        If you know that no node in `graph` is reachable by more than one path from the start
        node(s), consider using .forTree(SuccessorsFunction) instead.
        
        **Performance notes**
        
        
          - Traversals require *O(n)* time (where *n* is the number of nodes reachable from
              the start node), assuming that the node objects have *O(1)* `equals()` and
              `hashCode()` implementations. (See the <a
              href="https://github.com/google/guava/wiki/GraphsExplained#elements-must-be-useable-as-map-keys">
              notes on element objects</a> for more information.)
          - While traversing, the traverser will use *O(n)* space (where *n* is the number
              of nodes that have thus far been visited), plus *O(H)* space (where *H* is the
              number of nodes that have been seen but not yet visited, that is, the "horizon").

        Arguments
        - graph: SuccessorsFunction representing a general graph that may have cycles.
        """
        ...


    @staticmethod
    def forTree(tree: "SuccessorsFunction"["N"]) -> "Traverser"["N"]:
        """
        Creates a new traverser for a directed acyclic graph that has at most one path from the start
        node(s) to any node reachable from the start node(s), and has no paths from any start node to
        any other start node, such as a tree or forest.
        
        `forTree()` is especially useful (versus `forGraph()`) in cases where the data
        structure being traversed is, in addition to being a tree/forest, also defined <a
        href="https://github.com/google/guava/wiki/GraphsExplained#non-recursiveness">recursively</a>.
        This is because the `forTree()`-based implementations don't keep track of visited nodes,
        and therefore don't need to call `equals()` or `hashCode()` on the node objects; this saves
        both time and space versus traversing the same graph using `forGraph()`.
        
        Providing a graph to be traversed for which there is more than one path from the start
        node(s) to any node may lead to:
        
        
          - Traversal not terminating (if the graph has cycles)
          - Nodes being visited multiple times (if multiple paths exist from any start node to any
              node reachable from any start node)
        
        
        **Performance notes**
        
        
          - Traversals require *O(n)* time (where *n* is the number of nodes reachable from
              the start node).
          - While traversing, the traverser will use *O(H)* space (where *H* is the number
              of nodes that have been seen but not yet visited, that is, the "horizon").
        
        
        **Examples** (all edges are directed facing downwards)
        
        The graph below would be valid input with start nodes of `a, f, c`. However, if `b` were *also* a start node, then there would be multiple paths to reach `e` and
        `h`.
        
        ````a     b      c
          / \   / \     |
         /   \ /   \    |
        d     e     f   g
              |
              |
              h````
        
        .
        
        The graph below would be a valid input with start nodes of `a, f`. However, if `b` were a start node, there would be multiple paths to `f`.
        
        ````a     b
          / \   / \
         /   \ /   \
        c     d     e
               \   /
                \ /
                 f````
        
        **Note on binary trees**
        
        This method can be used to traverse over a binary tree. Given methods `leftChild(node)` and `rightChild(node)`, this method can be called as
        
        ````Traverser.forTree(node -> ImmutableList.of(leftChild(node), rightChild(node)));````

        Arguments
        - tree: SuccessorsFunction representing a directed acyclic graph that has at most
            one path between any two nodes
        """
        ...


    def breadthFirst(self, startNode: "N") -> Iterable["N"]:
        """
        Returns an unmodifiable `Iterable` over the nodes reachable from `startNode`, in
        the order of a breadth-first traversal. That is, all the nodes of depth 0 are returned, then
        depth 1, then 2, and so on.
        
        **Example:** The following graph with `startNode` `a` would return nodes in
        the order `abcdef` (assuming successors are returned in alphabetical order).
        
        ````b ---- a ---- d
        |      |
        |      |
        e ---- c ---- f````
        
        The behavior of this method is undefined if the nodes, or the topology of the graph, change
        while iteration is in progress.
        
        The returned `Iterable` can be iterated over multiple times. Every iterator will
        compute its next element on the fly. It is thus possible to limit the traversal to a certain
        number of nodes as follows:
        
        ````Iterables.limit(Traverser.forGraph(graph).breadthFirst(node), maxNumberOfNodes);````
        
        See <a href="https://en.wikipedia.org/wiki/Breadth-first_search">Wikipedia</a> for more
        info.

        Raises
        - IllegalArgumentException: if `startNode` is not an element of the graph
        """
        ...


    def breadthFirst(self, startNodes: Iterable["N"]) -> Iterable["N"]:
        """
        Returns an unmodifiable `Iterable` over the nodes reachable from any of the `startNodes`, in the order of a breadth-first traversal. This is equivalent to a breadth-first
        traversal of a graph with an additional root node whose successors are the listed `startNodes`.

        Raises
        - IllegalArgumentException: if any of `startNodes` is not an element of the graph

        See
        - .breadthFirst(Object)

        Since
        - 24.1
        """
        ...


    def depthFirstPreOrder(self, startNode: "N") -> Iterable["N"]:
        """
        Returns an unmodifiable `Iterable` over the nodes reachable from `startNode`, in
        the order of a depth-first pre-order traversal. "Pre-order" implies that nodes appear in the
        `Iterable` in the order in which they are first visited.
        
        **Example:** The following graph with `startNode` `a` would return nodes in
        the order `abecfd` (assuming successors are returned in alphabetical order).
        
        ````b ---- a ---- d
        |      |
        |      |
        e ---- c ---- f````
        
        The behavior of this method is undefined if the nodes, or the topology of the graph, change
        while iteration is in progress.
        
        The returned `Iterable` can be iterated over multiple times. Every iterator will
        compute its next element on the fly. It is thus possible to limit the traversal to a certain
        number of nodes as follows:
        
        ````Iterables.limit(
            Traverser.forGraph(graph).depthFirstPreOrder(node), maxNumberOfNodes);````
        
        See <a href="https://en.wikipedia.org/wiki/Depth-first_search">Wikipedia</a> for more info.

        Raises
        - IllegalArgumentException: if `startNode` is not an element of the graph
        """
        ...


    def depthFirstPreOrder(self, startNodes: Iterable["N"]) -> Iterable["N"]:
        """
        Returns an unmodifiable `Iterable` over the nodes reachable from any of the `startNodes`, in the order of a depth-first pre-order traversal. This is equivalent to a
        depth-first pre-order traversal of a graph with an additional root node whose successors are
        the listed `startNodes`.

        Raises
        - IllegalArgumentException: if any of `startNodes` is not an element of the graph

        See
        - .depthFirstPreOrder(Object)

        Since
        - 24.1
        """
        ...


    def depthFirstPostOrder(self, startNode: "N") -> Iterable["N"]:
        """
        Returns an unmodifiable `Iterable` over the nodes reachable from `startNode`, in
        the order of a depth-first post-order traversal. "Post-order" implies that nodes appear in the
        `Iterable` in the order in which they are visited for the last time.
        
        **Example:** The following graph with `startNode` `a` would return nodes in
        the order `fcebda` (assuming successors are returned in alphabetical order).
        
        ````b ---- a ---- d
        |      |
        |      |
        e ---- c ---- f````
        
        The behavior of this method is undefined if the nodes, or the topology of the graph, change
        while iteration is in progress.
        
        The returned `Iterable` can be iterated over multiple times. Every iterator will
        compute its next element on the fly. It is thus possible to limit the traversal to a certain
        number of nodes as follows:
        
        ````Iterables.limit(
            Traverser.forGraph(graph).depthFirstPostOrder(node), maxNumberOfNodes);````
        
        See <a href="https://en.wikipedia.org/wiki/Depth-first_search">Wikipedia</a> for more info.

        Raises
        - IllegalArgumentException: if `startNode` is not an element of the graph
        """
        ...


    def depthFirstPostOrder(self, startNodes: Iterable["N"]) -> Iterable["N"]:
        """
        Returns an unmodifiable `Iterable` over the nodes reachable from any of the `startNodes`, in the order of a depth-first post-order traversal. This is equivalent to a
        depth-first post-order traversal of a graph with an additional root node whose successors are
        the listed `startNodes`.

        Raises
        - IllegalArgumentException: if any of `startNodes` is not an element of the graph

        See
        - .depthFirstPostOrder(Object)

        Since
        - 24.1
        """
        ...
