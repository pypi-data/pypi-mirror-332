"""
Python module generated from Java source file com.google.common.cache.CacheBuilderSpec

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import VisibleForTesting
from com.google.common.base import MoreObjects
from com.google.common.base import Objects
from com.google.common.base import Splitter
from com.google.common.cache import *
from com.google.common.cache.LocalCache import Strength
from com.google.common.collect import ImmutableList
from com.google.common.collect import ImmutableMap
from java.util import Locale
from java.util.concurrent import TimeUnit
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class CacheBuilderSpec:
    """
    A specification of a CacheBuilder configuration.
    
    `CacheBuilderSpec` supports parsing configuration off of a string, which makes it
    especially useful for command-line configuration of a `CacheBuilder`.
    
    The string syntax is a series of comma-separated keys or key-value pairs, each corresponding
    to a `CacheBuilder` method.
    
    
      - `concurrencyLevel=[integer]`: sets CacheBuilder.concurrencyLevel.
      - `initialCapacity=[integer]`: sets CacheBuilder.initialCapacity.
      - `maximumSize=[long]`: sets CacheBuilder.maximumSize.
      - `maximumWeight=[long]`: sets CacheBuilder.maximumWeight.
      - `expireAfterAccess=[duration]`: sets CacheBuilder.expireAfterAccess.
      - `expireAfterWrite=[duration]`: sets CacheBuilder.expireAfterWrite.
      - `refreshAfterWrite=[duration]`: sets CacheBuilder.refreshAfterWrite.
      - `weakKeys`: sets CacheBuilder.weakKeys.
      - `softValues`: sets CacheBuilder.softValues.
      - `weakValues`: sets CacheBuilder.weakValues.
      - `recordStats`: sets CacheBuilder.recordStats.
    
    
    The set of supported keys will grow as `CacheBuilder` evolves, but existing keys will
    never be removed.
    
    Durations are represented by an integer, followed by one of "d", "h", "m", or "s",
    representing days, hours, minutes, or seconds respectively. (There is currently no syntax to
    request expiration in milliseconds, microseconds, or nanoseconds.)
    
    Whitespace before and after commas and equal signs is ignored. Keys may not be repeated; it is
    also illegal to use the following pairs of keys in a single value:
    
    
      - `maximumSize` and `maximumWeight`
      - `softValues` and `weakValues`
    
    
    `CacheBuilderSpec` does not support configuring `CacheBuilder` methods with
    non-value parameters. These must be configured in code.
    
    A new `CacheBuilder` can be instantiated from a `CacheBuilderSpec` using CacheBuilder.from(CacheBuilderSpec) or CacheBuilder.from(String).

    Author(s)
    - Adam Winer

    Since
    - 12.0
    """

    @staticmethod
    def parse(cacheBuilderSpecification: str) -> "CacheBuilderSpec":
        """
        Creates a CacheBuilderSpec from a string.

        Arguments
        - cacheBuilderSpecification: the string form
        """
        ...


    @staticmethod
    def disableCaching() -> "CacheBuilderSpec":
        """
        Returns a CacheBuilderSpec that will prevent caching.
        """
        ...


    def toParsableString(self) -> str:
        """
        Returns a string that can be used to parse an equivalent `CacheBuilderSpec`. The order
        and form of this representation is not guaranteed, except that reparsing its output will
        produce a `CacheBuilderSpec` equal to this instance.
        """
        ...


    def toString(self) -> str:
        """
        Returns a string representation for this CacheBuilderSpec instance. The form of this
        representation is not guaranteed.
        """
        ...


    def hashCode(self) -> int:
        ...


    def equals(self, obj: "Object") -> bool:
        ...
