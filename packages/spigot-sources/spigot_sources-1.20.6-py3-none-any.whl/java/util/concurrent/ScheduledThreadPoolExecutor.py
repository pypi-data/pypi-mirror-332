"""
Python module generated from Java source file java.util.concurrent.ScheduledThreadPoolExecutor

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import AbstractQueue
from java.util import Arrays
from java.util import Iterator
from java.util import NoSuchElementException
from java.util import Objects
from java.util.concurrent import *
from java.util.concurrent.atomic import AtomicLong
from java.util.concurrent.locks import Condition
from java.util.concurrent.locks import ReentrantLock
from typing import Any, Callable, Iterable, Tuple


class ScheduledThreadPoolExecutor(ThreadPoolExecutor, ScheduledExecutorService):
    """
    A ThreadPoolExecutor that can additionally schedule
    commands to run after a given delay, or to execute periodically.
    This class is preferable to java.util.Timer when multiple
    worker threads are needed, or when the additional flexibility or
    capabilities of ThreadPoolExecutor (which this class
    extends) are required.
    
    Delayed tasks execute no sooner than they are enabled, but
    without any real-time guarantees about when, after they are
    enabled, they will commence. Tasks scheduled for exactly the same
    execution time are enabled in first-in-first-out (FIFO) order of
    submission.
    
    When a submitted task is cancelled before it is run, execution
    is suppressed.  By default, such a cancelled task is not
    automatically removed from the work queue until its delay elapses.
    While this enables further inspection and monitoring, it may also
    cause unbounded retention of cancelled tasks.  To avoid this, use
    .setRemoveOnCancelPolicy to cause tasks to be immediately
    removed from the work queue at time of cancellation.
    
    Successive executions of a periodic task scheduled via
    .scheduleAtFixedRate scheduleAtFixedRate or
    .scheduleWithFixedDelay scheduleWithFixedDelay
    do not overlap. While different executions may be performed by
    different threads, the effects of prior executions
    <a href="package-summary.html#MemoryVisibility">*happen-before*</a>
    those of subsequent ones.
    
    While this class inherits from ThreadPoolExecutor, a few
    of the inherited tuning methods are not useful for it. In
    particular, because it acts as a fixed-sized pool using
    `corePoolSize` threads and an unbounded queue, adjustments
    to `maximumPoolSize` have no useful effect. Additionally, it
    is almost never a good idea to set `corePoolSize` to zero or
    use `allowCoreThreadTimeOut` because this may leave the pool
    without threads to handle tasks once they become eligible to run.
    
    As with `ThreadPoolExecutor`, if not otherwise specified,
    this class uses Executors.defaultThreadFactory as the
    default thread factory, and ThreadPoolExecutor.AbortPolicy
    as the default rejected execution handler.
    
    **Extension notes:** This class overrides the
    ThreadPoolExecutor.execute(Runnable) execute and
    AbstractExecutorService.submit(Runnable) submit
    methods to generate internal ScheduledFuture objects to
    control per-task delays and scheduling.  To preserve
    functionality, any further overrides of these methods in
    subclasses must invoke superclass versions, which effectively
    disables additional task customization.  However, this class
    provides alternative protected extension method
    `decorateTask` (one version each for `Runnable` and
    `Callable`) that can be used to customize the concrete task
    types used to execute commands entered via `execute`,
    `submit`, `schedule`, `scheduleAtFixedRate`,
    and `scheduleWithFixedDelay`.  By default, a
    `ScheduledThreadPoolExecutor` uses a task type extending
    FutureTask. However, this may be modified or replaced using
    subclasses of the form:
    
    ``` `public class CustomScheduledExecutor extends ScheduledThreadPoolExecutor {
    
      static class CustomTask<V> implements RunnableScheduledFuture<V> { ...`
    
      protected <V> RunnableScheduledFuture<V> decorateTask(
                   Runnable r, RunnableScheduledFuture<V> task) {
          return new CustomTask<V>(r, task);
      }
    
      protected <V> RunnableScheduledFuture<V> decorateTask(
                   Callable<V> c, RunnableScheduledFuture<V> task) {
          return new CustomTask<V>(c, task);
      }
      // ... add constructors, etc.
    }}```

    Author(s)
    - Doug Lea

    Since
    - 1.5
    """

    def __init__(self, corePoolSize: int):
        """
        Creates a new `ScheduledThreadPoolExecutor` with the
        given core pool size.

        Arguments
        - corePoolSize: the number of threads to keep in the pool, even
               if they are idle, unless `allowCoreThreadTimeOut` is set

        Raises
        - IllegalArgumentException: if `corePoolSize < 0`
        """
        ...


    def __init__(self, corePoolSize: int, threadFactory: "ThreadFactory"):
        """
        Creates a new `ScheduledThreadPoolExecutor` with the
        given initial parameters.

        Arguments
        - corePoolSize: the number of threads to keep in the pool, even
               if they are idle, unless `allowCoreThreadTimeOut` is set
        - threadFactory: the factory to use when the executor
               creates a new thread

        Raises
        - IllegalArgumentException: if `corePoolSize < 0`
        - NullPointerException: if `threadFactory` is null
        """
        ...


    def __init__(self, corePoolSize: int, handler: "RejectedExecutionHandler"):
        """
        Creates a new `ScheduledThreadPoolExecutor` with the
        given initial parameters.

        Arguments
        - corePoolSize: the number of threads to keep in the pool, even
               if they are idle, unless `allowCoreThreadTimeOut` is set
        - handler: the handler to use when execution is blocked
               because the thread bounds and queue capacities are reached

        Raises
        - IllegalArgumentException: if `corePoolSize < 0`
        - NullPointerException: if `handler` is null
        """
        ...


    def __init__(self, corePoolSize: int, threadFactory: "ThreadFactory", handler: "RejectedExecutionHandler"):
        """
        Creates a new `ScheduledThreadPoolExecutor` with the
        given initial parameters.

        Arguments
        - corePoolSize: the number of threads to keep in the pool, even
               if they are idle, unless `allowCoreThreadTimeOut` is set
        - threadFactory: the factory to use when the executor
               creates a new thread
        - handler: the handler to use when execution is blocked
               because the thread bounds and queue capacities are reached

        Raises
        - IllegalArgumentException: if `corePoolSize < 0`
        - NullPointerException: if `threadFactory` or
                `handler` is null
        """
        ...


    def schedule(self, command: "Runnable", delay: int, unit: "TimeUnit") -> "ScheduledFuture"[Any]:
        """
        Raises
        - RejectedExecutionException: 
        - NullPointerException: 
        """
        ...


    def schedule(self, callable: "Callable"["V"], delay: int, unit: "TimeUnit") -> "ScheduledFuture"["V"]:
        """
        Raises
        - RejectedExecutionException: 
        - NullPointerException: 
        """
        ...


    def scheduleAtFixedRate(self, command: "Runnable", initialDelay: int, period: int, unit: "TimeUnit") -> "ScheduledFuture"[Any]:
        """
        Submits a periodic action that becomes enabled first after the
        given initial delay, and subsequently with the given period;
        that is, executions will commence after
        `initialDelay`, then `initialDelay + period`, then
        `initialDelay + 2 * period`, and so on.
        
        The sequence of task executions continues indefinitely until
        one of the following exceptional completions occur:
        
        - The task is Future.cancel explicitly cancelled
        via the returned future.
        - Method .shutdown is called and the .getContinueExistingPeriodicTasksAfterShutdownPolicy policy on
        whether to continue after shutdown is not set True, or method
        .shutdownNow is called; also resulting in task
        cancellation.
        - An execution of the task throws an exception.  In this case
        calling Future.get() get on the returned future will throw
        ExecutionException, holding the exception as its cause.
        
        Subsequent executions are suppressed.  Subsequent calls to
        Future.isDone isDone() on the returned future will
        return `True`.
        
        If any execution of this task takes longer than its period, then
        subsequent executions may start late, but will not concurrently
        execute.

        Raises
        - RejectedExecutionException: 
        - NullPointerException: 
        - IllegalArgumentException: 
        """
        ...


    def scheduleWithFixedDelay(self, command: "Runnable", initialDelay: int, delay: int, unit: "TimeUnit") -> "ScheduledFuture"[Any]:
        """
        Submits a periodic action that becomes enabled first after the
        given initial delay, and subsequently with the given delay
        between the termination of one execution and the commencement of
        the next.
        
        The sequence of task executions continues indefinitely until
        one of the following exceptional completions occur:
        
        - The task is Future.cancel explicitly cancelled
        via the returned future.
        - Method .shutdown is called and the .getContinueExistingPeriodicTasksAfterShutdownPolicy policy on
        whether to continue after shutdown is not set True, or method
        .shutdownNow is called; also resulting in task
        cancellation.
        - An execution of the task throws an exception.  In this case
        calling Future.get() get on the returned future will throw
        ExecutionException, holding the exception as its cause.
        
        Subsequent executions are suppressed.  Subsequent calls to
        Future.isDone isDone() on the returned future will
        return `True`.

        Raises
        - RejectedExecutionException: 
        - NullPointerException: 
        - IllegalArgumentException: 
        """
        ...


    def execute(self, command: "Runnable") -> None:
        """
        Executes `command` with zero required delay.
        This has effect equivalent to
        .schedule(Runnable,long,TimeUnit) schedule(command, 0, anyUnit).
        Note that inspections of the queue and of the list returned by
        `shutdownNow` will access the zero-delayed
        ScheduledFuture, not the `command` itself.
        
        A consequence of the use of `ScheduledFuture` objects is
        that ThreadPoolExecutor.afterExecute afterExecute is always
        called with a null second `Throwable` argument, even if the
        `command` terminated abruptly.  Instead, the `Throwable`
        thrown by such a task can be obtained via Future.get.

        Raises
        - RejectedExecutionException: at discretion of
                `RejectedExecutionHandler`, if the task
                cannot be accepted for execution because the
                executor has been shut down
        - NullPointerException: 
        """
        ...


    def submit(self, task: "Runnable") -> "Future"[Any]:
        """
        Raises
        - RejectedExecutionException: 
        - NullPointerException: 
        """
        ...


    def submit(self, task: "Runnable", result: "T") -> "Future"["T"]:
        """
        Raises
        - RejectedExecutionException: 
        - NullPointerException: 
        """
        ...


    def submit(self, task: "Callable"["T"]) -> "Future"["T"]:
        """
        Raises
        - RejectedExecutionException: 
        - NullPointerException: 
        """
        ...


    def setContinueExistingPeriodicTasksAfterShutdownPolicy(self, value: bool) -> None:
        """
        Sets the policy on whether to continue executing existing
        periodic tasks even when this executor has been `shutdown`.
        In this case, executions will continue until `shutdownNow`
        or the policy is set to `False` when already shutdown.
        This value is by default `False`.

        Arguments
        - value: if `True`, continue after shutdown, else don't

        See
        - .getContinueExistingPeriodicTasksAfterShutdownPolicy
        """
        ...


    def getContinueExistingPeriodicTasksAfterShutdownPolicy(self) -> bool:
        """
        Gets the policy on whether to continue executing existing
        periodic tasks even when this executor has been `shutdown`.
        In this case, executions will continue until `shutdownNow`
        or the policy is set to `False` when already shutdown.
        This value is by default `False`.

        Returns
        - `True` if will continue after shutdown

        See
        - .setContinueExistingPeriodicTasksAfterShutdownPolicy
        """
        ...


    def setExecuteExistingDelayedTasksAfterShutdownPolicy(self, value: bool) -> None:
        """
        Sets the policy on whether to execute existing delayed
        tasks even when this executor has been `shutdown`.
        In this case, these tasks will only terminate upon
        `shutdownNow`, or after setting the policy to
        `False` when already shutdown.
        This value is by default `True`.

        Arguments
        - value: if `True`, execute after shutdown, else don't

        See
        - .getExecuteExistingDelayedTasksAfterShutdownPolicy
        """
        ...


    def getExecuteExistingDelayedTasksAfterShutdownPolicy(self) -> bool:
        """
        Gets the policy on whether to execute existing delayed
        tasks even when this executor has been `shutdown`.
        In this case, these tasks will only terminate upon
        `shutdownNow`, or after setting the policy to
        `False` when already shutdown.
        This value is by default `True`.

        Returns
        - `True` if will execute after shutdown

        See
        - .setExecuteExistingDelayedTasksAfterShutdownPolicy
        """
        ...


    def setRemoveOnCancelPolicy(self, value: bool) -> None:
        """
        Sets the policy on whether cancelled tasks should be immediately
        removed from the work queue at time of cancellation.  This value is
        by default `False`.

        Arguments
        - value: if `True`, remove on cancellation, else don't

        See
        - .getRemoveOnCancelPolicy

        Since
        - 1.7
        """
        ...


    def getRemoveOnCancelPolicy(self) -> bool:
        """
        Gets the policy on whether cancelled tasks should be immediately
        removed from the work queue at time of cancellation.  This value is
        by default `False`.

        Returns
        - `True` if cancelled tasks are immediately removed
                from the queue

        See
        - .setRemoveOnCancelPolicy

        Since
        - 1.7
        """
        ...


    def shutdown(self) -> None:
        """
        Initiates an orderly shutdown in which previously submitted
        tasks are executed, but no new tasks will be accepted.
        Invocation has no additional effect if already shut down.
        
        This method does not wait for previously submitted tasks to
        complete execution.  Use .awaitTermination awaitTermination
        to do that.
        
        If the `ExecuteExistingDelayedTasksAfterShutdownPolicy`
        has been set `False`, existing delayed tasks whose delays
        have not yet elapsed are cancelled.  And unless the `ContinueExistingPeriodicTasksAfterShutdownPolicy` has been set
        `True`, future executions of existing periodic tasks will
        be cancelled.

        Raises
        - SecurityException: 
        """
        ...


    def shutdownNow(self) -> list["Runnable"]:
        """
        Attempts to stop all actively executing tasks, halts the
        processing of waiting tasks, and returns a list of the tasks
        that were awaiting execution. These tasks are drained (removed)
        from the task queue upon return from this method.
        
        This method does not wait for actively executing tasks to
        terminate.  Use .awaitTermination awaitTermination to
        do that.
        
        There are no guarantees beyond best-effort attempts to stop
        processing actively executing tasks.  This implementation
        interrupts tasks via Thread.interrupt; any task that
        fails to respond to interrupts may never terminate.

        Returns
        - list of tasks that never commenced execution.
                Each element of this list is a ScheduledFuture.
                For tasks submitted via one of the `schedule`
                methods, the element will be identical to the returned
                `ScheduledFuture`.  For tasks submitted using
                .execute execute, the element will be a
                zero-delay `ScheduledFuture`.

        Raises
        - SecurityException: 
        """
        ...


    def getQueue(self) -> "BlockingQueue"["Runnable"]:
        """
        Returns the task queue used by this executor.  Access to the
        task queue is intended primarily for debugging and monitoring.
        This queue may be in active use.  Retrieving the task queue
        does not prevent queued tasks from executing.
        
        Each element of this queue is a ScheduledFuture.
        For tasks submitted via one of the `schedule` methods, the
        element will be identical to the returned `ScheduledFuture`.
        For tasks submitted using .execute execute, the element
        will be a zero-delay `ScheduledFuture`.
        
        Iteration over this queue is *not* guaranteed to traverse
        tasks in the order in which they will execute.

        Returns
        - the task queue
        """
        ...
