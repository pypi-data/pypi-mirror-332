"""
Python module generated from Java source file com.google.common.graph.EndpointPairIterator

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.collect import AbstractIterator
from com.google.common.collect import ImmutableSet
from com.google.common.collect import Sets
from com.google.common.graph import *
from java.util import Iterator
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class EndpointPairIterator(AbstractIterator):
    """
    A class to facilitate the set returned by Graph.edges().

    Author(s)
    - James Sexton
    """


