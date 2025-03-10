"""
Python module generated from Java source file com.google.common.util.concurrent.ExecutionSequencer

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.util.concurrent import *
from java.util.concurrent import Callable
from java.util.concurrent import Executor
from java.util.concurrent.atomic import AtomicReference
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class ExecutionSequencer:
    """
    Serializes execution of tasks, somewhat like an "asynchronous `synchronized` block." Each
    .submit enqueued callable will not be submitted to its associated executor until the
    previous callable has returned -- and, if the previous callable was an AsyncCallable, not
    until the `Future` it returned is Future.isDone done (successful, failed, or
    cancelled).
    
    This class has limited support for cancellation and other "early completion":
    
    
      - While calls to `submit` and `submitAsync` return a `Future` that can be
          cancelled, cancellation never propagates to a task that has started to run -- neither to
          the callable itself nor to any `Future` returned by an `AsyncCallable`.
          (However, cancellation can prevent an *unstarted* task from running.) Therefore, the
          next task will wait for any running callable (or pending `Future` returned by an
          `AsyncCallable`) to complete, without interrupting it (and without calling `cancel` on the `Future`). So beware: *Even if you cancel every precededing `Future` returned by this class, the next task may still have to wait.*.
      - Once an `AsyncCallable` returns a `Future`, this class considers that task to
          be "done" as soon as *that* `Future` completes in any way. Notably, a `Future` is "completed" even if it is cancelled while its underlying work continues on a
          thread, an RPC, etc. The `Future` is also "completed" if it fails "early" -- for
          example, if the deadline expires on a `Future` returned from Futures.withTimeout while the `Future` it wraps continues its underlying work. So
          beware: *Your `AsyncCallable` should not complete its `Future` until it is
          safe for the next task to start.*
    
    
    An additional limitation: this class serializes execution of *tasks* but not any
    *listeners* of those tasks.
    
    This class is similar to MoreExecutors.newSequentialExecutor. This class is different
    in a few ways:
    
    
      - Each task may be associated with a different executor.
      - Tasks may be of type `AsyncCallable`.
      - Running tasks *cannot* be interrupted. (Note that `newSequentialExecutor` does
          not return `Future` objects, so it doesn't support interruption directly, either.
          However, utilities that *use* that executor have the ability to interrupt tasks
          running on it. This class, by contrast, does not expose an `Executor` API.)
    
    
    If you don't need the features of this class, you may prefer `newSequentialExecutor` for
    its simplicity and ability to accommodate interruption.

    Since
    - 26.0
    """

    @staticmethod
    def create() -> "ExecutionSequencer":
        """
        Creates a new instance.
        """
        ...


    def submit(self, callable: "Callable"["T"], executor: "Executor") -> "ListenableFuture"["T"]:
        """
        Enqueues a task to run when the previous task (if any) completes.
        
        Cancellation does not propagate from the output future to a callable that has begun to
        execute, but if the output future is cancelled before Callable.call() is invoked,
        Callable.call() will not be invoked.
        """
        ...


    def submitAsync(self, callable: "AsyncCallable"["T"], executor: "Executor") -> "ListenableFuture"["T"]:
        """
        Enqueues a task to run when the previous task (if any) completes.
        
        Cancellation does not propagate from the output future to the future returned from `callable` or a callable that has begun to execute, but if the output future is cancelled before
        AsyncCallable.call() is invoked, AsyncCallable.call() will not be invoked.
        """
        ...
