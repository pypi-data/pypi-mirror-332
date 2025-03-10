"""
Python module generated from Java source file com.google.common.base.Suppliers

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import VisibleForTesting
from com.google.common.base import *
from java.io import Serializable
from java.util.concurrent import TimeUnit
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class Suppliers:
    """
    Useful suppliers.
    
    All methods return serializable suppliers as long as they're given serializable parameters.

    Author(s)
    - Harry Heymann

    Since
    - 2.0
    """

    @staticmethod
    def compose(function: "Function"["F", "T"], supplier: "Supplier"["F"]) -> "Supplier"["T"]:
        """
        Returns a new supplier which is the composition of the provided function and supplier. In other
        words, the new supplier's value will be computed by retrieving the value from `supplier`,
        and then applying `function` to that value. Note that the resulting supplier will not
        call `supplier` or invoke `function` until it is called.
        """
        ...


    @staticmethod
    def memoize(delegate: "Supplier"["T"]) -> "Supplier"["T"]:
        """
        Returns a supplier which caches the instance retrieved during the first call to `get()`
        and returns that value on subsequent calls to `get()`. See: <a
        href="http://en.wikipedia.org/wiki/Memoization">memoization</a>
        
        The returned supplier is thread-safe. The delegate's `get()` method will be invoked at
        most once unless the underlying `get()` throws an exception. The supplier's serialized
        form does not contain the cached value, which will be recalculated when `get()` is called
        on the deserialized instance.
        
        When the underlying delegate throws an exception then this memoizing supplier will keep
        delegating calls until it returns valid data.
        
        If `delegate` is an instance created by an earlier call to `memoize`, it is
        returned directly.
        """
        ...


    @staticmethod
    def memoizeWithExpiration(delegate: "Supplier"["T"], duration: int, unit: "TimeUnit") -> "Supplier"["T"]:
        """
        Returns a supplier that caches the instance supplied by the delegate and removes the cached
        value after the specified time has passed. Subsequent calls to `get()` return the cached
        value if the expiration time has not passed. After the expiration time, a new value is
        retrieved, cached, and returned. See: <a
        href="http://en.wikipedia.org/wiki/Memoization">memoization</a>
        
        The returned supplier is thread-safe. The supplier's serialized form does not contain the
        cached value, which will be recalculated when `get()` is called on the reserialized
        instance. The actual memoization does not happen when the underlying delegate throws an
        exception.
        
        When the underlying delegate throws an exception then this memoizing supplier will keep
        delegating calls until it returns valid data.

        Arguments
        - duration: the length of time after a value is created that it should stop being returned
            by subsequent `get()` calls
        - unit: the unit that `duration` is expressed in

        Raises
        - IllegalArgumentException: if `duration` is not positive

        Since
        - 2.0
        """
        ...


    @staticmethod
    def ofInstance(instance: "T") -> "Supplier"["T"]:
        """
        Returns a supplier that always supplies `instance`.
        """
        ...


    @staticmethod
    def synchronizedSupplier(delegate: "Supplier"["T"]) -> "Supplier"["T"]:
        """
        Returns a supplier whose `get()` method synchronizes on `delegate` before calling
        it, making it thread-safe.
        """
        ...


    @staticmethod
    def supplierFunction() -> "Function"["Supplier"["T"], "T"]:
        """
        Returns a function that accepts a supplier and returns the result of invoking Supplier.get on that supplier.
        
        **Java 8 users:** use the method reference `Supplier::get` instead.

        Since
        - 8.0
        """
        ...
