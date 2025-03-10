"""
Python module generated from Java source file com.google.common.util.concurrent.MoreExecutors

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import J2ktIncompatible
from com.google.common.annotations import VisibleForTesting
from com.google.common.base import Supplier
from com.google.common.base import Throwables
from com.google.common.collect import Lists
from com.google.common.collect import Queues
from com.google.common.util.concurrent import *
from com.google.common.util.concurrent.ForwardingListenableFuture import SimpleForwardingListenableFuture
from com.google.errorprone.annotations import CanIgnoreReturnValue
from com.google.errorprone.annotations.concurrent import GuardedBy
from java.lang.reflect import InvocationTargetException
from java.time import Duration
from java.util import Collections
from java.util import Iterator
from java.util.concurrent import BlockingQueue
from java.util.concurrent import Callable
from java.util.concurrent import Delayed
from java.util.concurrent import ExecutionException
from java.util.concurrent import Executor
from java.util.concurrent import ExecutorService
from java.util.concurrent import Executors
from java.util.concurrent import Future
from java.util.concurrent import RejectedExecutionException
from java.util.concurrent import ScheduledExecutorService
from java.util.concurrent import ScheduledFuture
from java.util.concurrent import ScheduledThreadPoolExecutor
from java.util.concurrent import ThreadFactory
from java.util.concurrent import ThreadPoolExecutor
from java.util.concurrent import TimeUnit
from java.util.concurrent import TimeoutException
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class MoreExecutors:
    """
    Factory and utility methods for java.util.concurrent.Executor, ExecutorService,
    and java.util.concurrent.ThreadFactory.

    Author(s)
    - Justin Mahoney

    Since
    - 3.0
    """

    @staticmethod
    def getExitingExecutorService(executor: "ThreadPoolExecutor", terminationTimeout: "Duration") -> "ExecutorService":
        """
        Converts the given ThreadPoolExecutor into an ExecutorService that exits when the application
        is complete. It does so by using daemon threads and adding a shutdown hook to wait for their
        completion.
        
        This is mainly for fixed thread pools. See Executors.newFixedThreadPool(int).

        Arguments
        - executor: the executor to modify to make sure it exits when the application is finished
        - terminationTimeout: how long to wait for the executor to finish before terminating the
            JVM

        Returns
        - an unmodifiable version of the input which will not hang the JVM

        Since
        - 28.0
        """
        ...


    @staticmethod
    def getExitingExecutorService(executor: "ThreadPoolExecutor", terminationTimeout: int, timeUnit: "TimeUnit") -> "ExecutorService":
        """
        Converts the given ThreadPoolExecutor into an ExecutorService that exits when the application
        is complete. It does so by using daemon threads and adding a shutdown hook to wait for their
        completion.
        
        This is mainly for fixed thread pools. See Executors.newFixedThreadPool(int).

        Arguments
        - executor: the executor to modify to make sure it exits when the application is finished
        - terminationTimeout: how long to wait for the executor to finish before terminating the
            JVM
        - timeUnit: unit of time for the time parameter

        Returns
        - an unmodifiable version of the input which will not hang the JVM
        """
        ...


    @staticmethod
    def getExitingExecutorService(executor: "ThreadPoolExecutor") -> "ExecutorService":
        """
        Converts the given ThreadPoolExecutor into an ExecutorService that exits when the application
        is complete. It does so by using daemon threads and adding a shutdown hook to wait for their
        completion.
        
        This method waits 120 seconds before continuing with JVM termination, even if the executor
        has not finished its work.
        
        This is mainly for fixed thread pools. See Executors.newFixedThreadPool(int).

        Arguments
        - executor: the executor to modify to make sure it exits when the application is finished

        Returns
        - an unmodifiable version of the input which will not hang the JVM
        """
        ...


    @staticmethod
    def getExitingScheduledExecutorService(executor: "ScheduledThreadPoolExecutor", terminationTimeout: "Duration") -> "ScheduledExecutorService":
        """
        Converts the given ScheduledThreadPoolExecutor into a ScheduledExecutorService that exits when
        the application is complete. It does so by using daemon threads and adding a shutdown hook to
        wait for their completion.
        
        This is mainly for fixed thread pools. See Executors.newScheduledThreadPool(int).

        Arguments
        - executor: the executor to modify to make sure it exits when the application is finished
        - terminationTimeout: how long to wait for the executor to finish before terminating the
            JVM

        Returns
        - an unmodifiable version of the input which will not hang the JVM

        Since
        - 28.0
        """
        ...


    @staticmethod
    def getExitingScheduledExecutorService(executor: "ScheduledThreadPoolExecutor", terminationTimeout: int, timeUnit: "TimeUnit") -> "ScheduledExecutorService":
        """
        Converts the given ScheduledThreadPoolExecutor into a ScheduledExecutorService that exits when
        the application is complete. It does so by using daemon threads and adding a shutdown hook to
        wait for their completion.
        
        This is mainly for fixed thread pools. See Executors.newScheduledThreadPool(int).

        Arguments
        - executor: the executor to modify to make sure it exits when the application is finished
        - terminationTimeout: how long to wait for the executor to finish before terminating the
            JVM
        - timeUnit: unit of time for the time parameter

        Returns
        - an unmodifiable version of the input which will not hang the JVM
        """
        ...


    @staticmethod
    def getExitingScheduledExecutorService(executor: "ScheduledThreadPoolExecutor") -> "ScheduledExecutorService":
        """
        Converts the given ScheduledThreadPoolExecutor into a ScheduledExecutorService that exits when
        the application is complete. It does so by using daemon threads and adding a shutdown hook to
        wait for their completion.
        
        This method waits 120 seconds before continuing with JVM termination, even if the executor
        has not finished its work.
        
        This is mainly for fixed thread pools. See Executors.newScheduledThreadPool(int).

        Arguments
        - executor: the executor to modify to make sure it exits when the application is finished

        Returns
        - an unmodifiable version of the input which will not hang the JVM
        """
        ...


    @staticmethod
    def addDelayedShutdownHook(service: "ExecutorService", terminationTimeout: "Duration") -> None:
        """
        Add a shutdown hook to wait for thread completion in the given ExecutorService service.
        This is useful if the given service uses daemon threads, and we want to keep the JVM from
        exiting immediately on shutdown, instead giving these daemon threads a chance to terminate
        normally.

        Arguments
        - service: ExecutorService which uses daemon threads
        - terminationTimeout: how long to wait for the executor to finish before terminating the
            JVM

        Since
        - 28.0
        """
        ...


    @staticmethod
    def addDelayedShutdownHook(service: "ExecutorService", terminationTimeout: int, timeUnit: "TimeUnit") -> None:
        """
        Add a shutdown hook to wait for thread completion in the given ExecutorService service.
        This is useful if the given service uses daemon threads, and we want to keep the JVM from
        exiting immediately on shutdown, instead giving these daemon threads a chance to terminate
        normally.

        Arguments
        - service: ExecutorService which uses daemon threads
        - terminationTimeout: how long to wait for the executor to finish before terminating the
            JVM
        - timeUnit: unit of time for the time parameter
        """
        ...


    @staticmethod
    def newDirectExecutorService() -> "ListeningExecutorService":
        """
        Creates an executor service that runs each task in the thread that invokes `execute/submit`, as in `ThreadPoolExecutor.CallerRunsPolicy`. This applies both to
        individually submitted tasks and to collections of tasks submitted via `invokeAll` or
        `invokeAny`. In the latter case, tasks will run serially on the calling thread. Tasks are
        run to completion before a `Future` is returned to the caller (unless the executor has
        been shutdown).
        
        Although all tasks are immediately executed in the thread that submitted the task, this
        `ExecutorService` imposes a small locking overhead on each task submission in order to
        implement shutdown and termination behavior.
        
        The implementation deviates from the `ExecutorService` specification with regards to
        the `shutdownNow` method. First, "best-effort" with regards to canceling running tasks is
        implemented as "no-effort". No interrupts or other attempts are made to stop threads executing
        tasks. Second, the returned list will always be empty, as any submitted task is considered to
        have started execution. This applies also to tasks given to `invokeAll` or `invokeAny` which are pending serial execution, even the subset of the tasks that have not yet
        started execution. It is unclear from the `ExecutorService` specification if these should
        be included, and it's much easier to implement the interpretation that they not be. Finally, a
        call to `shutdown` or `shutdownNow` may result in concurrent calls to `invokeAll/invokeAny` throwing RejectedExecutionException, although a subset of the tasks may
        already have been executed.

        Since
        - 18.0 (present as MoreExecutors.sameThreadExecutor() since 10.0)
        """
        ...


    @staticmethod
    def directExecutor() -> "Executor":
        """
        Returns an Executor that runs each task in the thread that invokes Executor.execute execute, as in `ThreadPoolExecutor.CallerRunsPolicy`.
        
        This executor is appropriate for tasks that are lightweight and not deeply chained.
        Inappropriate `directExecutor` usage can cause problems, and these problems can be
        difficult to reproduce because they depend on timing. For example:
        
        
          - When a `ListenableFuture` listener is registered to run under `directExecutor`, the listener can execute in any of three possible threads:
              <ol>
                - When a thread attaches a listener to a `ListenableFuture` that's already
                    complete, the listener runs immediately in that thread.
                - When a thread attaches a listener to a `ListenableFuture` that's
                    *in*complete and the `ListenableFuture` later completes normally, the
                    listener runs in the thread that completes the `ListenableFuture`.
                - When a listener is attached to a `ListenableFuture` and the `ListenableFuture` gets cancelled, the listener runs immediately in the thread that
                    cancelled the `Future`.
              </ol>
              Given all these possibilities, it is frequently possible for listeners to execute in UI
              threads, RPC network threads, or other latency-sensitive threads. In those cases, slow
              listeners can harm responsiveness, slow the system as a whole, or worse. (See also the
              note about locking below.)
          - If many tasks will be triggered by the same event, one heavyweight task may delay other
              tasks -- even tasks that are not themselves `directExecutor` tasks.
          - If many such tasks are chained together (such as with `future.transform(...).transform(...).transform(...)....`), they may overflow the stack.
              (In simple cases, callers can avoid this by registering all tasks with the same MoreExecutors.newSequentialExecutor wrapper around `directExecutor()`. More
              complex cases may require using thread pools or making deeper changes.)
          - If an exception propagates out of a `Runnable`, it is not necessarily seen by any
              `UncaughtExceptionHandler` for the thread. For example, if the callback passed to
              Futures.addCallback throws an exception, that exception will be typically be
              logged by the ListenableFuture implementation, even if the thread is configured
              to do something different. In other cases, no code will catch the exception, and it may
              terminate whichever thread happens to trigger the execution.
        
        
        A specific warning about locking: Code that executes user-supplied tasks, such as `ListenableFuture` listeners, should take care not to do so while holding a lock. Additionally,
        as a further line of defense, prefer not to perform any locking inside a task that will be run
        under `directExecutor`: Not only might the wait for a lock be long, but if the running
        thread was holding a lock, the listener may deadlock or break lock isolation.
        
        This instance is equivalent to:
        
        ````final class DirectExecutor implements Executor {
          public void execute(Runnable r) {
            r.run();`
        }
        }```
        
        This should be preferred to .newDirectExecutorService() because implementing the
        ExecutorService subinterface necessitates significant performance overhead.

        Since
        - 18.0
        """
        ...


    @staticmethod
    def newSequentialExecutor(delegate: "Executor") -> "Executor":
        """
        Returns an Executor that runs each task executed sequentially, such that no two tasks
        are running concurrently.
        
        Executor.execute executed tasks have a happens-before order as defined in the
        Java Language Specification. Tasks execute with the same happens-before order that the function
        calls to Executor.execute `execute()` that submitted those tasks had.
        
        The executor uses `delegate` in order to Executor.execute execute each task in
        turn, and does not create any threads of its own.
        
        After execution begins on a thread from the `delegate` Executor, tasks are
        polled and executed from a task queue until there are no more tasks. The thread will not be
        released until there are no more tasks to run.
        
        If a task is submitted while a thread is executing tasks from the task queue, the thread
        will not be released until that submitted task is also complete.
        
        If a task is Thread.interrupt interrupted while a task is running:
        
        <ol>
          - execution will not stop until the task queue is empty.
          - tasks will begin execution with the thread marked as not interrupted - any interruption
              applies only to the task that was running at the point of interruption.
          - if the thread was interrupted before the SequentialExecutor's worker begins execution,
              the interrupt will be restored to the thread after it completes so that its `delegate` Executor may process the interrupt.
          - subtasks are run with the thread uninterrupted and interrupts received during execution
              of a task are ignored.
        </ol>
        
        `RuntimeException`s thrown by tasks are simply logged and the executor keeps trucking.
        If an `Error` is thrown, the error will propagate and execution will stop until the next
        time a task is submitted.
        
        When an `Error` is thrown by an executed task, previously submitted tasks may never
        run. An attempt will be made to restart execution on the next call to `execute`. If the
        `delegate` has begun to reject execution, the previously submitted tasks may never run,
        despite not throwing a RejectedExecutionException synchronously with the call to `execute`. If this behaviour is problematic, use an Executor with a single thread (e.g. Executors.newSingleThreadExecutor).

        Since
        - 23.3 (since 23.1 as `sequentialExecutor`)
        """
        ...


    @staticmethod
    def listeningDecorator(delegate: "ExecutorService") -> "ListeningExecutorService":
        """
        Creates an ExecutorService whose `submit` and `invokeAll` methods submit
        ListenableFutureTask instances to the given delegate executor. Those methods, as well
        as `execute` and `invokeAny`, are implemented in terms of calls to `delegate.execute`. All other methods are forwarded unchanged to the delegate. This implies that
        the returned `ListeningExecutorService` never calls the delegate's `submit`, `invokeAll`, and `invokeAny` methods, so any special handling of tasks must be implemented
        in the delegate's `execute` method or by wrapping the returned `ListeningExecutorService`.
        
        If the delegate executor was already an instance of `ListeningExecutorService`, it is
        returned untouched, and the rest of this documentation does not apply.

        Since
        - 10.0
        """
        ...


    @staticmethod
    def listeningDecorator(delegate: "ScheduledExecutorService") -> "ListeningScheduledExecutorService":
        """
        Creates a ScheduledExecutorService whose `submit` and `invokeAll` methods
        submit ListenableFutureTask instances to the given delegate executor. Those methods, as
        well as `execute` and `invokeAny`, are implemented in terms of calls to `delegate.execute`. All other methods are forwarded unchanged to the delegate. This implies that
        the returned `ListeningScheduledExecutorService` never calls the delegate's `submit`, `invokeAll`, and `invokeAny` methods, so any special handling of tasks
        must be implemented in the delegate's `execute` method or by wrapping the returned `ListeningScheduledExecutorService`.
        
        If the delegate executor was already an instance of `ListeningScheduledExecutorService`, it is returned untouched, and the rest of this
        documentation does not apply.

        Since
        - 10.0
        """
        ...


    @staticmethod
    def platformThreadFactory() -> "ThreadFactory":
        """
        Returns a default thread factory used to create new threads.
        
        When running on AppEngine with access to <a
        href="https://cloud.google.com/appengine/docs/standard/java/javadoc/">AppEngine legacy
        APIs</a>, this method returns `ThreadManager.currentRequestThreadFactory()`. Otherwise,
        it returns Executors.defaultThreadFactory().

        Since
        - 14.0
        """
        ...


    @staticmethod
    def shutdownAndAwaitTermination(service: "ExecutorService", timeout: "Duration") -> bool:
        """
        Shuts down the given executor service gradually, first disabling new submissions and later, if
        necessary, cancelling remaining tasks.
        
        The method takes the following steps:
        
        <ol>
          - calls ExecutorService.shutdown(), disabling acceptance of new submitted tasks.
          - awaits executor service termination for half of the specified timeout.
          - if the timeout expires, it calls ExecutorService.shutdownNow(), cancelling
              pending tasks and interrupting running tasks.
          - awaits executor service termination for the other half of the specified timeout.
        </ol>
        
        If, at any step of the process, the calling thread is interrupted, the method calls ExecutorService.shutdownNow() and returns.

        Arguments
        - service: the `ExecutorService` to shut down
        - timeout: the maximum time to wait for the `ExecutorService` to terminate

        Returns
        - `True` if the `ExecutorService` was terminated successfully, `False`
            if the call timed out or was interrupted

        Since
        - 28.0
        """
        ...


    @staticmethod
    def shutdownAndAwaitTermination(service: "ExecutorService", timeout: int, unit: "TimeUnit") -> bool:
        """
        Shuts down the given executor service gradually, first disabling new submissions and later, if
        necessary, cancelling remaining tasks.
        
        The method takes the following steps:
        
        <ol>
          - calls ExecutorService.shutdown(), disabling acceptance of new submitted tasks.
          - awaits executor service termination for half of the specified timeout.
          - if the timeout expires, it calls ExecutorService.shutdownNow(), cancelling
              pending tasks and interrupting running tasks.
          - awaits executor service termination for the other half of the specified timeout.
        </ol>
        
        If, at any step of the process, the calling thread is interrupted, the method calls ExecutorService.shutdownNow() and returns.

        Arguments
        - service: the `ExecutorService` to shut down
        - timeout: the maximum time to wait for the `ExecutorService` to terminate
        - unit: the time unit of the timeout argument

        Returns
        - `True` if the `ExecutorService` was terminated successfully, `False`
            if the call timed out or was interrupted

        Since
        - 17.0
        """
        ...
