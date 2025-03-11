"""
Python module generated from Java source file com.google.common.base.Throwables

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import J2ktIncompatible
from com.google.common.annotations import VisibleForTesting
from com.google.common.base import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.io import IOException
from java.io import PrintWriter
from java.io import StringWriter
from java.lang.reflect import InvocationTargetException
from java.lang.reflect import Method
from java.util import AbstractList
from java.util import Collections
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class Throwables:
    """
    Static utility methods pertaining to instances of Throwable.
    
    See the Guava User Guide entry on <a
    href="https://github.com/google/guava/wiki/ThrowablesExplained">Throwables</a>.

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
        - Use .throwIfInstanceOf, which has the same behavior but rejects `null`.
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
        Propagates `throwable` exactly as-is, if and only if it is an instance of RuntimeException or Error.

        Deprecated
        - Use .throwIfUnchecked, which has the same behavior but rejects `null`.
        """
        ...


    @staticmethod
    def propagateIfPossible(throwable: "Throwable", declaredType: type["X"]) -> None:
        """
        Propagates `throwable` exactly as-is, if and only if it is an instance of RuntimeException, Error, or `declaredType`.
        
        **Discouraged** in favor of calling .throwIfInstanceOf and .throwIfUnchecked.

        Arguments
        - throwable: the Throwable to possibly propagate
        - declaredType: the single checked exception type declared by the calling method

        Deprecated
        - Use a combination of .throwIfInstanceOf and .throwIfUnchecked,
            which togther provide the same behavior except that they reject `null`.
        """
        ...


    @staticmethod
    def propagateIfPossible(throwable: "Throwable", declaredType1: type["X1"], declaredType2: type["X2"]) -> None:
        """
        Propagates `throwable` exactly as-is, if and only if it is an instance of RuntimeException, Error, `declaredType1`, or `declaredType2`.

        Arguments
        - throwable: the Throwable to possibly propagate
        - declaredType1: any checked exception type declared by the calling method
        - declaredType2: any other checked exception type declared by the calling method

        Deprecated
        - Use a combination of two calls to .throwIfInstanceOf and one call to .throwIfUnchecked, which togther provide the same behavior except that they reject `null`.
        """
        ...


    @staticmethod
    def propagate(throwable: "Throwable") -> "RuntimeException":
        """
        Propagates `throwable` as-is if it is an instance of RuntimeException or Error, or else as a last resort, wraps it in a `RuntimeException` and then propagates.
        
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
        - To preserve behavior, use `throw e` or `throw new RuntimeException(e)`
            directly, or use a combination of .throwIfUnchecked and `throw new
            RuntimeException(e)`. But consider whether users would be better off if your API threw a
            different type of exception. For background on the deprecation, read <a
            href="https://github.com/google/guava/wiki/Why-we-deprecated-Throwables.propagate">Why we
            deprecated `Throwables.propagate`</a>.
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

        Raises
        - IllegalArgumentException: if there is a loop in the causal chain
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

        Raises
        - IllegalArgumentException: if there is a loop in the causal chain
        """
        ...


    @staticmethod
    def getCauseAs(throwable: "Throwable", expectedCauseType: type["X"]) -> "X":
        """
        Returns `throwable`'s cause, cast to `expectedCauseType`.
        
        Prefer this method instead of manually casting an exception's cause. For example, `(IOException) e.getCause()` throws a ClassCastException that discards the original
        exception `e` if the cause is not an IOException, but `Throwables.getCauseAs(e, IOException.class)` keeps `e` as the ClassCastException's cause.

        Raises
        - ClassCastException: if the cause cannot be cast to the expected type. The `ClassCastException`'s cause is `throwable`.

        Since
        - 22.0
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
        """
        Returns the stack trace of `throwable`, possibly providing slower iteration over the full
        trace but faster iteration over parts of the trace. Here, "slower" and "faster" are defined in
        comparison to the normal way to access the stack trace, Throwable.getStackTrace()
        throwable.getStackTrace(). Note, however, that this method's special implementation is not
        available for all platforms and configurations. If that implementation is unavailable, this
        method falls back to `getStackTrace`. Callers that require the special implementation can
        check its availability with .lazyStackTraceIsLazy().
        
        The expected (but not guaranteed) performance of the special implementation differs from
        `getStackTrace` in one main way: The `lazyStackTrace` call itself returns quickly
        by delaying the per-stack-frame work until each element is accessed. Roughly speaking:
        
        
          - `getStackTrace` takes `stackSize` time to return but then negligible time to
              retrieve each element of the returned list.
          - `lazyStackTrace` takes negligible time to return but then `1/stackSize` time
              to retrieve each element of the returned list (probably slightly more than `1/stackSize`).
        
        
        Note: The special implementation does not respect calls to Throwable.setStackTrace
        throwable.setStackTrace. Instead, it always reflects the original stack trace from the
        exception's creation.

        Since
        - 19.0

        Deprecated
        - This method is equivalent to Throwable.getStackTrace() on JDK versions past
            JDK 8 and on all Android versions. Use Throwable.getStackTrace() directly, or where
            possible use the `java.lang.StackWalker.walk` method introduced in JDK 9.
        """
        ...


    @staticmethod
    def lazyStackTraceIsLazy() -> bool:
        """
        Returns whether .lazyStackTrace will use the special implementation described in its
        documentation.

        Since
        - 19.0

        Deprecated
        - This method always returns False on JDK versions past JDK 8 and on all Android
            versions.
        """
        ...
