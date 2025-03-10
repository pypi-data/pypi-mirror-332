"""
Python module generated from Java source file com.google.common.util.concurrent.ListeningExecutorService

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.util.concurrent import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.util.concurrent import Callable
from java.util.concurrent import ExecutorService
from java.util.concurrent import Future
from java.util.concurrent import RejectedExecutionException
from java.util.concurrent import TimeUnit
from typing import Any, Callable, Iterable, Tuple


class ListeningExecutorService(ExecutorService):
    """
    An ExecutorService that returns ListenableFuture instances. To create an instance
    from an existing ExecutorService, call MoreExecutors.listeningDecorator(ExecutorService).

    Author(s)
    - Chris Povirk

    Since
    - 10.0
    """

    def submit(self, task: "Callable"["T"]) -> "ListenableFuture"["T"]:
        """
        Returns
        - a `ListenableFuture` representing pending completion of the task

        Raises
        - RejectedExecutionException: 
        """
        ...


    def submit(self, task: "Runnable") -> "ListenableFuture"[Any]:
        """
        Returns
        - a `ListenableFuture` representing pending completion of the task

        Raises
        - RejectedExecutionException: 
        """
        ...


    def submit(self, task: "Runnable", result: "T") -> "ListenableFuture"["T"]:
        """
        Returns
        - a `ListenableFuture` representing pending completion of the task

        Raises
        - RejectedExecutionException: 
        """
        ...


    def invokeAll(self, tasks: Iterable["Callable"["T"]]) -> list["Future"["T"]]:
        """
        
        
        All elements in the returned list must be ListenableFuture instances. The easiest
        way to obtain a `List<ListenableFuture<T>>` from this method is an unchecked (but safe)
        cast:```
          `@SuppressWarnings("unchecked") // guaranteed by invokeAll contract`
          `List<ListenableFuture<T>> futures = (List) executor.invokeAll(tasks);`
        ```

        Returns
        - A list of `ListenableFuture` instances representing the tasks, in the same
            sequential order as produced by the iterator for the given task list, each of which has
            completed.

        Raises
        - RejectedExecutionException: 
        - NullPointerException: if any task is null
        """
        ...


    def invokeAll(self, tasks: Iterable["Callable"["T"]], timeout: int, unit: "TimeUnit") -> list["Future"["T"]]:
        """
        
        
        All elements in the returned list must be ListenableFuture instances. The easiest
        way to obtain a `List<ListenableFuture<T>>` from this method is an unchecked (but safe)
        cast:```
          `@SuppressWarnings("unchecked") // guaranteed by invokeAll contract`
          `List<ListenableFuture<T>> futures = (List) executor.invokeAll(tasks, timeout, unit);`
        ```

        Returns
        - a list of `ListenableFuture` instances representing the tasks, in the same
            sequential order as produced by the iterator for the given task list. If the operation did
            not time out, each task will have completed. If it did time out, some of these tasks will
            not have completed.

        Raises
        - RejectedExecutionException: 
        - NullPointerException: if any task is null
        """
        ...
