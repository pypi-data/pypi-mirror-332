"""
Python module generated from Java source file com.google.common.collect.CollectCollectors

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import GwtIncompatible
from com.google.common.base import Preconditions
from com.google.common.collect import *
from java.util import Comparator
from java.util import EnumMap
from java.util import EnumSet
from java.util.function import BinaryOperator
from java.util.function import Function
from java.util.function import Supplier
from java.util.function import ToIntFunction
from java.util.stream import Collector
from java.util.stream import Collectors
from java.util.stream import Stream
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class CollectCollectors:
    """
    Collectors utilities for `common.collect` internals.
    """

    @staticmethod
    def toImmutableMap(keyFunction: "Function"["T", "K"], valueFunction: "Function"["T", "V"], mergeFunction: "BinaryOperator"["V"]) -> "Collector"["T", Any, "ImmutableMap"["K", "V"]]:
        ...
