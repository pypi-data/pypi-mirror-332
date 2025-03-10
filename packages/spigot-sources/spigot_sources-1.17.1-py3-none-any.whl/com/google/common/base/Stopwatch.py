"""
Python module generated from Java source file com.google.common.base.Stopwatch

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.base import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.util.concurrent import TimeUnit
from typing import Any, Callable, Iterable, Tuple


class Stopwatch:
    """
    An object that measures elapsed time in nanoseconds. It is useful to measure elapsed time using
    this class instead of direct calls to System.nanoTime for a few reasons:
    
    
    - An alternate time source can be substituted, for testing or performance reasons.
    - As documented by `nanoTime`, the value returned has no absolute meaning, and can only
    be interpreted as relative to another timestamp returned by `nanoTime` at a different time.
    `Stopwatch` is a more effective abstraction because it exposes only these relative values,
    not the absolute ones.
    
    
    Basic usage: ```   `Stopwatch stopwatch = Stopwatch.createStarted();
      doSomething();
      stopwatch.stop(); // optional
    
      long millis = stopwatch.elapsed(MILLISECONDS);
    
      log.info("time: " + stopwatch); // formatted string like "12.3 ms"````
    
    Stopwatch methods are not idempotent; it is an error to start or stop a stopwatch that is
    already in the desired state.
    
    When testing code that uses this class, use .createUnstarted(Ticker) or
    .createStarted(Ticker) to supply a fake or mock ticker. This allows you to simulate any
    valid behavior of the stopwatch.
    
    **Note:** This class is not thread-safe.
    
    **Warning for Android users:** a stopwatch with default behavior may not continue to keep
    time while the device is asleep. Instead, create one like this: ```   `Stopwatch.createStarted(
            new Ticker() {
              public long read() {
                return android.os.SystemClock.elapsedRealtime();`
            });}```

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
        
        Note that the overhead of measurement can be more than a microsecond, so it is generally not
        useful to specify TimeUnit.NANOSECONDS precision here.

        Since
        - 14.0 (since 10.0 as `elapsedTime()`)
        """
        ...


    def toString(self) -> str:
        """
        Returns a string representation of the current elapsed time.
        """
        ...
