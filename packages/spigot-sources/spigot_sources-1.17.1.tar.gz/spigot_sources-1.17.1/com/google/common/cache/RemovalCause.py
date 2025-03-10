"""
Python module generated from Java source file com.google.common.cache.RemovalCause

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.cache import *
from enum import Enum
from java.util import Iterator
from java.util.concurrent import ConcurrentMap
from typing import Any, Callable, Iterable, Tuple


class RemovalCause(Enum):
    """
    The reason why a cached entry was removed.

    Author(s)
    - Charles Fry

    Since
    - 10.0
    """

    EXPLICIT = 0
    """
    The entry was manually removed by the user. This can result from the user invoking
    Cache.invalidate, Cache.invalidateAll(Iterable), Cache.invalidateAll(),
    Map.remove, ConcurrentMap.remove, or Iterator.remove.
    """
    REPLACED = 1
    """
    The entry itself was not actually removed, but its value was replaced by the user. This can
    result from the user invoking Cache.put, LoadingCache.refresh, Map.put,
    Map.putAll, ConcurrentMap.replace(Object, Object), or
    ConcurrentMap.replace(Object, Object, Object).
    """
    COLLECTED = 2
    """
    The entry was removed automatically because its key or value was garbage-collected. This can
    occur when using CacheBuilder.weakKeys, CacheBuilder.weakValues, or
    CacheBuilder.softValues.
    """
    EXPIRED = 3
    """
    The entry's expiration timestamp has passed. This can occur when using
    CacheBuilder.expireAfterWrite or CacheBuilder.expireAfterAccess.
    """
    SIZE = 4
    """
    The entry was evicted due to size constraints. This can occur when using
    CacheBuilder.maximumSize or CacheBuilder.maximumWeight.
    """
