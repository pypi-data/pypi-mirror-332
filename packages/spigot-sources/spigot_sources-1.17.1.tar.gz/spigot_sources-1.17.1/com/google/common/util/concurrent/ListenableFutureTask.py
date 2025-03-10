"""
Python module generated from Java source file com.google.common.util.concurrent.ListenableFutureTask

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.util.concurrent import *
from java.util.concurrent import Callable
from java.util.concurrent import Executor
from java.util.concurrent import FutureTask
from javax.annotation import Nullable
from typing import Any, Callable, Iterable, Tuple


class ListenableFutureTask(FutureTask, ListenableFuture):
    """
    A FutureTask that also implements the ListenableFuture interface. Unlike
    `FutureTask`, `ListenableFutureTask` does not provide an overrideable FutureTask.done() done() method. For similar functionality, call .addListener.
    
    Few users should use this class. It is intended primarily for those who are implementing an
    `ExecutorService`. Most users should call ListeningExecutorService.submit(Callable)
    ListeningExecutorService.submit on a service obtained from MoreExecutors.listeningDecorator.

    Author(s)
    - Sven Mawson

    Since
    - 1.0
    """

    @staticmethod
    def create(callable: "Callable"["V"]) -> "ListenableFutureTask"["V"]:
        """
        Creates a `ListenableFutureTask` that will upon running, execute the given `Callable`.

        Arguments
        - callable: the callable task

        Since
        - 10.0
        """
        ...


    @staticmethod
    def create(runnable: "Runnable", result: "V") -> "ListenableFutureTask"["V"]:
        """
        Creates a `ListenableFutureTask` that will upon running, execute the given `Runnable`, and arrange that `get` will return the given result on successful completion.

        Arguments
        - runnable: the runnable task
        - result: the result to return on successful completion. If you don't need a particular
            result, consider using constructions of the form: `ListenableFuture<?> f =
            ListenableFutureTask.create(runnable, null)`

        Since
        - 10.0
        """
        ...


    def addListener(self, listener: "Runnable", exec: "Executor") -> None:
        ...
