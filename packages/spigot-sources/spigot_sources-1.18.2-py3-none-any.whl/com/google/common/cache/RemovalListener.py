"""
Python module generated from Java source file com.google.common.cache.RemovalListener

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.cache import *
from typing import Any, Callable, Iterable, Tuple


class RemovalListener:
    """
    An object that can receive a notification when an entry is removed from a cache. The removal
    resulting in notification could have occurred to an entry being manually removed or replaced, or
    due to eviction resulting from timed expiration, exceeding a maximum size, or garbage collection.
    
    An instance may be called concurrently by multiple threads to process different entries.
    Implementations of this interface should avoid performing blocking calls or synchronizing on
    shared resources.
    
    Type `<K>`: the most general type of keys this listener can listen for; for example `Object`
        if any key is acceptable
    
    Type `<V>`: the most general type of values this listener can listen for; for example `Object` if any key is acceptable

    Author(s)
    - Charles Fry

    Since
    - 10.0
    """

    def onRemoval(self, notification: "RemovalNotification"["K", "V"]) -> None:
        ...
