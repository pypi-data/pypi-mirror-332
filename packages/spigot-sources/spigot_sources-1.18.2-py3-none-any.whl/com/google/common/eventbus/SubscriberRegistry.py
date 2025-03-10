"""
Python module generated from Java source file com.google.common.eventbus.SubscriberRegistry

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import VisibleForTesting
from com.google.common.base import MoreObjects
from com.google.common.base import Objects
from com.google.common.base import Throwables
from com.google.common.cache import CacheBuilder
from com.google.common.cache import CacheLoader
from com.google.common.cache import LoadingCache
from com.google.common.collect import HashMultimap
from com.google.common.collect import ImmutableList
from com.google.common.collect import ImmutableSet
from com.google.common.collect import Iterators
from com.google.common.collect import Lists
from com.google.common.collect import Maps
from com.google.common.collect import Multimap
from com.google.common.eventbus import *
from com.google.common.primitives import Primitives
from com.google.common.reflect import TypeToken
from com.google.common.util.concurrent import UncheckedExecutionException
from com.google.j2objc.annotations import Weak
from java.lang.reflect import Method
from java.util import Arrays
from java.util import Iterator
from java.util.concurrent import ConcurrentMap
from java.util.concurrent import CopyOnWriteArraySet
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class SubscriberRegistry:
    """
    Registry of subscribers to a single event bus.

    Author(s)
    - Colin Decker
    """


