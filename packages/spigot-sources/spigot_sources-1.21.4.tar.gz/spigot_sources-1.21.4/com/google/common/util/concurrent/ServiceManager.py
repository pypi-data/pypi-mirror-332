"""
Python module generated from Java source file com.google.common.util.concurrent.ServiceManager

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import J2ktIncompatible
from com.google.common.base import Function
from com.google.common.base import MoreObjects
from com.google.common.base import Stopwatch
from com.google.common.collect import Collections2
from com.google.common.collect import ImmutableCollection
from com.google.common.collect import ImmutableList
from com.google.common.collect import ImmutableMap
from com.google.common.collect import ImmutableSet
from com.google.common.collect import ImmutableSetMultimap
from com.google.common.collect import Lists
from com.google.common.collect import Maps
from com.google.common.collect import MultimapBuilder
from com.google.common.collect import Multimaps
from com.google.common.collect import Multiset
from com.google.common.collect import Ordering
from com.google.common.collect import SetMultimap
from com.google.common.util.concurrent import *
from com.google.common.util.concurrent.Service import State
from com.google.errorprone.annotations import CanIgnoreReturnValue
from com.google.errorprone.annotations.concurrent import GuardedBy
from com.google.j2objc.annotations import J2ObjCIncompatible
from com.google.j2objc.annotations import WeakOuter
from java.lang.ref import WeakReference
from java.time import Duration
from java.util import Collections
from java.util import EnumSet
from java.util import IdentityHashMap
from java.util.concurrent import Executor
from java.util.concurrent import TimeUnit
from java.util.concurrent import TimeoutException
from typing import Any, Callable, Iterable, Tuple


class ServiceManager(ServiceManagerBridge):
    """
    A manager for monitoring and controlling a set of Service services. This class
    provides methods for .startAsync() starting, .stopAsync() stopping and
    .servicesByState inspecting a collection of Service services.
    Additionally, users can monitor state transitions with the Listener listener
    mechanism.
    
    While it is recommended that service lifecycles be managed via this class, state transitions
    initiated via other mechanisms do not impact the correctness of its methods. For example, if the
    services are started by some mechanism besides .startAsync, the listeners will be invoked
    when appropriate and .awaitHealthy will still work as expected.
    
    Here is a simple example of how to use a `ServiceManager` to start a server.
    
    ````class Server {
      public static void main(String[] args) {
        Set<Service> services = ...;
        ServiceManager manager = new ServiceManager(services);
        manager.addListener(new Listener() {
            public void stopped() {`
            public void healthy() {
              // Services have been initialized and are healthy, start accepting requests...
            }
            public void failure(Service service) {
              // Something failed, at this point we could log it, notify a load balancer, or take
              // some other action.  For now we will just exit.
              System.exit(1);
            }
          },
          MoreExecutors.directExecutor());
    
        Runtime.getRuntime().addShutdownHook(new Thread() {
          public void run() {
            // Give the services 5 seconds to stop to ensure that we are responsive to shutdown
            // requests.
            try {
              manager.stopAsync().awaitStopped(5, TimeUnit.SECONDS);
            } catch (TimeoutException timeout) {
              // stopping timed out
            }
          }
        });
        manager.startAsync();  // start all the services asynchronously
      }
    }
    }```
    
    This class uses the ServiceManager's methods to start all of its services, to respond to
    service failure and to ensure that when the JVM is shutting down all the services are stopped.

    Author(s)
    - Luke Sandberg

    Since
    - 14.0
    """

    def __init__(self, services: Iterable["Service"]):
        """
        Constructs a new instance for managing the given services.

        Arguments
        - services: The services to manage

        Raises
        - IllegalArgumentException: if not all services are State.NEW new or if there
            are any duplicate services.
        """
        ...


    def addListener(self, listener: "Listener", executor: "Executor") -> None:
        """
        Registers a Listener to be Executor.execute executed on the given
        executor. The listener will not have previous state changes replayed, so it is suggested that
        listeners are added before any of the managed services are Service.startAsync
        started.
        
        `addListener` guarantees execution ordering across calls to a given listener but not
        across calls to multiple listeners. Specifically, a given listener will have its callbacks
        invoked in the same order as the underlying service enters those states. Additionally, at most
        one of the listener's callbacks will execute at once. However, multiple listeners' callbacks
        may execute concurrently, and listeners may execute in an order different from the one in which
        they were registered.
        
        RuntimeExceptions thrown by a listener will be caught and logged. Any exception thrown
        during `Executor.execute` (e.g., a `RejectedExecutionException`) will be caught and
        logged.
        
        When selecting an executor, note that `directExecutor` is dangerous in some cases. See
        the discussion in the ListenableFuture.addListener ListenableFuture.addListener
        documentation.

        Arguments
        - listener: the listener to run when the manager changes state
        - executor: the executor in which the listeners callback methods will be run.
        """
        ...


    def startAsync(self) -> "ServiceManager":
        """
        Initiates service Service.startAsync startup on all the services being managed. It
        is only valid to call this method if all of the services are State.NEW new.

        Returns
        - this

        Raises
        - IllegalStateException: if any of the Services are not State.NEW new when the
            method is called.
        """
        ...


    def awaitHealthy(self) -> None:
        """
        Waits for the ServiceManager to become .isHealthy() healthy. The manager
        will become healthy after all the component services have reached the State.RUNNING
        running state.

        Raises
        - IllegalStateException: if the service manager reaches a state from which it cannot
            become .isHealthy() healthy.
        """
        ...


    def awaitHealthy(self, timeout: "Duration") -> None:
        """
        Waits for the ServiceManager to become .isHealthy() healthy for no more
        than the given time. The manager will become healthy after all the component services have
        reached the State.RUNNING running state.

        Arguments
        - timeout: the maximum time to wait

        Raises
        - TimeoutException: if not all of the services have finished starting within the deadline
        - IllegalStateException: if the service manager reaches a state from which it cannot
            become .isHealthy() healthy.

        Since
        - 28.0
        """
        ...


    def awaitHealthy(self, timeout: int, unit: "TimeUnit") -> None:
        """
        Waits for the ServiceManager to become .isHealthy() healthy for no more
        than the given time. The manager will become healthy after all the component services have
        reached the State.RUNNING running state.

        Arguments
        - timeout: the maximum time to wait
        - unit: the time unit of the timeout argument

        Raises
        - TimeoutException: if not all of the services have finished starting within the deadline
        - IllegalStateException: if the service manager reaches a state from which it cannot
            become .isHealthy() healthy.
        """
        ...


    def stopAsync(self) -> "ServiceManager":
        """
        Initiates service Service.stopAsync shutdown if necessary on all the services
        being managed.

        Returns
        - this
        """
        ...


    def awaitStopped(self) -> None:
        """
        Waits for the all the services to reach a terminal state. After this method returns all
        services will either be Service.State.TERMINATED terminated or Service.State.FAILED failed.
        """
        ...


    def awaitStopped(self, timeout: "Duration") -> None:
        """
        Waits for the all the services to reach a terminal state for no more than the given time. After
        this method returns all services will either be Service.State.TERMINATED
        terminated or Service.State.FAILED failed.

        Arguments
        - timeout: the maximum time to wait

        Raises
        - TimeoutException: if not all of the services have stopped within the deadline

        Since
        - 28.0
        """
        ...


    def awaitStopped(self, timeout: int, unit: "TimeUnit") -> None:
        """
        Waits for the all the services to reach a terminal state for no more than the given time. After
        this method returns all services will either be Service.State.TERMINATED
        terminated or Service.State.FAILED failed.

        Arguments
        - timeout: the maximum time to wait
        - unit: the time unit of the timeout argument

        Raises
        - TimeoutException: if not all of the services have stopped within the deadline
        """
        ...


    def isHealthy(self) -> bool:
        """
        Returns True if all services are currently in the State.RUNNING running state.
        
        Users who want more detailed information should use the .servicesByState method to
        get detailed information about which services are not running.
        """
        ...


    def servicesByState(self) -> "ImmutableSetMultimap"["State", "Service"]:
        """
        Provides a snapshot of the current state of all the services under management.
        
        N.B. This snapshot is guaranteed to be consistent, i.e. the set of states returned will
        correspond to a point in time view of the services.

        Since
        - 29.0 (present with return type `ImmutableMultimap` since 14.0)
        """
        ...


    def startupTimes(self) -> "ImmutableMap"["Service", "Long"]:
        """
        Returns the service load times. This value will only return startup times for services that
        have finished starting.

        Returns
        - Map of services and their corresponding startup time in millis, the map entries will be
            ordered by startup time.
        """
        ...


    def startupDurations(self) -> "ImmutableMap"["Service", "Duration"]:
        """
        Returns the service load times. This value will only return startup times for services that
        have finished starting.

        Returns
        - Map of services and their corresponding startup time, the map entries will be ordered
            by startup time.

        Since
        - 31.0
        """
        ...


    def toString(self) -> str:
        ...


    class Listener:
        """
        A listener for the aggregate state changes of the services that are under management. Users
        that need to listen to more fine-grained events (such as when each particular Service service starts, or terminates), should attach Service.Listener service
        listeners to each individual service.

    Author(s)
        - Luke Sandberg

        Since
        - 15.0 (present as an interface in 14.0)
        """

        def healthy(self) -> None:
            """
            Called when the service initially becomes healthy.
            
            This will be called at most once after all the services have entered the State.RUNNING running state. If any services fail during start up or State.FAILED fail/State.TERMINATED terminate before all other services have
            started State.RUNNING running then this method will not be called.
            """
            ...


        def stopped(self) -> None:
            """
            Called when the all of the component services have reached a terminal state, either
            State.TERMINATED terminated or State.FAILED failed.
            """
            ...


        def failure(self, service: "Service") -> None:
            """
            Called when a component service has State.FAILED failed.

            Arguments
            - service: The service that failed.
            """
            ...
