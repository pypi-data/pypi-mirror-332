"""
Python module generated from Java source file com.google.common.io.Closer

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import VisibleForTesting
from com.google.common.base import Throwables
from com.google.common.io import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.io import Closeable
from java.io import IOException
from java.lang.reflect import Method
from java.util import ArrayDeque
from java.util import Deque
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class Closer(Closeable):

    @staticmethod
    def create() -> "Closer":
        """
        Creates a new Closer.
        """
        ...


    def register(self, closeable: "C") -> "C":
        ...


    def rethrow(self, e: "Throwable") -> "RuntimeException":
        """
        Stores the given throwable and rethrows it. It will be rethrown as is if it is an `IOException`, `RuntimeException` or `Error`. Otherwise, it will be rethrown wrapped
        in a `RuntimeException`. **Note:** Be sure to declare all of the checked exception
        types your try block can throw when calling an overload of this method so as to avoid losing
        the original exception type.
        
        This method always throws, and as such should be called as `throw closer.rethrow(e);`
        to ensure the compiler knows that it will throw.

        Returns
        - this method does not return; it always throws

        Raises
        - IOException: when the given throwable is an IOException
        """
        ...


    def rethrow(self, e: "Throwable", declaredType: type["X"]) -> "RuntimeException":
        """
        Stores the given throwable and rethrows it. It will be rethrown as is if it is an `IOException`, `RuntimeException`, `Error` or a checked exception of the given type.
        Otherwise, it will be rethrown wrapped in a `RuntimeException`. **Note:** Be sure to
        declare all of the checked exception types your try block can throw when calling an overload of
        this method so as to avoid losing the original exception type.
        
        This method always throws, and as such should be called as `throw closer.rethrow(e,
        ...);` to ensure the compiler knows that it will throw.

        Returns
        - this method does not return; it always throws

        Raises
        - IOException: when the given throwable is an IOException
        - X: when the given throwable is of the declared type X
        """
        ...


    def rethrow(self, e: "Throwable", declaredType1: type["X1"], declaredType2: type["X2"]) -> "RuntimeException":
        """
        Stores the given throwable and rethrows it. It will be rethrown as is if it is an `IOException`, `RuntimeException`, `Error` or a checked exception of either of the
        given types. Otherwise, it will be rethrown wrapped in a `RuntimeException`. **Note:**
        Be sure to declare all of the checked exception types your try block can throw when calling an
        overload of this method so as to avoid losing the original exception type.
        
        This method always throws, and as such should be called as `throw closer.rethrow(e,
        ...);` to ensure the compiler knows that it will throw.

        Returns
        - this method does not return; it always throws

        Raises
        - IOException: when the given throwable is an IOException
        - X1: when the given throwable is of the declared type X1
        - X2: when the given throwable is of the declared type X2
        """
        ...


    def close(self) -> None:
        """
        Closes all `Closeable` instances that have been added to this `Closer`. If an
        exception was thrown in the try block and passed to one of the `exceptionThrown` methods,
        any exceptions thrown when attempting to close a closeable will be suppressed. Otherwise, the
        *first* exception to be thrown from an attempt to close a closeable will be thrown and any
        additional exceptions that are thrown after that will be suppressed.
        """
        ...
