"""
Python module generated from Java source file com.google.common.cache.RemovalNotification

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.cache import *
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class RemovalNotification(SimpleImmutableEntry):
    """
    A notification of the removal of a single entry. The key and/or value may be null if they were
    already garbage collected.
    
    Like other `Entry` instances associated with `CacheBuilder`, this class holds
    strong references to the key and value, regardless of the type of references the cache may be
    using.

    Author(s)
    - Charles Fry

    Since
    - 10.0
    """

    @staticmethod
    def create(key: "K", value: "V", cause: "RemovalCause") -> "RemovalNotification"["K", "V"]:
        """
        Creates a new `RemovalNotification` for the given `key`/`value` pair, with
        the given `cause` for the removal. The `key` and/or `value` may be `null` if they were already garbage collected.

        Since
        - 19.0
        """
        ...


    def getCause(self) -> "RemovalCause":
        """
        Returns the cause for which the entry was removed.
        """
        ...


    def wasEvicted(self) -> bool:
        """
        Returns `True` if there was an automatic removal due to eviction (the cause is neither
        RemovalCause.EXPLICIT nor RemovalCause.REPLACED).
        """
        ...
