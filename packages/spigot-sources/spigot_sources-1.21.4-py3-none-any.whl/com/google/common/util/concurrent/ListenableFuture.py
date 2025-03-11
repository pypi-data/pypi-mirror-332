"""
Python module generated from Java source file com.google.common.util.concurrent.ListenableFuture

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.util.concurrent import *
from com.google.errorprone.annotations import DoNotMock
from java.util.concurrent import Executor
from java.util.concurrent import Future
from java.util.concurrent import RejectedExecutionException
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class ListenableFuture(Future):

    def addListener(self, listener: "Runnable", executor: "Executor") -> None:
        """
        Registers a listener to be Executor.execute(Runnable) run on the given executor.
        The listener will run when the `Future`'s computation is Future.isDone()
        complete or, if the computation is already complete, immediately.
        
        There is no guaranteed ordering of execution of listeners, but any listener added through
        this method is guaranteed to be called once the computation is complete.
        
        Exceptions thrown by a listener will be propagated up to the executor. Any exception thrown
        during `Executor.execute` (e.g., a `RejectedExecutionException` or an exception
        thrown by MoreExecutors.directExecutor direct execution) will be caught and
        logged.
        
        Note: If your listener is lightweight -- and will not cause stack overflow by completing
        more futures or adding more `directExecutor()` listeners inline -- consider MoreExecutors.directExecutor. Otherwise, avoid it: See the warnings on the docs for `directExecutor`.
        
        This is the most general listener interface. For common operations performed using
        listeners, see Futures. For a simplified but general listener interface, see Futures.addCallback addCallback().
        
        Memory consistency effects: Actions in a thread prior to adding a listener <a
        href="https://docs.oracle.com/javase/specs/jls/se7/html/jls-17.html#jls-17.4.5">
        *happen-before*</a> its execution begins, perhaps in another thread.
        
        Guava implementations of `ListenableFuture` promptly release references to listeners
        after executing them.

        Arguments
        - listener: the listener to run when the computation is complete
        - executor: the executor to run the listener in

        Raises
        - RejectedExecutionException: if we tried to execute the listener immediately but the
            executor rejected it.
        """
        ...
