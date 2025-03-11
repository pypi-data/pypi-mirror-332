"""
Python module generated from Java source file com.google.common.util.concurrent.Futures

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import J2ktIncompatible
from com.google.common.base import Function
from com.google.common.base import MoreObjects
from com.google.common.base import Preconditions
from com.google.common.collect import ImmutableList
from com.google.common.util.concurrent import *
from com.google.common.util.concurrent.CollectionFuture import ListFuture
from com.google.common.util.concurrent.ImmediateFuture import ImmediateCancelledFuture
from com.google.common.util.concurrent.ImmediateFuture import ImmediateFailedFuture
from com.google.common.util.concurrent.internal import InternalFutureFailureAccess
from com.google.common.util.concurrent.internal import InternalFutures
from com.google.errorprone.annotations import CanIgnoreReturnValue
from com.google.errorprone.annotations.concurrent import LazyInit
from java.time import Duration
from java.util.concurrent import Callable
from java.util.concurrent import CancellationException
from java.util.concurrent import ExecutionException
from java.util.concurrent import Executor
from java.util.concurrent import Future
from java.util.concurrent import RejectedExecutionException
from java.util.concurrent import ScheduledExecutorService
from java.util.concurrent import TimeUnit
from java.util.concurrent import TimeoutException
from java.util.concurrent.atomic import AtomicInteger
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class Futures(GwtFuturesCatchingSpecialization):
    """
    Static utility methods pertaining to the Future interface.
    
    Many of these methods use the ListenableFuture API; consult the Guava User Guide
    article on <a href="https://github.com/google/guava/wiki/ListenableFutureExplained">`ListenableFuture`</a>.
    
    The main purpose of `ListenableFuture` is to help you chain together a graph of
    asynchronous operations. You can chain them together manually with calls to methods like Futures.transform(ListenableFuture, Function, Executor) Futures.transform, but you will often
    find it easier to use a framework. Frameworks automate the process, often adding features like
    monitoring, debugging, and cancellation. Examples of frameworks include:
    
    
      - <a href="https://dagger.dev/producers.html">Dagger Producers</a>
    
    
    If you do chain your operations manually, you may want to use FluentFuture.

    Author(s)
    - Sven Mawson

    Since
    - 1.0
    """

    @staticmethod
    def immediateFuture(value: "V") -> "ListenableFuture"["V"]:
        """
        Creates a `ListenableFuture` which has its value set immediately upon construction. The
        getters just return the value. This `Future` can't be canceled or timed out and its
        `isDone()` method always returns `True`.
        """
        ...


    @staticmethod
    def immediateVoidFuture() -> "ListenableFuture"["Void"]:
        """
        Returns a successful `ListenableFuture<Void>`. This method is equivalent to `immediateFuture(null)` except that it is restricted to produce futures of type `Void`.

        Since
        - 29.0
        """
        ...


    @staticmethod
    def immediateFailedFuture(throwable: "Throwable") -> "ListenableFuture"["V"]:
        """
        Returns a `ListenableFuture` which has an exception set immediately upon construction.
        
        The returned `Future` can't be cancelled, and its `isDone()` method always
        returns `True`. Calling `get()` will immediately throw the provided `Throwable` wrapped in an `ExecutionException`.
        """
        ...


    @staticmethod
    def immediateCancelledFuture() -> "ListenableFuture"["V"]:
        """
        Creates a `ListenableFuture` which is cancelled immediately upon construction, so that
        `isCancelled()` always returns `True`.

        Since
        - 14.0
        """
        ...


    @staticmethod
    def submit(callable: "Callable"["O"], executor: "Executor") -> "ListenableFuture"["O"]:
        """
        Executes `callable` on the specified `executor`, returning a `Future`.

        Raises
        - RejectedExecutionException: if the task cannot be scheduled for execution

        Since
        - 28.2
        """
        ...


    @staticmethod
    def submit(runnable: "Runnable", executor: "Executor") -> "ListenableFuture"["Void"]:
        """
        Executes `runnable` on the specified `executor`, returning a `Future` that
        will complete after execution.

        Raises
        - RejectedExecutionException: if the task cannot be scheduled for execution

        Since
        - 28.2
        """
        ...


    @staticmethod
    def submitAsync(callable: "AsyncCallable"["O"], executor: "Executor") -> "ListenableFuture"["O"]:
        """
        Executes `callable` on the specified `executor`, returning a `Future`.

        Raises
        - RejectedExecutionException: if the task cannot be scheduled for execution

        Since
        - 23.0
        """
        ...


    @staticmethod
    def scheduleAsync(callable: "AsyncCallable"["O"], delay: "Duration", executorService: "ScheduledExecutorService") -> "ListenableFuture"["O"]:
        """
        Schedules `callable` on the specified `executor`, returning a `Future`.

        Raises
        - RejectedExecutionException: if the task cannot be scheduled for execution

        Since
        - 28.0
        """
        ...


    @staticmethod
    def scheduleAsync(callable: "AsyncCallable"["O"], delay: int, timeUnit: "TimeUnit", executorService: "ScheduledExecutorService") -> "ListenableFuture"["O"]:
        """
        Schedules `callable` on the specified `executor`, returning a `Future`.

        Raises
        - RejectedExecutionException: if the task cannot be scheduled for execution

        Since
        - 23.0
        """
        ...


    @staticmethod
    def catching(input: "ListenableFuture"["V"], exceptionType: type["X"], fallback: "Function"["X", "V"], executor: "Executor") -> "ListenableFuture"["V"]:
        """
        Returns a `Future` whose result is taken from the given primary `input` or, if the
        primary input fails with the given `exceptionType`, from the result provided by the
        `fallback`. Function.apply is not invoked until the primary input has failed, so
        if the primary input succeeds, it is never invoked. If, during the invocation of `fallback`, an exception is thrown, this exception is used as the result of the output `Future`.
        
        Usage example:
        
        ````ListenableFuture<Integer> fetchCounterFuture = ...;
        
        // Falling back to a zero counter in case an exception happens when
        // processing the RPC to fetch counters.
        ListenableFuture<Integer> faultTolerantFuture = Futures.catching(
            fetchCounterFuture, FetchException.class, x -> 0, directExecutor());````
        
        When selecting an executor, note that `directExecutor` is dangerous in some cases. See
        the warnings the MoreExecutors.directExecutor documentation.

        Arguments
        - input: the primary input `Future`
        - exceptionType: the exception type that triggers use of `fallback`. The exception
            type is matched against the input's exception. "The input's exception" means the cause of
            the ExecutionException thrown by `input.get()` or, if `get()` throws a
            different kind of exception, that exception itself. To avoid hiding bugs and other
            unrecoverable errors, callers should prefer more specific types, avoiding `Throwable.class` in particular.
        - fallback: the Function to be called if `input` fails with the expected
            exception type. The function's argument is the input's exception. "The input's exception"
            means the cause of the ExecutionException thrown by `input.get()` or, if
            `get()` throws a different kind of exception, that exception itself.
        - executor: the executor that runs `fallback` if `input` fails

        Since
        - 19.0
        """
        ...


    @staticmethod
    def catchingAsync(input: "ListenableFuture"["V"], exceptionType: type["X"], fallback: "AsyncFunction"["X", "V"], executor: "Executor") -> "ListenableFuture"["V"]:
        """
        Returns a `Future` whose result is taken from the given primary `input` or, if the
        primary input fails with the given `exceptionType`, from the result provided by the
        `fallback`. AsyncFunction.apply is not invoked until the primary input has
        failed, so if the primary input succeeds, it is never invoked. If, during the invocation of
        `fallback`, an exception is thrown, this exception is used as the result of the output
        `Future`.
        
        Usage examples:
        
        ````ListenableFuture<Integer> fetchCounterFuture = ...;
        
        // Falling back to a zero counter in case an exception happens when
        // processing the RPC to fetch counters.
        ListenableFuture<Integer> faultTolerantFuture = Futures.catchingAsync(
            fetchCounterFuture, FetchException.class, x -> immediateFuture(0), directExecutor());````
        
        The fallback can also choose to propagate the original exception when desired:
        
        ````ListenableFuture<Integer> fetchCounterFuture = ...;
        
        // Falling back to a zero counter only in case the exception was a
        // TimeoutException.
        ListenableFuture<Integer> faultTolerantFuture = Futures.catchingAsync(
            fetchCounterFuture,
            FetchException.class,
            e -> {
              if (omitDataOnFetchFailure) {
                return immediateFuture(0);`
              throw e;
            },
            directExecutor());
        }```
        
        When selecting an executor, note that `directExecutor` is dangerous in some cases. See
        the warnings the MoreExecutors.directExecutor documentation.

        Arguments
        - input: the primary input `Future`
        - exceptionType: the exception type that triggers use of `fallback`. The exception
            type is matched against the input's exception. "The input's exception" means the cause of
            the ExecutionException thrown by `input.get()` or, if `get()` throws a
            different kind of exception, that exception itself. To avoid hiding bugs and other
            unrecoverable errors, callers should prefer more specific types, avoiding `Throwable.class` in particular.
        - fallback: the AsyncFunction to be called if `input` fails with the expected
            exception type. The function's argument is the input's exception. "The input's exception"
            means the cause of the ExecutionException thrown by `input.get()` or, if
            `get()` throws a different kind of exception, that exception itself.
        - executor: the executor that runs `fallback` if `input` fails

        Since
        - 19.0 (similar functionality in 14.0 as `withFallback`)
        """
        ...


    @staticmethod
    def withTimeout(delegate: "ListenableFuture"["V"], time: "Duration", scheduledExecutor: "ScheduledExecutorService") -> "ListenableFuture"["V"]:
        """
        Returns a future that delegates to another but will finish early (via a TimeoutException wrapped in an ExecutionException) if the specified duration expires.
        
        The delegate future is interrupted and cancelled if it times out.

        Arguments
        - delegate: The future to delegate to.
        - time: when to time out the future
        - scheduledExecutor: The executor service to enforce the timeout.

        Since
        - 28.0
        """
        ...


    @staticmethod
    def withTimeout(delegate: "ListenableFuture"["V"], time: int, unit: "TimeUnit", scheduledExecutor: "ScheduledExecutorService") -> "ListenableFuture"["V"]:
        """
        Returns a future that delegates to another but will finish early (via a TimeoutException wrapped in an ExecutionException) if the specified duration expires.
        
        The delegate future is interrupted and cancelled if it times out.

        Arguments
        - delegate: The future to delegate to.
        - time: when to time out the future
        - unit: the time unit of the time parameter
        - scheduledExecutor: The executor service to enforce the timeout.

        Since
        - 19.0
        """
        ...


    @staticmethod
    def transformAsync(input: "ListenableFuture"["I"], function: "AsyncFunction"["I", "O"], executor: "Executor") -> "ListenableFuture"["O"]:
        """
        Returns a new `Future` whose result is asynchronously derived from the result of the
        given `Future`. If the given `Future` fails, the returned `Future` fails with
        the same exception (and the function is not invoked).
        
        More precisely, the returned `Future` takes its result from a `Future` produced
        by applying the given `AsyncFunction` to the result of the original `Future`.
        Example usage:
        
        ````ListenableFuture<RowKey> rowKeyFuture = indexService.lookUp(query);
        ListenableFuture<QueryResult> queryFuture =
            transformAsync(rowKeyFuture, dataService::readFuture, executor);````
        
        When selecting an executor, note that `directExecutor` is dangerous in some cases. See
        the warnings the MoreExecutors.directExecutor documentation.
        
        The returned `Future` attempts to keep its cancellation state in sync with that of the
        input future and that of the future returned by the chain function. That is, if the returned
        `Future` is cancelled, it will attempt to cancel the other two, and if either of the
        other two is cancelled, the returned `Future` will receive a callback in which it will
        attempt to cancel itself.

        Arguments
        - input: The future to transform
        - function: A function to transform the result of the input future to the result of the
            output future
        - executor: Executor to run the function in.

        Returns
        - A future that holds result of the function (if the input succeeded) or the original
            input's failure (if not)

        Since
        - 19.0 (in 11.0 as `transform`)
        """
        ...


    @staticmethod
    def transform(input: "ListenableFuture"["I"], function: "Function"["I", "O"], executor: "Executor") -> "ListenableFuture"["O"]:
        """
        Returns a new `Future` whose result is derived from the result of the given `Future`. If `input` fails, the returned `Future` fails with the same exception (and
        the function is not invoked). Example usage:
        
        ````ListenableFuture<QueryResult> queryFuture = ...;
        ListenableFuture<List<Row>> rowsFuture =
            transform(queryFuture, QueryResult::getRows, executor);````
        
        When selecting an executor, note that `directExecutor` is dangerous in some cases. See
        the warnings the MoreExecutors.directExecutor documentation.
        
        The returned `Future` attempts to keep its cancellation state in sync with that of the
        input future. That is, if the returned `Future` is cancelled, it will attempt to cancel
        the input, and if the input is cancelled, the returned `Future` will receive a callback
        in which it will attempt to cancel itself.
        
        An example use of this method is to convert a serializable object returned from an RPC into
        a POJO.

        Arguments
        - input: The future to transform
        - function: A Function to transform the results of the provided future to the results of
            the returned future.
        - executor: Executor to run the function in.

        Returns
        - A future that holds result of the transformation.

        Since
        - 9.0 (in 2.0 as `compose`)
        """
        ...


    @staticmethod
    def lazyTransform(input: "Future"["I"], function: "Function"["I", "O"]) -> "Future"["O"]:
        """
        Like .transform(ListenableFuture, Function, Executor) except that the transformation
        `function` is invoked on each call to Future.get() get() on the returned future.
        
        The returned `Future` reflects the input's cancellation state directly, and any
        attempt to cancel the returned Future is likewise passed through to the input Future.
        
        Note that calls to Future.get(long, TimeUnit) timed get only apply the timeout
        to the execution of the underlying `Future`, *not* to the execution of the
        transformation function.
        
        The primary audience of this method is callers of `transform` who don't have a `ListenableFuture` available and do not mind repeated, lazy function evaluation.

        Arguments
        - input: The future to transform
        - function: A Function to transform the results of the provided future to the results of
            the returned future.

        Returns
        - A future that returns the result of the transformation.

        Since
        - 10.0
        """
        ...


    @staticmethod
    def allAsList(*futures: Tuple["ListenableFuture"["V"], ...]) -> "ListenableFuture"[list["V"]]:
        """
        Creates a new `ListenableFuture` whose value is a list containing the values of all its
        input futures, if all succeed.
        
        The list of results is in the same order as the input list.
        
        This differs from .successfulAsList(ListenableFuture[]) in that it will return a
        failed future if any of the items fails.
        
        Canceling this future will attempt to cancel all the component futures, and if any of the
        provided futures fails or is canceled, this one is, too.

        Arguments
        - futures: futures to combine

        Returns
        - a future that provides a list of the results of the component futures

        Since
        - 10.0
        """
        ...


    @staticmethod
    def allAsList(futures: Iterable["ListenableFuture"["V"]]) -> "ListenableFuture"[list["V"]]:
        """
        Creates a new `ListenableFuture` whose value is a list containing the values of all its
        input futures, if all succeed.
        
        The list of results is in the same order as the input list.
        
        This differs from .successfulAsList(Iterable) in that it will return a failed future
        if any of the items fails.
        
        Canceling this future will attempt to cancel all the component futures, and if any of the
        provided futures fails or is canceled, this one is, too.

        Arguments
        - futures: futures to combine

        Returns
        - a future that provides a list of the results of the component futures

        Since
        - 10.0
        """
        ...


    @staticmethod
    def whenAllComplete(*futures: Tuple["ListenableFuture"["V"], ...]) -> "FutureCombiner"["V"]:
        """
        Creates a FutureCombiner that processes the completed futures whether or not they're
        successful.
        
        Any failures from the input futures will not be propagated to the returned future.

        Since
        - 20.0
        """
        ...


    @staticmethod
    def whenAllComplete(futures: Iterable["ListenableFuture"["V"]]) -> "FutureCombiner"["V"]:
        """
        Creates a FutureCombiner that processes the completed futures whether or not they're
        successful.
        
        Any failures from the input futures will not be propagated to the returned future.

        Since
        - 20.0
        """
        ...


    @staticmethod
    def whenAllSucceed(*futures: Tuple["ListenableFuture"["V"], ...]) -> "FutureCombiner"["V"]:
        """
        Creates a FutureCombiner requiring that all passed in futures are successful.
        
        If any input fails, the returned future fails immediately.

        Since
        - 20.0
        """
        ...


    @staticmethod
    def whenAllSucceed(futures: Iterable["ListenableFuture"["V"]]) -> "FutureCombiner"["V"]:
        """
        Creates a FutureCombiner requiring that all passed in futures are successful.
        
        If any input fails, the returned future fails immediately.

        Since
        - 20.0
        """
        ...


    @staticmethod
    def nonCancellationPropagating(future: "ListenableFuture"["V"]) -> "ListenableFuture"["V"]:
        """
        Returns a `ListenableFuture` whose result is set from the supplied future when it
        completes. Cancelling the supplied future will also cancel the returned future, but cancelling
        the returned future will have no effect on the supplied future.

        Since
        - 15.0
        """
        ...


    @staticmethod
    def successfulAsList(*futures: Tuple["ListenableFuture"["V"], ...]) -> "ListenableFuture"[list["V"]]:
        """
        Creates a new `ListenableFuture` whose value is a list containing the values of all its
        successful input futures. The list of results is in the same order as the input list, and if
        any of the provided futures fails or is canceled, its corresponding position will contain
        `null` (which is indistinguishable from the future having a successful value of `null`).
        
        The list of results is in the same order as the input list.
        
        This differs from .allAsList(ListenableFuture[]) in that it's tolerant of failed
        futures for any of the items, representing them as `null` in the result list.
        
        Canceling this future will attempt to cancel all the component futures.

        Arguments
        - futures: futures to combine

        Returns
        - a future that provides a list of the results of the component futures

        Since
        - 10.0
        """
        ...


    @staticmethod
    def successfulAsList(futures: Iterable["ListenableFuture"["V"]]) -> "ListenableFuture"[list["V"]]:
        """
        Creates a new `ListenableFuture` whose value is a list containing the values of all its
        successful input futures. The list of results is in the same order as the input list, and if
        any of the provided futures fails or is canceled, its corresponding position will contain
        `null` (which is indistinguishable from the future having a successful value of `null`).
        
        The list of results is in the same order as the input list.
        
        This differs from .allAsList(Iterable) in that it's tolerant of failed futures for
        any of the items, representing them as `null` in the result list.
        
        Canceling this future will attempt to cancel all the component futures.

        Arguments
        - futures: futures to combine

        Returns
        - a future that provides a list of the results of the component futures

        Since
        - 10.0
        """
        ...


    @staticmethod
    def inCompletionOrder(futures: Iterable["ListenableFuture"["T"]]) -> "ImmutableList"["ListenableFuture"["T"]]:
        """
        Returns a list of delegate futures that correspond to the futures received in the order that
        they complete. Delegate futures return the same value or throw the same exception as the
        corresponding input future returns/throws.
        
        "In the order that they complete" means, for practical purposes, about what you would
        expect, but there are some subtleties. First, we do guarantee that, if the output future at
        index n is done, the output future at index n-1 is also done. (But as usual with futures, some
        listeners for future n may complete before some for future n-1.) However, it is possible, if
        one input completes with result X and another later with result Y, for Y to come before X in
        the output future list. (Such races are impossible to solve without global synchronization of
        all future completions. And they should have little practical impact.)
        
        Cancelling a delegate future propagates to input futures once all the delegates complete,
        either from cancellation or because an input future has completed. If N futures are passed in,
        and M delegates are cancelled, the remaining M input futures will be cancelled once N - M of
        the input futures complete. If all the delegates are cancelled, all the input futures will be
        too.

        Since
        - 17.0
        """
        ...


    @staticmethod
    def addCallback(future: "ListenableFuture"["V"], callback: "FutureCallback"["V"], executor: "Executor") -> None:
        """
        Registers separate success and failure callbacks to be run when the `Future`'s
        computation is java.util.concurrent.Future.isDone() complete or, if the
        computation is already complete, immediately.
        
        The callback is run on `executor`. There is no guaranteed ordering of execution of
        callbacks, but any callback added through this method is guaranteed to be called once the
        computation is complete.
        
        Exceptions thrown by a `callback` will be propagated up to the executor. Any exception
        thrown during `Executor.execute` (e.g., a `RejectedExecutionException` or an
        exception thrown by MoreExecutors.directExecutor direct execution) will be caught
        and logged.
        
        Example:
        
        ````ListenableFuture<QueryResult> future = ...;
        Executor e = ...
        addCallback(future,
            new FutureCallback<QueryResult>() {
              public void onSuccess(QueryResult result) {
                storeInCache(result);`
              public void onFailure(Throwable t) {
                reportError(t);
              }
            }, e);
        }```
        
        When selecting an executor, note that `directExecutor` is dangerous in some cases. See
        the warnings the MoreExecutors.directExecutor documentation.
        
        For a more general interface to attach a completion listener to a `Future`, see ListenableFuture.addListener addListener.

        Arguments
        - future: The future attach the callback to.
        - callback: The callback to invoke when `future` is completed.
        - executor: The executor to run `callback` when the future completes.

        Since
        - 10.0
        """
        ...


    @staticmethod
    def getDone(future: "Future"["V"]) -> "V":
        """
        Returns the result of the input `Future`, which must have already completed.
        
        The benefits of this method are twofold. First, the name "getDone" suggests to readers that
        the `Future` is already done. Second, if buggy code calls `getDone` on a `Future` that is still pending, the program will throw instead of block. This can be important
        for APIs like .whenAllComplete whenAllComplete(...)`.`FutureCombiner.call(Callable, Executor) call(...), where it is easy to use a new input from
        the `call` implementation but forget to add it to the arguments of `whenAllComplete`.
        
        If you are looking for a method to determine whether a given `Future` is done, use the
        instance method Future.isDone().

        Raises
        - ExecutionException: if the `Future` failed with an exception
        - CancellationException: if the `Future` was cancelled
        - IllegalStateException: if the `Future` is not done

        Since
        - 20.0
        """
        ...


    @staticmethod
    def getChecked(future: "Future"["V"], exceptionClass: type["X"]) -> "V":
        """
        Returns the result of Future.get(), converting most exceptions to a new instance of the
        given checked exception type. This reduces boilerplate for a common use of `Future` in
        which it is unnecessary to programmatically distinguish between exception types or to extract
        other information from the exception instance.
        
        Exceptions from `Future.get` are treated as follows:
        
        
          - Any ExecutionException has its *cause* wrapped in an `X` if the cause
              is a checked exception, an UncheckedExecutionException if the cause is a `RuntimeException`, or an ExecutionError if the cause is an `Error`.
          - Any InterruptedException is wrapped in an `X` (after restoring the
              interrupt).
          - Any CancellationException is propagated untouched, as is any other RuntimeException (though `get` implementations are discouraged from throwing such
              exceptions).
        
        
        The overall principle is to continue to treat every checked exception as a checked
        exception, every unchecked exception as an unchecked exception, and every error as an error. In
        addition, the cause of any `ExecutionException` is wrapped in order to ensure that the
        new stack trace matches that of the current thread.
        
        Instances of `exceptionClass` are created by choosing an arbitrary public constructor
        that accepts zero or more arguments, all of type `String` or `Throwable`
        (preferring constructors with at least one `String`, then preferring constructors with at
        least one `Throwable`) and calling the constructor via reflection. If the exception did
        not already have a cause, one is set by calling Throwable.initCause(Throwable) on it.
        If no such constructor exists, an `IllegalArgumentException` is thrown.

        Raises
        - X: if `get` throws any checked exception except for an `ExecutionException`
            whose cause is not itself a checked exception
        - UncheckedExecutionException: if `get` throws an `ExecutionException` with a
            `RuntimeException` as its cause
        - ExecutionError: if `get` throws an `ExecutionException` with an `Error` as its cause
        - CancellationException: if `get` throws a `CancellationException`
        - IllegalArgumentException: if `exceptionClass` extends `RuntimeException` or
            does not have a suitable constructor

        Since
        - 19.0 (in 10.0 as `get`)
        """
        ...


    @staticmethod
    def getChecked(future: "Future"["V"], exceptionClass: type["X"], timeout: "Duration") -> "V":
        """
        Returns the result of Future.get(long, TimeUnit), converting most exceptions to a new
        instance of the given checked exception type. This reduces boilerplate for a common use of
        `Future` in which it is unnecessary to programmatically distinguish between exception
        types or to extract other information from the exception instance.
        
        Exceptions from `Future.get` are treated as follows:
        
        
          - Any ExecutionException has its *cause* wrapped in an `X` if the cause
              is a checked exception, an UncheckedExecutionException if the cause is a `RuntimeException`, or an ExecutionError if the cause is an `Error`.
          - Any InterruptedException is wrapped in an `X` (after restoring the
              interrupt).
          - Any TimeoutException is wrapped in an `X`.
          - Any CancellationException is propagated untouched, as is any other RuntimeException (though `get` implementations are discouraged from throwing such
              exceptions).
        
        
        The overall principle is to continue to treat every checked exception as a checked
        exception, every unchecked exception as an unchecked exception, and every error as an error. In
        addition, the cause of any `ExecutionException` is wrapped in order to ensure that the
        new stack trace matches that of the current thread.
        
        Instances of `exceptionClass` are created by choosing an arbitrary public constructor
        that accepts zero or more arguments, all of type `String` or `Throwable`
        (preferring constructors with at least one `String`, then preferring constructors with at
        least one `Throwable`) and calling the constructor via reflection. If the exception did
        not already have a cause, one is set by calling Throwable.initCause(Throwable) on it.
        If no such constructor exists, an `IllegalArgumentException` is thrown.

        Raises
        - X: if `get` throws any checked exception except for an `ExecutionException`
            whose cause is not itself a checked exception
        - UncheckedExecutionException: if `get` throws an `ExecutionException` with a
            `RuntimeException` as its cause
        - ExecutionError: if `get` throws an `ExecutionException` with an `Error` as its cause
        - CancellationException: if `get` throws a `CancellationException`
        - IllegalArgumentException: if `exceptionClass` extends `RuntimeException` or
            does not have a suitable constructor

        Since
        - 28.0
        """
        ...


    @staticmethod
    def getChecked(future: "Future"["V"], exceptionClass: type["X"], timeout: int, unit: "TimeUnit") -> "V":
        """
        Returns the result of Future.get(long, TimeUnit), converting most exceptions to a new
        instance of the given checked exception type. This reduces boilerplate for a common use of
        `Future` in which it is unnecessary to programmatically distinguish between exception
        types or to extract other information from the exception instance.
        
        Exceptions from `Future.get` are treated as follows:
        
        
          - Any ExecutionException has its *cause* wrapped in an `X` if the cause
              is a checked exception, an UncheckedExecutionException if the cause is a `RuntimeException`, or an ExecutionError if the cause is an `Error`.
          - Any InterruptedException is wrapped in an `X` (after restoring the
              interrupt).
          - Any TimeoutException is wrapped in an `X`.
          - Any CancellationException is propagated untouched, as is any other RuntimeException (though `get` implementations are discouraged from throwing such
              exceptions).
        
        
        The overall principle is to continue to treat every checked exception as a checked
        exception, every unchecked exception as an unchecked exception, and every error as an error. In
        addition, the cause of any `ExecutionException` is wrapped in order to ensure that the
        new stack trace matches that of the current thread.
        
        Instances of `exceptionClass` are created by choosing an arbitrary public constructor
        that accepts zero or more arguments, all of type `String` or `Throwable`
        (preferring constructors with at least one `String`) and calling the constructor via
        reflection. If the exception did not already have a cause, one is set by calling Throwable.initCause(Throwable) on it. If no such constructor exists, an `IllegalArgumentException` is thrown.

        Raises
        - X: if `get` throws any checked exception except for an `ExecutionException`
            whose cause is not itself a checked exception
        - UncheckedExecutionException: if `get` throws an `ExecutionException` with a
            `RuntimeException` as its cause
        - ExecutionError: if `get` throws an `ExecutionException` with an `Error` as its cause
        - CancellationException: if `get` throws a `CancellationException`
        - IllegalArgumentException: if `exceptionClass` extends `RuntimeException` or
            does not have a suitable constructor

        Since
        - 19.0 (in 10.0 as `get` and with different parameter order)
        """
        ...


    @staticmethod
    def getUnchecked(future: "Future"["V"]) -> "V":
        """
        Returns the result of calling Future.get() uninterruptibly on a task known not to throw
        a checked exception. This makes `Future` more suitable for lightweight, fast-running
        tasks that, barring bugs in the code, will not fail. This gives it exception-handling behavior
        similar to that of `ForkJoinTask.join`.
        
        Exceptions from `Future.get` are treated as follows:
        
        
          - Any ExecutionException has its *cause* wrapped in an UncheckedExecutionException (if the cause is an `Exception`) or ExecutionError (if the cause is an `Error`).
          - Any InterruptedException causes a retry of the `get` call. The interrupt is
              restored before `getUnchecked` returns.
          - Any CancellationException is propagated untouched. So is any other RuntimeException (`get` implementations are discouraged from throwing such
              exceptions).
        
        
        The overall principle is to eliminate all checked exceptions: to loop to avoid `InterruptedException`, to pass through `CancellationException`, and to wrap any exception
        from the underlying computation in an `UncheckedExecutionException` or `ExecutionError`.
        
        For an uninterruptible `get` that preserves other exceptions, see Uninterruptibles.getUninterruptibly(Future).

        Raises
        - UncheckedExecutionException: if `get` throws an `ExecutionException` with an
            `Exception` as its cause
        - ExecutionError: if `get` throws an `ExecutionException` with an `Error` as its cause
        - CancellationException: if `get` throws a `CancellationException`

        Since
        - 10.0
        """
        ...


    class FutureCombiner:
        """
        A helper to create a new `ListenableFuture` whose result is generated from a combination
        of input futures.
        
        See .whenAllComplete and .whenAllSucceed for how to instantiate this class.
        
        Example:
        
        ````final ListenableFuture<Instant> loginDateFuture =
            loginService.findLastLoginDate(username);
        final ListenableFuture<List<String>> recentCommandsFuture =
            recentCommandsService.findRecentCommands(username);
        ListenableFuture<UsageHistory> usageFuture =
            Futures.whenAllSucceed(loginDateFuture, recentCommandsFuture)
                .call(
                    () ->
                        new UsageHistory(
                            username,
                            Futures.getDone(loginDateFuture),
                            Futures.getDone(recentCommandsFuture)),
                    executor);````

        Since
        - 20.0
        """

        def callAsync(self, combiner: "AsyncCallable"["C"], executor: "Executor") -> "ListenableFuture"["C"]:
            """
            Creates the ListenableFuture which will return the result of calling AsyncCallable.call in `combiner` when all futures complete, using the specified `executor`.
            
            If the combiner throws a `CancellationException`, the returned future will be
            cancelled.
            
            If the combiner throws an `ExecutionException`, the cause of the thrown `ExecutionException` will be extracted and returned as the cause of the new `ExecutionException` that gets thrown by the returned combined future.
            
            Canceling this future will attempt to cancel all the component futures.

            Returns
            - a future whose result is based on `combiner` (or based on the input futures
                passed to `whenAllSucceed`, if that is the method you used to create this `FutureCombiner`). Even if you don't care about the value of the future, you should
                typically check whether it failed: See <a
                href="https://errorprone.info/bugpattern/FutureReturnValueIgnored">https://errorprone.info/bugpattern/FutureReturnValueIgnored</a>.
            """
            ...


        def call(self, combiner: "Callable"["C"], executor: "Executor") -> "ListenableFuture"["C"]:
            """
            Creates the ListenableFuture which will return the result of calling Callable.call in `combiner` when all futures complete, using the specified `executor`.
            
            If the combiner throws a `CancellationException`, the returned future will be
            cancelled.
            
            If the combiner throws an `ExecutionException`, the cause of the thrown `ExecutionException` will be extracted and returned as the cause of the new `ExecutionException` that gets thrown by the returned combined future.
            
            Canceling this future will attempt to cancel all the component futures.

            Returns
            - a future whose result is based on `combiner` (or based on the input futures
                passed to `whenAllSucceed`, if that is the method you used to create this `FutureCombiner`). Even if you don't care about the value of the future, you should
                typically check whether it failed: See <a
                href="https://errorprone.info/bugpattern/FutureReturnValueIgnored">https://errorprone.info/bugpattern/FutureReturnValueIgnored</a>.
            """
            ...


        def run(self, combiner: "Runnable", executor: "Executor") -> "ListenableFuture"[Any]:
            """
            Creates the ListenableFuture which will return the result of running `combiner`
            when all Futures complete. `combiner` will run using `executor`.
            
            If the combiner throws a `CancellationException`, the returned future will be
            cancelled.
            
            Canceling this Future will attempt to cancel all the component futures.

            Returns
            - a future whose result is based on `combiner` (or based on the input futures
                passed to `whenAllSucceed`, if that is the method you used to create this `FutureCombiner`). Even though the future never produces a value other than `null`,
                you should typically check whether it failed: See <a
                href="https://errorprone.info/bugpattern/FutureReturnValueIgnored">https://errorprone.info/bugpattern/FutureReturnValueIgnored</a>.

            Since
            - 23.6
            """
            ...
