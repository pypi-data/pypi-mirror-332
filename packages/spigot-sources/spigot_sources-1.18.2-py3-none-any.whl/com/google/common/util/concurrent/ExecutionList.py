"""
Python module generated from Java source file com.google.common.util.concurrent.ExecutionList

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.util.concurrent import *
from com.google.errorprone.annotations.concurrent import GuardedBy
from java.util.concurrent import Executor
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class ExecutionList:
    """
    A support class for `ListenableFuture` implementations to manage their listeners. An
    instance contains a list of listeners, each with an associated `Executor`, and guarantees
    that every `Runnable` that is .add added will be executed after .execute() is called. Any `Runnable` added after the call to `execute` is still
    guaranteed to execute. There is no guarantee, however, that listeners will be executed in the
    order that they are added.
    
    Exceptions thrown by a listener will be propagated up to the executor. Any exception thrown
    during `Executor.execute` (e.g., a `RejectedExecutionException` or an exception
    thrown by MoreExecutors.directExecutor direct execution) will be caught and logged.

    Author(s)
    - Sven Mawson

    Since
    - 1.0
    """

    def __init__(self):
        """
        Creates a new, empty ExecutionList.
        """
        ...


    def add(self, runnable: "Runnable", executor: "Executor") -> None:
        """
        Adds the `Runnable` and accompanying `Executor` to the list of listeners to
        execute. If execution has already begun, the listener is executed immediately.
        
        When selecting an executor, note that `directExecutor` is dangerous in some cases. See
        the discussion in the ListenableFuture.addListener ListenableFuture.addListener
        documentation.
        """
        ...


    def execute(self) -> None:
        """
        Runs this execution list, executing all existing pairs in the order they were added. However,
        note that listeners added after this point may be executed before those previously added, and
        note that the execution order of all listeners is ultimately chosen by the implementations of
        the supplied executors.
        
        This method is idempotent. Calling it several times in parallel is semantically equivalent
        to calling it exactly once.

        Since
        - 10.0 (present in 1.0 as `run`)
        """
        ...
