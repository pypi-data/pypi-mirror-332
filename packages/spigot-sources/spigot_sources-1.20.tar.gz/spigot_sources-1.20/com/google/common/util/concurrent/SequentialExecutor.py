"""
Python module generated from Java source file com.google.common.util.concurrent.SequentialExecutor

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.base import Preconditions
from com.google.common.util.concurrent import *
from com.google.errorprone.annotations.concurrent import GuardedBy
from com.google.j2objc.annotations import RetainedWith
from java.util import ArrayDeque
from java.util import Deque
from java.util.concurrent import Executor
from java.util.concurrent import RejectedExecutionException
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class SequentialExecutor(Executor):
    """
    Executor ensuring that all Runnables submitted are executed in order, using the provided
    Executor, and sequentially such that no two will ever be running at the same time.
    
    Tasks submitted to .execute(Runnable) are executed in FIFO order.
    
    The execution of tasks is done by one thread as long as there are tasks left in the queue.
    When a task is Thread.interrupt interrupted, execution of subsequent tasks
    continues. See QueueWorker.workOnQueue for details.
    
    `RuntimeException`s thrown by tasks are simply logged and the executor keeps trucking.
    If an `Error` is thrown, the error will propagate and execution will stop until it is
    restarted by a call to .execute.
    """

    def execute(self, task: "Runnable") -> None:
        """
        Adds a task to the queue and makes sure a worker thread is running.
        
        If this method throws, e.g. a `RejectedExecutionException` from the delegate executor,
        execution of tasks will stop until a call to this method is made.
        """
        ...


    def toString(self) -> str:
        ...
