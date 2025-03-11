"""
Python module generated from Java source file java.util.concurrent.locks.ReentrantReadWriteLock

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util.concurrent import TimeUnit
from java.util.concurrent.locks import *
from jdk.internal.vm.annotation import ReservedStackAccess
from typing import Any, Callable, Iterable, Tuple


class ReentrantReadWriteLock(ReadWriteLock, Serializable):
    """
    An implementation of ReadWriteLock supporting similar
    semantics to ReentrantLock.
    This class has the following properties:
    
    
    - **Acquisition order**
    
    This class does not impose a reader or writer preference
    ordering for lock access.  However, it does support an optional
    *fairness* policy.
    
    <dl>
    <dt>***Non-fair mode (default)***
    <dd>When constructed as non-fair (the default), the order of entry
    to the read and write lock is unspecified, subject to reentrancy
    constraints.  A nonfair lock that is continuously contended may
    indefinitely postpone one or more reader or writer threads, but
    will normally have higher throughput than a fair lock.
    
    <dt>***Fair mode***
    <dd>When constructed as fair, threads contend for entry using an
    approximately arrival-order policy. When the currently held lock
    is released, either the longest-waiting single writer thread will
    be assigned the write lock, or if there is a group of reader threads
    waiting longer than all waiting writer threads, that group will be
    assigned the read lock.
    
    A thread that tries to acquire a fair read lock (non-reentrantly)
    will block if either the write lock is held, or there is a waiting
    writer thread. The thread will not acquire the read lock until
    after the oldest currently waiting writer thread has acquired and
    released the write lock. Of course, if a waiting writer abandons
    its wait, leaving one or more reader threads as the longest waiters
    in the queue with the write lock free, then those readers will be
    assigned the read lock.
    
    A thread that tries to acquire a fair write lock (non-reentrantly)
    will block unless both the read lock and write lock are free (which
    implies there are no waiting threads).  (Note that the non-blocking
    ReadLock.tryLock() and WriteLock.tryLock() methods
    do not honor this fair setting and will immediately acquire the lock
    if it is possible, regardless of waiting threads.)
    </dl>
    
    - **Reentrancy**
    
    This lock allows both readers and writers to reacquire read or
    write locks in the style of a ReentrantLock. Non-reentrant
    readers are not allowed until all write locks held by the writing
    thread have been released.
    
    Additionally, a writer can acquire the read lock, but not
    vice-versa.  Among other applications, reentrancy can be useful
    when write locks are held during calls or callbacks to methods that
    perform reads under read locks.  If a reader tries to acquire the
    write lock it will never succeed.
    
    - **Lock downgrading**
    Reentrancy also allows downgrading from the write lock to a read lock,
    by acquiring the write lock, then the read lock and then releasing the
    write lock. However, upgrading from a read lock to the write lock is
    **not** possible.
    
    - **Interruption of lock acquisition**
    The read lock and write lock both support interruption during lock
    acquisition.
    
    - **Condition support**
    The write lock provides a Condition implementation that
    behaves in the same way, with respect to the write lock, as the
    Condition implementation provided by
    ReentrantLock.newCondition does for ReentrantLock.
    This Condition can, of course, only be used with the write lock.
    
    The read lock does not support a Condition and
    `readLock().newCondition()` throws
    `UnsupportedOperationException`.
    
    - **Instrumentation**
    This class supports methods to determine whether locks
    are held or contended. These methods are designed for monitoring
    system state, not for synchronization control.
    
    
    Serialization of this class behaves in the same way as built-in
    locks: a deserialized lock is in the unlocked state, regardless of
    its state when serialized.
    
    **Sample usages.** Here is a code sketch showing how to perform
    lock downgrading after updating a cache (exception handling is
    particularly tricky when handling multiple locks in a non-nested
    fashion):
    
    ``` `class CachedData {
      Object data;
      boolean cacheValid;
      final ReentrantReadWriteLock rwl = new ReentrantReadWriteLock();
    
      void processCachedData() {
        rwl.readLock().lock();
        if (!cacheValid) {
          // Must release read lock before acquiring write lock
          rwl.readLock().unlock();
          rwl.writeLock().lock();
          try {
            // Recheck state because another thread might have
            // acquired write lock and changed state before we did.
            if (!cacheValid) {
              data = ...;
              cacheValid = True;`
            // Downgrade by acquiring read lock before releasing write lock
            rwl.readLock().lock();
          } finally {
            rwl.writeLock().unlock(); // Unlock write, still hold read
          }
        }
    
        try {
          use(data);
        } finally {
          rwl.readLock().unlock();
        }
      }
    }}```
    
    ReentrantReadWriteLocks can be used to improve concurrency in some
    uses of some kinds of Collections. This is typically worthwhile
    only when the collections are expected to be large, accessed by
    more reader threads than writer threads, and entail operations with
    overhead that outweighs synchronization overhead. For example, here
    is a class using a TreeMap that is expected to be large and
    concurrently accessed.
    
    ``` `class RWDictionary {
      private final Map<String, Data> m = new TreeMap<>();
      private final ReentrantReadWriteLock rwl = new ReentrantReadWriteLock();
      private final Lock r = rwl.readLock();
      private final Lock w = rwl.writeLock();
    
      public Data get(String key) {
        r.lock();
        try { return m.get(key);`
        finally { r.unlock(); }
      }
      public List<String> allKeys() {
        r.lock();
        try { return new ArrayList<>(m.keySet()); }
        finally { r.unlock(); }
      }
      public Data put(String key, Data value) {
        w.lock();
        try { return m.put(key, value); }
        finally { w.unlock(); }
      }
      public void clear() {
        w.lock();
        try { m.clear(); }
        finally { w.unlock(); }
      }
    }}```
    
    <h2>Implementation Notes</h2>
    
    This lock supports a maximum of 65535 recursive write locks
    and 65535 read locks. Attempts to exceed these limits result in
    Error throws from locking methods.

    Author(s)
    - Doug Lea

    Since
    - 1.5
    """

    def __init__(self):
        """
        Creates a new `ReentrantReadWriteLock` with
        default (nonfair) ordering properties.
        """
        ...


    def __init__(self, fair: bool):
        """
        Creates a new `ReentrantReadWriteLock` with
        the given fairness policy.

        Arguments
        - fair: `True` if this lock should use a fair ordering policy
        """
        ...


    def writeLock(self) -> "ReentrantReadWriteLock.WriteLock":
        ...


    def readLock(self) -> "ReentrantReadWriteLock.ReadLock":
        ...


    def isFair(self) -> bool:
        """
        Returns `True` if this lock has fairness set True.

        Returns
        - `True` if this lock has fairness set True
        """
        ...


    def getReadLockCount(self) -> int:
        """
        Queries the number of read locks held for this lock. This
        method is designed for use in monitoring system state, not for
        synchronization control.

        Returns
        - the number of read locks held
        """
        ...


    def isWriteLocked(self) -> bool:
        """
        Queries if the write lock is held by any thread. This method is
        designed for use in monitoring system state, not for
        synchronization control.

        Returns
        - `True` if any thread holds the write lock and
                `False` otherwise
        """
        ...


    def isWriteLockedByCurrentThread(self) -> bool:
        """
        Queries if the write lock is held by the current thread.

        Returns
        - `True` if the current thread holds the write lock and
                `False` otherwise
        """
        ...


    def getWriteHoldCount(self) -> int:
        """
        Queries the number of reentrant write holds on this lock by the
        current thread.  A writer thread has a hold on a lock for
        each lock action that is not matched by an unlock action.

        Returns
        - the number of holds on the write lock by the current thread,
                or zero if the write lock is not held by the current thread
        """
        ...


    def getReadHoldCount(self) -> int:
        """
        Queries the number of reentrant read holds on this lock by the
        current thread.  A reader thread has a hold on a lock for
        each lock action that is not matched by an unlock action.

        Returns
        - the number of holds on the read lock by the current thread,
                or zero if the read lock is not held by the current thread

        Since
        - 1.6
        """
        ...


    def hasQueuedThreads(self) -> bool:
        """
        Queries whether any threads are waiting to acquire the read or
        write lock. Note that because cancellations may occur at any
        time, a `True` return does not guarantee that any other
        thread will ever acquire a lock.  This method is designed
        primarily for use in monitoring of the system state.

        Returns
        - `True` if there may be other threads waiting to
                acquire the lock
        """
        ...


    def hasQueuedThread(self, thread: "Thread") -> bool:
        """
        Queries whether the given thread is waiting to acquire either
        the read or write lock. Note that because cancellations may
        occur at any time, a `True` return does not guarantee
        that this thread will ever acquire a lock.  This method is
        designed primarily for use in monitoring of the system state.

        Arguments
        - thread: the thread

        Returns
        - `True` if the given thread is queued waiting for this lock

        Raises
        - NullPointerException: if the thread is null
        """
        ...


    def getQueueLength(self) -> int:
        """
        Returns an estimate of the number of threads waiting to acquire
        either the read or write lock.  The value is only an estimate
        because the number of threads may change dynamically while this
        method traverses internal data structures.  This method is
        designed for use in monitoring system state, not for
        synchronization control.

        Returns
        - the estimated number of threads waiting for this lock
        """
        ...


    def hasWaiters(self, condition: "Condition") -> bool:
        """
        Queries whether any threads are waiting on the given condition
        associated with the write lock. Note that because timeouts and
        interrupts may occur at any time, a `True` return does
        not guarantee that a future `signal` will awaken any
        threads.  This method is designed primarily for use in
        monitoring of the system state.

        Arguments
        - condition: the condition

        Returns
        - `True` if there are any waiting threads

        Raises
        - IllegalMonitorStateException: if this lock is not held
        - IllegalArgumentException: if the given condition is
                not associated with this lock
        - NullPointerException: if the condition is null
        """
        ...


    def getWaitQueueLength(self, condition: "Condition") -> int:
        """
        Returns an estimate of the number of threads waiting on the
        given condition associated with the write lock. Note that because
        timeouts and interrupts may occur at any time, the estimate
        serves only as an upper bound on the actual number of waiters.
        This method is designed for use in monitoring of the system
        state, not for synchronization control.

        Arguments
        - condition: the condition

        Returns
        - the estimated number of waiting threads

        Raises
        - IllegalMonitorStateException: if this lock is not held
        - IllegalArgumentException: if the given condition is
                not associated with this lock
        - NullPointerException: if the condition is null
        """
        ...


    def toString(self) -> str:
        """
        Returns a string identifying this lock, as well as its lock state.
        The state, in brackets, includes the String `"Write locks ="`
        followed by the number of reentrantly held write locks, and the
        String `"Read locks ="` followed by the number of held
        read locks.

        Returns
        - a string identifying this lock, as well as its lock state
        """
        ...


    class ReadLock(Lock, Serializable):
        """
        The lock returned by method ReentrantReadWriteLock.readLock.
        """

        def lock(self) -> None:
            """
            Acquires the read lock.
            
            Acquires the read lock if the write lock is not held by
            another thread and returns immediately.
            
            If the write lock is held by another thread then
            the current thread becomes disabled for thread scheduling
            purposes and lies dormant until the read lock has been acquired.
            """
            ...


        def lockInterruptibly(self) -> None:
            """
            Acquires the read lock unless the current thread is
            Thread.interrupt interrupted.
            
            Acquires the read lock if the write lock is not held
            by another thread and returns immediately.
            
            If the write lock is held by another thread then the
            current thread becomes disabled for thread scheduling
            purposes and lies dormant until one of two things happens:
            
            
            
            - The read lock is acquired by the current thread; or
            
            - Some other thread Thread.interrupt interrupts
            the current thread.
            
            
            
            If the current thread:
            
            
            
            - has its interrupted status set on entry to this method; or
            
            - is Thread.interrupt interrupted while
            acquiring the read lock,
            
            
            
            then InterruptedException is thrown and the current
            thread's interrupted status is cleared.
            
            In this implementation, as this method is an explicit
            interruption point, preference is given to responding to
            the interrupt over normal or reentrant acquisition of the
            lock.

            Raises
            - InterruptedException: if the current thread is interrupted
            """
            ...


        def tryLock(self) -> bool:
            """
            Acquires the read lock only if the write lock is not held by
            another thread at the time of invocation.
            
            Acquires the read lock if the write lock is not held by
            another thread and returns immediately with the value
            `True`. Even when this lock has been set to use a
            fair ordering policy, a call to `tryLock()`
            *will* immediately acquire the read lock if it is
            available, whether or not other threads are currently
            waiting for the read lock.  This &quot;barging&quot; behavior
            can be useful in certain circumstances, even though it
            breaks fairness. If you want to honor the fairness setting
            for this lock, then use .tryLock(long, TimeUnit)
            tryLock(0, TimeUnit.SECONDS) which is almost equivalent
            (it also detects interruption).
            
            If the write lock is held by another thread then
            this method will return immediately with the value
            `False`.

            Returns
            - `True` if the read lock was acquired
            """
            ...


        def tryLock(self, timeout: int, unit: "TimeUnit") -> bool:
            """
            Acquires the read lock if the write lock is not held by
            another thread within the given waiting time and the
            current thread has not been Thread.interrupt
            interrupted.
            
            Acquires the read lock if the write lock is not held by
            another thread and returns immediately with the value
            `True`. If this lock has been set to use a fair
            ordering policy then an available lock *will not* be
            acquired if any other threads are waiting for the
            lock. This is in contrast to the .tryLock()
            method. If you want a timed `tryLock` that does
            permit barging on a fair lock then combine the timed and
            un-timed forms together:
            
            ``` `if (lock.tryLock() ||
                lock.tryLock(timeout, unit)) {
              ...`}```
            
            If the write lock is held by another thread then the
            current thread becomes disabled for thread scheduling
            purposes and lies dormant until one of three things happens:
            
            
            
            - The read lock is acquired by the current thread; or
            
            - Some other thread Thread.interrupt interrupts
            the current thread; or
            
            - The specified waiting time elapses.
            
            
            
            If the read lock is acquired then the value `True` is
            returned.
            
            If the current thread:
            
            
            
            - has its interrupted status set on entry to this method; or
            
            - is Thread.interrupt interrupted while
            acquiring the read lock,
            
             then InterruptedException is thrown and the
            current thread's interrupted status is cleared.
            
            If the specified waiting time elapses then the value
            `False` is returned.  If the time is less than or
            equal to zero, the method will not wait at all.
            
            In this implementation, as this method is an explicit
            interruption point, preference is given to responding to
            the interrupt over normal or reentrant acquisition of the
            lock, and over reporting the elapse of the waiting time.

            Arguments
            - timeout: the time to wait for the read lock
            - unit: the time unit of the timeout argument

            Returns
            - `True` if the read lock was acquired

            Raises
            - InterruptedException: if the current thread is interrupted
            - NullPointerException: if the time unit is null
            """
            ...


        def unlock(self) -> None:
            """
            Attempts to release this lock.
            
            If the number of readers is now zero then the lock
            is made available for write lock attempts. If the current
            thread does not hold this lock then IllegalMonitorStateException is thrown.

            Raises
            - IllegalMonitorStateException: if the current thread
            does not hold this lock
            """
            ...


        def newCondition(self) -> "Condition":
            """
            Throws `UnsupportedOperationException` because
            `ReadLocks` do not support conditions.

            Raises
            - UnsupportedOperationException: always
            """
            ...


        def toString(self) -> str:
            """
            Returns a string identifying this lock, as well as its lock state.
            The state, in brackets, includes the String `"Read locks ="`
            followed by the number of held read locks.

            Returns
            - a string identifying this lock, as well as its lock state
            """
            ...


    class WriteLock(Lock, Serializable):
        """
        The lock returned by method ReentrantReadWriteLock.writeLock.
        """

        def lock(self) -> None:
            """
            Acquires the write lock.
            
            Acquires the write lock if neither the read nor write lock
            are held by another thread
            and returns immediately, setting the write lock hold count to
            one.
            
            If the current thread already holds the write lock then the
            hold count is incremented by one and the method returns
            immediately.
            
            If the lock is held by another thread then the current
            thread becomes disabled for thread scheduling purposes and
            lies dormant until the write lock has been acquired, at which
            time the write lock hold count is set to one.
            """
            ...


        def lockInterruptibly(self) -> None:
            """
            Acquires the write lock unless the current thread is
            Thread.interrupt interrupted.
            
            Acquires the write lock if neither the read nor write lock
            are held by another thread
            and returns immediately, setting the write lock hold count to
            one.
            
            If the current thread already holds this lock then the
            hold count is incremented by one and the method returns
            immediately.
            
            If the lock is held by another thread then the current
            thread becomes disabled for thread scheduling purposes and
            lies dormant until one of two things happens:
            
            
            
            - The write lock is acquired by the current thread; or
            
            - Some other thread Thread.interrupt interrupts
            the current thread.
            
            
            
            If the write lock is acquired by the current thread then the
            lock hold count is set to one.
            
            If the current thread:
            
            
            
            - has its interrupted status set on entry to this method;
            or
            
            - is Thread.interrupt interrupted while
            acquiring the write lock,
            
            
            
            then InterruptedException is thrown and the current
            thread's interrupted status is cleared.
            
            In this implementation, as this method is an explicit
            interruption point, preference is given to responding to
            the interrupt over normal or reentrant acquisition of the
            lock.

            Raises
            - InterruptedException: if the current thread is interrupted
            """
            ...


        def tryLock(self) -> bool:
            """
            Acquires the write lock only if it is not held by another thread
            at the time of invocation.
            
            Acquires the write lock if neither the read nor write lock
            are held by another thread
            and returns immediately with the value `True`,
            setting the write lock hold count to one. Even when this lock has
            been set to use a fair ordering policy, a call to
            `tryLock()` *will* immediately acquire the
            lock if it is available, whether or not other threads are
            currently waiting for the write lock.  This &quot;barging&quot;
            behavior can be useful in certain circumstances, even
            though it breaks fairness. If you want to honor the
            fairness setting for this lock, then use .tryLock(long, TimeUnit) tryLock(0, TimeUnit.SECONDS)
            which is almost equivalent (it also detects interruption).
            
            If the current thread already holds this lock then the
            hold count is incremented by one and the method returns
            `True`.
            
            If the lock is held by another thread then this method
            will return immediately with the value `False`.

            Returns
            - `True` if the lock was free and was acquired
            by the current thread, or the write lock was already held
            by the current thread; and `False` otherwise.
            """
            ...


        def tryLock(self, timeout: int, unit: "TimeUnit") -> bool:
            """
            Acquires the write lock if it is not held by another thread
            within the given waiting time and the current thread has
            not been Thread.interrupt interrupted.
            
            Acquires the write lock if neither the read nor write lock
            are held by another thread
            and returns immediately with the value `True`,
            setting the write lock hold count to one. If this lock has been
            set to use a fair ordering policy then an available lock
            *will not* be acquired if any other threads are
            waiting for the write lock. This is in contrast to the .tryLock() method. If you want a timed `tryLock`
            that does permit barging on a fair lock then combine the
            timed and un-timed forms together:
            
            ``` `if (lock.tryLock() ||
                lock.tryLock(timeout, unit)) {
              ...`}```
            
            If the current thread already holds this lock then the
            hold count is incremented by one and the method returns
            `True`.
            
            If the lock is held by another thread then the current
            thread becomes disabled for thread scheduling purposes and
            lies dormant until one of three things happens:
            
            
            
            - The write lock is acquired by the current thread; or
            
            - Some other thread Thread.interrupt interrupts
            the current thread; or
            
            - The specified waiting time elapses
            
            
            
            If the write lock is acquired then the value `True` is
            returned and the write lock hold count is set to one.
            
            If the current thread:
            
            
            
            - has its interrupted status set on entry to this method;
            or
            
            - is Thread.interrupt interrupted while
            acquiring the write lock,
            
            
            
            then InterruptedException is thrown and the current
            thread's interrupted status is cleared.
            
            If the specified waiting time elapses then the value
            `False` is returned.  If the time is less than or
            equal to zero, the method will not wait at all.
            
            In this implementation, as this method is an explicit
            interruption point, preference is given to responding to
            the interrupt over normal or reentrant acquisition of the
            lock, and over reporting the elapse of the waiting time.

            Arguments
            - timeout: the time to wait for the write lock
            - unit: the time unit of the timeout argument

            Returns
            - `True` if the lock was free and was acquired
            by the current thread, or the write lock was already held by the
            current thread; and `False` if the waiting time
            elapsed before the lock could be acquired.

            Raises
            - InterruptedException: if the current thread is interrupted
            - NullPointerException: if the time unit is null
            """
            ...


        def unlock(self) -> None:
            """
            Attempts to release this lock.
            
            If the current thread is the holder of this lock then
            the hold count is decremented. If the hold count is now
            zero then the lock is released.  If the current thread is
            not the holder of this lock then IllegalMonitorStateException is thrown.

            Raises
            - IllegalMonitorStateException: if the current thread does not
            hold this lock
            """
            ...


        def newCondition(self) -> "Condition":
            """
            Returns a Condition instance for use with this
            Lock instance.
            The returned Condition instance supports the same
            usages as do the Object monitor methods (Object.wait() wait, Object.notify notify, and Object.notifyAll notifyAll) when used with the built-in
            monitor lock.
            
            
            
            - If this write lock is not held when any Condition method is called then an IllegalMonitorStateException is thrown.  (Read locks are
            held independently of write locks, so are not checked or
            affected. However it is essentially always an error to
            invoke a condition waiting method when the current thread
            has also acquired read locks, since other threads that
            could unblock it will not be able to acquire the write
            lock.)
            
            - When the condition Condition.await() waiting
            methods are called the write lock is released and, before
            they return, the write lock is reacquired and the lock hold
            count restored to what it was when the method was called.
            
            - If a thread is Thread.interrupt interrupted while
            waiting then the wait will terminate, an InterruptedException will be thrown, and the thread's
            interrupted status will be cleared.
            
            - Waiting threads are signalled in FIFO order.
            
            - The ordering of lock reacquisition for threads returning
            from waiting methods is the same as for threads initially
            acquiring the lock, which is in the default case not specified,
            but for *fair* locks favors those threads that have been
            waiting the longest.
            

            Returns
            - the Condition object
            """
            ...


        def toString(self) -> str:
            """
            Returns a string identifying this lock, as well as its lock
            state.  The state, in brackets includes either the String
            `"Unlocked"` or the String `"Locked by"`
            followed by the Thread.getName name of the owning thread.

            Returns
            - a string identifying this lock, as well as its lock state
            """
            ...


        def isHeldByCurrentThread(self) -> bool:
            """
            Queries if this write lock is held by the current thread.
            Identical in effect to ReentrantReadWriteLock.isWriteLockedByCurrentThread.

            Returns
            - `True` if the current thread holds this lock and
                    `False` otherwise

            Since
            - 1.6
            """
            ...


        def getHoldCount(self) -> int:
            """
            Queries the number of holds on this write lock by the current
            thread.  A thread has a hold on a lock for each lock action
            that is not matched by an unlock action.  Identical in effect
            to ReentrantReadWriteLock.getWriteHoldCount.

            Returns
            - the number of holds on this lock by the current thread,
                    or zero if this lock is not held by the current thread

            Since
            - 1.6
            """
            ...
