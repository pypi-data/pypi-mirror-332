"""
Python module generated from Java source file com.google.common.util.concurrent.CycleDetectingLockFactory

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import VisibleForTesting
from com.google.common.base import MoreObjects
from com.google.common.base import Preconditions
from com.google.common.collect import ImmutableSet
from com.google.common.collect import Lists
from com.google.common.collect import MapMaker
from com.google.common.collect import Maps
from com.google.common.collect import Sets
from com.google.common.util.concurrent import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from com.google.j2objc.annotations import Weak
from enum import Enum
from java.util import Arrays
from java.util import Collections
from java.util import EnumMap
from java.util.concurrent import ConcurrentMap
from java.util.concurrent import TimeUnit
from java.util.concurrent.locks import ReentrantLock
from java.util.concurrent.locks import ReentrantReadWriteLock
from javax.annotation import Nullable
from javax.annotation.concurrent import ThreadSafe
from typing import Any, Callable, Iterable, Tuple


class CycleDetectingLockFactory:
    """
    The `CycleDetectingLockFactory` creates ReentrantLock instances and
    ReentrantReadWriteLock instances that detect potential deadlock by checking for cycles in
    lock acquisition order.
    
    Potential deadlocks detected when calling the `lock()`, `lockInterruptibly()`, or
    `tryLock()` methods will result in the execution of the Policy specified when
    creating the factory. The currently available policies are:
    
    - DISABLED
    - WARN
    - THROW
    
    
    The locks created by a factory instance will detect lock acquisition cycles with locks created
    by other `CycleDetectingLockFactory` instances (except those with `Policy.DISABLED`).
    A lock's behavior when a cycle is detected, however, is defined by the `Policy` of the
    factory that created it. This allows detection of cycles across components while delegating
    control over lock behavior to individual components.
    
    Applications are encouraged to use a `CycleDetectingLockFactory` to create any locks for
    which external/unmanaged code is executed while the lock is held. (See caveats under
    <strong>Performance</strong>).
    
    <strong>Cycle Detection</strong>
    
    Deadlocks can arise when locks are acquired in an order that forms a cycle. In a simple
    example involving two locks and two threads, deadlock occurs when one thread acquires Lock A, and
    then Lock B, while another thread acquires Lock B, and then Lock A:
    
    ```
    Thread1: acquire(LockA) --X acquire(LockB)
    Thread2: acquire(LockB) --X acquire(LockA)
    ```
    
    Neither thread will progress because each is waiting for the other. In more complex
    applications, cycles can arise from interactions among more than 2 locks:
    
    ```
    Thread1: acquire(LockA) --X acquire(LockB)
    Thread2: acquire(LockB) --X acquire(LockC)
    ...
    ThreadN: acquire(LockN) --X acquire(LockA)
    ```
    
    The implementation detects cycles by constructing a directed graph in which each lock
    represents a node and each edge represents an acquisition ordering between two locks.
    
    - Each lock adds (and removes) itself to/from a ThreadLocal Set of acquired locks when the
        Thread acquires its first hold (and releases its last remaining hold).
    - Before the lock is acquired, the lock is checked against the current set of acquired
        locks---to each of the acquired locks, an edge from the soon-to-be-acquired lock is either
        verified or created.
    - If a new edge needs to be created, the outgoing edges of the acquired locks are traversed to
        check for a cycle that reaches the lock to be acquired. If no cycle is detected, a new "safe"
        edge is created.
    - If a cycle is detected, an "unsafe" (cyclic) edge is created to represent a potential
        deadlock situation, and the appropriate Policy is executed.
    
    
    Note that detection of potential deadlock does not necessarily indicate that deadlock will
    happen, as it is possible that higher level application logic prevents the cyclic lock
    acquisition from occurring. One example of a False positive is:
    
    ```
    LockA -&gt; LockB -&gt; LockC
    LockA -&gt; LockC -&gt; LockB
    ```
    
    <strong>ReadWriteLocks</strong>
    
    While `ReadWriteLock` instances have different properties and can form cycles without
    potential deadlock, this class treats `ReadWriteLock` instances as equivalent to
    traditional exclusive locks. Although this increases the False positives that the locks detect
    (i.e. cycles that will not actually result in deadlock), it simplifies the algorithm and
    implementation considerably. The assumption is that a user of this factory wishes to eliminate
    any cyclic acquisition ordering.
    
    <strong>Explicit Lock Acquisition Ordering</strong>
    
    The CycleDetectingLockFactory.WithExplicitOrdering class can be used to enforce an
    application-specific ordering in addition to performing general cycle detection.
    
    <strong>Garbage Collection</strong>
    
    In order to allow proper garbage collection of unused locks, the edges of the lock graph are
    weak references.
    
    <strong>Performance</strong>
    
    The extra bookkeeping done by cycle detecting locks comes at some cost to performance.
    Benchmarks (as of December 2011) show that:
    
    
    - for an unnested `lock()` and `unlock()`, a cycle detecting lock takes 38ns as
        opposed to the 24ns taken by a plain lock.
    - for nested locking, the cost increases with the depth of the nesting:
        
        - 2 levels: average of 64ns per lock()/unlock()
        - 3 levels: average of 77ns per lock()/unlock()
        - 4 levels: average of 99ns per lock()/unlock()
        - 5 levels: average of 103ns per lock()/unlock()
        - 10 levels: average of 184ns per lock()/unlock()
        - 20 levels: average of 393ns per lock()/unlock()
        
    
    
    As such, the CycleDetectingLockFactory may not be suitable for performance-critical
    applications which involve tightly-looped or deeply-nested locking algorithms.

    Author(s)
    - Darick Tong

    Since
    - 13.0
    """

    @staticmethod
    def newInstance(policy: "Policy") -> "CycleDetectingLockFactory":
        """
        Creates a new factory with the specified policy.
        """
        ...


    def newReentrantLock(self, lockName: str) -> "ReentrantLock":
        """
        Equivalent to `newReentrantLock(lockName, False)`.
        """
        ...


    def newReentrantLock(self, lockName: str, fair: bool) -> "ReentrantLock":
        """
        Creates a ReentrantLock with the given fairness policy. The `lockName` is used in
        the warning or exception output to help identify the locks involved in the detected deadlock.
        """
        ...


    def newReentrantReadWriteLock(self, lockName: str) -> "ReentrantReadWriteLock":
        """
        Equivalent to `newReentrantReadWriteLock(lockName, False)`.
        """
        ...


    def newReentrantReadWriteLock(self, lockName: str, fair: bool) -> "ReentrantReadWriteLock":
        """
        Creates a ReentrantReadWriteLock with the given fairness policy. The `lockName`
        is used in the warning or exception output to help identify the locks involved in the detected
        deadlock.
        """
        ...


    @staticmethod
    def newInstanceWithExplicitOrdering(enumClass: type["E"], policy: "Policy") -> "WithExplicitOrdering"["E"]:
        """
        Creates a `CycleDetectingLockFactory.WithExplicitOrdering<E>`.
        """
        ...


    class Policy:
        """
        Encapsulates the action to be taken when a potential deadlock is encountered. Clients can use
        one of the predefined Policies or specify a custom implementation. Implementations must
        be thread-safe.

        Since
        - 13.0
        """

        def handlePotentialDeadlock(self, exception: "PotentialDeadlockException") -> None:
            """
            Called when a potential deadlock is encountered. Implementations can throw the given
            `exception` and/or execute other desired logic.
            
            Note that the method will be called even upon an invocation of `tryLock()`. Although
            `tryLock()` technically recovers from deadlock by eventually timing out, this behavior
            is chosen based on the assumption that it is the application's wish to prohibit any cyclical
            lock acquisitions.
            """
            ...


    class WithExplicitOrdering(CycleDetectingLockFactory):
        """
        A `CycleDetectingLockFactory.WithExplicitOrdering` provides the additional enforcement
        of an application-specified ordering of lock acquisitions. The application defines the allowed
        ordering with an `Enum` whose values each correspond to a lock type. The order in which
        the values are declared dictates the allowed order of lock acquisition. In other words, locks
        corresponding to smaller values of Enum.ordinal() should only be acquired before locks
        with larger ordinals. Example:
        
        ```   `enum MyLockOrder {
          FIRST, SECOND, THIRD;`
        
        CycleDetectingLockFactory.WithExplicitOrdering<MyLockOrder> factory =
          CycleDetectingLockFactory.newInstanceWithExplicitOrdering(Policies.THROW);
        
        Lock lock1 = factory.newReentrantLock(MyLockOrder.FIRST);
        Lock lock2 = factory.newReentrantLock(MyLockOrder.SECOND);
        Lock lock3 = factory.newReentrantLock(MyLockOrder.THIRD);
        
        lock1.lock();
        lock3.lock();
        lock2.lock();  // will throw an IllegalStateException}```
        
        As with all locks created by instances of `CycleDetectingLockFactory` explicitly
        ordered locks participate in general cycle detection with all other cycle detecting locks, and
        a lock's behavior when detecting a cyclic lock acquisition is defined by the `Policy` of
        the factory that created it.
        
        Note, however, that although multiple locks can be created for a given Enum value, whether
        it be through separate factory instances or through multiple calls to the same factory,
        attempting to acquire multiple locks with the same Enum value (within the same thread) will
        result in an IllegalStateException regardless of the factory's policy. For example:
        
        ```   `CycleDetectingLockFactory.WithExplicitOrdering<MyLockOrder> factory1 =
          CycleDetectingLockFactory.newInstanceWithExplicitOrdering(...);
        CycleDetectingLockFactory.WithExplicitOrdering<MyLockOrder> factory2 =
          CycleDetectingLockFactory.newInstanceWithExplicitOrdering(...);
        
        Lock lockA = factory1.newReentrantLock(MyLockOrder.FIRST);
        Lock lockB = factory1.newReentrantLock(MyLockOrder.FIRST);
        Lock lockC = factory2.newReentrantLock(MyLockOrder.FIRST);
        
        lockA.lock();
        
        lockB.lock();  // will throw an IllegalStateException
        lockC.lock();  // will throw an IllegalStateException
        
        lockA.lock();  // reentrant acquisition is okay````
        
        It is the responsibility of the application to ensure that multiple lock instances with the
        same rank are never acquired in the same thread.
        
        Type `<E>`: The Enum type representing the explicit lock ordering.

        Since
        - 13.0
        """

        def newReentrantLock(self, rank: "E") -> "ReentrantLock":
            """
            Equivalent to `newReentrantLock(rank, False)`.
            """
            ...


        def newReentrantLock(self, rank: "E", fair: bool) -> "ReentrantLock":
            """
            Creates a ReentrantLock with the given fairness policy and rank. The values returned
            by Enum.getDeclaringClass() and Enum.name() are used to describe the lock in
            warning or exception output.

            Raises
            - IllegalStateException: If the factory has already created a `Lock` with the
                specified rank.
            """
            ...


        def newReentrantReadWriteLock(self, rank: "E") -> "ReentrantReadWriteLock":
            """
            Equivalent to `newReentrantReadWriteLock(rank, False)`.
            """
            ...


        def newReentrantReadWriteLock(self, rank: "E", fair: bool) -> "ReentrantReadWriteLock":
            """
            Creates a ReentrantReadWriteLock with the given fairness policy and rank. The values
            returned by Enum.getDeclaringClass() and Enum.name() are used to describe the
            lock in warning or exception output.

            Raises
            - IllegalStateException: If the factory has already created a `Lock` with the
                specified rank.
            """
            ...


    class PotentialDeadlockException(ExampleStackTrace):
        """
        Represents a detected cycle in lock acquisition ordering. The exception includes a causal chain
        of `ExampleStackTrace` instances to illustrate the cycle, e.g.
        
        ```
        com....PotentialDeadlockException: Potential Deadlock from LockC -&gt; ReadWriteA
          at ...
          at ...
        Caused by: com...ExampleStackTrace: LockB -&gt; LockC
          at ...
          at ...
        Caused by: com...ExampleStackTrace: ReadWriteA -&gt; LockB
          at ...
          at ...
        ```
        
        Instances are logged for the `Policies.WARN`, and thrown for `Policies.THROW`.

        Since
        - 13.0
        """

        def getConflictingStackTrace(self) -> "ExampleStackTrace":
            ...


        def getMessage(self) -> str:
            """
            Appends the chain of messages from the `conflictingStackTrace` to the original
            `message`.
            """
            ...


    class Policies(Enum):
        """
        Pre-defined Policy implementations.

        Since
        - 13.0
        """

        THROW = 0
        """
        When potential deadlock is detected, this policy results in the throwing of the
        `PotentialDeadlockException` indicating the potential deadlock, which includes stack
        traces illustrating the cycle in lock acquisition order.
        """
        WARN = 1
        """
        When potential deadlock is detected, this policy results in the logging of a
        Level.SEVERE message indicating the potential deadlock, which includes stack traces
        illustrating the cycle in lock acquisition order.
        """
        DISABLED = 2
        """
        Disables cycle detection. This option causes the factory to return unmodified lock
        implementations provided by the JDK, and is provided to allow applications to easily
        parameterize when cycle detection is enabled.
        
        Note that locks created by a factory with this policy will *not* participate the
        cycle detection performed by locks created by other factories.
        """
