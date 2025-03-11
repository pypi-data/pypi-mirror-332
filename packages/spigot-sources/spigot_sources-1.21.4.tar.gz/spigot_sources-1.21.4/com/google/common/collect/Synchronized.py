"""
Python module generated from Java source file com.google.common.collect.Synchronized

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import J2ktIncompatible
from com.google.common.annotations import VisibleForTesting
from com.google.common.collect import *
from com.google.j2objc.annotations import RetainedWith
from java.io import IOException
from java.io import ObjectOutputStream
from java.io import Serializable
from java.util import Comparator
from java.util import Deque
from java.util import Iterator
from java.util import ListIterator
from java.util import NavigableMap
from java.util import NavigableSet
from java.util import Queue
from java.util import RandomAccess
from java.util import SortedMap
from java.util import SortedSet
from java.util import Spliterator
from java.util.function import BiConsumer
from java.util.function import BiFunction
from java.util.function import Consumer
from java.util.function import Function
from java.util.function import Predicate
from java.util.function import UnaryOperator
from java.util.stream import Stream
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import NonNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class Synchronized:
    """
    Synchronized collection views. The returned synchronized collection views are serializable if the
    backing collection and the mutex are serializable.
    
    If `null` is passed as the `mutex` parameter to any of this class's top-level
    methods or inner class constructors, the created object uses itself as the synchronization mutex.
    
    This class should be used by other collection classes only.

    Author(s)
    - Jared Levy
    """


