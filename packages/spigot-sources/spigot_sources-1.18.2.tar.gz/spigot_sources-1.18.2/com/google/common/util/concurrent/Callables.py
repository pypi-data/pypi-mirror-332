"""
Python module generated from Java source file com.google.common.util.concurrent.Callables

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import GwtIncompatible
from com.google.common.base import Supplier
from com.google.common.util.concurrent import *
from java.util.concurrent import Callable
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class Callables:
    """
    Static utility methods pertaining to the Callable interface.

    Author(s)
    - Isaac Shum

    Since
    - 1.0
    """

    @staticmethod
    def returning(value: "T") -> "Callable"["T"]:
        """
        Creates a `Callable` which immediately returns a preset value each time it is called.
        """
        ...


    @staticmethod
    def asAsyncCallable(callable: "Callable"["T"], listeningExecutorService: "ListeningExecutorService") -> "AsyncCallable"["T"]:
        """
        Creates an AsyncCallable from a Callable.
        
        The AsyncCallable returns the ListenableFuture resulting from ListeningExecutorService.submit(Callable).

        Since
        - 20.0
        """
        ...
