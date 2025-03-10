"""
Python module generated from Java source file com.google.common.util.concurrent.Uninterruptibles

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import GwtIncompatible
from com.google.common.base import Preconditions
from com.google.common.util.concurrent import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.util.concurrent import BlockingQueue
from java.util.concurrent import CancellationException
from java.util.concurrent import CountDownLatch
from java.util.concurrent import ExecutionException
from java.util.concurrent import Future
from java.util.concurrent import Semaphore
from java.util.concurrent import TimeUnit
from java.util.concurrent import TimeoutException
from typing import Any, Callable, Iterable, Tuple


class Uninterruptibles:
    """
    Utilities for treating interruptible operations as uninterruptible. In all cases, if a thread is
    interrupted during such a call, the call continues to block until the result is available or the
    timeout elapses, and only then re-interrupts the thread.

    Author(s)
    - Anthony Zana

    Since
    - 10.0
    """

    @staticmethod
    def awaitUninterruptibly(latch: "CountDownLatch") -> None:
        """
        Invokes `latch.`CountDownLatch.await() await() uninterruptibly.
        """
        ...


    @staticmethod
    def awaitUninterruptibly(latch: "CountDownLatch", timeout: int, unit: "TimeUnit") -> bool:
        """
        Invokes `latch.`CountDownLatch.await(long, TimeUnit) await(timeout, unit)
        uninterruptibly.
        """
        ...


    @staticmethod
    def joinUninterruptibly(toJoin: "Thread") -> None:
        """
        Invokes `toJoin.`Thread.join() join() uninterruptibly.
        """
        ...


    @staticmethod
    def getUninterruptibly(future: "Future"["V"]) -> "V":
        """
        Invokes `future.`Future.get() get() uninterruptibly.
        
        Similar methods:
        
        
        - To retrieve a result from a `Future` that is already done, use
            Futures.getDone Futures.getDone.
        - To treat InterruptedException uniformly with other exceptions, use
            Futures.getChecked(Future, Class) Futures.getChecked.
        - To get uninterruptibility and remove checked exceptions, use Futures.getUnchecked.

        Raises
        - ExecutionException: if the computation threw an exception
        - CancellationException: if the computation was cancelled
        """
        ...


    @staticmethod
    def getUninterruptibly(future: "Future"["V"], timeout: int, unit: "TimeUnit") -> "V":
        """
        Invokes `future.`Future.get(long, TimeUnit) get(timeout, unit) uninterruptibly.
        
        Similar methods:
        
        
        - To retrieve a result from a `Future` that is already done, use
            Futures.getDone Futures.getDone.
        - To treat InterruptedException uniformly with other exceptions, use
            Futures.getChecked(Future, Class, long, TimeUnit) Futures.getChecked.
        - To get uninterruptibility and remove checked exceptions, use Futures.getUnchecked.

        Raises
        - ExecutionException: if the computation threw an exception
        - CancellationException: if the computation was cancelled
        - TimeoutException: if the wait timed out
        """
        ...


    @staticmethod
    def joinUninterruptibly(toJoin: "Thread", timeout: int, unit: "TimeUnit") -> None:
        """
        Invokes `unit.`TimeUnit.timedJoin(Thread, long) timedJoin(toJoin, timeout)
        uninterruptibly.
        """
        ...


    @staticmethod
    def takeUninterruptibly(queue: "BlockingQueue"["E"]) -> "E":
        """
        Invokes `queue.`BlockingQueue.take() take() uninterruptibly.
        """
        ...


    @staticmethod
    def putUninterruptibly(queue: "BlockingQueue"["E"], element: "E") -> None:
        """
        Invokes `queue.`BlockingQueue.put(Object) put(element) uninterruptibly.

        Raises
        - ClassCastException: if the class of the specified element prevents it from being added
            to the given queue
        - IllegalArgumentException: if some property of the specified element prevents it from
            being added to the given queue
        """
        ...


    @staticmethod
    def sleepUninterruptibly(sleepFor: int, unit: "TimeUnit") -> None:
        """
        Invokes `unit.`TimeUnit.sleep(long) sleep(sleepFor) uninterruptibly.
        """
        ...


    @staticmethod
    def tryAcquireUninterruptibly(semaphore: "Semaphore", timeout: int, unit: "TimeUnit") -> bool:
        """
        Invokes `semaphore.`Semaphore.tryAcquire(int, long, TimeUnit) tryAcquire(1,
        timeout, unit) uninterruptibly.

        Since
        - 18.0
        """
        ...


    @staticmethod
    def tryAcquireUninterruptibly(semaphore: "Semaphore", permits: int, timeout: int, unit: "TimeUnit") -> bool:
        """
        Invokes `semaphore.`Semaphore.tryAcquire(int, long, TimeUnit) tryAcquire(permits,
        timeout, unit) uninterruptibly.

        Since
        - 18.0
        """
        ...
