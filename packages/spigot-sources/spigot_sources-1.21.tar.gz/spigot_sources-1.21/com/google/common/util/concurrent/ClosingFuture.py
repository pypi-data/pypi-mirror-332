"""
Python module generated from Java source file com.google.common.util.concurrent.ClosingFuture

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import J2ktIncompatible
from com.google.common.annotations import VisibleForTesting
from com.google.common.collect import FluentIterable
from com.google.common.collect import ImmutableList
from com.google.common.util.concurrent import *
from com.google.common.util.concurrent.ClosingFuture.Combiner import AsyncCombiningCallable
from com.google.common.util.concurrent.ClosingFuture.Combiner import CombiningCallable
from com.google.common.util.concurrent.Futures import FutureCombiner
from com.google.errorprone.annotations import CanIgnoreReturnValue
from com.google.errorprone.annotations import DoNotMock
from com.google.j2objc.annotations import RetainedWith
from java.io import Closeable
from java.util import IdentityHashMap
from java.util.concurrent import Callable
from java.util.concurrent import CancellationException
from java.util.concurrent import CountDownLatch
from java.util.concurrent import ExecutionException
from java.util.concurrent import Executor
from java.util.concurrent import Future
from java.util.concurrent import RejectedExecutionException
from java.util.concurrent.atomic import AtomicReference
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class ClosingFuture:

    @staticmethod
    def submit(callable: "ClosingCallable"["V"], executor: "Executor") -> "ClosingFuture"["V"]:
        """
        Starts a ClosingFuture pipeline by submitting a callable block to an executor.

        Raises
        - java.util.concurrent.RejectedExecutionException: if the task cannot be scheduled for
            execution
        """
        ...


    @staticmethod
    def submitAsync(callable: "AsyncClosingCallable"["V"], executor: "Executor") -> "ClosingFuture"["V"]:
        """
        Starts a ClosingFuture pipeline by submitting a callable block to an executor.

        Raises
        - java.util.concurrent.RejectedExecutionException: if the task cannot be scheduled for
            execution

        Since
        - 30.1
        """
        ...


    @staticmethod
    def from(future: "ListenableFuture"["V"]) -> "ClosingFuture"["V"]:
        """
        Starts a ClosingFuture pipeline with a ListenableFuture.
        
        `future`'s value will not be closed when the pipeline is done even if `V`
        implements Closeable. In order to start a pipeline with a value that will be closed
        when the pipeline is done, use .submit(ClosingCallable, Executor) instead.
        """
        ...


    @staticmethod
    def eventuallyClosing(future: "ListenableFuture"["C"], closingExecutor: "Executor") -> "ClosingFuture"["C"]:
        """
        Starts a ClosingFuture pipeline with a ListenableFuture.
        
        If `future` succeeds, its value will be closed (using `closingExecutor)`) when
        the pipeline is done, even if the pipeline is canceled or fails.
        
        Cancelling the pipeline will not cancel `future`, so that the pipeline can access its
        value in order to close it.

        Arguments
        - future: the future to create the `ClosingFuture` from. For discussion of the
            future's result type `C`, see DeferredCloser.eventuallyClose(Object,
            Executor).
        - closingExecutor: the future's result will be closed on this executor

        Deprecated
        - Creating Futures of closeable types is dangerous in general because the
            underlying value may never be closed if the Future is canceled after its operation
            begins. Consider replacing code that creates ListenableFutures of closeable types,
            including those that pass them to this method, with .submit(ClosingCallable,
            Executor) in order to ensure that resources do not leak. Or, to start a pipeline with a
            ListenableFuture that doesn't create values that should be closed, use ClosingFuture.from.
        """
        ...


    @staticmethod
    def whenAllComplete(futures: Iterable["ClosingFuture"[Any]]) -> "Combiner":
        """
        Starts specifying how to combine ClosingFutures into a single pipeline.

        Raises
        - IllegalStateException: if a `ClosingFuture` has already been derived from any of
            the `futures`, or if any has already been .finishToFuture() finished
        """
        ...


    @staticmethod
    def whenAllComplete(future1: "ClosingFuture"[Any], *moreFutures: Tuple["ClosingFuture"[Any], ...]) -> "Combiner":
        """
        Starts specifying how to combine ClosingFutures into a single pipeline.

        Raises
        - IllegalStateException: if a `ClosingFuture` has already been derived from any of
            the arguments, or if any has already been .finishToFuture() finished
        """
        ...


    @staticmethod
    def whenAllSucceed(futures: Iterable["ClosingFuture"[Any]]) -> "Combiner":
        """
        Starts specifying how to combine ClosingFutures into a single pipeline, assuming they
        all succeed. If any fail, the resulting pipeline will fail.

        Raises
        - IllegalStateException: if a `ClosingFuture` has already been derived from any of
            the `futures`, or if any has already been .finishToFuture() finished
        """
        ...


    @staticmethod
    def whenAllSucceed(future1: "ClosingFuture"["V1"], future2: "ClosingFuture"["V2"]) -> "Combiner2"["V1", "V2"]:
        """
        Starts specifying how to combine two ClosingFutures into a single pipeline, assuming
        they all succeed. If any fail, the resulting pipeline will fail.
        
        Calling this method allows you to use lambdas or method references typed with the types of
        the input ClosingFutures.

        Raises
        - IllegalStateException: if a `ClosingFuture` has already been derived from any of
            the arguments, or if any has already been .finishToFuture() finished
        """
        ...


    @staticmethod
    def whenAllSucceed(future1: "ClosingFuture"["V1"], future2: "ClosingFuture"["V2"], future3: "ClosingFuture"["V3"]) -> "Combiner3"["V1", "V2", "V3"]:
        """
        Starts specifying how to combine three ClosingFutures into a single pipeline, assuming
        they all succeed. If any fail, the resulting pipeline will fail.
        
        Calling this method allows you to use lambdas or method references typed with the types of
        the input ClosingFutures.

        Raises
        - IllegalStateException: if a `ClosingFuture` has already been derived from any of
            the arguments, or if any has already been .finishToFuture() finished
        """
        ...


    @staticmethod
    def whenAllSucceed(future1: "ClosingFuture"["V1"], future2: "ClosingFuture"["V2"], future3: "ClosingFuture"["V3"], future4: "ClosingFuture"["V4"]) -> "Combiner4"["V1", "V2", "V3", "V4"]:
        """
        Starts specifying how to combine four ClosingFutures into a single pipeline, assuming
        they all succeed. If any fail, the resulting pipeline will fail.
        
        Calling this method allows you to use lambdas or method references typed with the types of
        the input ClosingFutures.

        Raises
        - IllegalStateException: if a `ClosingFuture` has already been derived from any of
            the arguments, or if any has already been .finishToFuture() finished
        """
        ...


    @staticmethod
    def whenAllSucceed(future1: "ClosingFuture"["V1"], future2: "ClosingFuture"["V2"], future3: "ClosingFuture"["V3"], future4: "ClosingFuture"["V4"], future5: "ClosingFuture"["V5"]) -> "Combiner5"["V1", "V2", "V3", "V4", "V5"]:
        """
        Starts specifying how to combine five ClosingFutures into a single pipeline, assuming
        they all succeed. If any fail, the resulting pipeline will fail.
        
        Calling this method allows you to use lambdas or method references typed with the types of
        the input ClosingFutures.

        Raises
        - IllegalStateException: if a `ClosingFuture` has already been derived from any of
            the arguments, or if any has already been .finishToFuture() finished
        """
        ...


    @staticmethod
    def whenAllSucceed(future1: "ClosingFuture"[Any], future2: "ClosingFuture"[Any], future3: "ClosingFuture"[Any], future4: "ClosingFuture"[Any], future5: "ClosingFuture"[Any], future6: "ClosingFuture"[Any], *moreFutures: Tuple["ClosingFuture"[Any], ...]) -> "Combiner":
        """
        Starts specifying how to combine ClosingFutures into a single pipeline, assuming they
        all succeed. If any fail, the resulting pipeline will fail.

        Raises
        - IllegalStateException: if a `ClosingFuture` has already been derived from any of
            the arguments, or if any has already been .finishToFuture() finished
        """
        ...


    def statusFuture(self) -> "ListenableFuture"[Any]:
        """
        Returns a future that finishes when this step does. Calling `get()` on the returned
        future returns `null` if the step is successful or throws the same exception that would
        be thrown by calling `finishToFuture().get()` if this were the last step. Calling `cancel()` on the returned future has no effect on the `ClosingFuture` pipeline.
        
        `statusFuture` differs from most methods on `ClosingFuture`: You can make calls
        to `statusFuture` *in addition to* the call you make to .finishToFuture() or
        a derivation method *on the same instance*. This is important because calling `statusFuture` alone does not provide a way to close the pipeline.
        """
        ...


    def transform(self, function: "ClosingFunction"["V", "U"], executor: "Executor") -> "ClosingFuture"["U"]:
        """
        Returns a new `ClosingFuture` pipeline step derived from this one by applying a function
        to its value. The function can use a DeferredCloser to capture objects to be closed
        when the pipeline is done.
        
        If this `ClosingFuture` fails, the function will not be called, and the derived `ClosingFuture` will be equivalent to this one.
        
        If the function throws an exception, that exception is used as the result of the derived
        `ClosingFuture`.
        
        Example usage:
        
        ````ClosingFuture<List<Row>> rowsFuture =
            queryFuture.transform((closer, result) -> result.getRows(), executor);````
        
        When selecting an executor, note that `directExecutor` is dangerous in some cases. See
        the discussion in the ListenableFuture.addListener documentation. All its warnings
        about heavyweight listeners are also applicable to heavyweight functions passed to this method.
        
        After calling this method, you may not call .finishToFuture(), .finishToValueAndCloser(ValueAndCloserConsumer, Executor), or any other derivation method on
        this `ClosingFuture`.

        Arguments
        - function: transforms the value of this step to the value of the derived step
        - executor: executor to run the function in

        Returns
        - the derived step

        Raises
        - IllegalStateException: if a `ClosingFuture` has already been derived from this
            one, or if this `ClosingFuture` has already been .finishToFuture()
            finished
        """
        ...


    def transformAsync(self, function: "AsyncClosingFunction"["V", "U"], executor: "Executor") -> "ClosingFuture"["U"]:
        """
        Returns a new `ClosingFuture` pipeline step derived from this one by applying a function
        that returns a `ClosingFuture` to its value. The function can use a DeferredCloser to capture objects to be closed when the pipeline is done (other than those
        captured by the returned ClosingFuture).
        
        If this `ClosingFuture` succeeds, the derived one will be equivalent to the one
        returned by the function.
        
        If this `ClosingFuture` fails, the function will not be called, and the derived `ClosingFuture` will be equivalent to this one.
        
        If the function throws an exception, that exception is used as the result of the derived
        `ClosingFuture`. But if the exception is thrown after the function creates a `ClosingFuture`, then none of the closeable objects in that `ClosingFuture` will be
        closed.
        
        Usage guidelines for this method:
        
        
          - Use this method only when calling an API that returns a ListenableFuture or a
              `ClosingFuture`. If possible, prefer calling .transform(ClosingFunction,
              Executor) instead, with a function that returns the next value directly.
          - Call DeferredCloser.eventuallyClose(Object, Executor) closer.eventuallyClose()
              for every closeable object this step creates in order to capture it for later closing.
          - Return a `ClosingFuture`. To turn a ListenableFuture into a `ClosingFuture` call .from(ListenableFuture).
          - In case this step doesn't create new closeables, you can adapt an API that returns a
              ListenableFuture to return a `ClosingFuture` by wrapping it with a call to
              .withoutCloser(AsyncFunction)
        
        
        Example usage:
        
        ````// Result.getRowsClosingFuture() returns a ClosingFuture.
        ClosingFuture<List<Row>> rowsFuture =
            queryFuture.transformAsync((closer, result) -> result.getRowsClosingFuture(), executor);
        
        // Result.writeRowsToOutputStreamFuture() returns a ListenableFuture that resolves to the
        // number of written rows. openOutputFile() returns a FileOutputStream (which implements
        // Closeable).
        ClosingFuture<Integer> rowsFuture2 =
            queryFuture.transformAsync(
                (closer, result) -> {
                  FileOutputStream fos = closer.eventuallyClose(openOutputFile(), closingExecutor);
                  return ClosingFuture.from(result.writeRowsToOutputStreamFuture(fos));`,
             executor);
        
        // Result.getRowsFuture() returns a ListenableFuture (no new closeables are created).
        ClosingFuture<List<Row>> rowsFuture3 =
            queryFuture.transformAsync(withoutCloser(Result::getRowsFuture), executor);
        
        }```
        
        When selecting an executor, note that `directExecutor` is dangerous in some cases. See
        the discussion in the ListenableFuture.addListener documentation. All its warnings
        about heavyweight listeners are also applicable to heavyweight functions passed to this method.
        (Specifically, `directExecutor` functions should avoid heavyweight operations inside
        `AsyncClosingFunction.apply`. Any heavyweight operations should occur in other threads
        responsible for completing the returned `ClosingFuture`.)
        
        After calling this method, you may not call .finishToFuture(), .finishToValueAndCloser(ValueAndCloserConsumer, Executor), or any other derivation method on
        this `ClosingFuture`.

        Arguments
        - function: transforms the value of this step to a `ClosingFuture` with the value of
            the derived step
        - executor: executor to run the function in

        Returns
        - the derived step

        Raises
        - IllegalStateException: if a `ClosingFuture` has already been derived from this
            one, or if this `ClosingFuture` has already been .finishToFuture()
            finished
        """
        ...


    @staticmethod
    def withoutCloser(function: "AsyncFunction"["V", "U"]) -> "AsyncClosingFunction"["V", "U"]:
        """
        Returns an AsyncClosingFunction that applies an AsyncFunction to an input,
        ignoring the DeferredCloser and returning a `ClosingFuture` derived from the returned
        ListenableFuture.
        
        Use this method to pass a transformation to .transformAsync(AsyncClosingFunction,
        Executor) or to .catchingAsync(Class, AsyncClosingFunction, Executor) as long as it
        meets these conditions:
        
        
          - It does not need to capture any Closeable objects by calling DeferredCloser.eventuallyClose(Object, Executor).
          - It returns a ListenableFuture.
        
        
        Example usage:
        
        ````// Result.getRowsFuture() returns a ListenableFuture.
        ClosingFuture<List<Row>> rowsFuture =
            queryFuture.transformAsync(withoutCloser(Result::getRowsFuture), executor);````

        Arguments
        - function: transforms the value of a `ClosingFuture` step to a ListenableFuture with the value of a derived step
        """
        ...


    def catching(self, exceptionType: type["X"], fallback: "ClosingFunction"["X", "V"], executor: "Executor") -> "ClosingFuture"["V"]:
        """
        Returns a new `ClosingFuture` pipeline step derived from this one by applying a function
        to its exception if it is an instance of a given exception type. The function can use a DeferredCloser to capture objects to be closed when the pipeline is done.
        
        If this `ClosingFuture` succeeds or fails with a different exception type, the
        function will not be called, and the derived `ClosingFuture` will be equivalent to this
        one.
        
        If the function throws an exception, that exception is used as the result of the derived
        `ClosingFuture`.
        
        Example usage:
        
        ````ClosingFuture<QueryResult> queryFuture =
            queryFuture.catching(
                QueryException.class, (closer, x) -> Query.emptyQueryResult(), executor);````
        
        When selecting an executor, note that `directExecutor` is dangerous in some cases. See
        the discussion in the ListenableFuture.addListener documentation. All its warnings
        about heavyweight listeners are also applicable to heavyweight functions passed to this method.
        
        After calling this method, you may not call .finishToFuture(), .finishToValueAndCloser(ValueAndCloserConsumer, Executor), or any other derivation method on
        this `ClosingFuture`.

        Arguments
        - exceptionType: the exception type that triggers use of `fallback`. The exception
            type is matched against this step's exception. "This step's exception" means the cause of
            the ExecutionException thrown by Future.get() on the Future
            underlying this step or, if `get()` throws a different kind of exception, that
            exception itself. To avoid hiding bugs and other unrecoverable errors, callers should
            prefer more specific types, avoiding `Throwable.class` in particular.
        - fallback: the function to be called if this step fails with the expected exception type.
            The function's argument is this step's exception. "This step's exception" means the cause
            of the ExecutionException thrown by Future.get() on the Future
            underlying this step or, if `get()` throws a different kind of exception, that
            exception itself.
        - executor: the executor that runs `fallback` if the input fails
        """
        ...


    def catchingAsync(self, exceptionType: type["X"], fallback: "AsyncClosingFunction"["X", "V"], executor: "Executor") -> "ClosingFuture"["V"]:
        ...


    def finishToFuture(self) -> "FluentFuture"["V"]:
        """
        Marks this step as the last step in the `ClosingFuture` pipeline.
        
        The returned Future is completed when the pipeline's computation completes, or when
        the pipeline is cancelled.
        
        All objects the pipeline has captured for closing will begin to be closed asynchronously
        **after** the returned `Future` is done: the future completes before closing starts,
        rather than once it has finished.
        
        After calling this method, you may not call .finishToValueAndCloser(ValueAndCloserConsumer, Executor), this method, or any other
        derivation method on this `ClosingFuture`.

        Returns
        - a Future that represents the final value or exception of the pipeline
        """
        ...


    def finishToValueAndCloser(self, consumer: "ValueAndCloserConsumer"["V"], executor: "Executor") -> None:
        """
        Marks this step as the last step in the `ClosingFuture` pipeline. When this step is done,
        `receiver` will be called with an object that contains the result of the operation. The
        receiver can store the ValueAndCloser outside the receiver for later synchronous use.
        
        After calling this method, you may not call .finishToFuture(), this method again, or
        any other derivation method on this `ClosingFuture`.

        Arguments
        - consumer: a callback whose method will be called (using `executor`) when this
            operation is done
        """
        ...


    def cancel(self, mayInterruptIfRunning: bool) -> bool:
        """
        Attempts to cancel execution of this step. This attempt will fail if the step has already
        completed, has already been cancelled, or could not be cancelled for some other reason. If
        successful, and this step has not started when `cancel` is called, this step should never
        run.
        
        If successful, causes the objects captured by this step (if already started) and its input
        step(s) for later closing to be closed on their respective Executors. If any such calls
        specified MoreExecutors.directExecutor(), those objects will be closed synchronously.

        Arguments
        - mayInterruptIfRunning: `True` if the thread executing this task should be
            interrupted; otherwise, in-progress tasks are allowed to complete, but the step will be
            cancelled regardless

        Returns
        - `False` if the step could not be cancelled, typically because it has already
            completed normally; `True` otherwise
        """
        ...


    def toString(self) -> str:
        ...


    class DeferredCloser:
        """
        An object that can capture objects to be closed later, when a ClosingFuture pipeline is
        done.
        """

        def eventuallyClose(self, closeable: "C", closingExecutor: "Executor") -> "C":
            """
            Captures an object to be closed when a ClosingFuture pipeline is done.
            
            For users of the `-jre` flavor of Guava, the object can be any `AutoCloseable`. For users of the `-android` flavor, the object must be a `Closeable`. (For more about the flavors, see <a
            href="https://github.com/google/guava#adding-guava-to-your-build">Adding Guava to your
            build</a>.)
            
            Be careful when targeting an older SDK than you are building against (most commonly when
            building for Android): Ensure that any object you pass implements the interface not just in
            your current SDK version but also at the oldest version you support. For example, <a
            href="https://developer.android.com/sdk/api_diff/16/">API Level 16</a> is the first version
            in which `Cursor` is `Closeable`. To support older versions, pass a wrapper
            `Closeable` with a method reference like `cursor::close`.
            
            Note that this method is still binary-compatible between flavors because the erasure of
            its parameter type is `Object`, not `AutoCloseable` or `Closeable`.

            Arguments
            - closeable: the object to be closed (see notes above)
            - closingExecutor: the object will be closed on this executor

            Returns
            - the first argument
            """
            ...


    class ClosingCallable:
        """
        An operation that computes a result.
        
        Type `<V>`: the type of the result
        """

        def call(self, closer: "DeferredCloser") -> "V":
            """
            Computes a result, or throws an exception if unable to do so.
            
            Any objects that are passed to DeferredCloser.eventuallyClose(Object, Executor)
            closer.eventuallyClose() will be closed when the ClosingFuture pipeline is done (but
            not before this method completes), even if this method throws or the pipeline is cancelled.
            """
            ...


    class AsyncClosingCallable:
        """
        An operation that computes a ClosingFuture of a result.
        
        Type `<V>`: the type of the result

        Since
        - 30.1
        """

        def call(self, closer: "DeferredCloser") -> "ClosingFuture"["V"]:
            """
            Computes a result, or throws an exception if unable to do so.
            
            Any objects that are passed to DeferredCloser.eventuallyClose(Object, Executor)
            closer.eventuallyClose() will be closed when the ClosingFuture pipeline is done (but
            not before this method completes), even if this method throws or the pipeline is cancelled.
            """
            ...


    class ClosingFunction:
        """
        A function from an input to a result.
        
        Type `<T>`: the type of the input to the function
        
        Type `<U>`: the type of the result of the function
        """

        def apply(self, closer: "DeferredCloser", input: "T") -> "U":
            """
            Applies this function to an input, or throws an exception if unable to do so.
            
            Any objects that are passed to DeferredCloser.eventuallyClose(Object, Executor)
            closer.eventuallyClose() will be closed when the ClosingFuture pipeline is done (but
            not before this method completes), even if this method throws or the pipeline is cancelled.
            """
            ...


    class AsyncClosingFunction:
        """
        A function from an input to a ClosingFuture of a result.
        
        Type `<T>`: the type of the input to the function
        
        Type `<U>`: the type of the result of the function
        """

        def apply(self, closer: "DeferredCloser", input: "T") -> "ClosingFuture"["U"]:
            """
            Applies this function to an input, or throws an exception if unable to do so.
            
            Any objects that are passed to DeferredCloser.eventuallyClose(Object, Executor)
            closer.eventuallyClose() will be closed when the ClosingFuture pipeline is done (but
            not before this method completes), even if this method throws or the pipeline is cancelled.
            """
            ...


    class ValueAndCloser:
        """
        An object that holds the final result of an asynchronous ClosingFuture operation and
        allows the user to close all the closeable objects that were captured during it for later
        closing.
        
        The asynchronous operation will have completed before this object is created.
        
        Type `<V>`: the type of the value of a successful operation

        See
        - ClosingFuture.finishToValueAndCloser(ValueAndCloserConsumer, Executor)
        """

        def get(self) -> "V":
            """
            Returns the final value of the associated ClosingFuture, or throws an exception as
            Future.get() would.
            
            Because the asynchronous operation has already completed, this method is synchronous and
            returns immediately.

            Raises
            - CancellationException: if the computation was cancelled
            - ExecutionException: if the computation threw an exception
            """
            ...


        def closeAsync(self) -> None:
            """
            Starts closing all closeable objects captured during the ClosingFuture's asynchronous
            operation on the Executors specified by calls to DeferredCloser.eventuallyClose(Object, Executor).
            
            If any such calls specified MoreExecutors.directExecutor(), those objects will be
            closed synchronously.
            
            Idempotent: objects will be closed at most once.
            """
            ...


    class ValueAndCloserConsumer:
        """
        Represents an operation that accepts a ValueAndCloser for the last step in a ClosingFuture pipeline.
        
        Type `<V>`: the type of the final value of a successful pipeline

        See
        - ClosingFuture.finishToValueAndCloser(ValueAndCloserConsumer, Executor)
        """

        def accept(self, valueAndCloser: "ValueAndCloser"["V"]) -> None:
            """
            Accepts a ValueAndCloser for the last step in a ClosingFuture pipeline.
            """
            ...


    class Peeker:
        """
        An object that can return the value of the ClosingFutures that are passed to .whenAllComplete(Iterable) or .whenAllSucceed(Iterable).
        
        Only for use by a CombiningCallable or AsyncCombiningCallable object.
        """

        def getDone(self, closingFuture: "ClosingFuture"["D"]) -> "D":
            """
            Returns the value of `closingFuture`.

            Raises
            - ExecutionException: if `closingFuture` is a failed step
            - CancellationException: if the `closingFuture`'s future was cancelled
            - IllegalArgumentException: if `closingFuture` is not one of the futures passed to
                .whenAllComplete(Iterable) or .whenAllComplete(Iterable)
            - IllegalStateException: if called outside of a call to CombiningCallable.call(DeferredCloser, Peeker) or AsyncCombiningCallable.call(DeferredCloser, Peeker)
            """
            ...


    class Combiner:

        def call(self, combiningCallable: "CombiningCallable"["V"], executor: "Executor") -> "ClosingFuture"["V"]:
            """
            Returns a new `ClosingFuture` pipeline step derived from the inputs by applying a
            combining function to their values. The function can use a DeferredCloser to capture
            objects to be closed when the pipeline is done.
            
            If this combiner was returned by a .whenAllSucceed method and any of the inputs
            fail, so will the returned step.
            
            If the combiningCallable throws a `CancellationException`, the pipeline will be
            cancelled.
            
            If the combiningCallable throws an `ExecutionException`, the cause of the thrown
            `ExecutionException` will be extracted and used as the failure of the derived step.
            """
            ...


        def callAsync(self, combiningCallable: "AsyncCombiningCallable"["V"], executor: "Executor") -> "ClosingFuture"["V"]:
            """
            Returns a new `ClosingFuture` pipeline step derived from the inputs by applying a
            `ClosingFuture`-returning function to their values. The function can use a DeferredCloser to capture objects to be closed when the pipeline is done (other than those
            captured by the returned ClosingFuture).
            
            If this combiner was returned by a .whenAllSucceed method and any of the inputs
            fail, so will the returned step.
            
            If the combiningCallable throws a `CancellationException`, the pipeline will be
            cancelled.
            
            If the combiningCallable throws an `ExecutionException`, the cause of the thrown
            `ExecutionException` will be extracted and used as the failure of the derived step.
            
            If the combiningCallable throws any other exception, it will be used as the failure of the
            derived step.
            
            If an exception is thrown after the combiningCallable creates a `ClosingFuture`,
            then none of the closeable objects in that `ClosingFuture` will be closed.
            
            Usage guidelines for this method:
            
            
              - Use this method only when calling an API that returns a ListenableFuture or a
                  `ClosingFuture`. If possible, prefer calling .call(CombiningCallable,
                  Executor) instead, with a function that returns the next value directly.
              - Call DeferredCloser.eventuallyClose(Object, Executor) closer.eventuallyClose()
                  for every closeable object this step creates in order to capture it for later closing.
              - Return a `ClosingFuture`. To turn a ListenableFuture into a `ClosingFuture` call .from(ListenableFuture).
            
            
            The same warnings about doing heavyweight operations within ClosingFuture.transformAsync(AsyncClosingFunction, Executor) apply here.
            """
            ...


        class CombiningCallable:
            """
            An operation that returns a result and may throw an exception.
            
            Type `<V>`: the type of the result
            """

            def call(self, closer: "DeferredCloser", peeker: "Peeker") -> "V":
                """
                Computes a result, or throws an exception if unable to do so.
                
                Any objects that are passed to DeferredCloser.eventuallyClose(Object, Executor)
                closer.eventuallyClose() will be closed when the ClosingFuture pipeline is done
                (but not before this method completes), even if this method throws or the pipeline is
                cancelled.

                Arguments
                - peeker: used to get the value of any of the input futures
                """
                ...


        class AsyncCombiningCallable:
            """
            An operation that returns a ClosingFuture result and may throw an exception.
            
            Type `<V>`: the type of the result
            """

            def call(self, closer: "DeferredCloser", peeker: "Peeker") -> "ClosingFuture"["V"]:
                """
                Computes a ClosingFuture result, or throws an exception if unable to do so.
                
                Any objects that are passed to DeferredCloser.eventuallyClose(Object, Executor)
                closer.eventuallyClose() will be closed when the ClosingFuture pipeline is done
                (but not before this method completes), even if this method throws or the pipeline is
                cancelled.

                Arguments
                - peeker: used to get the value of any of the input futures
                """
                ...


    class Combiner2(Combiner):
        """
        A generic Combiner that lets you use a lambda or method reference to combine two ClosingFutures. Use .whenAllSucceed(ClosingFuture, ClosingFuture) to start this
        combination.

        Arguments
        - <V1>: the type returned by the first future
        - <V2>: the type returned by the second future
        """

        def call(self, function: "ClosingFunction2"["V1", "V2", "U"], executor: "Executor") -> "ClosingFuture"["U"]:
            """
            Returns a new `ClosingFuture` pipeline step derived from the inputs by applying a
            combining function to their values. The function can use a DeferredCloser to capture
            objects to be closed when the pipeline is done.
            
            If this combiner was returned by .whenAllSucceed(ClosingFuture, ClosingFuture) and
            any of the inputs fail, so will the returned step.
            
            If the function throws a `CancellationException`, the pipeline will be cancelled.
            
            If the function throws an `ExecutionException`, the cause of the thrown `ExecutionException` will be extracted and used as the failure of the derived step.
            """
            ...


        def callAsync(self, function: "AsyncClosingFunction2"["V1", "V2", "U"], executor: "Executor") -> "ClosingFuture"["U"]:
            """
            Returns a new `ClosingFuture` pipeline step derived from the inputs by applying a
            `ClosingFuture`-returning function to their values. The function can use a DeferredCloser to capture objects to be closed when the pipeline is done (other than those
            captured by the returned ClosingFuture).
            
            If this combiner was returned by .whenAllSucceed(ClosingFuture, ClosingFuture) and
            any of the inputs fail, so will the returned step.
            
            If the function throws a `CancellationException`, the pipeline will be cancelled.
            
            If the function throws an `ExecutionException`, the cause of the thrown `ExecutionException` will be extracted and used as the failure of the derived step.
            
            If the function throws any other exception, it will be used as the failure of the derived
            step.
            
            If an exception is thrown after the function creates a `ClosingFuture`, then none of
            the closeable objects in that `ClosingFuture` will be closed.
            
            Usage guidelines for this method:
            
            
              - Use this method only when calling an API that returns a ListenableFuture or a
                  `ClosingFuture`. If possible, prefer calling .call(CombiningCallable,
                  Executor) instead, with a function that returns the next value directly.
              - Call DeferredCloser.eventuallyClose(Object, Executor) closer.eventuallyClose()
                  for every closeable object this step creates in order to capture it for later closing.
              - Return a `ClosingFuture`. To turn a ListenableFuture into a `ClosingFuture` call .from(ListenableFuture).
            
            
            The same warnings about doing heavyweight operations within ClosingFuture.transformAsync(AsyncClosingFunction, Executor) apply here.
            """
            ...


        class ClosingFunction2:
            """
            A function that returns a value when applied to the values of the two futures passed to
            .whenAllSucceed(ClosingFuture, ClosingFuture).
            
            Type `<U>`: the type returned by the function

            Arguments
            - <V1>: the type returned by the first future
            - <V2>: the type returned by the second future
            """

            def apply(self, closer: "DeferredCloser", value1: "V1", value2: "V2") -> "U":
                """
                Applies this function to two inputs, or throws an exception if unable to do so.
                
                Any objects that are passed to DeferredCloser.eventuallyClose(Object, Executor)
                closer.eventuallyClose() will be closed when the ClosingFuture pipeline is done
                (but not before this method completes), even if this method throws or the pipeline is
                cancelled.
                """
                ...


        class AsyncClosingFunction2:
            """
            A function that returns a ClosingFuture when applied to the values of the two futures
            passed to .whenAllSucceed(ClosingFuture, ClosingFuture).
            
            Type `<U>`: the type returned by the function

            Arguments
            - <V1>: the type returned by the first future
            - <V2>: the type returned by the second future
            """

            def apply(self, closer: "DeferredCloser", value1: "V1", value2: "V2") -> "ClosingFuture"["U"]:
                """
                Applies this function to two inputs, or throws an exception if unable to do so.
                
                Any objects that are passed to DeferredCloser.eventuallyClose(Object, Executor)
                closer.eventuallyClose() will be closed when the ClosingFuture pipeline is done
                (but not before this method completes), even if this method throws or the pipeline is
                cancelled.
                """
                ...


    class Combiner3(Combiner):
        """
        A generic Combiner that lets you use a lambda or method reference to combine three
        ClosingFutures. Use .whenAllSucceed(ClosingFuture, ClosingFuture,
        ClosingFuture) to start this combination.

        Arguments
        - <V1>: the type returned by the first future
        - <V2>: the type returned by the second future
        - <V3>: the type returned by the third future
        """

        def call(self, function: "ClosingFunction3"["V1", "V2", "V3", "U"], executor: "Executor") -> "ClosingFuture"["U"]:
            """
            Returns a new `ClosingFuture` pipeline step derived from the inputs by applying a
            combining function to their values. The function can use a DeferredCloser to capture
            objects to be closed when the pipeline is done.
            
            If this combiner was returned by .whenAllSucceed(ClosingFuture, ClosingFuture,
            ClosingFuture) and any of the inputs fail, so will the returned step.
            
            If the function throws a `CancellationException`, the pipeline will be cancelled.
            
            If the function throws an `ExecutionException`, the cause of the thrown `ExecutionException` will be extracted and used as the failure of the derived step.
            """
            ...


        def callAsync(self, function: "AsyncClosingFunction3"["V1", "V2", "V3", "U"], executor: "Executor") -> "ClosingFuture"["U"]:
            """
            Returns a new `ClosingFuture` pipeline step derived from the inputs by applying a
            `ClosingFuture`-returning function to their values. The function can use a DeferredCloser to capture objects to be closed when the pipeline is done (other than those
            captured by the returned ClosingFuture).
            
            If this combiner was returned by .whenAllSucceed(ClosingFuture, ClosingFuture,
            ClosingFuture) and any of the inputs fail, so will the returned step.
            
            If the function throws a `CancellationException`, the pipeline will be cancelled.
            
            If the function throws an `ExecutionException`, the cause of the thrown `ExecutionException` will be extracted and used as the failure of the derived step.
            
            If the function throws any other exception, it will be used as the failure of the derived
            step.
            
            If an exception is thrown after the function creates a `ClosingFuture`, then none of
            the closeable objects in that `ClosingFuture` will be closed.
            
            Usage guidelines for this method:
            
            
              - Use this method only when calling an API that returns a ListenableFuture or a
                  `ClosingFuture`. If possible, prefer calling .call(CombiningCallable,
                  Executor) instead, with a function that returns the next value directly.
              - Call DeferredCloser.eventuallyClose(Object, Executor) closer.eventuallyClose()
                  for every closeable object this step creates in order to capture it for later closing.
              - Return a `ClosingFuture`. To turn a ListenableFuture into a `ClosingFuture` call .from(ListenableFuture).
            
            
            The same warnings about doing heavyweight operations within ClosingFuture.transformAsync(AsyncClosingFunction, Executor) apply here.
            """
            ...


        class ClosingFunction3:
            """
            A function that returns a value when applied to the values of the three futures passed to
            .whenAllSucceed(ClosingFuture, ClosingFuture, ClosingFuture).
            
            Type `<U>`: the type returned by the function

            Arguments
            - <V1>: the type returned by the first future
            - <V2>: the type returned by the second future
            - <V3>: the type returned by the third future
            """

            def apply(self, closer: "DeferredCloser", value1: "V1", value2: "V2", value3: "V3") -> "U":
                """
                Applies this function to three inputs, or throws an exception if unable to do so.
                
                Any objects that are passed to DeferredCloser.eventuallyClose(Object, Executor)
                closer.eventuallyClose() will be closed when the ClosingFuture pipeline is done
                (but not before this method completes), even if this method throws or the pipeline is
                cancelled.
                """
                ...


        class AsyncClosingFunction3:
            """
            A function that returns a ClosingFuture when applied to the values of the three
            futures passed to .whenAllSucceed(ClosingFuture, ClosingFuture, ClosingFuture).
            
            Type `<U>`: the type returned by the function

            Arguments
            - <V1>: the type returned by the first future
            - <V2>: the type returned by the second future
            - <V3>: the type returned by the third future
            """

            def apply(self, closer: "DeferredCloser", value1: "V1", value2: "V2", value3: "V3") -> "ClosingFuture"["U"]:
                """
                Applies this function to three inputs, or throws an exception if unable to do so.
                
                Any objects that are passed to DeferredCloser.eventuallyClose(Object, Executor)
                closer.eventuallyClose() will be closed when the ClosingFuture pipeline is done
                (but not before this method completes), even if this method throws or the pipeline is
                cancelled.
                """
                ...


    class Combiner4(Combiner):
        """
        A generic Combiner that lets you use a lambda or method reference to combine four
        ClosingFutures. Use .whenAllSucceed(ClosingFuture, ClosingFuture, ClosingFuture,
        ClosingFuture) to start this combination.

        Arguments
        - <V1>: the type returned by the first future
        - <V2>: the type returned by the second future
        - <V3>: the type returned by the third future
        - <V4>: the type returned by the fourth future
        """

        def call(self, function: "ClosingFunction4"["V1", "V2", "V3", "V4", "U"], executor: "Executor") -> "ClosingFuture"["U"]:
            """
            Returns a new `ClosingFuture` pipeline step derived from the inputs by applying a
            combining function to their values. The function can use a DeferredCloser to capture
            objects to be closed when the pipeline is done.
            
            If this combiner was returned by .whenAllSucceed(ClosingFuture, ClosingFuture,
            ClosingFuture, ClosingFuture) and any of the inputs fail, so will the returned step.
            
            If the function throws a `CancellationException`, the pipeline will be cancelled.
            
            If the function throws an `ExecutionException`, the cause of the thrown `ExecutionException` will be extracted and used as the failure of the derived step.
            """
            ...


        def callAsync(self, function: "AsyncClosingFunction4"["V1", "V2", "V3", "V4", "U"], executor: "Executor") -> "ClosingFuture"["U"]:
            """
            Returns a new `ClosingFuture` pipeline step derived from the inputs by applying a
            `ClosingFuture`-returning function to their values. The function can use a DeferredCloser to capture objects to be closed when the pipeline is done (other than those
            captured by the returned ClosingFuture).
            
            If this combiner was returned by .whenAllSucceed(ClosingFuture, ClosingFuture,
            ClosingFuture, ClosingFuture) and any of the inputs fail, so will the returned step.
            
            If the function throws a `CancellationException`, the pipeline will be cancelled.
            
            If the function throws an `ExecutionException`, the cause of the thrown `ExecutionException` will be extracted and used as the failure of the derived step.
            
            If the function throws any other exception, it will be used as the failure of the derived
            step.
            
            If an exception is thrown after the function creates a `ClosingFuture`, then none of
            the closeable objects in that `ClosingFuture` will be closed.
            
            Usage guidelines for this method:
            
            
              - Use this method only when calling an API that returns a ListenableFuture or a
                  `ClosingFuture`. If possible, prefer calling .call(CombiningCallable,
                  Executor) instead, with a function that returns the next value directly.
              - Call DeferredCloser.eventuallyClose(Object, Executor) closer.eventuallyClose()
                  for every closeable object this step creates in order to capture it for later closing.
              - Return a `ClosingFuture`. To turn a ListenableFuture into a `ClosingFuture` call .from(ListenableFuture).
            
            
            The same warnings about doing heavyweight operations within ClosingFuture.transformAsync(AsyncClosingFunction, Executor) apply here.
            """
            ...


        class ClosingFunction4:
            """
            A function that returns a value when applied to the values of the four futures passed to
            .whenAllSucceed(ClosingFuture, ClosingFuture, ClosingFuture, ClosingFuture).
            
            Type `<U>`: the type returned by the function

            Arguments
            - <V1>: the type returned by the first future
            - <V2>: the type returned by the second future
            - <V3>: the type returned by the third future
            - <V4>: the type returned by the fourth future
            """

            def apply(self, closer: "DeferredCloser", value1: "V1", value2: "V2", value3: "V3", value4: "V4") -> "U":
                """
                Applies this function to four inputs, or throws an exception if unable to do so.
                
                Any objects that are passed to DeferredCloser.eventuallyClose(Object, Executor)
                closer.eventuallyClose() will be closed when the ClosingFuture pipeline is done
                (but not before this method completes), even if this method throws or the pipeline is
                cancelled.
                """
                ...


        class AsyncClosingFunction4:
            """
            A function that returns a ClosingFuture when applied to the values of the four
            futures passed to .whenAllSucceed(ClosingFuture, ClosingFuture, ClosingFuture,
            ClosingFuture).
            
            Type `<U>`: the type returned by the function

            Arguments
            - <V1>: the type returned by the first future
            - <V2>: the type returned by the second future
            - <V3>: the type returned by the third future
            - <V4>: the type returned by the fourth future
            """

            def apply(self, closer: "DeferredCloser", value1: "V1", value2: "V2", value3: "V3", value4: "V4") -> "ClosingFuture"["U"]:
                """
                Applies this function to four inputs, or throws an exception if unable to do so.
                
                Any objects that are passed to DeferredCloser.eventuallyClose(Object, Executor)
                closer.eventuallyClose() will be closed when the ClosingFuture pipeline is done
                (but not before this method completes), even if this method throws or the pipeline is
                cancelled.
                """
                ...


    class Combiner5(Combiner):
        """
        A generic Combiner that lets you use a lambda or method reference to combine five
        ClosingFutures. Use .whenAllSucceed(ClosingFuture, ClosingFuture, ClosingFuture,
        ClosingFuture, ClosingFuture) to start this combination.

        Arguments
        - <V1>: the type returned by the first future
        - <V2>: the type returned by the second future
        - <V3>: the type returned by the third future
        - <V4>: the type returned by the fourth future
        - <V5>: the type returned by the fifth future
        """

        def call(self, function: "ClosingFunction5"["V1", "V2", "V3", "V4", "V5", "U"], executor: "Executor") -> "ClosingFuture"["U"]:
            """
            Returns a new `ClosingFuture` pipeline step derived from the inputs by applying a
            combining function to their values. The function can use a DeferredCloser to capture
            objects to be closed when the pipeline is done.
            
            If this combiner was returned by .whenAllSucceed(ClosingFuture, ClosingFuture,
            ClosingFuture, ClosingFuture, ClosingFuture) and any of the inputs fail, so will the
            returned step.
            
            If the function throws a `CancellationException`, the pipeline will be cancelled.
            
            If the function throws an `ExecutionException`, the cause of the thrown `ExecutionException` will be extracted and used as the failure of the derived step.
            """
            ...


        def callAsync(self, function: "AsyncClosingFunction5"["V1", "V2", "V3", "V4", "V5", "U"], executor: "Executor") -> "ClosingFuture"["U"]:
            """
            Returns a new `ClosingFuture` pipeline step derived from the inputs by applying a
            `ClosingFuture`-returning function to their values. The function can use a DeferredCloser to capture objects to be closed when the pipeline is done (other than those
            captured by the returned ClosingFuture).
            
            If this combiner was returned by .whenAllSucceed(ClosingFuture, ClosingFuture,
            ClosingFuture, ClosingFuture, ClosingFuture) and any of the inputs fail, so will the
            returned step.
            
            If the function throws a `CancellationException`, the pipeline will be cancelled.
            
            If the function throws an `ExecutionException`, the cause of the thrown `ExecutionException` will be extracted and used as the failure of the derived step.
            
            If the function throws any other exception, it will be used as the failure of the derived
            step.
            
            If an exception is thrown after the function creates a `ClosingFuture`, then none of
            the closeable objects in that `ClosingFuture` will be closed.
            
            Usage guidelines for this method:
            
            
              - Use this method only when calling an API that returns a ListenableFuture or a
                  `ClosingFuture`. If possible, prefer calling .call(CombiningCallable,
                  Executor) instead, with a function that returns the next value directly.
              - Call DeferredCloser.eventuallyClose(Object, Executor) closer.eventuallyClose()
                  for every closeable object this step creates in order to capture it for later closing.
              - Return a `ClosingFuture`. To turn a ListenableFuture into a `ClosingFuture` call .from(ListenableFuture).
            
            
            The same warnings about doing heavyweight operations within ClosingFuture.transformAsync(AsyncClosingFunction, Executor) apply here.
            """
            ...


        class ClosingFunction5:
            """
            A function that returns a value when applied to the values of the five futures passed to
            .whenAllSucceed(ClosingFuture, ClosingFuture, ClosingFuture, ClosingFuture,
            ClosingFuture).
            
            Type `<U>`: the type returned by the function

            Arguments
            - <V1>: the type returned by the first future
            - <V2>: the type returned by the second future
            - <V3>: the type returned by the third future
            - <V4>: the type returned by the fourth future
            - <V5>: the type returned by the fifth future
            """

            def apply(self, closer: "DeferredCloser", value1: "V1", value2: "V2", value3: "V3", value4: "V4", value5: "V5") -> "U":
                """
                Applies this function to five inputs, or throws an exception if unable to do so.
                
                Any objects that are passed to DeferredCloser.eventuallyClose(Object, Executor)
                closer.eventuallyClose() will be closed when the ClosingFuture pipeline is done
                (but not before this method completes), even if this method throws or the pipeline is
                cancelled.
                """
                ...


        class AsyncClosingFunction5:
            """
            A function that returns a ClosingFuture when applied to the values of the five
            futures passed to .whenAllSucceed(ClosingFuture, ClosingFuture, ClosingFuture,
            ClosingFuture, ClosingFuture).
            
            Type `<U>`: the type returned by the function

            Arguments
            - <V1>: the type returned by the first future
            - <V2>: the type returned by the second future
            - <V3>: the type returned by the third future
            - <V4>: the type returned by the fourth future
            - <V5>: the type returned by the fifth future
            """

            def apply(self, closer: "DeferredCloser", value1: "V1", value2: "V2", value3: "V3", value4: "V4", value5: "V5") -> "ClosingFuture"["U"]:
                """
                Applies this function to five inputs, or throws an exception if unable to do so.
                
                Any objects that are passed to DeferredCloser.eventuallyClose(Object, Executor)
                closer.eventuallyClose() will be closed when the ClosingFuture pipeline is done
                (but not before this method completes), even if this method throws or the pipeline is
                cancelled.
                """
                ...
