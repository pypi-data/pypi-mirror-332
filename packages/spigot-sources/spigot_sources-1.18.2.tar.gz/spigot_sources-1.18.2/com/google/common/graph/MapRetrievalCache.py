"""
Python module generated from Java source file com.google.common.graph.MapRetrievalCache

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.graph import *
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class MapRetrievalCache(MapIteratorCache):
    """
    A MapIteratorCache that adds additional caching. In addition to the caching provided by
    MapIteratorCache, this structure caches values for the two most recently retrieved keys.

    Author(s)
    - James Sexton
    """


