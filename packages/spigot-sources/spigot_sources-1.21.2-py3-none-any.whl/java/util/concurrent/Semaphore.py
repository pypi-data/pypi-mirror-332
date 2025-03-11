"""
Python module generated from Java source file java.util.concurrent.Semaphore

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util.concurrent import *
from java.util.concurrent.locks import AbstractQueuedSynchronizer
from typing import Any, Callable, Iterable, Tuple


class Semaphore(Serializable):
    """
    A counting semaphore.  Conceptually, a semaphore maintains a set of
    permits.  Each .acquire blocks if necessary until a permit is
    available, and then takes it.  Each .release adds a permit,
    potentially releasing a blocking acquirer.
    However, no actual permit objects are used; the `Semaphore` just
    keeps a count of the number available and acts accordingly.
    
    Semaphores are often used to restrict the number of threads than can
    access some (physical or logical) resource. For example, here is
    a class that uses a semaphore to control access to a pool of items:
    ``` `class Pool {
      private static final int MAX_AVAILABLE = 100;
      private final Semaphore available = new Semaphore(MAX_AVAILABLE, True);
    
      public Object getItem() throws InterruptedException {
        available.acquire();
        return getNextAvailableItem();`
    
      public void putItem(Object x) {
        if (markAsUnused(x))
          available.release();
      }
    
      // Not a particularly efficient data structure; just for demo
    
      protected Object[] items = ...; // whatever kinds of items being managed
      protected boolean[] used = new boolean[MAX_AVAILABLE];
    
      protected synchronized Object getNextAvailableItem() {
        for (int i = 0; i < MAX_AVAILABLE; ++i) {
          if (!used[i]) {
            used[i] = True;
            return items[i];
          }
        }
        return null; // not reached
      }
    
      protected synchronized boolean markAsUnused(Object item) {
        for (int i = 0; i < MAX_AVAILABLE; ++i) {
          if (item == items[i]) {
            if (used[i]) {
              used[i] = False;
              return True;
            } else
              return False;
          }
        }
        return False;
      }
    }}```
    
    Before obtaining an item each thread must acquire a permit from
    the semaphore, guaranteeing that an item is available for use. When
    the thread has finished with the item it is returned back to the
    pool and a permit is returned to the semaphore, allowing another
    thread to acquire that item.  Note that no synchronization lock is
    held when .acquire is called as that would prevent an item
    from being returned to the pool.  The semaphore encapsulates the
    synchronization needed to restrict access to the pool, separately
    from any synchronization needed to maintain the consistency of the
    pool itself.
    
    A semaphore initialized to one, and which is used such that it
    only has at most one permit available, can serve as a mutual
    exclusion lock.  This is more commonly known as a *binary
    semaphore*, because it only has two states: one permit
    available, or zero permits available.  When used in this way, the
    binary semaphore has the property (unlike many java.util.concurrent.locks.Lock
    implementations), that the &quot;lock&quot; can be released by a
    thread other than the owner (as semaphores have no notion of
    ownership).  This can be useful in some specialized contexts, such
    as deadlock recovery.
    
    The constructor for this class optionally accepts a
    *fairness* parameter. When set False, this class makes no
    guarantees about the order in which threads acquire permits. In
    particular, *barging* is permitted, that is, a thread
    invoking .acquire can be allocated a permit ahead of a
    thread that has been waiting - logically the new thread places itself at
    the head of the queue of waiting threads. When fairness is set True, the
    semaphore guarantees that threads invoking any of the .acquire() acquire methods are selected to obtain permits in the order in
    which their invocation of those methods was processed
    (first-in-first-out; FIFO). Note that FIFO ordering necessarily
    applies to specific internal points of execution within these
    methods.  So, it is possible for one thread to invoke
    `acquire` before another, but reach the ordering point after
    the other, and similarly upon return from the method.
    Also note that the untimed .tryAcquire() tryAcquire methods do not
    honor the fairness setting, but will take any permits that are
    available.
    
    Generally, semaphores used to control resource access should be
    initialized as fair, to ensure that no thread is starved out from
    accessing a resource. When using semaphores for other kinds of
    synchronization control, the throughput advantages of non-fair
    ordering often outweigh fairness considerations.
    
    This class also provides convenience methods to .acquire(int) acquire and .release(int) release multiple
    permits at a time. These methods are generally more efficient and
    effective than loops. However, they do not establish any preference
    order. For example, if thread A invokes `s.acquire(3`) and
    thread B invokes `s.acquire(2)`, and two permits become
    available, then there is no guarantee that thread B will obtain
    them unless its acquire came first and Semaphore `s` is in
    fair mode.
    
    Memory consistency effects: Actions in a thread prior to calling
    a "release" method such as `release()`
    <a href="package-summary.html#MemoryVisibility">*happen-before*</a>
    actions following a successful "acquire" method such as `acquire()`
    in another thread.

    Author(s)
    - Doug Lea

    Since
    - 1.5
    """

    def __init__(self, permits: int):
        """
        Creates a `Semaphore` with the given number of
        permits and nonfair fairness setting.

        Arguments
        - permits: the initial number of permits available.
               This value may be negative, in which case releases
               must occur before any acquires will be granted.
        """
        ...


    def __init__(self, permits: int, fair: bool):
        """
        Creates a `Semaphore` with the given number of
        permits and the given fairness setting.

        Arguments
        - permits: the initial number of permits available.
               This value may be negative, in which case releases
               must occur before any acquires will be granted.
        - fair: `True` if this semaphore will guarantee
               first-in first-out granting of permits under contention,
               else `False`
        """
        ...


    def acquire(self) -> None:
        """
        Acquires a permit from this semaphore, blocking until one is
        available, or the thread is Thread.interrupt interrupted.
        
        Acquires a permit, if one is available and returns immediately,
        reducing the number of available permits by one.
        
        If no permit is available then the current thread becomes
        disabled for thread scheduling purposes and lies dormant until
        one of two things happens:
        
        - Some other thread invokes the .release method for this
        semaphore and the current thread is next to be assigned a permit; or
        - Some other thread Thread.interrupt interrupts
        the current thread.
        
        
        If the current thread:
        
        - has its interrupted status set on entry to this method; or
        - is Thread.interrupt interrupted while waiting
        for a permit,
        
        then InterruptedException is thrown and the current thread's
        interrupted status is cleared.

        Raises
        - InterruptedException: if the current thread is interrupted
        """
        ...


    def acquireUninterruptibly(self) -> None:
        """
        Acquires a permit from this semaphore, blocking until one is
        available.
        
        Acquires a permit, if one is available and returns immediately,
        reducing the number of available permits by one.
        
        If no permit is available then the current thread becomes
        disabled for thread scheduling purposes and lies dormant until
        some other thread invokes the .release method for this
        semaphore and the current thread is next to be assigned a permit.
        
        If the current thread is Thread.interrupt interrupted
        while waiting for a permit then it will continue to wait, but the
        time at which the thread is assigned a permit may change compared to
        the time it would have received the permit had no interruption
        occurred.  When the thread does return from this method its interrupt
        status will be set.
        """
        ...


    def tryAcquire(self) -> bool:
        """
        Acquires a permit from this semaphore, only if one is available at the
        time of invocation.
        
        Acquires a permit, if one is available and returns immediately,
        with the value `True`,
        reducing the number of available permits by one.
        
        If no permit is available then this method will return
        immediately with the value `False`.
        
        Even when this semaphore has been set to use a
        fair ordering policy, a call to `tryAcquire()` *will*
        immediately acquire a permit if one is available, whether or not
        other threads are currently waiting.
        This &quot;barging&quot; behavior can be useful in certain
        circumstances, even though it breaks fairness. If you want to honor
        the fairness setting, then use
        .tryAcquire(long, TimeUnit) tryAcquire(0, TimeUnit.SECONDS)
        which is almost equivalent (it also detects interruption).

        Returns
        - `True` if a permit was acquired and `False`
                otherwise
        """
        ...


    def tryAcquire(self, timeout: int, unit: "TimeUnit") -> bool:
        """
        Acquires a permit from this semaphore, if one becomes available
        within the given waiting time and the current thread has not
        been Thread.interrupt interrupted.
        
        Acquires a permit, if one is available and returns immediately,
        with the value `True`,
        reducing the number of available permits by one.
        
        If no permit is available then the current thread becomes
        disabled for thread scheduling purposes and lies dormant until
        one of three things happens:
        
        - Some other thread invokes the .release method for this
        semaphore and the current thread is next to be assigned a permit; or
        - Some other thread Thread.interrupt interrupts
        the current thread; or
        - The specified waiting time elapses.
        
        
        If a permit is acquired then the value `True` is returned.
        
        If the current thread:
        
        - has its interrupted status set on entry to this method; or
        - is Thread.interrupt interrupted while waiting
        to acquire a permit,
        
        then InterruptedException is thrown and the current thread's
        interrupted status is cleared.
        
        If the specified waiting time elapses then the value `False`
        is returned.  If the time is less than or equal to zero, the method
        will not wait at all.

        Arguments
        - timeout: the maximum time to wait for a permit
        - unit: the time unit of the `timeout` argument

        Returns
        - `True` if a permit was acquired and `False`
                if the waiting time elapsed before a permit was acquired

        Raises
        - InterruptedException: if the current thread is interrupted
        """
        ...


    def release(self) -> None:
        """
        Releases a permit, returning it to the semaphore.
        
        Releases a permit, increasing the number of available permits by
        one.  If any threads are trying to acquire a permit, then one is
        selected and given the permit that was just released.  That thread
        is (re)enabled for thread scheduling purposes.
        
        There is no requirement that a thread that releases a permit must
        have acquired that permit by calling .acquire.
        Correct usage of a semaphore is established by programming convention
        in the application.
        """
        ...


    def acquire(self, permits: int) -> None:
        """
        Acquires the given number of permits from this semaphore,
        blocking until all are available,
        or the thread is Thread.interrupt interrupted.
        
        Acquires the given number of permits, if they are available,
        and returns immediately, reducing the number of available permits
        by the given amount. This method has the same effect as the
        loop `for (int i = 0; i < permits; ++i) acquire();` except
        that it atomically acquires the permits all at once:
        
        If insufficient permits are available then the current thread becomes
        disabled for thread scheduling purposes and lies dormant until
        one of two things happens:
        
        - Some other thread invokes one of the .release() release
        methods for this semaphore and the current thread is next to be assigned
        permits and the number of available permits satisfies this request; or
        - Some other thread Thread.interrupt interrupts
        the current thread.
        
        
        If the current thread:
        
        - has its interrupted status set on entry to this method; or
        - is Thread.interrupt interrupted while waiting
        for a permit,
        
        then InterruptedException is thrown and the current thread's
        interrupted status is cleared.
        Any permits that were to be assigned to this thread are instead
        assigned to other threads trying to acquire permits, as if
        permits had been made available by a call to .release().

        Arguments
        - permits: the number of permits to acquire

        Raises
        - InterruptedException: if the current thread is interrupted
        - IllegalArgumentException: if `permits` is negative
        """
        ...


    def acquireUninterruptibly(self, permits: int) -> None:
        """
        Acquires the given number of permits from this semaphore,
        blocking until all are available.
        
        Acquires the given number of permits, if they are available,
        and returns immediately, reducing the number of available permits
        by the given amount. This method has the same effect as the
        loop `for (int i = 0; i < permits; ++i) acquireUninterruptibly();`
        except that it atomically acquires the permits all at once:
        
        If insufficient permits are available then the current thread becomes
        disabled for thread scheduling purposes and lies dormant until
        some other thread invokes one of the .release() release
        methods for this semaphore and the current thread is next to be assigned
        permits and the number of available permits satisfies this request.
        
        If the current thread is Thread.interrupt interrupted
        while waiting for permits then it will continue to wait and its
        position in the queue is not affected.  When the thread does return
        from this method its interrupt status will be set.

        Arguments
        - permits: the number of permits to acquire

        Raises
        - IllegalArgumentException: if `permits` is negative
        """
        ...


    def tryAcquire(self, permits: int) -> bool:
        """
        Acquires the given number of permits from this semaphore, only
        if all are available at the time of invocation.
        
        Acquires the given number of permits, if they are available, and
        returns immediately, with the value `True`,
        reducing the number of available permits by the given amount.
        
        If insufficient permits are available then this method will return
        immediately with the value `False` and the number of available
        permits is unchanged.
        
        Even when this semaphore has been set to use a fair ordering
        policy, a call to `tryAcquire` *will*
        immediately acquire a permit if one is available, whether or
        not other threads are currently waiting.  This
        &quot;barging&quot; behavior can be useful in certain
        circumstances, even though it breaks fairness. If you want to
        honor the fairness setting, then use .tryAcquire(int,
        long, TimeUnit) tryAcquire(permits, 0, TimeUnit.SECONDS)
        which is almost equivalent (it also detects interruption).

        Arguments
        - permits: the number of permits to acquire

        Returns
        - `True` if the permits were acquired and
                `False` otherwise

        Raises
        - IllegalArgumentException: if `permits` is negative
        """
        ...


    def tryAcquire(self, permits: int, timeout: int, unit: "TimeUnit") -> bool:
        """
        Acquires the given number of permits from this semaphore, if all
        become available within the given waiting time and the current
        thread has not been Thread.interrupt interrupted.
        
        Acquires the given number of permits, if they are available and
        returns immediately, with the value `True`,
        reducing the number of available permits by the given amount.
        
        If insufficient permits are available then
        the current thread becomes disabled for thread scheduling
        purposes and lies dormant until one of three things happens:
        
        - Some other thread invokes one of the .release() release
        methods for this semaphore and the current thread is next to be assigned
        permits and the number of available permits satisfies this request; or
        - Some other thread Thread.interrupt interrupts
        the current thread; or
        - The specified waiting time elapses.
        
        
        If the permits are acquired then the value `True` is returned.
        
        If the current thread:
        
        - has its interrupted status set on entry to this method; or
        - is Thread.interrupt interrupted while waiting
        to acquire the permits,
        
        then InterruptedException is thrown and the current thread's
        interrupted status is cleared.
        Any permits that were to be assigned to this thread, are instead
        assigned to other threads trying to acquire permits, as if
        the permits had been made available by a call to .release().
        
        If the specified waiting time elapses then the value `False`
        is returned.  If the time is less than or equal to zero, the method
        will not wait at all.  Any permits that were to be assigned to this
        thread, are instead assigned to other threads trying to acquire
        permits, as if the permits had been made available by a call to
        .release().

        Arguments
        - permits: the number of permits to acquire
        - timeout: the maximum time to wait for the permits
        - unit: the time unit of the `timeout` argument

        Returns
        - `True` if all permits were acquired and `False`
                if the waiting time elapsed before all permits were acquired

        Raises
        - InterruptedException: if the current thread is interrupted
        - IllegalArgumentException: if `permits` is negative
        """
        ...


    def release(self, permits: int) -> None:
        """
        Releases the given number of permits, returning them to the semaphore.
        
        Releases the given number of permits, increasing the number of
        available permits by that amount.
        If any threads are trying to acquire permits, then one thread
        is selected and given the permits that were just released.
        If the number of available permits satisfies that thread's request
        then that thread is (re)enabled for thread scheduling purposes;
        otherwise the thread will wait until sufficient permits are available.
        If there are still permits available
        after this thread's request has been satisfied, then those permits
        are assigned in turn to other threads trying to acquire permits.
        
        There is no requirement that a thread that releases a permit must
        have acquired that permit by calling Semaphore.acquire acquire.
        Correct usage of a semaphore is established by programming convention
        in the application.

        Arguments
        - permits: the number of permits to release

        Raises
        - IllegalArgumentException: if `permits` is negative
        """
        ...


    def availablePermits(self) -> int:
        """
        Returns the current number of permits available in this semaphore.
        
        This method is typically used for debugging and testing purposes.

        Returns
        - the number of permits available in this semaphore
        """
        ...


    def drainPermits(self) -> int:
        """
        Acquires and returns all permits that are immediately
        available, or if negative permits are available, releases them.
        Upon return, zero permits are available.

        Returns
        - the number of permits acquired or, if negative, the
        number released
        """
        ...


    def isFair(self) -> bool:
        """
        Returns `True` if this semaphore has fairness set True.

        Returns
        - `True` if this semaphore has fairness set True
        """
        ...


    def hasQueuedThreads(self) -> bool:
        """
        Queries whether any threads are waiting to acquire. Note that
        because cancellations may occur at any time, a `True`
        return does not guarantee that any other thread will ever
        acquire.  This method is designed primarily for use in
        monitoring of the system state.

        Returns
        - `True` if there may be other threads waiting to
                acquire the lock
        """
        ...


    def getQueueLength(self) -> int:
        """
        Returns an estimate of the number of threads waiting to acquire.
        The value is only an estimate because the number of threads may
        change dynamically while this method traverses internal data
        structures.  This method is designed for use in monitoring
        system state, not for synchronization control.

        Returns
        - the estimated number of threads waiting for this lock
        """
        ...


    def toString(self) -> str:
        """
        Returns a string identifying this semaphore, as well as its state.
        The state, in brackets, includes the String `"Permits ="`
        followed by the number of permits.

        Returns
        - a string identifying this semaphore, as well as its state
        """
        ...
