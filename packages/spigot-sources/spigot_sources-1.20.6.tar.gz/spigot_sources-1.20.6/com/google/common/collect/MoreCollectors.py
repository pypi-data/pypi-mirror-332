"""
Python module generated from Java source file com.google.common.collect.MoreCollectors

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.collect import *
from java.util import NoSuchElementException
from java.util import Optional
from java.util.stream import Collector
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class MoreCollectors:
    """
    Collectors not present in `java.util.stream.Collectors` that are not otherwise associated
    with a `com.google.common` type.

    Author(s)
    - Louis Wasserman

    Since
    - 21.0
    """

    @staticmethod
    def toOptional() -> "Collector"["T", Any, "Optional"["T"]]:
        """
        A collector that converts a stream of zero or one elements to an `Optional`.

        Returns
        - `Optional.of(onlyElement)` if the stream has exactly one element (must not be
            `null`) and returns `Optional.empty()` if it has none.

        Raises
        - IllegalArgumentException: if the stream consists of two or more elements.
        - NullPointerException: if any element in the stream is `null`.
        """
        ...


    @staticmethod
    def onlyElement() -> "Collector"["T", Any, "T"]:
        """
        A collector that takes a stream containing exactly one element and returns that element. The
        returned collector throws an `IllegalArgumentException` if the stream consists of two or
        more elements, and a `NoSuchElementException` if the stream is empty.
        """
        ...
