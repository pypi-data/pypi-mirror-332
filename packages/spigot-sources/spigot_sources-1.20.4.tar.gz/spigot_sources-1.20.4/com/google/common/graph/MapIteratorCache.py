"""
Python module generated from Java source file com.google.common.graph.MapIteratorCache

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.collect import UnmodifiableIterator
from com.google.common.graph import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.util import AbstractSet
from java.util import Iterator
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class MapIteratorCache:
    """
    A map-like data structure that wraps a backing map and caches values while iterating through
    .unmodifiableKeySet(). By design, the cache is cleared when this structure is mutated. If
    this structure is never mutated, it provides a thread-safe view of the backing map.
    
    The MapIteratorCache assumes ownership of the backing map, and cannot guarantee
    correctness in the face of external mutations to the backing map. As such, it is **strongly**
    recommended that the caller does not persist a reference to the backing map (unless the backing
    map is immutable).
    
    This class is tailored toward use cases in common.graph. It is *NOT* a general purpose map.

    Author(s)
    - James Sexton
    """


