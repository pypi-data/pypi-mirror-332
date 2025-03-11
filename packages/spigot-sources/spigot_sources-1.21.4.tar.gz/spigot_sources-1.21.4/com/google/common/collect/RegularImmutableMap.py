"""
Python module generated from Java source file com.google.common.collect.RegularImmutableMap

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
from com.google.common.collect.ImmutableMapEntry import NonTerminalImmutableMapEntry
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.io import Serializable
from java.util import IdentityHashMap
from java.util.function import BiConsumer
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class RegularImmutableMap(ImmutableMap):
    """
    Implementation of ImmutableMap used for 0 entries and for 2+ entries. Additional
    implementations exist for particular cases, like ImmutableTable views and hash flooding.
    (This doc discusses ImmutableMap subclasses only for the JRE flavor; the Android flavor
    differs.)

    Author(s)
    - Gregory Kick
    """

    def get(self, key: "Object") -> "V":
        ...


    def forEach(self, action: "BiConsumer"["K", "V"]) -> None:
        ...


    def size(self) -> int:
        ...
