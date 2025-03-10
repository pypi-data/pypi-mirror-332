"""
Python module generated from Java source file java.util.concurrent.Executors

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.security import AccessControlContext
from java.security import AccessControlException
from java.security import AccessController
from java.security import PrivilegedAction
from java.security import PrivilegedActionException
from java.security import PrivilegedExceptionAction
from java.util.concurrent import *
from java.util.concurrent.atomic import AtomicInteger
from sun.security.util import SecurityConstants
from typing import Any, Callable, Iterable, Tuple


class Executors:
    """
    Factory and utility methods for Executor, ExecutorService, ScheduledExecutorService, ThreadFactory, and Callable classes defined in this
    package. This class supports the following kinds of methods:
    
    
      - Methods that create and return an ExecutorService
          set up with commonly useful configuration settings.
      - Methods that create and return a ScheduledExecutorService
          set up with commonly useful configuration settings.
      - Methods that create and return a "wrapped" ExecutorService, that
          disables reconfiguration by making implementation-specific methods
          inaccessible.
      - Methods that create and return a ThreadFactory
          that sets newly created threads to a known state.
      - Methods that create and return a Callable
          out of other closure-like forms, so they can be used
          in execution methods requiring `Callable`.

    Author(s)
    - Doug Lea

    Since
    - 1.5
    """

    @staticmethod
    def newFixedThreadPool(nThreads: int) -> "ExecutorService":
        """
        Creates a thread pool that reuses a fixed number of threads
        operating off a shared unbounded queue.  At any point, at most
        `nThreads` threads will be active processing tasks.
        If additional tasks are submitted when all threads are active,
        they will wait in the queue until a thread is available.
        If any thread terminates due to a failure during execution
        prior to shutdown, a new one will take its place if needed to
        execute subsequent tasks.  The threads in the pool will exist
        until it is explicitly ExecutorService.shutdown shutdown.

        Arguments
        - nThreads: the number of threads in the pool

        Returns
        - the newly created thread pool

        Raises
        - IllegalArgumentException: if `nThreads <= 0`
        """
        ...


    @staticmethod
    def newWorkStealingPool(parallelism: int) -> "ExecutorService":
        """
        Creates a thread pool that maintains enough threads to support
        the given parallelism level, and may use multiple queues to
        reduce contention. The parallelism level corresponds to the
        maximum number of threads actively engaged in, or available to
        engage in, task processing. The actual number of threads may
        grow and shrink dynamically. A work-stealing pool makes no
        guarantees about the order in which submitted tasks are
        executed.

        Arguments
        - parallelism: the targeted parallelism level

        Returns
        - the newly created thread pool

        Raises
        - IllegalArgumentException: if `parallelism <= 0`

        Since
        - 1.8
        """
        ...


    @staticmethod
    def newWorkStealingPool() -> "ExecutorService":
        """
        Creates a work-stealing thread pool using the number of
        Runtime.availableProcessors available processors
        as its target parallelism level.

        Returns
        - the newly created thread pool

        See
        - .newWorkStealingPool(int)

        Since
        - 1.8
        """
        ...


    @staticmethod
    def newFixedThreadPool(nThreads: int, threadFactory: "ThreadFactory") -> "ExecutorService":
        """
        Creates a thread pool that reuses a fixed number of threads
        operating off a shared unbounded queue, using the provided
        ThreadFactory to create new threads when needed.  At any point,
        at most `nThreads` threads will be active processing
        tasks.  If additional tasks are submitted when all threads are
        active, they will wait in the queue until a thread is
        available.  If any thread terminates due to a failure during
        execution prior to shutdown, a new one will take its place if
        needed to execute subsequent tasks.  The threads in the pool will
        exist until it is explicitly ExecutorService.shutdown
        shutdown.

        Arguments
        - nThreads: the number of threads in the pool
        - threadFactory: the factory to use when creating new threads

        Returns
        - the newly created thread pool

        Raises
        - NullPointerException: if threadFactory is null
        - IllegalArgumentException: if `nThreads <= 0`
        """
        ...


    @staticmethod
    def newSingleThreadExecutor() -> "ExecutorService":
        """
        Creates an Executor that uses a single worker thread operating
        off an unbounded queue. (Note however that if this single
        thread terminates due to a failure during execution prior to
        shutdown, a new one will take its place if needed to execute
        subsequent tasks.)  Tasks are guaranteed to execute
        sequentially, and no more than one task will be active at any
        given time. Unlike the otherwise equivalent
        `newFixedThreadPool(1)` the returned executor is
        guaranteed not to be reconfigurable to use additional threads.

        Returns
        - the newly created single-threaded Executor
        """
        ...


    @staticmethod
    def newSingleThreadExecutor(threadFactory: "ThreadFactory") -> "ExecutorService":
        """
        Creates an Executor that uses a single worker thread operating
        off an unbounded queue, and uses the provided ThreadFactory to
        create a new thread when needed. Unlike the otherwise
        equivalent `newFixedThreadPool(1, threadFactory)` the
        returned executor is guaranteed not to be reconfigurable to use
        additional threads.

        Arguments
        - threadFactory: the factory to use when creating new threads

        Returns
        - the newly created single-threaded Executor

        Raises
        - NullPointerException: if threadFactory is null
        """
        ...


    @staticmethod
    def newCachedThreadPool() -> "ExecutorService":
        """
        Creates a thread pool that creates new threads as needed, but
        will reuse previously constructed threads when they are
        available.  These pools will typically improve the performance
        of programs that execute many short-lived asynchronous tasks.
        Calls to `execute` will reuse previously constructed
        threads if available. If no existing thread is available, a new
        thread will be created and added to the pool. Threads that have
        not been used for sixty seconds are terminated and removed from
        the cache. Thus, a pool that remains idle for long enough will
        not consume any resources. Note that pools with similar
        properties but different details (for example, timeout parameters)
        may be created using ThreadPoolExecutor constructors.

        Returns
        - the newly created thread pool
        """
        ...


    @staticmethod
    def newCachedThreadPool(threadFactory: "ThreadFactory") -> "ExecutorService":
        """
        Creates a thread pool that creates new threads as needed, but
        will reuse previously constructed threads when they are
        available, and uses the provided
        ThreadFactory to create new threads when needed.

        Arguments
        - threadFactory: the factory to use when creating new threads

        Returns
        - the newly created thread pool

        Raises
        - NullPointerException: if threadFactory is null
        """
        ...


    @staticmethod
    def newSingleThreadScheduledExecutor() -> "ScheduledExecutorService":
        """
        Creates a single-threaded executor that can schedule commands
        to run after a given delay, or to execute periodically.
        (Note however that if this single
        thread terminates due to a failure during execution prior to
        shutdown, a new one will take its place if needed to execute
        subsequent tasks.)  Tasks are guaranteed to execute
        sequentially, and no more than one task will be active at any
        given time. Unlike the otherwise equivalent
        `newScheduledThreadPool(1)` the returned executor is
        guaranteed not to be reconfigurable to use additional threads.

        Returns
        - the newly created scheduled executor
        """
        ...


    @staticmethod
    def newSingleThreadScheduledExecutor(threadFactory: "ThreadFactory") -> "ScheduledExecutorService":
        """
        Creates a single-threaded executor that can schedule commands
        to run after a given delay, or to execute periodically.  (Note
        however that if this single thread terminates due to a failure
        during execution prior to shutdown, a new one will take its
        place if needed to execute subsequent tasks.)  Tasks are
        guaranteed to execute sequentially, and no more than one task
        will be active at any given time. Unlike the otherwise
        equivalent `newScheduledThreadPool(1, threadFactory)`
        the returned executor is guaranteed not to be reconfigurable to
        use additional threads.

        Arguments
        - threadFactory: the factory to use when creating new threads

        Returns
        - the newly created scheduled executor

        Raises
        - NullPointerException: if threadFactory is null
        """
        ...


    @staticmethod
    def newScheduledThreadPool(corePoolSize: int) -> "ScheduledExecutorService":
        """
        Creates a thread pool that can schedule commands to run after a
        given delay, or to execute periodically.

        Arguments
        - corePoolSize: the number of threads to keep in the pool,
        even if they are idle

        Returns
        - the newly created scheduled thread pool

        Raises
        - IllegalArgumentException: if `corePoolSize < 0`
        """
        ...


    @staticmethod
    def newScheduledThreadPool(corePoolSize: int, threadFactory: "ThreadFactory") -> "ScheduledExecutorService":
        """
        Creates a thread pool that can schedule commands to run after a
        given delay, or to execute periodically.

        Arguments
        - corePoolSize: the number of threads to keep in the pool,
        even if they are idle
        - threadFactory: the factory to use when the executor
        creates a new thread

        Returns
        - the newly created scheduled thread pool

        Raises
        - IllegalArgumentException: if `corePoolSize < 0`
        - NullPointerException: if threadFactory is null
        """
        ...


    @staticmethod
    def unconfigurableExecutorService(executor: "ExecutorService") -> "ExecutorService":
        """
        Returns an object that delegates all defined ExecutorService methods to the given executor, but not any
        other methods that might otherwise be accessible using
        casts. This provides a way to safely "freeze" configuration and
        disallow tuning of a given concrete implementation.

        Arguments
        - executor: the underlying implementation

        Returns
        - an `ExecutorService` instance

        Raises
        - NullPointerException: if executor null
        """
        ...


    @staticmethod
    def unconfigurableScheduledExecutorService(executor: "ScheduledExecutorService") -> "ScheduledExecutorService":
        """
        Returns an object that delegates all defined ScheduledExecutorService methods to the given executor, but
        not any other methods that might otherwise be accessible using
        casts. This provides a way to safely "freeze" configuration and
        disallow tuning of a given concrete implementation.

        Arguments
        - executor: the underlying implementation

        Returns
        - a `ScheduledExecutorService` instance

        Raises
        - NullPointerException: if executor null
        """
        ...


    @staticmethod
    def defaultThreadFactory() -> "ThreadFactory":
        """
        Returns a default thread factory used to create new threads.
        This factory creates all new threads used by an Executor in the
        same ThreadGroup. If there is a java.lang.SecurityManager, it uses the group of System.getSecurityManager, else the group of the thread
        invoking this `defaultThreadFactory` method. Each new
        thread is created as a non-daemon thread with priority set to
        the smaller of `Thread.NORM_PRIORITY` and the maximum
        priority permitted in the thread group.  New threads have names
        accessible via Thread.getName of
        *pool-N-thread-M*, where *N* is the sequence
        number of this factory, and *M* is the sequence number
        of the thread created by this factory.

        Returns
        - a thread factory
        """
        ...


    @staticmethod
    def privilegedThreadFactory() -> "ThreadFactory":
        """
        Returns a thread factory used to create new threads that
        have the same permissions as the current thread.
        This factory creates threads with the same settings as Executors.defaultThreadFactory, additionally setting the
        AccessControlContext and contextClassLoader of new threads to
        be the same as the thread invoking this
        `privilegedThreadFactory` method.  A new
        `privilegedThreadFactory` can be created within an
        AccessController.doPrivileged AccessController.doPrivileged
        action setting the current thread's access control context to
        create threads with the selected permission settings holding
        within that action.
        
        Note that while tasks running within such threads will have
        the same access control and class loader settings as the
        current thread, they need not have the same java.lang.ThreadLocal or java.lang.InheritableThreadLocal values. If necessary,
        particular values of thread locals can be set or reset before
        any task runs in ThreadPoolExecutor subclasses using
        ThreadPoolExecutor.beforeExecute(Thread, Runnable).
        Also, if it is necessary to initialize worker threads to have
        the same InheritableThreadLocal settings as some other
        designated thread, you can create a custom ThreadFactory in
        which that thread waits for and services requests to create
        others that will inherit its values.

        Returns
        - a thread factory

        Raises
        - AccessControlException: if the current access control
        context does not have permission to both get and set context
        class loader

        Deprecated
        - This method is only useful in conjunction with
              SecurityManager the Security Manager, which is
              deprecated and subject to removal in a future release.
              Consequently, this method is also deprecated and subject to
              removal. There is no replacement for the Security Manager or this
              method.
        """
        ...


    @staticmethod
    def callable(task: "Runnable", result: "T") -> "Callable"["T"]:
        """
        Returns a Callable object that, when
        called, runs the given task and returns the given result.  This
        can be useful when applying methods requiring a
        `Callable` to an otherwise resultless action.
        
        Type `<T>`: the type of the result

        Arguments
        - task: the task to run
        - result: the result to return

        Returns
        - a callable object

        Raises
        - NullPointerException: if task null
        """
        ...


    @staticmethod
    def callable(task: "Runnable") -> "Callable"["Object"]:
        """
        Returns a Callable object that, when
        called, runs the given task and returns `null`.

        Arguments
        - task: the task to run

        Returns
        - a callable object

        Raises
        - NullPointerException: if task null
        """
        ...


    @staticmethod
    def callable(action: "PrivilegedAction"[Any]) -> "Callable"["Object"]:
        """
        Returns a Callable object that, when
        called, runs the given privileged action and returns its result.

        Arguments
        - action: the privileged action to run

        Returns
        - a callable object

        Raises
        - NullPointerException: if action null
        """
        ...


    @staticmethod
    def callable(action: "PrivilegedExceptionAction"[Any]) -> "Callable"["Object"]:
        """
        Returns a Callable object that, when
        called, runs the given privileged exception action and returns
        its result.

        Arguments
        - action: the privileged exception action to run

        Returns
        - a callable object

        Raises
        - NullPointerException: if action null
        """
        ...


    @staticmethod
    def privilegedCallable(callable: "Callable"["T"]) -> "Callable"["T"]:
        """
        Returns a Callable object that will, when called,
        execute the given `callable` under the current access
        control context. This method should normally be invoked within
        an AccessController.doPrivileged AccessController.doPrivileged
        action to create callables that will, if possible, execute
        under the selected permission settings holding within that
        action; or if not possible, throw an associated AccessControlException.
        
        Type `<T>`: the type of the callable's result

        Arguments
        - callable: the underlying task

        Returns
        - a callable object

        Raises
        - NullPointerException: if callable null

        Deprecated
        - This method is only useful in conjunction with
              SecurityManager the Security Manager, which is
              deprecated and subject to removal in a future release.
              Consequently, this method is also deprecated and subject to
              removal. There is no replacement for the Security Manager or this
              method.
        """
        ...


    @staticmethod
    def privilegedCallableUsingCurrentClassLoader(callable: "Callable"["T"]) -> "Callable"["T"]:
        """
        Returns a Callable object that will, when called,
        execute the given `callable` under the current access
        control context, with the current context class loader as the
        context class loader. This method should normally be invoked
        within an
        AccessController.doPrivileged AccessController.doPrivileged
        action to create callables that will, if possible, execute
        under the selected permission settings holding within that
        action; or if not possible, throw an associated AccessControlException.
        
        Type `<T>`: the type of the callable's result

        Arguments
        - callable: the underlying task

        Returns
        - a callable object

        Raises
        - NullPointerException: if callable null
        - AccessControlException: if the current access control
        context does not have permission to both set and get context
        class loader

        Deprecated
        - This method is only useful in conjunction with
              SecurityManager the Security Manager, which is
              deprecated and subject to removal in a future release.
              Consequently, this method is also deprecated and subject to
              removal. There is no replacement for the Security Manager or this
              method.
        """
        ...
