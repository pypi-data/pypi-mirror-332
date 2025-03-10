"""
Python module generated from Java source file java.util.concurrent.FutureTask

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.lang.invoke import MethodHandles
from java.lang.invoke import VarHandle
from java.util.concurrent import *
from java.util.concurrent.locks import LockSupport
from typing import Any, Callable, Iterable, Tuple


class FutureTask(RunnableFuture):
    """
    A cancellable asynchronous computation.  This class provides a base
    implementation of Future, with methods to start and cancel
    a computation, query to see if the computation is complete, and
    retrieve the result of the computation.  The result can only be
    retrieved when the computation has completed; the `get`
    methods will block if the computation has not yet completed.  Once
    the computation has completed, the computation cannot be restarted
    or cancelled (unless the computation is invoked using
    .runAndReset).
    
    A `FutureTask` can be used to wrap a Callable or
    Runnable object.  Because `FutureTask` implements
    `Runnable`, a `FutureTask` can be submitted to an
    Executor for execution.
    
    In addition to serving as a standalone class, this class provides
    `protected` functionality that may be useful when creating
    customized task classes.
    
    Type `<V>`: The result type returned by this FutureTask's `get` methods

    Author(s)
    - Doug Lea

    Since
    - 1.5
    """

    def __init__(self, callable: "Callable"["V"]):
        """
        Creates a `FutureTask` that will, upon running, execute the
        given `Callable`.

        Arguments
        - callable: the callable task

        Raises
        - NullPointerException: if the callable is null
        """
        ...


    def __init__(self, runnable: "Runnable", result: "V"):
        """
        Creates a `FutureTask` that will, upon running, execute the
        given `Runnable`, and arrange that `get` will return the
        given result on successful completion.

        Arguments
        - runnable: the runnable task
        - result: the result to return on successful completion. If
        you don't need a particular result, consider using
        constructions of the form:
        `Future<?> f = new FutureTask<Void>(runnable, null)`

        Raises
        - NullPointerException: if the runnable is null
        """
        ...


    def isCancelled(self) -> bool:
        ...


    def isDone(self) -> bool:
        ...


    def cancel(self, mayInterruptIfRunning: bool) -> bool:
        ...


    def get(self) -> "V":
        """
        Raises
        - CancellationException: 
        """
        ...


    def get(self, timeout: int, unit: "TimeUnit") -> "V":
        """
        Raises
        - CancellationException: 
        """
        ...


    def run(self) -> None:
        ...


    def toString(self) -> str:
        """
        Returns a string representation of this FutureTask.

        Returns
        - a string representation of this FutureTask

        Unknown Tags
        - The default implementation returns a string identifying this
        FutureTask, as well as its completion state.  The state, in
        brackets, contains one of the strings `"Completed Normally"`,
        `"Completed Exceptionally"`, `"Cancelled"`, or `"Not completed"`.
        """
        ...
