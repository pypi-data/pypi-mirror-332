"""
Python module generated from Java source file com.google.common.util.concurrent.SettableFuture

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtCompatible
from com.google.common.util.concurrent import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from javax.annotation import Nullable
from typing import Any, Callable, Iterable, Tuple


class SettableFuture(TrustedFuture):
    """
    A ListenableFuture whose result can be set by a .set(Object), .setException(Throwable) or .setFuture(ListenableFuture) call. It can also, like any
    other `Future`, be .cancel cancelled.
    
    `SettableFuture` is the recommended `ListenableFuture` implementation when your
    task cannot be implemented with ListeningExecutorService, the various Futures
    utility methods, or ListenableFutureTask. Those APIs have less opportunity for developer
    error. If your needs are more complex than `SettableFuture` supports, use
    AbstractFuture, which offers an extensible version of the API.

    Author(s)
    - Sven Mawson

    Since
    - 9.0 (in 1.0 as `ValueFuture`)
    """

    @staticmethod
    def create() -> "SettableFuture"["V"]:
        """
        Creates a new `SettableFuture` that can be completed or cancelled by a later method call.
        """
        ...


    def set(self, value: "V") -> bool:
        ...


    def setException(self, throwable: "Throwable") -> bool:
        ...


    def setFuture(self, future: "ListenableFuture"["V"]) -> bool:
        ...
