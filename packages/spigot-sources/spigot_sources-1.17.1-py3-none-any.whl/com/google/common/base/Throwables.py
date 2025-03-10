"""
Python module generated from Java source file com.google.common.base.Throwables

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import VisibleForTesting
from com.google.common.base import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.io import PrintWriter
from java.io import StringWriter
from java.lang.reflect import InvocationTargetException
from java.lang.reflect import Method
from java.util import AbstractList
from java.util import Collections
from javax.annotation import Nullable
from typing import Any, Callable, Iterable, Tuple


class Throwables:
    """
    Static utility methods pertaining to instances of Throwable.
    
    See the Guava User Guide entry on
    <a href="https://github.com/google/guava/wiki/ThrowablesExplained">Throwables</a>.

    Author(s)
    - Ben Yu

    Since
    - 1.0
    """

    @staticmethod
    def throwIfInstanceOf(throwable: "Throwable", declaredType: type["X"]) -> None:
        """
        Throws `throwable` if it is an instance of `declaredType`. Example usage:
        
        ```
        for (Foo foo : foos) {
          try {
            foo.bar();
          } catch (BarException | RuntimeException | Error t) {
            failure = t;
          }
        }
        if (failure != null) {
          throwIfInstanceOf(failure, BarException.class);
          throwIfUnchecked(failure);
          throw new AssertionError(failure);
        }
        ```

        Since
        - 20.0
        """
        ...


    @staticmethod
    def propagateIfInstanceOf(throwable: "Throwable", declaredType: type["X"]) -> None:
        """
        Propagates `throwable` exactly as-is, if and only if it is an instance of `declaredType`. Example usage:
        
        ```
        try {
          someMethodThatCouldThrowAnything();
        } catch (IKnowWhatToDoWithThisException e) {
          handle(e);
        } catch (Throwable t) {
          Throwables.propagateIfInstanceOf(t, IOException.class);
          Throwables.propagateIfInstanceOf(t, SQLException.class);
          throw Throwables.propagate(t);
        }
        ```

        Deprecated
        - Use .throwIfInstanceOf, which has the same behavior
            but rejects `null`. This method is scheduled to be removed in July 2018.
        """
        ...


    @staticmethod
    def throwIfUnchecked(throwable: "Throwable") -> None:
        """
        Throws `throwable` if it is a RuntimeException or Error. Example usage:
        
        ```
        for (Foo foo : foos) {
          try {
            foo.bar();
          } catch (RuntimeException | Error t) {
            failure = t;
          }
        }
        if (failure != null) {
          throwIfUnchecked(failure);
          throw new AssertionError(failure);
        }
        ```

        Since
        - 20.0
        """
        ...


    @staticmethod
    def propagateIfPossible(throwable: "Throwable") -> None:
        """
        Propagates `throwable` exactly as-is, if and only if it is an instance of
        RuntimeException or Error. Example usage:
        
        ```
        try {
          someMethodThatCouldThrowAnything();
        } catch (IKnowWhatToDoWithThisException e) {
          handle(e);
        } catch (Throwable t) {
          Throwables.propagateIfPossible(t);
          throw new RuntimeException("unexpected", t);
        }
        ```

        Deprecated
        - Use .throwIfUnchecked, which has the same behavior but rejects
            `null`. This method is scheduled to be removed in July 2018.
        """
        ...


    @staticmethod
    def propagateIfPossible(throwable: "Throwable", declaredType: type["X"]) -> None:
        """
        Propagates `throwable` exactly as-is, if and only if it is an instance of
        RuntimeException, Error, or `declaredType`. Example usage:
        
        ```
        try {
          someMethodThatCouldThrowAnything();
        } catch (IKnowWhatToDoWithThisException e) {
          handle(e);
        } catch (Throwable t) {
          Throwables.propagateIfPossible(t, OtherException.class);
          throw new RuntimeException("unexpected", t);
        }
        ```

        Arguments
        - throwable: the Throwable to possibly propagate
        - declaredType: the single checked exception type declared by the calling method
        """
        ...


    @staticmethod
    def propagateIfPossible(throwable: "Throwable", declaredType1: type["X1"], declaredType2: type["X2"]) -> None:
        """
        Propagates `throwable` exactly as-is, if and only if it is an instance of
        RuntimeException, Error, `declaredType1`, or `declaredType2`. In
        the unlikely case that you have three or more declared checked exception types, you can handle
        them all by invoking these methods repeatedly. See usage example in
        .propagateIfPossible(Throwable, Class).

        Arguments
        - throwable: the Throwable to possibly propagate
        - declaredType1: any checked exception type declared by the calling method
        - declaredType2: any other checked exception type declared by the calling method
        """
        ...


    @staticmethod
    def propagate(throwable: "Throwable") -> "RuntimeException":
        """
        Propagates `throwable` as-is if it is an instance of RuntimeException or
        Error, or else as a last resort, wraps it in a `RuntimeException` and then
        propagates.
        
        This method always throws an exception. The `RuntimeException` return type allows
        client code to signal to the compiler that statements after the call are unreachable. Example
        usage:
        
        ```
        T doSomething() {
          try {
            return someMethodThatCouldThrowAnything();
          } catch (IKnowWhatToDoWithThisException e) {
            return handle(e);
          } catch (Throwable t) {
            throw Throwables.propagate(t);
          }
        }
        ```

        Arguments
        - throwable: the Throwable to propagate

        Returns
        - nothing will ever be returned; this return type is only for your convenience, as
            illustrated in the example above

        Deprecated
        - Use `throw e` or `throw new RuntimeException(e)` directly, or use a
            combination of .throwIfUnchecked and `throw new RuntimeException(e)`. This
            method is scheduled to be removed in July 2018.
        """
        ...


    @staticmethod
    def getRootCause(throwable: "Throwable") -> "Throwable":
        """
        Returns the innermost cause of `throwable`. The first throwable in a chain provides
        context from when the error or exception was initially detected. Example usage:
        
        ```
        assertEquals("Unable to assign a customer id", Throwables.getRootCause(e).getMessage());
        ```
        """
        ...


    @staticmethod
    def getCausalChain(throwable: "Throwable") -> list["Throwable"]:
        """
        Gets a `Throwable` cause chain as a list. The first entry in the list will be `throwable` followed by its cause hierarchy. Note that this is a snapshot of the cause chain and
        will not reflect any subsequent changes to the cause chain.
        
        Here's an example of how it can be used to find specific types of exceptions in the cause
        chain:
        
        ```
        Iterables.filter(Throwables.getCausalChain(e), IOException.class));
        ```

        Arguments
        - throwable: the non-null `Throwable` to extract causes from

        Returns
        - an unmodifiable list containing the cause chain starting with `throwable`
        """
        ...


    @staticmethod
    def getStackTraceAsString(throwable: "Throwable") -> str:
        """
        Returns a string containing the result of Throwable.toString() toString(), followed by
        the full, recursive stack trace of `throwable`. Note that you probably should not be
        parsing the resulting string; if you need programmatic access to the stack frames, you can call
        Throwable.getStackTrace().
        """
        ...


    @staticmethod
    def lazyStackTrace(throwable: "Throwable") -> list["StackTraceElement"]:
        ...


    @staticmethod
    def lazyStackTraceIsLazy() -> bool:
        """
        Returns whether .lazyStackTrace will use the special implementation described in its
        documentation.

        Since
        - 19.0
        """
        ...
