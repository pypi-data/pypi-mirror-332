"""
Python module generated from Java source file com.google.common.util.concurrent.Service

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import J2ktIncompatible
from com.google.common.util.concurrent import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from com.google.errorprone.annotations import DoNotMock
from java.time import Duration
from java.util.concurrent import Executor
from java.util.concurrent import TimeUnit
from java.util.concurrent import TimeoutException
from typing import Any, Callable, Iterable, Tuple


class Service:
    """
    An object with an operational state, plus asynchronous .startAsync() and .stopAsync() lifecycle methods to transition between states. Example services include
    webservers, RPC servers and timers.
    
    The normal lifecycle of a service is:
    
    
      - State.NEW NEW -&gt;
      - State.STARTING STARTING -&gt;
      - State.RUNNING RUNNING -&gt;
      - State.STOPPING STOPPING -&gt;
      - State.TERMINATED TERMINATED
    
    
    There are deviations from this if there are failures or if Service.stopAsync is called
    before the Service reaches the State.RUNNING RUNNING state. The set of legal
    transitions form a <a href="http://en.wikipedia.org/wiki/Directed_acyclic_graph">DAG</a>,
    therefore every method of the listener will be called at most once. N.B. The State.FAILED
    and State.TERMINATED states are terminal states, once a service enters either of these
    states it cannot ever leave them.
    
    Implementors of this interface are strongly encouraged to extend one of the abstract classes
    in this package which implement this interface and make the threading and state management
    easier.

    Author(s)
    - Luke Sandberg

    Since
    - 9.0 (in 1.0 as `com.google.common.base.Service`)
    """

    def startAsync(self) -> "Service":
        """
        If the service state is State.NEW, this initiates service startup and returns
        immediately. A stopped service may not be restarted.

        Returns
        - this

        Raises
        - IllegalStateException: if the service is not State.NEW

        Since
        - 15.0
        """
        ...


    def isRunning(self) -> bool:
        """
        Returns `True` if this service is State.RUNNING running.
        """
        ...


    def state(self) -> "State":
        """
        Returns the lifecycle state of the service.
        """
        ...


    def stopAsync(self) -> "Service":
        """
        If the service is State.STARTING starting or State.RUNNING running,
        this initiates service shutdown and returns immediately. If the service is State.NEW new, it is State.TERMINATED terminated without having been started nor
        stopped. If the service has already been stopped, this method returns immediately without
        taking action.

        Returns
        - this

        Since
        - 15.0
        """
        ...


    def awaitRunning(self) -> None:
        """
        Waits for the Service to reach the State.RUNNING running state.

        Raises
        - IllegalStateException: if the service reaches a state from which it is not possible to
            enter the State.RUNNING state. e.g. if the `state` is `State.TERMINATED` when this method is called then this will throw an IllegalStateException.

        Since
        - 15.0
        """
        ...


    def awaitRunning(self, timeout: "Duration") -> None:
        """
        Waits for the Service to reach the State.RUNNING running state for no more
        than the given time.

        Arguments
        - timeout: the maximum time to wait

        Raises
        - TimeoutException: if the service has not reached the given state within the deadline
        - IllegalStateException: if the service reaches a state from which it is not possible to
            enter the State.RUNNING RUNNING state. e.g. if the `state` is `State.TERMINATED` when this method is called then this will throw an IllegalStateException.

        Since
        - 28.0
        """
        ...


    def awaitRunning(self, timeout: int, unit: "TimeUnit") -> None:
        """
        Waits for the Service to reach the State.RUNNING running state for no more
        than the given time.

        Arguments
        - timeout: the maximum time to wait
        - unit: the time unit of the timeout argument

        Raises
        - TimeoutException: if the service has not reached the given state within the deadline
        - IllegalStateException: if the service reaches a state from which it is not possible to
            enter the State.RUNNING RUNNING state. e.g. if the `state` is `State.TERMINATED` when this method is called then this will throw an IllegalStateException.

        Since
        - 15.0
        """
        ...


    def awaitTerminated(self) -> None:
        """
        Waits for the Service to reach the State.TERMINATED terminated state.

        Raises
        - IllegalStateException: if the service State.FAILED fails.

        Since
        - 15.0
        """
        ...


    def awaitTerminated(self, timeout: "Duration") -> None:
        """
        Waits for the Service to reach a terminal state (either Service.State.TERMINATED
        terminated or Service.State.FAILED failed) for no more than the given time.

        Arguments
        - timeout: the maximum time to wait

        Raises
        - TimeoutException: if the service has not reached the given state within the deadline
        - IllegalStateException: if the service State.FAILED fails.

        Since
        - 28.0
        """
        ...


    def awaitTerminated(self, timeout: int, unit: "TimeUnit") -> None:
        """
        Waits for the Service to reach a terminal state (either Service.State.TERMINATED
        terminated or Service.State.FAILED failed) for no more than the given time.

        Arguments
        - timeout: the maximum time to wait
        - unit: the time unit of the timeout argument

        Raises
        - TimeoutException: if the service has not reached the given state within the deadline
        - IllegalStateException: if the service State.FAILED fails.

        Since
        - 15.0
        """
        ...


    def failureCause(self) -> "Throwable":
        """
        Returns the Throwable that caused this service to fail.

        Raises
        - IllegalStateException: if this service's state isn't State.FAILED FAILED.

        Since
        - 14.0
        """
        ...


    def addListener(self, listener: "Listener", executor: "Executor") -> None:
        """
        Registers a Listener to be Executor.execute executed on the given
        executor. The listener will have the corresponding transition method called whenever the
        service changes state. The listener will not have previous state changes replayed, so it is
        suggested that listeners are added before the service starts.
        
        `addListener` guarantees execution ordering across calls to a given listener but not
        across calls to multiple listeners. Specifically, a given listener will have its callbacks
        invoked in the same order as the underlying service enters those states. Additionally, at most
        one of the listener's callbacks will execute at once. However, multiple listeners' callbacks
        may execute concurrently, and listeners may execute in an order different from the one in which
        they were registered.
        
        RuntimeExceptions thrown by a listener will be caught and logged. Any exception thrown
        during `Executor.execute` (e.g., a `RejectedExecutionException`) will be caught and
        logged.

        Arguments
        - listener: the listener to run when the service changes state is complete
        - executor: the executor in which the listeners callback methods will be run. For fast,
            lightweight listeners that would be safe to execute in any thread, consider MoreExecutors.directExecutor.

        Since
        - 13.0
        """
        ...
