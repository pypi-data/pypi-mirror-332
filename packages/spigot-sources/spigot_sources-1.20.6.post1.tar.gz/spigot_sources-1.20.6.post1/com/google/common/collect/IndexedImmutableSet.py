"""
Python module generated from Java source file com.google.common.collect.IndexedImmutableSet

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import GwtIncompatible
from com.google.common.collect import *
from java.util import Spliterator
from java.util.function import Consumer
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class IndexedImmutableSet(CachingAsList):

    def iterator(self) -> "UnmodifiableIterator"["E"]:
        ...


    def spliterator(self) -> "Spliterator"["E"]:
        ...


    def forEach(self, consumer: "Consumer"["E"]) -> None:
        ...
