"""
Python module generated from Java source file com.google.common.util.concurrent.FluentFuture

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import J2ktIncompatible
from com.google.common.base import Function
from com.google.common.util.concurrent import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from com.google.errorprone.annotations import DoNotMock
from java.time import Duration
from java.util.concurrent import ExecutionException
from java.util.concurrent import Executor
from java.util.concurrent import ScheduledExecutorService
from java.util.concurrent import TimeUnit
from java.util.concurrent import TimeoutException
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class FluentFuture(GwtFluentFutureCatchingSpecialization):
    """
    A ListenableFuture that supports fluent chains of operations. For example:
    
    ````ListenableFuture<Boolean> adminIsLoggedIn =
        FluentFuture.from(usersDatabase.getAdminUser())
            .transform(User::getId, directExecutor())
            .transform(ActivityService::isLoggedIn, threadPool)
            .catching(RpcException.class, e -> False, directExecutor());````
    
    <h3>Alternatives</h3>
    
    <h4>Frameworks</h4>
    
    When chaining together a graph of asynchronous operations, you will often find it easier to
    use a framework. Frameworks automate the process, often adding features like monitoring,
    debugging, and cancellation. Examples of frameworks include:
    
    
      - <a href="https://dagger.dev/producers.html">Dagger Producers</a>
    
    
    <h4>java.util.concurrent.CompletableFuture / java.util.concurrent.CompletionStage
    </h4>
    
    Users of `CompletableFuture` will likely want to continue using `CompletableFuture`. `FluentFuture` is targeted at people who use `ListenableFuture`,
    who can't use Java 8, or who want an API more focused than `CompletableFuture`. (If you
    need to adapt between `CompletableFuture` and `ListenableFuture`, consider <a
    href="https://github.com/lukas-krecan/future-converter">Future Converter</a>.)
    
    <h3>Extension</h3>
    
    If you want a class like `FluentFuture` but with extra methods, we recommend declaring your
    own subclass of ListenableFuture, complete with a method like .from to adapt an
    existing `ListenableFuture`, implemented atop a ForwardingListenableFuture that
    forwards to that future and adds the desired methods.

    Since
    - 23.0
    """

    @staticmethod
    def from(future: "ListenableFuture"["V"]) -> "FluentFuture"["V"]:
        """
        Converts the given `ListenableFuture` to an equivalent `FluentFuture`.
        
        If the given `ListenableFuture` is already a `FluentFuture`, it is returned
        directly. If not, it is wrapped in a `FluentFuture` that delegates all calls to the
        original `ListenableFuture`.
        """
        ...


    @staticmethod
    def from(future: "FluentFuture"["V"]) -> "FluentFuture"["V"]:
        """
        Simply returns its argument.

        Since
        - 28.0

        Deprecated
        - no need to use this
        """
        ...


    def catching(self, exceptionType: type["X"], fallback: "Function"["X", "V"], executor: "Executor") -> "FluentFuture"["V"]:
        """
        Returns a `Future` whose result is taken from this `Future` or, if this `Future` fails with the given `exceptionType`, from the result provided by the `fallback`. Function.apply is not invoked until the primary input has failed, so if the
        primary input succeeds, it is never invoked. If, during the invocation of `fallback`, an
        exception is thrown, this exception is used as the result of the output `Future`.
        
        Usage example:
        
        ````// Falling back to a zero counter in case an exception happens when processing the RPC to fetch
        // counters.
        ListenableFuture<Integer> faultTolerantFuture =
            fetchCounters().catching(FetchException.class, x -> 0, directExecutor());````
        
        When selecting an executor, note that `directExecutor` is dangerous in some cases. See
        the discussion in the .addListener documentation. All its warnings about heavyweight
        listeners are also applicable to heavyweight functions passed to this method.
        
        This method is similar to java.util.concurrent.CompletableFuture.exceptionally. It
        can also serve some of the use cases of java.util.concurrent.CompletableFuture.handle
        and java.util.concurrent.CompletableFuture.handleAsync when used along with .transform.

        Arguments
        - exceptionType: the exception type that triggers use of `fallback`. The exception
            type is matched against the input's exception. "The input's exception" means the cause of
            the ExecutionException thrown by `input.get()` or, if `get()` throws a
            different kind of exception, that exception itself. To avoid hiding bugs and other
            unrecoverable errors, callers should prefer more specific types, avoiding `Throwable.class` in particular.
        - fallback: the Function to be called if the input fails with the expected
            exception type. The function's argument is the input's exception. "The input's exception"
            means the cause of the ExecutionException thrown by `this.get()` or, if
            `get()` throws a different kind of exception, that exception itself.
        - executor: the executor that runs `fallback` if the input fails
        """
        ...


    def catchingAsync(self, exceptionType: type["X"], fallback: "AsyncFunction"["X", "V"], executor: "Executor") -> "FluentFuture"["V"]:
        """
        Returns a `Future` whose result is taken from this `Future` or, if this `Future` fails with the given `exceptionType`, from the result provided by the `fallback`. AsyncFunction.apply is not invoked until the primary input has failed, so if
        the primary input succeeds, it is never invoked. If, during the invocation of `fallback`,
        an exception is thrown, this exception is used as the result of the output `Future`.
        
        Usage examples:
        
        ````// Falling back to a zero counter in case an exception happens when processing the RPC to fetch
        // counters.
        ListenableFuture<Integer> faultTolerantFuture =
            fetchCounters().catchingAsync(
                FetchException.class, x -> immediateFuture(0), directExecutor());````
        
        The fallback can also choose to propagate the original exception when desired:
        
        ````// Falling back to a zero counter only in case the exception was a
        // TimeoutException.
        ListenableFuture<Integer> faultTolerantFuture =
            fetchCounters().catchingAsync(
                FetchException.class,
                e -> {
                  if (omitDataOnFetchFailure) {
                    return immediateFuture(0);`
                  throw e;
                },
                directExecutor());
        }```
        
        When selecting an executor, note that `directExecutor` is dangerous in some cases. See
        the discussion in the .addListener documentation. All its warnings about heavyweight
        listeners are also applicable to heavyweight functions passed to this method. (Specifically,
        `directExecutor` functions should avoid heavyweight operations inside `AsyncFunction.apply`. Any heavyweight operations should occur in other threads responsible for
        completing the returned `Future`.)
        
        This method is similar to java.util.concurrent.CompletableFuture.exceptionally. It
        can also serve some of the use cases of java.util.concurrent.CompletableFuture.handle
        and java.util.concurrent.CompletableFuture.handleAsync when used along with .transform.

        Arguments
        - exceptionType: the exception type that triggers use of `fallback`. The exception
            type is matched against the input's exception. "The input's exception" means the cause of
            the ExecutionException thrown by `this.get()` or, if `get()` throws a
            different kind of exception, that exception itself. To avoid hiding bugs and other
            unrecoverable errors, callers should prefer more specific types, avoiding `Throwable.class` in particular.
        - fallback: the AsyncFunction to be called if the input fails with the expected
            exception type. The function's argument is the input's exception. "The input's exception"
            means the cause of the ExecutionException thrown by `input.get()` or, if
            `get()` throws a different kind of exception, that exception itself.
        - executor: the executor that runs `fallback` if the input fails
        """
        ...


    def withTimeout(self, timeout: "Duration", scheduledExecutor: "ScheduledExecutorService") -> "FluentFuture"["V"]:
        """
        Returns a future that delegates to this future but will finish early (via a TimeoutException wrapped in an ExecutionException) if the specified timeout expires.
        If the timeout expires, not only will the output future finish, but also the input future
        (`this`) will be cancelled and interrupted.

        Arguments
        - timeout: when to time out the future
        - scheduledExecutor: The executor service to enforce the timeout.

        Since
        - 28.0
        """
        ...


    def withTimeout(self, timeout: int, unit: "TimeUnit", scheduledExecutor: "ScheduledExecutorService") -> "FluentFuture"["V"]:
        """
        Returns a future that delegates to this future but will finish early (via a TimeoutException wrapped in an ExecutionException) if the specified timeout expires.
        If the timeout expires, not only will the output future finish, but also the input future
        (`this`) will be cancelled and interrupted.

        Arguments
        - timeout: when to time out the future
        - unit: the time unit of the time parameter
        - scheduledExecutor: The executor service to enforce the timeout.
        """
        ...


    def transformAsync(self, function: "AsyncFunction"["V", "T"], executor: "Executor") -> "FluentFuture"["T"]:
        """
        Returns a new `Future` whose result is asynchronously derived from the result of this
        `Future`. If the input `Future` fails, the returned `Future` fails with the
        same exception (and the function is not invoked).
        
        More precisely, the returned `Future` takes its result from a `Future` produced
        by applying the given `AsyncFunction` to the result of the original `Future`.
        Example usage:
        
        ````FluentFuture<RowKey> rowKeyFuture = FluentFuture.from(indexService.lookUp(query));
        ListenableFuture<QueryResult> queryFuture =
            rowKeyFuture.transformAsync(dataService::readFuture, executor);````
        
        When selecting an executor, note that `directExecutor` is dangerous in some cases. See
        the discussion in the .addListener documentation. All its warnings about heavyweight
        listeners are also applicable to heavyweight functions passed to this method. (Specifically,
        `directExecutor` functions should avoid heavyweight operations inside `AsyncFunction.apply`. Any heavyweight operations should occur in other threads responsible for
        completing the returned `Future`.)
        
        The returned `Future` attempts to keep its cancellation state in sync with that of the
        input future and that of the future returned by the chain function. That is, if the returned
        `Future` is cancelled, it will attempt to cancel the other two, and if either of the
        other two is cancelled, the returned `Future` will receive a callback in which it will
        attempt to cancel itself.
        
        This method is similar to java.util.concurrent.CompletableFuture.thenCompose and
        java.util.concurrent.CompletableFuture.thenComposeAsync. It can also serve some of the
        use cases of java.util.concurrent.CompletableFuture.handle and java.util.concurrent.CompletableFuture.handleAsync when used along with .catching.

        Arguments
        - function: A function to transform the result of this future to the result of the output
            future
        - executor: Executor to run the function in.

        Returns
        - A future that holds result of the function (if the input succeeded) or the original
            input's failure (if not)
        """
        ...


    def transform(self, function: "Function"["V", "T"], executor: "Executor") -> "FluentFuture"["T"]:
        """
        Returns a new `Future` whose result is derived from the result of this `Future`. If
        this input `Future` fails, the returned `Future` fails with the same exception (and
        the function is not invoked). Example usage:
        
        ````ListenableFuture<List<Row>> rowsFuture =
            queryFuture.transform(QueryResult::getRows, executor);````
        
        When selecting an executor, note that `directExecutor` is dangerous in some cases. See
        the discussion in the .addListener documentation. All its warnings about heavyweight
        listeners are also applicable to heavyweight functions passed to this method.
        
        The returned `Future` attempts to keep its cancellation state in sync with that of the
        input future. That is, if the returned `Future` is cancelled, it will attempt to cancel
        the input, and if the input is cancelled, the returned `Future` will receive a callback
        in which it will attempt to cancel itself.
        
        An example use of this method is to convert a serializable object returned from an RPC into
        a POJO.
        
        This method is similar to java.util.concurrent.CompletableFuture.thenApply and
        java.util.concurrent.CompletableFuture.thenApplyAsync. It can also serve some of the
        use cases of java.util.concurrent.CompletableFuture.handle and java.util.concurrent.CompletableFuture.handleAsync when used along with .catching.

        Arguments
        - function: A Function to transform the results of this future to the results of the
            returned future.
        - executor: Executor to run the function in.

        Returns
        - A future that holds result of the transformation.
        """
        ...


    def addCallback(self, callback: "FutureCallback"["V"], executor: "Executor") -> None:
        """
        Registers separate success and failure callbacks to be run when this `Future`'s
        computation is java.util.concurrent.Future.isDone() complete or, if the
        computation is already complete, immediately.
        
        The callback is run on `executor`. There is no guaranteed ordering of execution of
        callbacks, but any callback added through this method is guaranteed to be called once the
        computation is complete.
        
        Example:
        
        ````future.addCallback(
            new FutureCallback<QueryResult>() {
              public void onSuccess(QueryResult result) {
                storeInCache(result);`
              public void onFailure(Throwable t) {
                reportError(t);
              }
            }, executor);
        }```
        
        When selecting an executor, note that `directExecutor` is dangerous in some cases. See
        the discussion in the .addListener documentation. All its warnings about heavyweight
        listeners are also applicable to heavyweight callbacks passed to this method.
        
        For a more general interface to attach a completion listener, see .addListener.
        
        This method is similar to java.util.concurrent.CompletableFuture.whenComplete and
        java.util.concurrent.CompletableFuture.whenCompleteAsync. It also serves the use case
        of java.util.concurrent.CompletableFuture.thenAccept and java.util.concurrent.CompletableFuture.thenAcceptAsync.

        Arguments
        - callback: The callback to invoke when this `Future` is completed.
        - executor: The executor to run `callback` when the future completes.
        """
        ...
