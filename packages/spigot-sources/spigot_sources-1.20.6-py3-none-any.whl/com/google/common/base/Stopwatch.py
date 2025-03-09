"""
Python module generated from Java source file com.google.common.base.Stopwatch

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import J2ktIncompatible
from com.google.common.base import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from com.google.j2objc.annotations import J2ObjCIncompatible
from java.time import Duration
from java.util.concurrent import TimeUnit
from typing import Any, Callable, Iterable, Tuple


class Stopwatch:
    """
    An object that accurately measures *elapsed time*: the measured duration between two
    successive readings of "now" in the same process.
    
    In contrast, *wall time* is a reading of "now" as given by a method like
    System.currentTimeMillis(), best represented as an java.time.Instant. Such values
    *can* be subtracted to obtain a `Duration` (such as by `Duration.between`), but
    doing so does *not* give a reliable measurement of elapsed time, because wall time readings
    are inherently approximate, routinely affected by periodic clock corrections. Because this class
    (by default) uses System.nanoTime, it is unaffected by these changes.
    
    Use this class instead of direct calls to System.nanoTime for two reasons:
    
    
      - The raw `long` values returned by `nanoTime` are meaningless and unsafe to use
          in any other way than how `Stopwatch` uses them.
      - An alternative source of nanosecond ticks can be substituted, for example for testing or
          performance reasons, without affecting most of your code.
    
    
    The one downside of `Stopwatch` relative to System.nanoTime() is that `Stopwatch` requires object allocation and additional method calls, which can reduce the accuracy
    of the elapsed times reported. `Stopwatch` is still suitable for logging and metrics where
    reasonably accurate values are sufficient. If the uncommon case that you need to maximize
    accuracy, use `System.nanoTime()` directly instead.
    
    Basic usage:
    
    ````Stopwatch stopwatch = Stopwatch.createStarted();
    doSomething();
    stopwatch.stop(); // optional
    
    Duration duration = stopwatch.elapsed();
    
    log.info("time: " + stopwatch); // formatted string like "12.3 ms"````
    
    The state-changing methods are not idempotent; it is an error to start or stop a stopwatch
    that is already in the desired state.
    
    When testing code that uses this class, use .createUnstarted(Ticker) or .createStarted(Ticker) to supply a fake or mock ticker. This allows you to simulate any valid
    behavior of the stopwatch.
    
    **Note:** This class is not thread-safe.
    
    **Warning for Android users:** a stopwatch with default behavior may not continue to keep
    time while the device is asleep. Instead, create one like this:
    
    ````Stopwatch.createStarted(
         new Ticker() {
           public long read() {
             return android.os.SystemClock.elapsedRealtimeNanos(); // requires API Level 17`
         });
    }```

    Author(s)
    - Kevin Bourrillion

    Since
    - 10.0
    """

    @staticmethod
    def createUnstarted() -> "Stopwatch":
        """
        Creates (but does not start) a new stopwatch using System.nanoTime as its time source.

        Since
        - 15.0
        """
        ...


    @staticmethod
    def createUnstarted(ticker: "Ticker") -> "Stopwatch":
        """
        Creates (but does not start) a new stopwatch, using the specified time source.

        Since
        - 15.0
        """
        ...


    @staticmethod
    def createStarted() -> "Stopwatch":
        """
        Creates (and starts) a new stopwatch using System.nanoTime as its time source.

        Since
        - 15.0
        """
        ...


    @staticmethod
    def createStarted(ticker: "Ticker") -> "Stopwatch":
        """
        Creates (and starts) a new stopwatch, using the specified time source.

        Since
        - 15.0
        """
        ...


    def isRunning(self) -> bool:
        """
        Returns `True` if .start() has been called on this stopwatch, and .stop()
        has not been called since the last call to `start()`.
        """
        ...


    def start(self) -> "Stopwatch":
        """
        Starts the stopwatch.

        Returns
        - this `Stopwatch` instance

        Raises
        - IllegalStateException: if the stopwatch is already running.
        """
        ...


    def stop(self) -> "Stopwatch":
        """
        Stops the stopwatch. Future reads will return the fixed duration that had elapsed up to this
        point.

        Returns
        - this `Stopwatch` instance

        Raises
        - IllegalStateException: if the stopwatch is already stopped.
        """
        ...


    def reset(self) -> "Stopwatch":
        """
        Sets the elapsed time for this stopwatch to zero, and places it in a stopped state.

        Returns
        - this `Stopwatch` instance
        """
        ...


    def elapsed(self, desiredUnit: "TimeUnit") -> int:
        """
        Returns the current elapsed time shown on this stopwatch, expressed in the desired time unit,
        with any fraction rounded down.
        
        **Note:** the overhead of measurement can be more than a microsecond, so it is generally
        not useful to specify TimeUnit.NANOSECONDS precision here.
        
        It is generally not a good idea to use an ambiguous, unitless `long` to represent
        elapsed time. Therefore, we recommend using .elapsed() instead, which returns a
        strongly-typed `Duration` instance.

        Since
        - 14.0 (since 10.0 as `elapsedTime()`)
        """
        ...


    def elapsed(self) -> "Duration":
        """
        Returns the current elapsed time shown on this stopwatch as a Duration. Unlike .elapsed(TimeUnit), this method does not lose any precision due to rounding.

        Since
        - 22.0
        """
        ...


    def toString(self) -> str:
        """
        Returns a string representation of the current elapsed time.
        """
        ...
