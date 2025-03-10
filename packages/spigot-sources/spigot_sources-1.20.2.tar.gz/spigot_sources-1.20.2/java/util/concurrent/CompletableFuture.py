"""
Python module generated from Java source file java.util.concurrent.CompletableFuture

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.lang.invoke import MethodHandles
from java.lang.invoke import VarHandle
from java.util import Objects
from java.util.concurrent import *
from java.util.concurrent.locks import LockSupport
from java.util.function import BiConsumer
from java.util.function import BiFunction
from java.util.function import Consumer
from java.util.function import Function
from java.util.function import Supplier
from typing import Any, Callable, Iterable, Tuple


class CompletableFuture(Future, CompletionStage):
    """
    A Future that may be explicitly completed (setting its
    value and status), and may be used as a CompletionStage,
    supporting dependent functions and actions that trigger upon its
    completion.
    
    When two or more threads attempt to
    .complete complete,
    .completeExceptionally completeExceptionally, or
    .cancel cancel
    a CompletableFuture, only one of them succeeds.
    
    In addition to these and related methods for directly
    manipulating status and results, CompletableFuture implements
    interface CompletionStage with the following policies: 
    
    - Actions supplied for dependent completions of
    *non-async* methods may be performed by the thread that
    completes the current CompletableFuture, or by any other caller of
    a completion method.
    
    - All *async* methods without an explicit Executor
    argument are performed using the ForkJoinPool.commonPool()
    (unless it does not support a parallelism level of at least two, in
    which case, a new Thread is created to run each task).  This may be
    overridden for non-static methods in subclasses by defining method
    .defaultExecutor(). To simplify monitoring, debugging,
    and tracking, all generated asynchronous tasks are instances of the
    marker interface AsynchronousCompletionTask.  Operations
    with time-delays can use adapter methods defined in this class, for
    example: `supplyAsync(supplier, delayedExecutor(timeout,
    timeUnit))`.  To support methods with delays and timeouts, this
    class maintains at most one daemon thread for triggering and
    cancelling actions, not for running them.
    
    - All CompletionStage methods are implemented independently of
    other public methods, so the behavior of one method is not impacted
    by overrides of others in subclasses.
    
    - All CompletionStage methods return CompletableFutures.  To
    restrict usages to only those methods defined in interface
    CompletionStage, use method .minimalCompletionStage. Or to
    ensure only that clients do not themselves modify a future, use
    method .copy.
    
    
    CompletableFuture also implements Future with the following
    policies: 
    
    - Since (unlike FutureTask) this class has no direct
    control over the computation that causes it to be completed,
    cancellation is treated as just another form of exceptional
    completion.  Method .cancel cancel has the same effect as
    `completeExceptionally(new CancellationException())`. Method
    .isCompletedExceptionally can be used to determine if a
    CompletableFuture completed in any exceptional fashion.
    
    - In case of exceptional completion with a CompletionException,
    methods .get() and .get(long, TimeUnit) throw an
    ExecutionException with the same cause as held in the
    corresponding CompletionException.  To simplify usage in most
    contexts, this class also defines methods .join() and
    .getNow that instead throw the CompletionException directly
    in these cases.
    
    
    Arguments used to pass a completion result (that is, for
    parameters of type `T`) for methods accepting them may be
    null, but passing a null value for any other parameter will result
    in a NullPointerException being thrown.
    
    Subclasses of this class should normally override the "virtual
    constructor" method .newIncompleteFuture, which establishes
    the concrete type returned by CompletionStage methods. For example,
    here is a class that substitutes a different default Executor and
    disables the `obtrude` methods:
    
    ``` `class MyCompletableFuture<T> extends CompletableFuture<T> {
      static final Executor myExecutor = ...;
      public MyCompletableFuture() {`
      public <U> CompletableFuture<U> newIncompleteFuture() {
        return new MyCompletableFuture<U>(); }
      public Executor defaultExecutor() {
        return myExecutor; }
      public void obtrudeValue(T value) {
        throw new UnsupportedOperationException(); }
      public void obtrudeException(Throwable ex) {
        throw new UnsupportedOperationException(); }
    }}```
    
    Type `<T>`: The result type returned by this future's `join`
    and `get` methods

    Author(s)
    - Doug Lea

    Since
    - 1.8
    """

    def __init__(self):
        """
        Creates a new incomplete CompletableFuture.
        """
        ...


    @staticmethod
    def supplyAsync(supplier: "Supplier"["U"]) -> "CompletableFuture"["U"]:
        """
        Returns a new CompletableFuture that is asynchronously completed
        by a task running in the ForkJoinPool.commonPool() with
        the value obtained by calling the given Supplier.
        
        Type `<U>`: the function's return type

        Arguments
        - supplier: a function returning the value to be used
        to complete the returned CompletableFuture

        Returns
        - the new CompletableFuture
        """
        ...


    @staticmethod
    def supplyAsync(supplier: "Supplier"["U"], executor: "Executor") -> "CompletableFuture"["U"]:
        """
        Returns a new CompletableFuture that is asynchronously completed
        by a task running in the given executor with the value obtained
        by calling the given Supplier.
        
        Type `<U>`: the function's return type

        Arguments
        - supplier: a function returning the value to be used
        to complete the returned CompletableFuture
        - executor: the executor to use for asynchronous execution

        Returns
        - the new CompletableFuture
        """
        ...


    @staticmethod
    def runAsync(runnable: "Runnable") -> "CompletableFuture"["Void"]:
        """
        Returns a new CompletableFuture that is asynchronously completed
        by a task running in the ForkJoinPool.commonPool() after
        it runs the given action.

        Arguments
        - runnable: the action to run before completing the
        returned CompletableFuture

        Returns
        - the new CompletableFuture
        """
        ...


    @staticmethod
    def runAsync(runnable: "Runnable", executor: "Executor") -> "CompletableFuture"["Void"]:
        """
        Returns a new CompletableFuture that is asynchronously completed
        by a task running in the given executor after it runs the given
        action.

        Arguments
        - runnable: the action to run before completing the
        returned CompletableFuture
        - executor: the executor to use for asynchronous execution

        Returns
        - the new CompletableFuture
        """
        ...


    @staticmethod
    def completedFuture(value: "U") -> "CompletableFuture"["U"]:
        """
        Returns a new CompletableFuture that is already completed with
        the given value.
        
        Type `<U>`: the type of the value

        Arguments
        - value: the value

        Returns
        - the completed CompletableFuture
        """
        ...


    def isDone(self) -> bool:
        """
        Returns `True` if completed in any fashion: normally,
        exceptionally, or via cancellation.

        Returns
        - `True` if completed
        """
        ...


    def get(self) -> "T":
        """
        Waits if necessary for this future to complete, and then
        returns its result.

        Returns
        - the result value

        Raises
        - CancellationException: if this future was cancelled
        - ExecutionException: if this future completed exceptionally
        - InterruptedException: if the current thread was interrupted
        while waiting
        """
        ...


    def get(self, timeout: int, unit: "TimeUnit") -> "T":
        """
        Waits if necessary for at most the given time for this future
        to complete, and then returns its result, if available.

        Arguments
        - timeout: the maximum time to wait
        - unit: the time unit of the timeout argument

        Returns
        - the result value

        Raises
        - CancellationException: if this future was cancelled
        - ExecutionException: if this future completed exceptionally
        - InterruptedException: if the current thread was interrupted
        while waiting
        - TimeoutException: if the wait timed out
        """
        ...


    def join(self) -> "T":
        """
        Returns the result value when complete, or throws an
        (unchecked) exception if completed exceptionally. To better
        conform with the use of common functional forms, if a
        computation involved in the completion of this
        CompletableFuture threw an exception, this method throws an
        (unchecked) CompletionException with the underlying
        exception as its cause.

        Returns
        - the result value

        Raises
        - CancellationException: if the computation was cancelled
        - CompletionException: if this future completed
        exceptionally or a completion computation threw an exception
        """
        ...


    def getNow(self, valueIfAbsent: "T") -> "T":
        """
        Returns the result value (or throws any encountered exception)
        if completed, else returns the given valueIfAbsent.

        Arguments
        - valueIfAbsent: the value to return if not completed

        Returns
        - the result value, if completed, else the given valueIfAbsent

        Raises
        - CancellationException: if the computation was cancelled
        - CompletionException: if this future completed
        exceptionally or a completion computation threw an exception
        """
        ...


    def complete(self, value: "T") -> bool:
        """
        If not already completed, sets the value returned by .get() and related methods to the given value.

        Arguments
        - value: the result value

        Returns
        - `True` if this invocation caused this CompletableFuture
        to transition to a completed state, else `False`
        """
        ...


    def completeExceptionally(self, ex: "Throwable") -> bool:
        """
        If not already completed, causes invocations of .get()
        and related methods to throw the given exception.

        Arguments
        - ex: the exception

        Returns
        - `True` if this invocation caused this CompletableFuture
        to transition to a completed state, else `False`
        """
        ...


    def thenApply(self, fn: "Function"["T", "U"]) -> "CompletableFuture"["U"]:
        ...


    def thenApplyAsync(self, fn: "Function"["T", "U"]) -> "CompletableFuture"["U"]:
        ...


    def thenApplyAsync(self, fn: "Function"["T", "U"], executor: "Executor") -> "CompletableFuture"["U"]:
        ...


    def thenAccept(self, action: "Consumer"["T"]) -> "CompletableFuture"["Void"]:
        ...


    def thenAcceptAsync(self, action: "Consumer"["T"]) -> "CompletableFuture"["Void"]:
        ...


    def thenAcceptAsync(self, action: "Consumer"["T"], executor: "Executor") -> "CompletableFuture"["Void"]:
        ...


    def thenRun(self, action: "Runnable") -> "CompletableFuture"["Void"]:
        ...


    def thenRunAsync(self, action: "Runnable") -> "CompletableFuture"["Void"]:
        ...


    def thenRunAsync(self, action: "Runnable", executor: "Executor") -> "CompletableFuture"["Void"]:
        ...


    def thenCombine(self, other: "CompletionStage"["U"], fn: "BiFunction"["T", "U", "V"]) -> "CompletableFuture"["V"]:
        ...


    def thenCombineAsync(self, other: "CompletionStage"["U"], fn: "BiFunction"["T", "U", "V"]) -> "CompletableFuture"["V"]:
        ...


    def thenCombineAsync(self, other: "CompletionStage"["U"], fn: "BiFunction"["T", "U", "V"], executor: "Executor") -> "CompletableFuture"["V"]:
        ...


    def thenAcceptBoth(self, other: "CompletionStage"["U"], action: "BiConsumer"["T", "U"]) -> "CompletableFuture"["Void"]:
        ...


    def thenAcceptBothAsync(self, other: "CompletionStage"["U"], action: "BiConsumer"["T", "U"]) -> "CompletableFuture"["Void"]:
        ...


    def thenAcceptBothAsync(self, other: "CompletionStage"["U"], action: "BiConsumer"["T", "U"], executor: "Executor") -> "CompletableFuture"["Void"]:
        ...


    def runAfterBoth(self, other: "CompletionStage"[Any], action: "Runnable") -> "CompletableFuture"["Void"]:
        ...


    def runAfterBothAsync(self, other: "CompletionStage"[Any], action: "Runnable") -> "CompletableFuture"["Void"]:
        ...


    def runAfterBothAsync(self, other: "CompletionStage"[Any], action: "Runnable", executor: "Executor") -> "CompletableFuture"["Void"]:
        ...


    def applyToEither(self, other: "CompletionStage"["T"], fn: "Function"["T", "U"]) -> "CompletableFuture"["U"]:
        ...


    def applyToEitherAsync(self, other: "CompletionStage"["T"], fn: "Function"["T", "U"]) -> "CompletableFuture"["U"]:
        ...


    def applyToEitherAsync(self, other: "CompletionStage"["T"], fn: "Function"["T", "U"], executor: "Executor") -> "CompletableFuture"["U"]:
        ...


    def acceptEither(self, other: "CompletionStage"["T"], action: "Consumer"["T"]) -> "CompletableFuture"["Void"]:
        ...


    def acceptEitherAsync(self, other: "CompletionStage"["T"], action: "Consumer"["T"]) -> "CompletableFuture"["Void"]:
        ...


    def acceptEitherAsync(self, other: "CompletionStage"["T"], action: "Consumer"["T"], executor: "Executor") -> "CompletableFuture"["Void"]:
        ...


    def runAfterEither(self, other: "CompletionStage"[Any], action: "Runnable") -> "CompletableFuture"["Void"]:
        ...


    def runAfterEitherAsync(self, other: "CompletionStage"[Any], action: "Runnable") -> "CompletableFuture"["Void"]:
        ...


    def runAfterEitherAsync(self, other: "CompletionStage"[Any], action: "Runnable", executor: "Executor") -> "CompletableFuture"["Void"]:
        ...


    def thenCompose(self, fn: "Function"["T", "CompletionStage"["U"]]) -> "CompletableFuture"["U"]:
        ...


    def thenComposeAsync(self, fn: "Function"["T", "CompletionStage"["U"]]) -> "CompletableFuture"["U"]:
        ...


    def thenComposeAsync(self, fn: "Function"["T", "CompletionStage"["U"]], executor: "Executor") -> "CompletableFuture"["U"]:
        ...


    def whenComplete(self, action: "BiConsumer"["T", "Throwable"]) -> "CompletableFuture"["T"]:
        ...


    def whenCompleteAsync(self, action: "BiConsumer"["T", "Throwable"]) -> "CompletableFuture"["T"]:
        ...


    def whenCompleteAsync(self, action: "BiConsumer"["T", "Throwable"], executor: "Executor") -> "CompletableFuture"["T"]:
        ...


    def handle(self, fn: "BiFunction"["T", "Throwable", "U"]) -> "CompletableFuture"["U"]:
        ...


    def handleAsync(self, fn: "BiFunction"["T", "Throwable", "U"]) -> "CompletableFuture"["U"]:
        ...


    def handleAsync(self, fn: "BiFunction"["T", "Throwable", "U"], executor: "Executor") -> "CompletableFuture"["U"]:
        ...


    def toCompletableFuture(self) -> "CompletableFuture"["T"]:
        """
        Returns this CompletableFuture.

        Returns
        - this CompletableFuture
        """
        ...


    def exceptionally(self, fn: "Function"["Throwable", "T"]) -> "CompletableFuture"["T"]:
        ...


    def exceptionallyAsync(self, fn: "Function"["Throwable", "T"]) -> "CompletableFuture"["T"]:
        ...


    def exceptionallyAsync(self, fn: "Function"["Throwable", "T"], executor: "Executor") -> "CompletableFuture"["T"]:
        ...


    def exceptionallyCompose(self, fn: "Function"["Throwable", "CompletionStage"["T"]]) -> "CompletableFuture"["T"]:
        ...


    def exceptionallyComposeAsync(self, fn: "Function"["Throwable", "CompletionStage"["T"]]) -> "CompletableFuture"["T"]:
        ...


    def exceptionallyComposeAsync(self, fn: "Function"["Throwable", "CompletionStage"["T"]], executor: "Executor") -> "CompletableFuture"["T"]:
        ...


    @staticmethod
    def allOf(*cfs: Tuple["CompletableFuture"[Any], ...]) -> "CompletableFuture"["Void"]:
        """
        Returns a new CompletableFuture that is completed when all of
        the given CompletableFutures complete.  If any of the given
        CompletableFutures complete exceptionally, then the returned
        CompletableFuture also does so, with a CompletionException
        holding this exception as its cause.  Otherwise, the results,
        if any, of the given CompletableFutures are not reflected in
        the returned CompletableFuture, but may be obtained by
        inspecting them individually. If no CompletableFutures are
        provided, returns a CompletableFuture completed with the value
        `null`.
        
        Among the applications of this method is to await completion
        of a set of independent CompletableFutures before continuing a
        program, as in: `CompletableFuture.allOf(c1, c2,
        c3).join();`.

        Arguments
        - cfs: the CompletableFutures

        Returns
        - a new CompletableFuture that is completed when all of the
        given CompletableFutures complete

        Raises
        - NullPointerException: if the array or any of its elements are
        `null`
        """
        ...


    @staticmethod
    def anyOf(*cfs: Tuple["CompletableFuture"[Any], ...]) -> "CompletableFuture"["Object"]:
        """
        Returns a new CompletableFuture that is completed when any of
        the given CompletableFutures complete, with the same result.
        Otherwise, if it completed exceptionally, the returned
        CompletableFuture also does so, with a CompletionException
        holding this exception as its cause.  If no CompletableFutures
        are provided, returns an incomplete CompletableFuture.

        Arguments
        - cfs: the CompletableFutures

        Returns
        - a new CompletableFuture that is completed with the
        result or exception of any of the given CompletableFutures when
        one completes

        Raises
        - NullPointerException: if the array or any of its elements are
        `null`
        """
        ...


    def cancel(self, mayInterruptIfRunning: bool) -> bool:
        """
        If not already completed, completes this CompletableFuture with
        a CancellationException. Dependent CompletableFutures
        that have not already completed will also complete
        exceptionally, with a CompletionException caused by
        this `CancellationException`.

        Arguments
        - mayInterruptIfRunning: this value has no effect in this
        implementation because interrupts are not used to control
        processing.

        Returns
        - `True` if this task is now cancelled
        """
        ...


    def isCancelled(self) -> bool:
        """
        Returns `True` if this CompletableFuture was cancelled
        before it completed normally.

        Returns
        - `True` if this CompletableFuture was cancelled
        before it completed normally
        """
        ...


    def isCompletedExceptionally(self) -> bool:
        """
        Returns `True` if this CompletableFuture completed
        exceptionally, in any way. Possible causes include
        cancellation, explicit invocation of `completeExceptionally`, and abrupt termination of a
        CompletionStage action.

        Returns
        - `True` if this CompletableFuture completed
        exceptionally
        """
        ...


    def obtrudeValue(self, value: "T") -> None:
        """
        Forcibly sets or resets the value subsequently returned by
        method .get() and related methods, whether or not
        already completed. This method is designed for use only in
        error recovery actions, and even in such situations may result
        in ongoing dependent completions using established versus
        overwritten outcomes.

        Arguments
        - value: the completion value
        """
        ...


    def obtrudeException(self, ex: "Throwable") -> None:
        """
        Forcibly causes subsequent invocations of method .get()
        and related methods to throw the given exception, whether or
        not already completed. This method is designed for use only in
        error recovery actions, and even in such situations may result
        in ongoing dependent completions using established versus
        overwritten outcomes.

        Arguments
        - ex: the exception

        Raises
        - NullPointerException: if the exception is null
        """
        ...


    def getNumberOfDependents(self) -> int:
        """
        Returns the estimated number of CompletableFutures whose
        completions are awaiting completion of this CompletableFuture.
        This method is designed for use in monitoring system state, not
        for synchronization control.

        Returns
        - the number of dependent CompletableFutures
        """
        ...


    def toString(self) -> str:
        """
        Returns a string identifying this CompletableFuture, as well as
        its completion state.  The state, in brackets, contains the
        String `"Completed Normally"` or the String `"Completed Exceptionally"`, or the String `"Not
        completed"` followed by the number of CompletableFutures
        dependent upon its completion, if any.

        Returns
        - a string identifying this CompletableFuture, as well as its state
        """
        ...


    def newIncompleteFuture(self) -> "CompletableFuture"["U"]:
        """
        Returns a new incomplete CompletableFuture of the type to be
        returned by a CompletionStage method. Subclasses should
        normally override this method to return an instance of the same
        class as this CompletableFuture. The default implementation
        returns an instance of class CompletableFuture.
        
        Type `<U>`: the type of the value

        Returns
        - a new CompletableFuture

        Since
        - 9
        """
        ...


    def defaultExecutor(self) -> "Executor":
        """
        Returns the default Executor used for async methods that do not
        specify an Executor. This class uses the ForkJoinPool.commonPool() if it supports more than one
        parallel thread, or else an Executor using one thread per async
        task.  This method may be overridden in subclasses to return
        an Executor that provides at least one independent thread.

        Returns
        - the executor

        Since
        - 9
        """
        ...


    def copy(self) -> "CompletableFuture"["T"]:
        """
        Returns a new CompletableFuture that is completed normally with
        the same value as this CompletableFuture when it completes
        normally. If this CompletableFuture completes exceptionally,
        then the returned CompletableFuture completes exceptionally
        with a CompletionException with this exception as cause. The
        behavior is equivalent to `thenApply(x -> x)`. This
        method may be useful as a form of "defensive copying", to
        prevent clients from completing, while still being able to
        arrange dependent actions.

        Returns
        - the new CompletableFuture

        Since
        - 9
        """
        ...


    def minimalCompletionStage(self) -> "CompletionStage"["T"]:
        """
        Returns a new CompletionStage that is completed normally with
        the same value as this CompletableFuture when it completes
        normally, and cannot be independently completed or otherwise
        used in ways not defined by the methods of interface CompletionStage.  If this CompletableFuture completes
        exceptionally, then the returned CompletionStage completes
        exceptionally with a CompletionException with this exception as
        cause.
        
        Unless overridden by a subclass, a new non-minimal
        CompletableFuture with all methods available can be obtained from
        a minimal CompletionStage via .toCompletableFuture().
        For example, completion of a minimal stage can be awaited by
        
        ``` `minimalStage.toCompletableFuture().join();````

        Returns
        - the new CompletionStage

        Since
        - 9
        """
        ...


    def completeAsync(self, supplier: "Supplier"["T"], executor: "Executor") -> "CompletableFuture"["T"]:
        """
        Completes this CompletableFuture with the result of
        the given Supplier function invoked from an asynchronous
        task using the given executor.

        Arguments
        - supplier: a function returning the value to be used
        to complete this CompletableFuture
        - executor: the executor to use for asynchronous execution

        Returns
        - this CompletableFuture

        Since
        - 9
        """
        ...


    def completeAsync(self, supplier: "Supplier"["T"]) -> "CompletableFuture"["T"]:
        """
        Completes this CompletableFuture with the result of the given
        Supplier function invoked from an asynchronous task using the
        default executor.

        Arguments
        - supplier: a function returning the value to be used
        to complete this CompletableFuture

        Returns
        - this CompletableFuture

        Since
        - 9
        """
        ...


    def orTimeout(self, timeout: int, unit: "TimeUnit") -> "CompletableFuture"["T"]:
        """
        Exceptionally completes this CompletableFuture with
        a TimeoutException if not otherwise completed
        before the given timeout.

        Arguments
        - timeout: how long to wait before completing exceptionally
               with a TimeoutException, in units of `unit`
        - unit: a `TimeUnit` determining how to interpret the
               `timeout` parameter

        Returns
        - this CompletableFuture

        Since
        - 9
        """
        ...


    def completeOnTimeout(self, value: "T", timeout: int, unit: "TimeUnit") -> "CompletableFuture"["T"]:
        """
        Completes this CompletableFuture with the given value if not
        otherwise completed before the given timeout.

        Arguments
        - value: the value to use upon timeout
        - timeout: how long to wait before completing normally
               with the given value, in units of `unit`
        - unit: a `TimeUnit` determining how to interpret the
               `timeout` parameter

        Returns
        - this CompletableFuture

        Since
        - 9
        """
        ...


    @staticmethod
    def delayedExecutor(delay: int, unit: "TimeUnit", executor: "Executor") -> "Executor":
        """
        Returns a new Executor that submits a task to the given base
        executor after the given delay (or no delay if non-positive).
        Each delay commences upon invocation of the returned executor's
        `execute` method.

        Arguments
        - delay: how long to delay, in units of `unit`
        - unit: a `TimeUnit` determining how to interpret the
               `delay` parameter
        - executor: the base executor

        Returns
        - the new delayed executor

        Since
        - 9
        """
        ...


    @staticmethod
    def delayedExecutor(delay: int, unit: "TimeUnit") -> "Executor":
        """
        Returns a new Executor that submits a task to the default
        executor after the given delay (or no delay if non-positive).
        Each delay commences upon invocation of the returned executor's
        `execute` method.

        Arguments
        - delay: how long to delay, in units of `unit`
        - unit: a `TimeUnit` determining how to interpret the
               `delay` parameter

        Returns
        - the new delayed executor

        Since
        - 9
        """
        ...


    @staticmethod
    def completedStage(value: "U") -> "CompletionStage"["U"]:
        """
        Returns a new CompletionStage that is already completed with
        the given value and supports only those methods in
        interface CompletionStage.
        
        Type `<U>`: the type of the value

        Arguments
        - value: the value

        Returns
        - the completed CompletionStage

        Since
        - 9
        """
        ...


    @staticmethod
    def failedFuture(ex: "Throwable") -> "CompletableFuture"["U"]:
        """
        Returns a new CompletableFuture that is already completed
        exceptionally with the given exception.
        
        Type `<U>`: the type of the value

        Arguments
        - ex: the exception

        Returns
        - the exceptionally completed CompletableFuture

        Since
        - 9
        """
        ...


    @staticmethod
    def failedStage(ex: "Throwable") -> "CompletionStage"["U"]:
        """
        Returns a new CompletionStage that is already completed
        exceptionally with the given exception and supports only those
        methods in interface CompletionStage.
        
        Type `<U>`: the type of the value

        Arguments
        - ex: the exception

        Returns
        - the exceptionally completed CompletionStage

        Since
        - 9
        """
        ...


    class AsynchronousCompletionTask:
        """
        A marker interface identifying asynchronous tasks produced by
        `async` methods. This may be useful for monitoring,
        debugging, and tracking asynchronous activities.

        Since
        - 1.8
        """


