"""
Python module generated from Java source file com.google.common.util.concurrent.AbstractScheduledService

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import J2ktIncompatible
from com.google.common.util.concurrent import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from com.google.errorprone.annotations.concurrent import GuardedBy
from com.google.j2objc.annotations import WeakOuter
from java.time import Duration
from java.util.concurrent import Callable
from java.util.concurrent import Executor
from java.util.concurrent import Executors
from java.util.concurrent import Future
from java.util.concurrent import ScheduledExecutorService
from java.util.concurrent import ScheduledFuture
from java.util.concurrent import ThreadFactory
from java.util.concurrent import TimeUnit
from java.util.concurrent import TimeoutException
from java.util.concurrent.locks import ReentrantLock
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class AbstractScheduledService(Service):
    """
    Base class for services that can implement .startUp and .shutDown but while in
    the "running" state need to perform a periodic task. Subclasses can implement .startUp,
    .shutDown and also a .runOneIteration method that will be executed periodically.
    
    This class uses the ScheduledExecutorService returned from .executor to run
    the .startUp and .shutDown methods and also uses that service to schedule the
    .runOneIteration that will be executed periodically as specified by its Scheduler. When this service is asked to stop via .stopAsync it will cancel the periodic
    task (but not interrupt it) and wait for it to stop before running the .shutDown method.
    
    Subclasses are guaranteed that the life cycle methods (.runOneIteration, .startUp and .shutDown) will never run concurrently. Notably, if any execution of .runOneIteration takes longer than its schedule defines, then subsequent executions may start
    late. Also, all life cycle methods are executed with a lock held, so subclasses can safely modify
    shared state without additional synchronization necessary for visibility to later executions of
    the life cycle methods.
    
    <h3>Usage Example</h3>
    
    Here is a sketch of a service which crawls a website and uses the scheduling capabilities to
    rate limit itself.
    
    ````class CrawlingService extends AbstractScheduledService {
      private Set<Uri> visited;
      private Queue<Uri> toCrawl;
      protected void startUp() throws Exception {
        toCrawl = readStartingUris();`
    
      protected void runOneIteration() throws Exception {
        Uri uri = toCrawl.remove();
        Collection<Uri> newUris = crawl(uri);
        visited.add(uri);
        for (Uri newUri : newUris) {
          if (!visited.contains(newUri)) { toCrawl.add(newUri); }
        }
      }
    
      protected void shutDown() throws Exception {
        saveUris(toCrawl);
      }
    
      protected Scheduler scheduler() {
        return Scheduler.newFixedRateSchedule(0, 1, TimeUnit.SECONDS);
      }
    }
    }```
    
    This class uses the life cycle methods to read in a list of starting URIs and save the set of
    outstanding URIs when shutting down. Also, it takes advantage of the scheduling functionality to
    rate limit the number of queries we perform.

    Author(s)
    - Luke Sandberg

    Since
    - 11.0
    """

    def toString(self) -> str:
        ...


    def isRunning(self) -> bool:
        ...


    def state(self) -> "State":
        ...


    def addListener(self, listener: "Listener", executor: "Executor") -> None:
        """
        Since
        - 13.0
        """
        ...


    def failureCause(self) -> "Throwable":
        """
        Since
        - 14.0
        """
        ...


    def startAsync(self) -> "Service":
        """
        Since
        - 15.0
        """
        ...


    def stopAsync(self) -> "Service":
        """
        Since
        - 15.0
        """
        ...


    def awaitRunning(self) -> None:
        """
        Since
        - 15.0
        """
        ...


    def awaitRunning(self, timeout: "Duration") -> None:
        """
        Since
        - 28.0
        """
        ...


    def awaitRunning(self, timeout: int, unit: "TimeUnit") -> None:
        """
        Since
        - 15.0
        """
        ...


    def awaitTerminated(self) -> None:
        """
        Since
        - 15.0
        """
        ...


    def awaitTerminated(self, timeout: "Duration") -> None:
        """
        Since
        - 28.0
        """
        ...


    def awaitTerminated(self, timeout: int, unit: "TimeUnit") -> None:
        """
        Since
        - 15.0
        """
        ...


    class Scheduler:
        """
        A scheduler defines the policy for how the AbstractScheduledService should run its
        task.
        
        Consider using the .newFixedDelaySchedule and .newFixedRateSchedule factory
        methods, these provide Scheduler instances for the common use case of running the
        service with a fixed schedule. If more flexibility is needed then consider subclassing CustomScheduler.

    Author(s)
        - Luke Sandberg

        Since
        - 11.0
        """

        @staticmethod
        def newFixedDelaySchedule(initialDelay: "Duration", delay: "Duration") -> "Scheduler":
            """
            Returns a Scheduler that schedules the task using the ScheduledExecutorService.scheduleWithFixedDelay method.

            Arguments
            - initialDelay: the time to delay first execution
            - delay: the delay between the termination of one execution and the commencement of the
                next

            Since
            - 28.0
            """
            ...


        @staticmethod
        def newFixedDelaySchedule(initialDelay: int, delay: int, unit: "TimeUnit") -> "Scheduler":
            """
            Returns a Scheduler that schedules the task using the ScheduledExecutorService.scheduleWithFixedDelay method.

            Arguments
            - initialDelay: the time to delay first execution
            - delay: the delay between the termination of one execution and the commencement of the
                next
            - unit: the time unit of the initialDelay and delay parameters
            """
            ...


        @staticmethod
        def newFixedRateSchedule(initialDelay: "Duration", period: "Duration") -> "Scheduler":
            """
            Returns a Scheduler that schedules the task using the ScheduledExecutorService.scheduleAtFixedRate method.

            Arguments
            - initialDelay: the time to delay first execution
            - period: the period between successive executions of the task

            Since
            - 28.0
            """
            ...


        @staticmethod
        def newFixedRateSchedule(initialDelay: int, period: int, unit: "TimeUnit") -> "Scheduler":
            """
            Returns a Scheduler that schedules the task using the ScheduledExecutorService.scheduleAtFixedRate method.

            Arguments
            - initialDelay: the time to delay first execution
            - period: the period between successive executions of the task
            - unit: the time unit of the initialDelay and period parameters
            """
            ...


    class CustomScheduler(Scheduler):
        """
        A Scheduler that provides a convenient way for the AbstractScheduledService to
        use a dynamically changing schedule. After every execution of the task, assuming it hasn't been
        cancelled, the .getNextSchedule method will be called.

    Author(s)
        - Luke Sandberg

        Since
        - 11.0
        """


