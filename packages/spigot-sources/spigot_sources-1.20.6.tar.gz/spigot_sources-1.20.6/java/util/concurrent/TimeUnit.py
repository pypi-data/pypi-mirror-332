"""
Python module generated from Java source file java.util.concurrent.TimeUnit

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from java.time import Duration
from java.time.temporal import ChronoUnit
from java.util import Objects
from java.util.concurrent import *
from typing import Any, Callable, Iterable, Tuple


class TimeUnit(Enum):
    """
    A `TimeUnit` represents time durations at a given unit of
    granularity and provides utility methods to convert across units,
    and to perform timing and delay operations in these units.  A
    `TimeUnit` does not maintain time information, but only
    helps organize and use time representations that may be maintained
    separately across various contexts.  A nanosecond is defined as one
    thousandth of a microsecond, a microsecond as one thousandth of a
    millisecond, a millisecond as one thousandth of a second, a minute
    as sixty seconds, an hour as sixty minutes, and a day as twenty four
    hours.
    
    A `TimeUnit` is mainly used to inform time-based methods
    how a given timing parameter should be interpreted. For example,
    the following code will timeout in 50 milliseconds if the java.util.concurrent.locks.Lock lock is not available:
    
    ``` `Lock lock = ...;
    if (lock.tryLock(50L, TimeUnit.MILLISECONDS)) ...````
    
    while this code will timeout in 50 seconds:
    ``` `Lock lock = ...;
    if (lock.tryLock(50L, TimeUnit.SECONDS)) ...````
    
    Note however, that there is no guarantee that a particular timeout
    implementation will be able to notice the passage of time at the
    same granularity as the given `TimeUnit`.

    Author(s)
    - Doug Lea

    Since
    - 1.5
    """

    NANOSECONDS = (TimeUnit.NANO_SCALE)
    """
    Time unit representing one thousandth of a microsecond.
    """
    MICROSECONDS = (TimeUnit.MICRO_SCALE)
    """
    Time unit representing one thousandth of a millisecond.
    """
    MILLISECONDS = (TimeUnit.MILLI_SCALE)
    """
    Time unit representing one thousandth of a second.
    """
    SECONDS = (TimeUnit.SECOND_SCALE)
    """
    Time unit representing one second.
    """
    MINUTES = (TimeUnit.MINUTE_SCALE)
    """
    Time unit representing sixty seconds.

    Since
    - 1.6
    """
    HOURS = (TimeUnit.HOUR_SCALE)
    """
    Time unit representing sixty minutes.

    Since
    - 1.6
    """
    DAYS = (TimeUnit.DAY_SCALE)
    """
    Time unit representing twenty four hours.

    Since
    - 1.6
    """


    def convert(self, sourceDuration: int, sourceUnit: "TimeUnit") -> int:
        """
        Converts the given time duration in the given unit to this unit.
        Conversions from finer to coarser granularities truncate, so
        lose precision. For example, converting `999` milliseconds
        to seconds results in `0`. Conversions from coarser to
        finer granularities with arguments that would numerically
        overflow saturate to `Long.MIN_VALUE` if negative or
        `Long.MAX_VALUE` if positive.
        
        For example, to convert 10 minutes to milliseconds, use:
        `TimeUnit.MILLISECONDS.convert(10L, TimeUnit.MINUTES)`

        Arguments
        - sourceDuration: the time duration in the given `sourceUnit`
        - sourceUnit: the unit of the `sourceDuration` argument

        Returns
        - the converted duration in this unit,
        or `Long.MIN_VALUE` if conversion would negatively overflow,
        or `Long.MAX_VALUE` if it would positively overflow.
        """
        ...


    def convert(self, duration: "Duration") -> int:
        """
        Converts the given time duration to this unit.
        
        For any TimeUnit `unit`,
        `unit.convert(Duration.ofNanos(n))`
        is equivalent to
        `unit.convert(n, NANOSECONDS)`, and
        `unit.convert(Duration.of(n, unit.toChronoUnit()))`
        is equivalent to `n` (in the absence of overflow).

        Arguments
        - duration: the time duration

        Returns
        - the converted duration in this unit,
        or `Long.MIN_VALUE` if conversion would negatively overflow,
        or `Long.MAX_VALUE` if it would positively overflow.

        Raises
        - NullPointerException: if `duration` is null

        See
        - Duration.of(long,TemporalUnit)

        Since
        - 11

        Unknown Tags
        - This method differs from Duration.toNanos() in that it
        does not throw ArithmeticException on numeric overflow.
        """
        ...


    def toNanos(self, duration: int) -> int:
        """
        Equivalent to
        .convert(long, TimeUnit) NANOSECONDS.convert(duration, this).

        Arguments
        - duration: the duration

        Returns
        - the converted duration,
        or `Long.MIN_VALUE` if conversion would negatively overflow,
        or `Long.MAX_VALUE` if it would positively overflow.
        """
        ...


    def toMicros(self, duration: int) -> int:
        """
        Equivalent to
        .convert(long, TimeUnit) MICROSECONDS.convert(duration, this).

        Arguments
        - duration: the duration

        Returns
        - the converted duration,
        or `Long.MIN_VALUE` if conversion would negatively overflow,
        or `Long.MAX_VALUE` if it would positively overflow.
        """
        ...


    def toMillis(self, duration: int) -> int:
        """
        Equivalent to
        .convert(long, TimeUnit) MILLISECONDS.convert(duration, this).

        Arguments
        - duration: the duration

        Returns
        - the converted duration,
        or `Long.MIN_VALUE` if conversion would negatively overflow,
        or `Long.MAX_VALUE` if it would positively overflow.
        """
        ...


    def toSeconds(self, duration: int) -> int:
        """
        Equivalent to
        .convert(long, TimeUnit) SECONDS.convert(duration, this).

        Arguments
        - duration: the duration

        Returns
        - the converted duration,
        or `Long.MIN_VALUE` if conversion would negatively overflow,
        or `Long.MAX_VALUE` if it would positively overflow.
        """
        ...


    def toMinutes(self, duration: int) -> int:
        """
        Equivalent to
        .convert(long, TimeUnit) MINUTES.convert(duration, this).

        Arguments
        - duration: the duration

        Returns
        - the converted duration,
        or `Long.MIN_VALUE` if conversion would negatively overflow,
        or `Long.MAX_VALUE` if it would positively overflow.

        Since
        - 1.6
        """
        ...


    def toHours(self, duration: int) -> int:
        """
        Equivalent to
        .convert(long, TimeUnit) HOURS.convert(duration, this).

        Arguments
        - duration: the duration

        Returns
        - the converted duration,
        or `Long.MIN_VALUE` if conversion would negatively overflow,
        or `Long.MAX_VALUE` if it would positively overflow.

        Since
        - 1.6
        """
        ...


    def toDays(self, duration: int) -> int:
        """
        Equivalent to
        .convert(long, TimeUnit) DAYS.convert(duration, this).

        Arguments
        - duration: the duration

        Returns
        - the converted duration

        Since
        - 1.6
        """
        ...


    def timedWait(self, obj: "Object", timeout: int) -> None:
        """
        Performs a timed Object.wait(long, int) Object.wait
        using this time unit.
        This is a convenience method that converts timeout arguments
        into the form required by the `Object.wait` method.
        
        For example, you could implement a blocking `poll` method
        (see BlockingQueue.poll(long, TimeUnit) BlockingQueue.poll)
        using:
        
        ``` `public E poll(long timeout, TimeUnit unit)
            throws InterruptedException {
          synchronized (lock) {
            while (isEmpty()) {
              unit.timedWait(lock, timeout);
              ...`
          }
        }}```

        Arguments
        - obj: the object to wait on
        - timeout: the maximum time to wait. If less than
        or equal to zero, do not wait at all.

        Raises
        - InterruptedException: if interrupted while waiting
        """
        ...


    def timedJoin(self, thread: "Thread", timeout: int) -> None:
        """
        Performs a timed Thread.join(long, int) Thread.join
        using this time unit.
        This is a convenience method that converts time arguments into the
        form required by the `Thread.join` method.

        Arguments
        - thread: the thread to wait for
        - timeout: the maximum time to wait. If less than
        or equal to zero, do not wait at all.

        Raises
        - InterruptedException: if interrupted while waiting
        """
        ...


    def sleep(self, timeout: int) -> None:
        """
        Performs a Thread.sleep(long, int) Thread.sleep using
        this time unit.
        This is a convenience method that converts time arguments into the
        form required by the `Thread.sleep` method.

        Arguments
        - timeout: the minimum time to sleep. If less than
        or equal to zero, do not sleep at all.

        Raises
        - InterruptedException: if interrupted while sleeping
        """
        ...


    def toChronoUnit(self) -> "ChronoUnit":
        """
        Converts this `TimeUnit` to the equivalent `ChronoUnit`.

        Returns
        - the converted equivalent ChronoUnit

        Since
        - 9
        """
        ...


    @staticmethod
    def of(chronoUnit: "ChronoUnit") -> "TimeUnit":
        """
        Converts a `ChronoUnit` to the equivalent `TimeUnit`.

        Arguments
        - chronoUnit: the ChronoUnit to convert

        Returns
        - the converted equivalent TimeUnit

        Raises
        - IllegalArgumentException: if `chronoUnit` has no
                equivalent TimeUnit
        - NullPointerException: if `chronoUnit` is null

        Since
        - 9
        """
        ...
