"""
Python module generated from Java source file com.google.common.collect.Interners

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import J2ktIncompatible
from com.google.common.annotations import VisibleForTesting
from com.google.common.base import Equivalence
from com.google.common.base import Function
from com.google.common.collect import *
from com.google.common.collect.MapMaker import Dummy
from com.google.common.collect.MapMakerInternalMap import InternalEntry
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class Interners:
    """
    Contains static methods pertaining to instances of Interner.

    Author(s)
    - Kevin Bourrillion

    Since
    - 3.0
    """

    @staticmethod
    def newBuilder() -> "InternerBuilder":
        """
        Returns a fresh InternerBuilder instance.
        """
        ...


    @staticmethod
    def newStrongInterner() -> "Interner"["E"]:
        """
        Returns a new thread-safe interner which retains a strong reference to each instance it has
        interned, thus preventing these instances from being garbage-collected. If this retention is
        acceptable, this implementation may perform better than .newWeakInterner.
        """
        ...


    @staticmethod
    def newWeakInterner() -> "Interner"["E"]:
        """
        Returns a new thread-safe interner which retains a weak reference to each instance it has
        interned, and so does not prevent these instances from being garbage-collected. This most
        likely does not perform as well as .newStrongInterner, but is the best alternative when
        the memory usage of that implementation is unacceptable.
        """
        ...


    @staticmethod
    def asFunction(interner: "Interner"["E"]) -> "Function"["E", "E"]:
        """
        Returns a function that delegates to the Interner.intern method of the given interner.

        Since
        - 8.0
        """
        ...


    class InternerBuilder:
        """
        Builder for Interner instances.

        Since
        - 21.0
        """

        def strong(self) -> "InternerBuilder":
            """
            Instructs the InternerBuilder to build a strong interner.

            See
            - Interners.newStrongInterner()
            """
            ...


        def weak(self) -> "InternerBuilder":
            """
            Instructs the InternerBuilder to build a weak interner.

            See
            - Interners.newWeakInterner()
            """
            ...


        def concurrencyLevel(self, concurrencyLevel: int) -> "InternerBuilder":
            """
            Sets the concurrency level that will be used by the to-be-built Interner.

            See
            - MapMaker.concurrencyLevel(int)
            """
            ...


        def build(self) -> "Interner"["E"]:
            ...
