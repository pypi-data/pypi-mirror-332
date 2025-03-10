"""
Python module generated from Java source file com.google.common.util.concurrent.JdkFutureAdapters

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtIncompatible
from com.google.common.util.concurrent import *
from java.util.concurrent import Executor
from java.util.concurrent import Executors
from java.util.concurrent import Future
from java.util.concurrent import ThreadFactory
from java.util.concurrent.atomic import AtomicBoolean
from typing import Any, Callable, Iterable, Tuple


class JdkFutureAdapters:
    """
    Utilities necessary for working with libraries that supply plain Future instances. Note
    that, whenever possible, it is strongly preferred to modify those libraries to return `ListenableFuture` directly.

    Author(s)
    - Sven Mawson

    Since
    - 10.0 (replacing `Futures.makeListenable`, which existed in 1.0)
    """

    @staticmethod
    def listenInPoolThread(future: "Future"["V"]) -> "ListenableFuture"["V"]:
        """
        Assigns a thread to the given Future to provide ListenableFuture functionality.
        
        **Warning:** If the input future does not already implement `ListenableFuture`, the
        returned future will emulate ListenableFuture.addListener by taking a thread from an
        internal, unbounded pool at the first call to `addListener` and holding it until the
        future is Future.isDone() done.
        
        Prefer to create `ListenableFuture` instances with SettableFuture, MoreExecutors.listeningDecorator( java.util.concurrent.ExecutorService), ListenableFutureTask, AbstractFuture, and other utilities over creating plain `Future` instances to be upgraded to `ListenableFuture` after the fact.
        """
        ...


    @staticmethod
    def listenInPoolThread(future: "Future"["V"], executor: "Executor") -> "ListenableFuture"["V"]:
        """
        Submits a blocking task for the given Future to provide ListenableFuture
        functionality.
        
        **Warning:** If the input future does not already implement `ListenableFuture`, the
        returned future will emulate ListenableFuture.addListener by submitting a task to the
        given executor at the first call to `addListener`. The task must be started by the
        executor promptly, or else the returned `ListenableFuture` may fail to work. The task's
        execution consists of blocking until the input future is Future.isDone() done, so
        each call to this method may claim and hold a thread for an arbitrary length of time. Use of
        bounded executors or other executors that may fail to execute a task promptly may result in
        deadlocks.
        
        Prefer to create `ListenableFuture` instances with SettableFuture, MoreExecutors.listeningDecorator( java.util.concurrent.ExecutorService), ListenableFutureTask, AbstractFuture, and other utilities over creating plain `Future` instances to be upgraded to `ListenableFuture` after the fact.

        Since
        - 12.0
        """
        ...
