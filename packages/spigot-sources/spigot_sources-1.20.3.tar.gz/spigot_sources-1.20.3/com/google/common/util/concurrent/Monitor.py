"""
Python module generated from Java source file com.google.common.util.concurrent.Monitor

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import J2ktIncompatible
from com.google.common.primitives import Longs
from com.google.common.util.concurrent import *
from com.google.errorprone.annotations.concurrent import GuardedBy
from com.google.j2objc.annotations import Weak
from java.time import Duration
from java.util.concurrent import TimeUnit
from java.util.concurrent.locks import Condition
from java.util.concurrent.locks import ReentrantLock
from java.util.function import BooleanSupplier
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class Monitor:
    """
    A synchronization abstraction supporting waiting on arbitrary boolean conditions.
    
    This class is intended as a replacement for ReentrantLock. Code using `Monitor`
    is less error-prone and more readable than code using `ReentrantLock`, without significant
    performance loss. `Monitor` even has the potential for performance gain by optimizing the
    evaluation and signaling of conditions. Signaling is entirely <a
    href="http://en.wikipedia.org/wiki/Monitor_(synchronization)#Implicit_signaling">implicit</a>. By
    eliminating explicit signaling, this class can guarantee that only one thread is awakened when a
    condition becomes True (no "signaling storms" due to use of java.util.concurrent.locks.Condition.signalAll Condition.signalAll) and that no signals are lost
    (no "hangs" due to incorrect use of java.util.concurrent.locks.Condition.signal
    Condition.signal).
    
    A thread is said to *occupy* a monitor if it has *entered* the monitor but not yet
    *left*. Only one thread may occupy a given monitor at any moment. A monitor is also
    reentrant, so a thread may enter a monitor any number of times, and then must leave the same
    number of times. The *enter* and *leave* operations have the same synchronization
    semantics as the built-in Java language synchronization primitives.
    
    A call to any of the *enter* methods with **void** return type should always be
    followed immediately by a *try/finally* block to ensure that the current thread leaves the
    monitor cleanly:
    
    ````monitor.enter();
    try {
      // do things while occupying the monitor` finally {
      monitor.leave();
    }
    }```
    
    A call to any of the *enter* methods with **boolean** return type should always appear
    as the condition of an *if* statement containing a *try/finally* block to ensure that
    the current thread leaves the monitor cleanly:
    
    ````if (monitor.tryEnter()) {
      try {
        // do things while occupying the monitor` finally {
        monitor.leave();
      }
    } else {
      // do other things since the monitor was not available
    }
    }```
    
    <h2>Comparison with `synchronized` and `ReentrantLock`</h2>
    
    The following examples show a simple threadsafe holder expressed using `synchronized`,
    ReentrantLock, and `Monitor`.
    
    <h3>`synchronized`</h3>
    
    This version is the fewest lines of code, largely because the synchronization mechanism used
    is built into the language and runtime. But the programmer has to remember to avoid a couple of
    common bugs: The `wait()` must be inside a `while` instead of an `if`, and
    `notifyAll()` must be used instead of `notify()` because there are two different
    logical conditions being awaited.
    
    ````public class SafeBox<V> {
      private V value;
    
      public synchronized V get() throws InterruptedException {
        while (value == null) {
          wait();`
        V result = value;
        value = null;
        notifyAll();
        return result;
      }
    
      public synchronized void set(V newValue) throws InterruptedException {
        while (value != null) {
          wait();
        }
        value = newValue;
        notifyAll();
      }
    }
    }```
    
    <h3>`ReentrantLock`</h3>
    
    This version is much more verbose than the `synchronized` version, and still suffers
    from the need for the programmer to remember to use `while` instead of `if`. However,
    one advantage is that we can introduce two separate `Condition` objects, which allows us to
    use `signal()` instead of `signalAll()`, which may be a performance benefit.
    
    ````public class SafeBox<V> {
      private V value;
      private final ReentrantLock lock = new ReentrantLock();
      private final Condition valuePresent = lock.newCondition();
      private final Condition valueAbsent = lock.newCondition();
    
      public V get() throws InterruptedException {
        lock.lock();
        try {
          while (value == null) {
            valuePresent.await();`
          V result = value;
          value = null;
          valueAbsent.signal();
          return result;
        } finally {
          lock.unlock();
        }
      }
    
      public void set(V newValue) throws InterruptedException {
        lock.lock();
        try {
          while (value != null) {
            valueAbsent.await();
          }
          value = newValue;
          valuePresent.signal();
        } finally {
          lock.unlock();
        }
      }
    }
    }```
    
    <h3>`Monitor`</h3>
    
    This version adds some verbosity around the `Guard` objects, but removes that same
    verbosity, and more, from the `get` and `set` methods. `Monitor` implements the
    same efficient signaling as we had to hand-code in the `ReentrantLock` version above.
    Finally, the programmer no longer has to hand-code the wait loop, and therefore doesn't have to
    remember to use `while` instead of `if`.
    
    ````public class SafeBox<V> {
      private V value;
      private final Monitor monitor = new Monitor();
      private final Monitor.Guard valuePresent = monitor.newGuard(() -> value != null);
      private final Monitor.Guard valueAbsent = monitor.newGuard(() -> value == null);
    
      public V get() throws InterruptedException {
        monitor.enterWhen(valuePresent);
        try {
          V result = value;
          value = null;
          return result;` finally {
          monitor.leave();
        }
      }
    
      public void set(V newValue) throws InterruptedException {
        monitor.enterWhen(valueAbsent);
        try {
          value = newValue;
        } finally {
          monitor.leave();
        }
      }
    }
    }```

    Author(s)
    - Martin Buchholz

    Since
    - 10.0
    """

    def __init__(self):
        """
        Creates a monitor with a non-fair (but fast) ordering policy. Equivalent to `Monitor(False)`.
        """
        ...


    def __init__(self, fair: bool):
        """
        Creates a monitor with the given ordering policy.

        Arguments
        - fair: whether this monitor should use a fair ordering policy rather than a non-fair (but
            fast) one
        """
        ...


    def newGuard(self, isSatisfied: "BooleanSupplier") -> "Guard":
        """
        Creates a new Guard guard for this monitor.

        Arguments
        - isSatisfied: the new guard's boolean condition (see Guard.isSatisfied
            isSatisfied())

        Since
        - 21.0
        """
        ...


    def enter(self) -> None:
        """
        Enters this monitor. Blocks indefinitely.
        """
        ...


    def enter(self, time: "Duration") -> bool:
        """
        Enters this monitor. Blocks at most the given time.

        Returns
        - whether the monitor was entered

        Since
        - 28.0
        """
        ...


    def enter(self, time: int, unit: "TimeUnit") -> bool:
        """
        Enters this monitor. Blocks at most the given time.

        Returns
        - whether the monitor was entered
        """
        ...


    def enterInterruptibly(self) -> None:
        """
        Enters this monitor. Blocks indefinitely, but may be interrupted.

        Raises
        - InterruptedException: if interrupted while waiting
        """
        ...


    def enterInterruptibly(self, time: "Duration") -> bool:
        """
        Enters this monitor. Blocks at most the given time, and may be interrupted.

        Returns
        - whether the monitor was entered

        Raises
        - InterruptedException: if interrupted while waiting

        Since
        - 28.0
        """
        ...


    def enterInterruptibly(self, time: int, unit: "TimeUnit") -> bool:
        """
        Enters this monitor. Blocks at most the given time, and may be interrupted.

        Returns
        - whether the monitor was entered

        Raises
        - InterruptedException: if interrupted while waiting
        """
        ...


    def tryEnter(self) -> bool:
        """
        Enters this monitor if it is possible to do so immediately. Does not block.
        
        **Note:** This method disregards the fairness setting of this monitor.

        Returns
        - whether the monitor was entered
        """
        ...


    def enterWhen(self, guard: "Guard") -> None:
        """
        Enters this monitor when the guard is satisfied. Blocks indefinitely, but may be interrupted.

        Raises
        - InterruptedException: if interrupted while waiting
        """
        ...


    def enterWhen(self, guard: "Guard", time: "Duration") -> bool:
        """
        Enters this monitor when the guard is satisfied. Blocks at most the given time, including both
        the time to acquire the lock and the time to wait for the guard to be satisfied, and may be
        interrupted.

        Returns
        - whether the monitor was entered, which guarantees that the guard is now satisfied

        Raises
        - InterruptedException: if interrupted while waiting

        Since
        - 28.0
        """
        ...


    def enterWhen(self, guard: "Guard", time: int, unit: "TimeUnit") -> bool:
        """
        Enters this monitor when the guard is satisfied. Blocks at most the given time, including both
        the time to acquire the lock and the time to wait for the guard to be satisfied, and may be
        interrupted.

        Returns
        - whether the monitor was entered, which guarantees that the guard is now satisfied

        Raises
        - InterruptedException: if interrupted while waiting
        """
        ...


    def enterWhenUninterruptibly(self, guard: "Guard") -> None:
        """
        Enters this monitor when the guard is satisfied. Blocks indefinitely.
        """
        ...


    def enterWhenUninterruptibly(self, guard: "Guard", time: "Duration") -> bool:
        """
        Enters this monitor when the guard is satisfied. Blocks at most the given time, including both
        the time to acquire the lock and the time to wait for the guard to be satisfied.

        Returns
        - whether the monitor was entered, which guarantees that the guard is now satisfied

        Since
        - 28.0
        """
        ...


    def enterWhenUninterruptibly(self, guard: "Guard", time: int, unit: "TimeUnit") -> bool:
        """
        Enters this monitor when the guard is satisfied. Blocks at most the given time, including both
        the time to acquire the lock and the time to wait for the guard to be satisfied.

        Returns
        - whether the monitor was entered, which guarantees that the guard is now satisfied
        """
        ...


    def enterIf(self, guard: "Guard") -> bool:
        """
        Enters this monitor if the guard is satisfied. Blocks indefinitely acquiring the lock, but does
        not wait for the guard to be satisfied.

        Returns
        - whether the monitor was entered, which guarantees that the guard is now satisfied
        """
        ...


    def enterIf(self, guard: "Guard", time: "Duration") -> bool:
        """
        Enters this monitor if the guard is satisfied. Blocks at most the given time acquiring the
        lock, but does not wait for the guard to be satisfied.

        Returns
        - whether the monitor was entered, which guarantees that the guard is now satisfied

        Since
        - 28.0
        """
        ...


    def enterIf(self, guard: "Guard", time: int, unit: "TimeUnit") -> bool:
        """
        Enters this monitor if the guard is satisfied. Blocks at most the given time acquiring the
        lock, but does not wait for the guard to be satisfied.

        Returns
        - whether the monitor was entered, which guarantees that the guard is now satisfied
        """
        ...


    def enterIfInterruptibly(self, guard: "Guard") -> bool:
        """
        Enters this monitor if the guard is satisfied. Blocks indefinitely acquiring the lock, but does
        not wait for the guard to be satisfied, and may be interrupted.

        Returns
        - whether the monitor was entered, which guarantees that the guard is now satisfied

        Raises
        - InterruptedException: if interrupted while waiting
        """
        ...


    def enterIfInterruptibly(self, guard: "Guard", time: "Duration") -> bool:
        """
        Enters this monitor if the guard is satisfied. Blocks at most the given time acquiring the
        lock, but does not wait for the guard to be satisfied, and may be interrupted.

        Returns
        - whether the monitor was entered, which guarantees that the guard is now satisfied

        Since
        - 28.0
        """
        ...


    def enterIfInterruptibly(self, guard: "Guard", time: int, unit: "TimeUnit") -> bool:
        """
        Enters this monitor if the guard is satisfied. Blocks at most the given time acquiring the
        lock, but does not wait for the guard to be satisfied, and may be interrupted.

        Returns
        - whether the monitor was entered, which guarantees that the guard is now satisfied
        """
        ...


    def tryEnterIf(self, guard: "Guard") -> bool:
        """
        Enters this monitor if it is possible to do so immediately and the guard is satisfied. Does not
        block acquiring the lock and does not wait for the guard to be satisfied.
        
        **Note:** This method disregards the fairness setting of this monitor.

        Returns
        - whether the monitor was entered, which guarantees that the guard is now satisfied
        """
        ...


    def waitFor(self, guard: "Guard") -> None:
        """
        Waits for the guard to be satisfied. Waits indefinitely, but may be interrupted. May be called
        only by a thread currently occupying this monitor.

        Raises
        - InterruptedException: if interrupted while waiting
        """
        ...


    def waitFor(self, guard: "Guard", time: "Duration") -> bool:
        """
        Waits for the guard to be satisfied. Waits at most the given time, and may be interrupted. May
        be called only by a thread currently occupying this monitor.

        Returns
        - whether the guard is now satisfied

        Raises
        - InterruptedException: if interrupted while waiting

        Since
        - 28.0
        """
        ...


    def waitFor(self, guard: "Guard", time: int, unit: "TimeUnit") -> bool:
        """
        Waits for the guard to be satisfied. Waits at most the given time, and may be interrupted. May
        be called only by a thread currently occupying this monitor.

        Returns
        - whether the guard is now satisfied

        Raises
        - InterruptedException: if interrupted while waiting
        """
        ...


    def waitForUninterruptibly(self, guard: "Guard") -> None:
        """
        Waits for the guard to be satisfied. Waits indefinitely. May be called only by a thread
        currently occupying this monitor.
        """
        ...


    def waitForUninterruptibly(self, guard: "Guard", time: "Duration") -> bool:
        """
        Waits for the guard to be satisfied. Waits at most the given time. May be called only by a
        thread currently occupying this monitor.

        Returns
        - whether the guard is now satisfied

        Since
        - 28.0
        """
        ...


    def waitForUninterruptibly(self, guard: "Guard", time: int, unit: "TimeUnit") -> bool:
        """
        Waits for the guard to be satisfied. Waits at most the given time. May be called only by a
        thread currently occupying this monitor.

        Returns
        - whether the guard is now satisfied
        """
        ...


    def leave(self) -> None:
        """
        Leaves this monitor. May be called only by a thread currently occupying this monitor.
        """
        ...


    def isFair(self) -> bool:
        """
        Returns whether this monitor is using a fair ordering policy.
        """
        ...


    def isOccupied(self) -> bool:
        """
        Returns whether this monitor is occupied by any thread. This method is designed for use in
        monitoring of the system state, not for synchronization control.
        """
        ...


    def isOccupiedByCurrentThread(self) -> bool:
        """
        Returns whether the current thread is occupying this monitor (has entered more times than it
        has left).
        """
        ...


    def getOccupiedDepth(self) -> int:
        """
        Returns the number of times the current thread has entered this monitor in excess of the number
        of times it has left. Returns 0 if the current thread is not occupying this monitor.
        """
        ...


    def getQueueLength(self) -> int:
        """
        Returns an estimate of the number of threads waiting to enter this monitor. The value is only
        an estimate because the number of threads may change dynamically while this method traverses
        internal data structures. This method is designed for use in monitoring of the system state,
        not for synchronization control.
        """
        ...


    def hasQueuedThreads(self) -> bool:
        """
        Returns whether any threads are waiting to enter this monitor. Note that because cancellations
        may occur at any time, a `True` return does not guarantee that any other thread will ever
        enter this monitor. This method is designed primarily for use in monitoring of the system
        state.
        """
        ...


    def hasQueuedThread(self, thread: "Thread") -> bool:
        """
        Queries whether the given thread is waiting to enter this monitor. Note that because
        cancellations may occur at any time, a `True` return does not guarantee that this thread
        will ever enter this monitor. This method is designed primarily for use in monitoring of the
        system state.
        """
        ...


    def hasWaiters(self, guard: "Guard") -> bool:
        """
        Queries whether any threads are waiting for the given guard to become satisfied. Note that
        because timeouts and interrupts may occur at any time, a `True` return does not guarantee
        that the guard becoming satisfied in the future will awaken any threads. This method is
        designed primarily for use in monitoring of the system state.
        """
        ...


    def getWaitQueueLength(self, guard: "Guard") -> int:
        """
        Returns an estimate of the number of threads waiting for the given guard to become satisfied.
        Note that because timeouts and interrupts may occur at any time, the estimate serves only as an
        upper bound on the actual number of waiters. This method is designed for use in monitoring of
        the system state, not for synchronization control.
        """
        ...


    class Guard:
        """
        A boolean condition for which a thread may wait. A `Guard` is associated with a single
        `Monitor`. The monitor may check the guard at arbitrary times from any thread occupying
        the monitor, so code should not be written to rely on how often a guard might or might not be
        checked.
        
        If a `Guard` is passed into any method of a `Monitor` other than the one it is
        associated with, an IllegalMonitorStateException is thrown.

        Since
        - 10.0
        """

        def isSatisfied(self) -> bool:
            """
            Evaluates this guard's boolean condition. This method is always called with the associated
            monitor already occupied. Implementations of this method must depend only on state protected
            by the associated monitor, and must not modify that state.
            """
            ...
