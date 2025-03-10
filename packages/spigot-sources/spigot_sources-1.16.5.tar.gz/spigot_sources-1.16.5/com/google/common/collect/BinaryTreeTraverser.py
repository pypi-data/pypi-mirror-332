"""
Python module generated from Java source file com.google.common.collect.BinaryTreeTraverser

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtCompatible
from com.google.common.base import Optional
from com.google.common.collect import *
from java.util import ArrayDeque
from java.util import BitSet
from java.util import Deque
from java.util import Iterator
from java.util.function import Consumer
from typing import Any, Callable, Iterable, Tuple


class BinaryTreeTraverser(TreeTraverser):
    """
    A variant of TreeTraverser for binary trees, providing additional traversals specific to
    binary trees.

    Author(s)
    - Louis Wasserman

    Since
    - 15.0
    """

    def leftChild(self, root: "T") -> "Optional"["T"]:
        """
        Returns the left child of the specified node, or Optional.absent() if the specified
        node has no left child.
        """
        ...


    def rightChild(self, root: "T") -> "Optional"["T"]:
        """
        Returns the right child of the specified node, or Optional.absent() if the specified
        node has no right child.
        """
        ...


    def children(self, root: "T") -> Iterable["T"]:
        """
        Returns the children of this node, in left-to-right order.
        """
        ...


    def inOrderTraversal(self, root: "T") -> "FluentIterable"["T"]:
        ...
