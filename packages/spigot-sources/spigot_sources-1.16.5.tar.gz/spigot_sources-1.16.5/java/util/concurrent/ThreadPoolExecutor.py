"""
Python module generated from Java source file java.util.concurrent.ThreadPoolExecutor

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import ConcurrentModificationException
from java.util import Iterator
from java.util.concurrent import *
from java.util.concurrent.atomic import AtomicInteger
from java.util.concurrent.locks import AbstractQueuedSynchronizer
from java.util.concurrent.locks import Condition
from java.util.concurrent.locks import ReentrantLock
from typing import Any, Callable, Iterable, Tuple


class ThreadPoolExecutor(AbstractExecutorService):
    """
    An ExecutorService that executes each submitted task using
    one of possibly several pooled threads, normally configured
    using Executors factory methods.
    
    Thread pools address two different problems: they usually
    provide improved performance when executing large numbers of
    asynchronous tasks, due to reduced per-task invocation overhead,
    and they provide a means of bounding and managing the resources,
    including threads, consumed when executing a collection of tasks.
    Each `ThreadPoolExecutor` also maintains some basic
    statistics, such as the number of completed tasks.
    
    To be useful across a wide range of contexts, this class
    provides many adjustable parameters and extensibility
    hooks. However, programmers are urged to use the more convenient
    Executors factory methods Executors.newCachedThreadPool (unbounded thread pool, with
    automatic thread reclamation), Executors.newFixedThreadPool
    (fixed size thread pool) and Executors.newSingleThreadExecutor (single background thread), that
    preconfigure settings for the most common usage
    scenarios. Otherwise, use the following guide when manually
    configuring and tuning this class:
    
    <dl>
    
    <dt>Core and maximum pool sizes</dt>
    
    <dd>A `ThreadPoolExecutor` will automatically adjust the
    pool size (see .getPoolSize)
    according to the bounds set by
    corePoolSize (see .getCorePoolSize) and
    maximumPoolSize (see .getMaximumPoolSize).
    
    When a new task is submitted in method .execute(Runnable),
    if fewer than corePoolSize threads are running, a new thread is
    created to handle the request, even if other worker threads are
    idle.  Else if fewer than maximumPoolSize threads are running, a
    new thread will be created to handle the request only if the queue
    is full.  By setting corePoolSize and maximumPoolSize the same, you
    create a fixed-size thread pool. By setting maximumPoolSize to an
    essentially unbounded value such as `Integer.MAX_VALUE`, you
    allow the pool to accommodate an arbitrary number of concurrent
    tasks. Most typically, core and maximum pool sizes are set only
    upon construction, but they may also be changed dynamically using
    .setCorePoolSize and .setMaximumPoolSize. </dd>
    
    <dt>On-demand construction</dt>
    
    <dd>By default, even core threads are initially created and
    started only when new tasks arrive, but this can be overridden
    dynamically using method .prestartCoreThread or .prestartAllCoreThreads.  You probably want to prestart threads if
    you construct the pool with a non-empty queue. </dd>
    
    <dt>Creating new threads</dt>
    
    <dd>New threads are created using a ThreadFactory.  If not
    otherwise specified, a Executors.defaultThreadFactory is
    used, that creates threads to all be in the same ThreadGroup and with the same `NORM_PRIORITY` priority and
    non-daemon status. By supplying a different ThreadFactory, you can
    alter the thread's name, thread group, priority, daemon status,
    etc. If a `ThreadFactory` fails to create a thread when asked
    by returning null from `newThread`, the executor will
    continue, but might not be able to execute any tasks. Threads
    should possess the "modifyThread" `RuntimePermission`. If
    worker threads or other threads using the pool do not possess this
    permission, service may be degraded: configuration changes may not
    take effect in a timely manner, and a shutdown pool may remain in a
    state in which termination is possible but not completed.</dd>
    
    <dt>Keep-alive times</dt>
    
    <dd>If the pool currently has more than corePoolSize threads,
    excess threads will be terminated if they have been idle for more
    than the keepAliveTime (see .getKeepAliveTime(TimeUnit)).
    This provides a means of reducing resource consumption when the
    pool is not being actively used. If the pool becomes more active
    later, new threads will be constructed. This parameter can also be
    changed dynamically using method .setKeepAliveTime(long,
    TimeUnit).  Using a value of `Long.MAX_VALUE` TimeUnit.NANOSECONDS effectively disables idle threads from ever
    terminating prior to shut down. By default, the keep-alive policy
    applies only when there are more than corePoolSize threads, but
    method .allowCoreThreadTimeOut(boolean) can be used to
    apply this time-out policy to core threads as well, so long as the
    keepAliveTime value is non-zero. </dd>
    
    <dt>Queuing</dt>
    
    <dd>Any BlockingQueue may be used to transfer and hold
    submitted tasks.  The use of this queue interacts with pool sizing:
    
    
    
    - If fewer than corePoolSize threads are running, the Executor
    always prefers adding a new thread
    rather than queuing.
    
    - If corePoolSize or more threads are running, the Executor
    always prefers queuing a request rather than adding a new
    thread.
    
    - If a request cannot be queued, a new thread is created unless
    this would exceed maximumPoolSize, in which case, the task will be
    rejected.
    
    
    
    There are three general strategies for queuing:
    <ol>
    
    - * Direct handoffs.* A good default choice for a work
    queue is a SynchronousQueue that hands off tasks to threads
    without otherwise holding them. Here, an attempt to queue a task
    will fail if no threads are immediately available to run it, so a
    new thread will be constructed. This policy avoids lockups when
    handling sets of requests that might have internal dependencies.
    Direct handoffs generally require unbounded maximumPoolSizes to
    avoid rejection of new submitted tasks. This in turn admits the
    possibility of unbounded thread growth when commands continue to
    arrive on average faster than they can be processed.
    
    - * Unbounded queues.* Using an unbounded queue (for
    example a LinkedBlockingQueue without a predefined
    capacity) will cause new tasks to wait in the queue when all
    corePoolSize threads are busy. Thus, no more than corePoolSize
    threads will ever be created. (And the value of the maximumPoolSize
    therefore doesn't have any effect.)  This may be appropriate when
    each task is completely independent of others, so tasks cannot
    affect each others execution; for example, in a web page server.
    While this style of queuing can be useful in smoothing out
    transient bursts of requests, it admits the possibility of
    unbounded work queue growth when commands continue to arrive on
    average faster than they can be processed.
    
    - *Bounded queues.* A bounded queue (for example, an
    ArrayBlockingQueue) helps prevent resource exhaustion when
    used with finite maximumPoolSizes, but can be more difficult to
    tune and control.  Queue sizes and maximum pool sizes may be traded
    off for each other: Using large queues and small pools minimizes
    CPU usage, OS resources, and context-switching overhead, but can
    lead to artificially low throughput.  If tasks frequently block (for
    example if they are I/O bound), a system may be able to schedule
    time for more threads than you otherwise allow. Use of small queues
    generally requires larger pool sizes, which keeps CPUs busier but
    may encounter unacceptable scheduling overhead, which also
    decreases throughput.
    
    </ol>
    
    </dd>
    
    <dt>Rejected tasks</dt>
    
    <dd>New tasks submitted in method .execute(Runnable) will be
    *rejected* when the Executor has been shut down, and also when
    the Executor uses finite bounds for both maximum threads and work queue
    capacity, and is saturated.  In either case, the `execute` method
    invokes the RejectedExecutionHandler.rejectedExecution(Runnable, ThreadPoolExecutor)
    method of its RejectedExecutionHandler.  Four predefined handler
    policies are provided:
    
    <ol>
    
    - In the default ThreadPoolExecutor.AbortPolicy, the handler
    throws a runtime RejectedExecutionException upon rejection.
    
    - In ThreadPoolExecutor.CallerRunsPolicy, the thread
    that invokes `execute` itself runs the task. This provides a
    simple feedback control mechanism that will slow down the rate that
    new tasks are submitted.
    
    - In ThreadPoolExecutor.DiscardPolicy, a task that cannot
    be executed is simply dropped. This policy is designed only for
    those rare cases in which task completion is never relied upon.
    
    - In ThreadPoolExecutor.DiscardOldestPolicy, if the
    executor is not shut down, the task at the head of the work queue
    is dropped, and then execution is retried (which can fail again,
    causing this to be repeated.) This policy is rarely acceptable.  In
    nearly all cases, you should also cancel the task to cause an
    exception in any component waiting for its completion, and/or log
    the failure, as illustrated in ThreadPoolExecutor.DiscardOldestPolicy documentation.
    
    </ol>
    
    It is possible to define and use other kinds of RejectedExecutionHandler classes. Doing so requires some care
    especially when policies are designed to work only under particular
    capacity or queuing policies. </dd>
    
    <dt>Hook methods</dt>
    
    <dd>This class provides `protected` overridable
    .beforeExecute(Thread, Runnable) and
    .afterExecute(Runnable, Throwable) methods that are called
    before and after execution of each task.  These can be used to
    manipulate the execution environment; for example, reinitializing
    ThreadLocals, gathering statistics, or adding log entries.
    Additionally, method .terminated can be overridden to perform
    any special processing that needs to be done once the Executor has
    fully terminated.
    
    If hook, callback, or BlockingQueue methods throw exceptions,
    internal worker threads may in turn fail, abruptly terminate, and
    possibly be replaced.</dd>
    
    <dt>Queue maintenance</dt>
    
    <dd>Method .getQueue() allows access to the work queue
    for purposes of monitoring and debugging.  Use of this method for
    any other purpose is strongly discouraged.  Two supplied methods,
    .remove(Runnable) and .purge are available to
    assist in storage reclamation when large numbers of queued tasks
    become cancelled.</dd>
    
    <dt>Reclamation</dt>
    
    <dd>A pool that is no longer referenced in a program *AND*
    has no remaining threads may be reclaimed (garbage collected)
    without being explicitly shutdown. You can configure a pool to
    allow all unused threads to eventually die by setting appropriate
    keep-alive times, using a lower bound of zero core threads and/or
    setting .allowCoreThreadTimeOut(boolean).  </dd>
    
    </dl>
    
    **Extension example.** Most extensions of this class
    override one or more of the protected hook methods. For example,
    here is a subclass that adds a simple pause/resume feature:
    
    ``` `class PausableThreadPoolExecutor extends ThreadPoolExecutor {
      private boolean isPaused;
      private ReentrantLock pauseLock = new ReentrantLock();
      private Condition unpaused = pauseLock.newCondition();
    
      public PausableThreadPoolExecutor(...) { super(...);`
    
      protected void beforeExecute(Thread t, Runnable r) {
        super.beforeExecute(t, r);
        pauseLock.lock();
        try {
          while (isPaused) unpaused.await();
        } catch (InterruptedException ie) {
          t.interrupt();
        } finally {
          pauseLock.unlock();
        }
      }
    
      public void pause() {
        pauseLock.lock();
        try {
          isPaused = True;
        } finally {
          pauseLock.unlock();
        }
      }
    
      public void resume() {
        pauseLock.lock();
        try {
          isPaused = False;
          unpaused.signalAll();
        } finally {
          pauseLock.unlock();
        }
      }
    }}```

    Author(s)
    - Doug Lea

    Since
    - 1.5
    """

    def __init__(self, corePoolSize: int, maximumPoolSize: int, keepAliveTime: int, unit: "TimeUnit", workQueue: "BlockingQueue"["Runnable"]):
        """
        Creates a new `ThreadPoolExecutor` with the given initial
        parameters, the
        Executors.defaultThreadFactory default thread factory
        and the ThreadPoolExecutor.AbortPolicy
        default rejected execution handler.
        
        It may be more convenient to use one of the Executors
        factory methods instead of this general purpose constructor.

        Arguments
        - corePoolSize: the number of threads to keep in the pool, even
               if they are idle, unless `allowCoreThreadTimeOut` is set
        - maximumPoolSize: the maximum number of threads to allow in the
               pool
        - keepAliveTime: when the number of threads is greater than
               the core, this is the maximum time that excess idle threads
               will wait for new tasks before terminating.
        - unit: the time unit for the `keepAliveTime` argument
        - workQueue: the queue to use for holding tasks before they are
               executed.  This queue will hold only the `Runnable`
               tasks submitted by the `execute` method.

        Raises
        - IllegalArgumentException: if one of the following holds:
                `corePoolSize < 0`
                `keepAliveTime < 0`
                `maximumPoolSize <= 0`
                `maximumPoolSize < corePoolSize`
        - NullPointerException: if `workQueue` is null
        """
        ...


    def __init__(self, corePoolSize: int, maximumPoolSize: int, keepAliveTime: int, unit: "TimeUnit", workQueue: "BlockingQueue"["Runnable"], threadFactory: "ThreadFactory"):
        """
        Creates a new `ThreadPoolExecutor` with the given initial
        parameters and the ThreadPoolExecutor.AbortPolicy
        default rejected execution handler.

        Arguments
        - corePoolSize: the number of threads to keep in the pool, even
               if they are idle, unless `allowCoreThreadTimeOut` is set
        - maximumPoolSize: the maximum number of threads to allow in the
               pool
        - keepAliveTime: when the number of threads is greater than
               the core, this is the maximum time that excess idle threads
               will wait for new tasks before terminating.
        - unit: the time unit for the `keepAliveTime` argument
        - workQueue: the queue to use for holding tasks before they are
               executed.  This queue will hold only the `Runnable`
               tasks submitted by the `execute` method.
        - threadFactory: the factory to use when the executor
               creates a new thread

        Raises
        - IllegalArgumentException: if one of the following holds:
                `corePoolSize < 0`
                `keepAliveTime < 0`
                `maximumPoolSize <= 0`
                `maximumPoolSize < corePoolSize`
        - NullPointerException: if `workQueue`
                or `threadFactory` is null
        """
        ...


    def __init__(self, corePoolSize: int, maximumPoolSize: int, keepAliveTime: int, unit: "TimeUnit", workQueue: "BlockingQueue"["Runnable"], handler: "RejectedExecutionHandler"):
        """
        Creates a new `ThreadPoolExecutor` with the given initial
        parameters and the
        Executors.defaultThreadFactory default thread factory.

        Arguments
        - corePoolSize: the number of threads to keep in the pool, even
               if they are idle, unless `allowCoreThreadTimeOut` is set
        - maximumPoolSize: the maximum number of threads to allow in the
               pool
        - keepAliveTime: when the number of threads is greater than
               the core, this is the maximum time that excess idle threads
               will wait for new tasks before terminating.
        - unit: the time unit for the `keepAliveTime` argument
        - workQueue: the queue to use for holding tasks before they are
               executed.  This queue will hold only the `Runnable`
               tasks submitted by the `execute` method.
        - handler: the handler to use when execution is blocked
               because the thread bounds and queue capacities are reached

        Raises
        - IllegalArgumentException: if one of the following holds:
                `corePoolSize < 0`
                `keepAliveTime < 0`
                `maximumPoolSize <= 0`
                `maximumPoolSize < corePoolSize`
        - NullPointerException: if `workQueue`
                or `handler` is null
        """
        ...


    def __init__(self, corePoolSize: int, maximumPoolSize: int, keepAliveTime: int, unit: "TimeUnit", workQueue: "BlockingQueue"["Runnable"], threadFactory: "ThreadFactory", handler: "RejectedExecutionHandler"):
        """
        Creates a new `ThreadPoolExecutor` with the given initial
        parameters.

        Arguments
        - corePoolSize: the number of threads to keep in the pool, even
               if they are idle, unless `allowCoreThreadTimeOut` is set
        - maximumPoolSize: the maximum number of threads to allow in the
               pool
        - keepAliveTime: when the number of threads is greater than
               the core, this is the maximum time that excess idle threads
               will wait for new tasks before terminating.
        - unit: the time unit for the `keepAliveTime` argument
        - workQueue: the queue to use for holding tasks before they are
               executed.  This queue will hold only the `Runnable`
               tasks submitted by the `execute` method.
        - threadFactory: the factory to use when the executor
               creates a new thread
        - handler: the handler to use when execution is blocked
               because the thread bounds and queue capacities are reached

        Raises
        - IllegalArgumentException: if one of the following holds:
                `corePoolSize < 0`
                `keepAliveTime < 0`
                `maximumPoolSize <= 0`
                `maximumPoolSize < corePoolSize`
        - NullPointerException: if `workQueue`
                or `threadFactory` or `handler` is null
        """
        ...


    def execute(self, command: "Runnable") -> None:
        """
        Executes the given task sometime in the future.  The task
        may execute in a new thread or in an existing pooled thread.
        
        If the task cannot be submitted for execution, either because this
        executor has been shutdown or because its capacity has been reached,
        the task is handled by the current RejectedExecutionHandler.

        Arguments
        - command: the task to execute

        Raises
        - RejectedExecutionException: at discretion of
                `RejectedExecutionHandler`, if the task
                cannot be accepted for execution
        - NullPointerException: if `command` is null
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

        Raises
        - SecurityException: 
        """
        ...


    def isShutdown(self) -> bool:
        ...


    def isTerminating(self) -> bool:
        """
        Returns True if this executor is in the process of terminating
        after .shutdown or .shutdownNow but has not
        completely terminated.  This method may be useful for
        debugging. A return of `True` reported a sufficient
        period after shutdown may indicate that submitted tasks have
        ignored or suppressed interruption, causing this executor not
        to properly terminate.

        Returns
        - `True` if terminating but not yet terminated
        """
        ...


    def isTerminated(self) -> bool:
        ...


    def awaitTermination(self, timeout: int, unit: "TimeUnit") -> bool:
        ...


    def setThreadFactory(self, threadFactory: "ThreadFactory") -> None:
        """
        Sets the thread factory used to create new threads.

        Arguments
        - threadFactory: the new thread factory

        Raises
        - NullPointerException: if threadFactory is null

        See
        - .getThreadFactory
        """
        ...


    def getThreadFactory(self) -> "ThreadFactory":
        """
        Returns the thread factory used to create new threads.

        Returns
        - the current thread factory

        See
        - .setThreadFactory(ThreadFactory)
        """
        ...


    def setRejectedExecutionHandler(self, handler: "RejectedExecutionHandler") -> None:
        """
        Sets a new handler for unexecutable tasks.

        Arguments
        - handler: the new handler

        Raises
        - NullPointerException: if handler is null

        See
        - .getRejectedExecutionHandler
        """
        ...


    def getRejectedExecutionHandler(self) -> "RejectedExecutionHandler":
        """
        Returns the current handler for unexecutable tasks.

        Returns
        - the current handler

        See
        - .setRejectedExecutionHandler(RejectedExecutionHandler)
        """
        ...


    def setCorePoolSize(self, corePoolSize: int) -> None:
        """
        Sets the core number of threads.  This overrides any value set
        in the constructor.  If the new value is smaller than the
        current value, excess existing threads will be terminated when
        they next become idle.  If larger, new threads will, if needed,
        be started to execute any queued tasks.

        Arguments
        - corePoolSize: the new core size

        Raises
        - IllegalArgumentException: if `corePoolSize < 0`
                or `corePoolSize` is greater than the .getMaximumPoolSize() maximum pool size

        See
        - .getCorePoolSize
        """
        ...


    def getCorePoolSize(self) -> int:
        """
        Returns the core number of threads.

        Returns
        - the core number of threads

        See
        - .setCorePoolSize
        """
        ...


    def prestartCoreThread(self) -> bool:
        """
        Starts a core thread, causing it to idly wait for work. This
        overrides the default policy of starting core threads only when
        new tasks are executed. This method will return `False`
        if all core threads have already been started.

        Returns
        - `True` if a thread was started
        """
        ...


    def prestartAllCoreThreads(self) -> int:
        """
        Starts all core threads, causing them to idly wait for work. This
        overrides the default policy of starting core threads only when
        new tasks are executed.

        Returns
        - the number of threads started
        """
        ...


    def allowsCoreThreadTimeOut(self) -> bool:
        """
        Returns True if this pool allows core threads to time out and
        terminate if no tasks arrive within the keepAlive time, being
        replaced if needed when new tasks arrive. When True, the same
        keep-alive policy applying to non-core threads applies also to
        core threads. When False (the default), core threads are never
        terminated due to lack of incoming tasks.

        Returns
        - `True` if core threads are allowed to time out,
                else `False`

        Since
        - 1.6
        """
        ...


    def allowCoreThreadTimeOut(self, value: bool) -> None:
        """
        Sets the policy governing whether core threads may time out and
        terminate if no tasks arrive within the keep-alive time, being
        replaced if needed when new tasks arrive. When False, core
        threads are never terminated due to lack of incoming
        tasks. When True, the same keep-alive policy applying to
        non-core threads applies also to core threads. To avoid
        continual thread replacement, the keep-alive time must be
        greater than zero when setting `True`. This method
        should in general be called before the pool is actively used.

        Arguments
        - value: `True` if should time out, else `False`

        Raises
        - IllegalArgumentException: if value is `True`
                and the current keep-alive time is not greater than zero

        Since
        - 1.6
        """
        ...


    def setMaximumPoolSize(self, maximumPoolSize: int) -> None:
        """
        Sets the maximum allowed number of threads. This overrides any
        value set in the constructor. If the new value is smaller than
        the current value, excess existing threads will be
        terminated when they next become idle.

        Arguments
        - maximumPoolSize: the new maximum

        Raises
        - IllegalArgumentException: if the new maximum is
                less than or equal to zero, or
                less than the .getCorePoolSize core pool size

        See
        - .getMaximumPoolSize
        """
        ...


    def getMaximumPoolSize(self) -> int:
        """
        Returns the maximum allowed number of threads.

        Returns
        - the maximum allowed number of threads

        See
        - .setMaximumPoolSize
        """
        ...


    def setKeepAliveTime(self, time: int, unit: "TimeUnit") -> None:
        """
        Sets the thread keep-alive time, which is the amount of time
        that threads may remain idle before being terminated.
        Threads that wait this amount of time without processing a
        task will be terminated if there are more than the core
        number of threads currently in the pool, or if this pool
        .allowsCoreThreadTimeOut() allows core thread timeout.
        This overrides any value set in the constructor.

        Arguments
        - time: the time to wait.  A time value of zero will cause
               excess threads to terminate immediately after executing tasks.
        - unit: the time unit of the `time` argument

        Raises
        - IllegalArgumentException: if `time` less than zero or
                if `time` is zero and `allowsCoreThreadTimeOut`

        See
        - .getKeepAliveTime(TimeUnit)
        """
        ...


    def getKeepAliveTime(self, unit: "TimeUnit") -> int:
        """
        Returns the thread keep-alive time, which is the amount of time
        that threads may remain idle before being terminated.
        Threads that wait this amount of time without processing a
        task will be terminated if there are more than the core
        number of threads currently in the pool, or if this pool
        .allowsCoreThreadTimeOut() allows core thread timeout.

        Arguments
        - unit: the desired time unit of the result

        Returns
        - the time limit

        See
        - .setKeepAliveTime(long, TimeUnit)
        """
        ...


    def getQueue(self) -> "BlockingQueue"["Runnable"]:
        """
        Returns the task queue used by this executor. Access to the
        task queue is intended primarily for debugging and monitoring.
        This queue may be in active use.  Retrieving the task queue
        does not prevent queued tasks from executing.

        Returns
        - the task queue
        """
        ...


    def remove(self, task: "Runnable") -> bool:
        """
        Removes this task from the executor's internal queue if it is
        present, thus causing it not to be run if it has not already
        started.
        
        This method may be useful as one part of a cancellation
        scheme.  It may fail to remove tasks that have been converted
        into other forms before being placed on the internal queue.
        For example, a task entered using `submit` might be
        converted into a form that maintains `Future` status.
        However, in such cases, method .purge may be used to
        remove those Futures that have been cancelled.

        Arguments
        - task: the task to remove

        Returns
        - `True` if the task was removed
        """
        ...


    def purge(self) -> None:
        """
        Tries to remove from the work queue all Future
        tasks that have been cancelled. This method can be useful as a
        storage reclamation operation, that has no other impact on
        functionality. Cancelled tasks are never executed, but may
        accumulate in work queues until worker threads can actively
        remove them. Invoking this method instead tries to remove them now.
        However, this method may fail to remove tasks in
        the presence of interference by other threads.
        """
        ...


    def getPoolSize(self) -> int:
        """
        Returns the current number of threads in the pool.

        Returns
        - the number of threads
        """
        ...


    def getActiveCount(self) -> int:
        """
        Returns the approximate number of threads that are actively
        executing tasks.

        Returns
        - the number of threads
        """
        ...


    def getLargestPoolSize(self) -> int:
        """
        Returns the largest number of threads that have ever
        simultaneously been in the pool.

        Returns
        - the number of threads
        """
        ...


    def getTaskCount(self) -> int:
        """
        Returns the approximate total number of tasks that have ever been
        scheduled for execution. Because the states of tasks and
        threads may change dynamically during computation, the returned
        value is only an approximation.

        Returns
        - the number of tasks
        """
        ...


    def getCompletedTaskCount(self) -> int:
        """
        Returns the approximate total number of tasks that have
        completed execution. Because the states of tasks and threads
        may change dynamically during computation, the returned value
        is only an approximation, but one that does not ever decrease
        across successive calls.

        Returns
        - the number of tasks
        """
        ...


    def toString(self) -> str:
        """
        Returns a string identifying this pool, as well as its state,
        including indications of run state and estimated worker and
        task counts.

        Returns
        - a string identifying this pool, as well as its state
        """
        ...


    class CallerRunsPolicy(RejectedExecutionHandler):
        """
        A handler for rejected tasks that runs the rejected task
        directly in the calling thread of the `execute` method,
        unless the executor has been shut down, in which case the task
        is discarded.
        """

        def __init__(self):
            """
            Creates a `CallerRunsPolicy`.
            """
            ...


        def rejectedExecution(self, r: "Runnable", e: "ThreadPoolExecutor") -> None:
            """
            Executes task r in the caller's thread, unless the executor
            has been shut down, in which case the task is discarded.

            Arguments
            - r: the runnable task requested to be executed
            - e: the executor attempting to execute this task
            """
            ...


    class AbortPolicy(RejectedExecutionHandler):
        """
        A handler for rejected tasks that throws a
        RejectedExecutionException.
        
        This is the default handler for ThreadPoolExecutor and
        ScheduledThreadPoolExecutor.
        """

        def __init__(self):
            """
            Creates an `AbortPolicy`.
            """
            ...


        def rejectedExecution(self, r: "Runnable", e: "ThreadPoolExecutor") -> None:
            """
            Always throws RejectedExecutionException.

            Arguments
            - r: the runnable task requested to be executed
            - e: the executor attempting to execute this task

            Raises
            - RejectedExecutionException: always
            """
            ...


    class DiscardPolicy(RejectedExecutionHandler):
        """
        A handler for rejected tasks that silently discards the
        rejected task.
        """

        def __init__(self):
            """
            Creates a `DiscardPolicy`.
            """
            ...


        def rejectedExecution(self, r: "Runnable", e: "ThreadPoolExecutor") -> None:
            """
            Does nothing, which has the effect of discarding task r.

            Arguments
            - r: the runnable task requested to be executed
            - e: the executor attempting to execute this task
            """
            ...


    class DiscardOldestPolicy(RejectedExecutionHandler):
        """
        A handler for rejected tasks that discards the oldest unhandled
        request and then retries `execute`, unless the executor
        is shut down, in which case the task is discarded. This policy is
        rarely useful in cases where other threads may be waiting for
        tasks to terminate, or failures must be recorded. Instead consider
        using a handler of the form:
        ``` `new RejectedExecutionHandler() {
          public void rejectedExecution(Runnable r, ThreadPoolExecutor e) {
            Runnable dropped = e.getQueue().poll();
            if (dropped instanceof Future<?>) {
              ((Future<?>)dropped).cancel(False);
              // also consider logging the failure`
            e.execute(r);  // retry
        }}}```
        """

        def __init__(self):
            """
            Creates a `DiscardOldestPolicy` for the given executor.
            """
            ...


        def rejectedExecution(self, r: "Runnable", e: "ThreadPoolExecutor") -> None:
            """
            Obtains and ignores the next task that the executor
            would otherwise execute, if one is immediately available,
            and then retries execution of task r, unless the executor
            is shut down, in which case task r is instead discarded.

            Arguments
            - r: the runnable task requested to be executed
            - e: the executor attempting to execute this task
            """
            ...
