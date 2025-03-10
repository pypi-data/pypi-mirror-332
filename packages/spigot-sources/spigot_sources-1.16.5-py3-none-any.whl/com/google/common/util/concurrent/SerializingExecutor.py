"""
Python module generated from Java source file com.google.common.util.concurrent.SerializingExecutor

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.base import Preconditions
from com.google.common.util.concurrent import *
from java.util import ArrayDeque
from java.util import Deque
from java.util.concurrent import Executor
from javax.annotation.concurrent import GuardedBy
from typing import Any, Callable, Iterable, Tuple


class SerializingExecutor(Executor):
    """
    Executor ensuring that all Runnables submitted are executed in order, using the provided
    Executor, and serially such that no two will ever be running at the same time.
    
    Tasks submitted to .execute(Runnable) are executed in FIFO order.
    
    Tasks can also be prepended to the queue to be executed in LIFO order before any other
    submitted tasks. Primarily intended for the currently executing task to be able to schedule a
    continuation task.
    
    Execution on the queue can be .suspend suspended, e.g. while waiting for an RPC,
    and execution can be .resume resumed later.
    
    The execution of tasks is done by one thread as long as there are tasks left in the queue and
    execution has not been suspended. (Even if one task is Thread.interrupt interrupted,
    execution of subsequent tasks continues.) `RuntimeException`s thrown by tasks are simply
    logged and the executor keeps trucking. If an `Error` is thrown, the error will propagate
    and execution will stop until it is restarted by external calls.
    """

    def __init__(self, executor: "Executor"):
        ...


    def execute(self, task: "Runnable") -> None:
        """
        Adds a task to the queue and makes sure a worker thread is running, unless the queue has been
        suspended.
        
        If this method throws, e.g. a `RejectedExecutionException` from the delegate executor,
        execution of tasks will stop until a call to this method or to .resume() is made.
        """
        ...


    def executeFirst(self, task: "Runnable") -> None:
        """
        Prepends a task to the front of the queue and makes sure a worker thread is running, unless the
        queue has been suspended.
        """
        ...


    def suspend(self) -> None:
        """
        Suspends the running of tasks until .resume() is called. This can be called multiple
        times to increase the suspensions count and execution will not continue until .resume
        has been called the same number of times as `suspend` has been.
        
        Any task that has already been pulled off the queue for execution will be completed before
        execution is suspended.
        """
        ...


    def resume(self) -> None:
        """
        Continue execution of tasks after a call to .suspend(). More accurately, decreases the
        suspension counter, as has been incremented by calls to .suspend, and resumes execution
        if the suspension counter is zero.
        
        If this method throws, e.g. a `RejectedExecutionException` from the delegate executor,
        execution of tasks will stop until a call to this method or to .execute(Runnable) or
        .executeFirst(Runnable) is made.

        Raises
        - java.lang.IllegalStateException: if this executor is not suspended.
        """
        ...
