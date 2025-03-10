"""
Python module generated from Java source file com.google.common.util.concurrent.RateLimiter

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import VisibleForTesting
from com.google.common.base import Stopwatch
from com.google.common.util.concurrent import *
from com.google.common.util.concurrent.SmoothRateLimiter import SmoothBursty
from com.google.common.util.concurrent.SmoothRateLimiter import SmoothWarmingUp
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.time import Duration
from java.util import Locale
from java.util.concurrent import TimeUnit
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class RateLimiter:

    @staticmethod
    def create(permitsPerSecond: float) -> "RateLimiter":
        ...


    @staticmethod
    def create(permitsPerSecond: float, warmupPeriod: "Duration") -> "RateLimiter":
        """
        Creates a `RateLimiter` with the specified stable throughput, given as "permits per
        second" (commonly referred to as *QPS*, queries per second), and a *warmup period*,
        during which the `RateLimiter` smoothly ramps up its rate, until it reaches its maximum
        rate at the end of the period (as long as there are enough requests to saturate it). Similarly,
        if the `RateLimiter` is left *unused* for a duration of `warmupPeriod`, it
        will gradually return to its "cold" state, i.e. it will go through the same warming up process
        as when it was first created.
        
        The returned `RateLimiter` is intended for cases where the resource that actually
        fulfills the requests (e.g., a remote server) needs "warmup" time, rather than being
        immediately accessed at the stable (maximum) rate.
        
        The returned `RateLimiter` starts in a "cold" state (i.e. the warmup period will
        follow), and if it is left unused for long enough, it will return to that state.

        Arguments
        - permitsPerSecond: the rate of the returned `RateLimiter`, measured in how many
            permits become available per second
        - warmupPeriod: the duration of the period where the `RateLimiter` ramps up its rate,
            before reaching its stable (maximum) rate

        Raises
        - IllegalArgumentException: if `permitsPerSecond` is negative or zero or `warmupPeriod` is negative

        Since
        - 28.0
        """
        ...


    @staticmethod
    def create(permitsPerSecond: float, warmupPeriod: int, unit: "TimeUnit") -> "RateLimiter":
        """
        Creates a `RateLimiter` with the specified stable throughput, given as "permits per
        second" (commonly referred to as *QPS*, queries per second), and a *warmup period*,
        during which the `RateLimiter` smoothly ramps up its rate, until it reaches its maximum
        rate at the end of the period (as long as there are enough requests to saturate it). Similarly,
        if the `RateLimiter` is left *unused* for a duration of `warmupPeriod`, it
        will gradually return to its "cold" state, i.e. it will go through the same warming up process
        as when it was first created.
        
        The returned `RateLimiter` is intended for cases where the resource that actually
        fulfills the requests (e.g., a remote server) needs "warmup" time, rather than being
        immediately accessed at the stable (maximum) rate.
        
        The returned `RateLimiter` starts in a "cold" state (i.e. the warmup period will
        follow), and if it is left unused for long enough, it will return to that state.

        Arguments
        - permitsPerSecond: the rate of the returned `RateLimiter`, measured in how many
            permits become available per second
        - warmupPeriod: the duration of the period where the `RateLimiter` ramps up its rate,
            before reaching its stable (maximum) rate
        - unit: the time unit of the warmupPeriod argument

        Raises
        - IllegalArgumentException: if `permitsPerSecond` is negative or zero or `warmupPeriod` is negative
        """
        ...


    def setRate(self, permitsPerSecond: float) -> None:
        """
        Updates the stable rate of this `RateLimiter`, that is, the `permitsPerSecond`
        argument provided in the factory method that constructed the `RateLimiter`. Currently
        throttled threads will **not** be awakened as a result of this invocation, thus they do not
        observe the new rate; only subsequent requests will.
        
        Note though that, since each request repays (by waiting, if necessary) the cost of the
        *previous* request, this means that the very next request after an invocation to `setRate` will not be affected by the new rate; it will pay the cost of the previous request,
        which is in terms of the previous rate.
        
        The behavior of the `RateLimiter` is not modified in any other way, e.g. if the `RateLimiter` was configured with a warmup period of 20 seconds, it still has a warmup period of
        20 seconds after this method invocation.

        Arguments
        - permitsPerSecond: the new stable rate of this `RateLimiter`

        Raises
        - IllegalArgumentException: if `permitsPerSecond` is negative or zero
        """
        ...


    def getRate(self) -> float:
        """
        Returns the stable rate (as `permits per seconds`) with which this `RateLimiter` is
        configured with. The initial value of this is the same as the `permitsPerSecond` argument
        passed in the factory method that produced this `RateLimiter`, and it is only updated
        after invocations to .setRate.
        """
        ...


    def acquire(self) -> float:
        """
        Acquires a single permit from this `RateLimiter`, blocking until the request can be
        granted. Tells the amount of time slept, if any.
        
        This method is equivalent to `acquire(1)`.

        Returns
        - time spent sleeping to enforce rate, in seconds; 0.0 if not rate-limited

        Since
        - 16.0 (present in 13.0 with `void` return type})
        """
        ...


    def acquire(self, permits: int) -> float:
        """
        Acquires the given number of permits from this `RateLimiter`, blocking until the request
        can be granted. Tells the amount of time slept, if any.

        Arguments
        - permits: the number of permits to acquire

        Returns
        - time spent sleeping to enforce rate, in seconds; 0.0 if not rate-limited

        Raises
        - IllegalArgumentException: if the requested number of permits is negative or zero

        Since
        - 16.0 (present in 13.0 with `void` return type})
        """
        ...


    def tryAcquire(self, timeout: "Duration") -> bool:
        """
        Acquires a permit from this `RateLimiter` if it can be obtained without exceeding the
        specified `timeout`, or returns `False` immediately (without waiting) if the permit
        would not have been granted before the timeout expired.
        
        This method is equivalent to `tryAcquire(1, timeout)`.

        Arguments
        - timeout: the maximum time to wait for the permit. Negative values are treated as zero.

        Returns
        - `True` if the permit was acquired, `False` otherwise

        Raises
        - IllegalArgumentException: if the requested number of permits is negative or zero

        Since
        - 28.0
        """
        ...


    def tryAcquire(self, timeout: int, unit: "TimeUnit") -> bool:
        """
        Acquires a permit from this `RateLimiter` if it can be obtained without exceeding the
        specified `timeout`, or returns `False` immediately (without waiting) if the permit
        would not have been granted before the timeout expired.
        
        This method is equivalent to `tryAcquire(1, timeout, unit)`.

        Arguments
        - timeout: the maximum time to wait for the permit. Negative values are treated as zero.
        - unit: the time unit of the timeout argument

        Returns
        - `True` if the permit was acquired, `False` otherwise

        Raises
        - IllegalArgumentException: if the requested number of permits is negative or zero
        """
        ...


    def tryAcquire(self, permits: int) -> bool:
        """
        Acquires permits from this RateLimiter if it can be acquired immediately without delay.
        
        This method is equivalent to `tryAcquire(permits, 0, anyUnit)`.

        Arguments
        - permits: the number of permits to acquire

        Returns
        - `True` if the permits were acquired, `False` otherwise

        Raises
        - IllegalArgumentException: if the requested number of permits is negative or zero

        Since
        - 14.0
        """
        ...


    def tryAcquire(self) -> bool:
        """
        Acquires a permit from this RateLimiter if it can be acquired immediately without
        delay.
        
        This method is equivalent to `tryAcquire(1)`.

        Returns
        - `True` if the permit was acquired, `False` otherwise

        Since
        - 14.0
        """
        ...


    def tryAcquire(self, permits: int, timeout: "Duration") -> bool:
        """
        Acquires the given number of permits from this `RateLimiter` if it can be obtained
        without exceeding the specified `timeout`, or returns `False` immediately (without
        waiting) if the permits would not have been granted before the timeout expired.

        Arguments
        - permits: the number of permits to acquire
        - timeout: the maximum time to wait for the permits. Negative values are treated as zero.

        Returns
        - `True` if the permits were acquired, `False` otherwise

        Raises
        - IllegalArgumentException: if the requested number of permits is negative or zero

        Since
        - 28.0
        """
        ...


    def tryAcquire(self, permits: int, timeout: int, unit: "TimeUnit") -> bool:
        """
        Acquires the given number of permits from this `RateLimiter` if it can be obtained
        without exceeding the specified `timeout`, or returns `False` immediately (without
        waiting) if the permits would not have been granted before the timeout expired.

        Arguments
        - permits: the number of permits to acquire
        - timeout: the maximum time to wait for the permits. Negative values are treated as zero.
        - unit: the time unit of the timeout argument

        Returns
        - `True` if the permits were acquired, `False` otherwise

        Raises
        - IllegalArgumentException: if the requested number of permits is negative or zero
        """
        ...


    def toString(self) -> str:
        ...
