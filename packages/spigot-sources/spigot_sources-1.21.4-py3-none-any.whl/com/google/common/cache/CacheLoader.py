"""
Python module generated from Java source file com.google.common.cache.CacheLoader

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import GwtIncompatible
from com.google.common.base import Function
from com.google.common.base import Supplier
from com.google.common.cache import *
from com.google.common.util.concurrent import Futures
from com.google.common.util.concurrent import ListenableFuture
from com.google.common.util.concurrent import ListenableFutureTask
from java.io import Serializable
from java.util.concurrent import Executor
from typing import Any, Callable, Iterable, Tuple


class CacheLoader:
    """
    Computes or retrieves values, based on a key, for use in populating a LoadingCache.
    
    Most implementations will only need to implement .load. Other methods may be
    overridden as desired.
    
    Usage example:
    
    ````CacheLoader<Key, Graph> loader = new CacheLoader<Key, Graph>() {
      public Graph load(Key key) throws AnyException {
        return createExpensiveGraph(key);`
    };
    LoadingCache<Key, Graph> cache = CacheBuilder.newBuilder().build(loader);
    }```
    
    Since this example doesn't support reloading or bulk loading, it can also be specified much
    more simply:
    
    ````CacheLoader<Key, Graph> loader = CacheLoader.from(key -> createExpensiveGraph(key));````

    Author(s)
    - Charles Fry

    Since
    - 10.0
    """

    def load(self, key: "K") -> "V":
        """
        Computes or retrieves the value corresponding to `key`.

        Arguments
        - key: the non-null key whose value should be loaded

        Returns
        - the value associated with `key`; **must not be null**

        Raises
        - Exception: if unable to load the result
        - InterruptedException: if this method is interrupted. `InterruptedException` is
            treated like any other `Exception` in all respects except that, when it is caught,
            the thread's interrupt status is set
        """
        ...


    def reload(self, key: "K", oldValue: "V") -> "ListenableFuture"["V"]:
        """
        Computes or retrieves a replacement value corresponding to an already-cached `key`. This
        method is called when an existing cache entry is refreshed by CacheBuilder.refreshAfterWrite, or through a call to LoadingCache.refresh.
        
        This implementation synchronously delegates to .load. It is recommended that it be
        overridden with an asynchronous implementation when using CacheBuilder.refreshAfterWrite.
        
        **Note:** *all exceptions thrown by this method will be logged and then swallowed*.

        Arguments
        - key: the non-null key whose value should be loaded
        - oldValue: the non-null old value corresponding to `key`

        Returns
        - the future new value associated with `key`; **must not be null, must not return
            null**

        Raises
        - Exception: if unable to reload the result
        - InterruptedException: if this method is interrupted. `InterruptedException` is
            treated like any other `Exception` in all respects except that, when it is caught,
            the thread's interrupt status is set

        Since
        - 11.0
        """
        ...


    def loadAll(self, keys: Iterable["K"]) -> dict["K", "V"]:
        """
        Computes or retrieves the values corresponding to `keys`. This method is called by LoadingCache.getAll.
        
        If the returned map doesn't contain all requested `keys` then the entries it does
        contain will be cached, but `getAll` will throw an exception. If the returned map
        contains extra keys not present in `keys` then all returned entries will be cached, but
        only the entries for `keys` will be returned from `getAll`.
        
        This method should be overridden when bulk retrieval is significantly more efficient than
        many individual lookups. Note that LoadingCache.getAll will defer to individual calls
        to LoadingCache.get if this method is not overridden.

        Arguments
        - keys: the unique, non-null keys whose values should be loaded

        Returns
        - a map from each key in `keys` to the value associated with that key; **may not
            contain null values**

        Raises
        - Exception: if unable to load the result
        - InterruptedException: if this method is interrupted. `InterruptedException` is
            treated like any other `Exception` in all respects except that, when it is caught,
            the thread's interrupt status is set

        Since
        - 11.0
        """
        ...


    @staticmethod
    def from(function: "Function"["K", "V"]) -> "CacheLoader"["K", "V"]:
        """
        Returns a cache loader that uses `function` to load keys, without supporting either
        reloading or bulk loading. This allows creating a cache loader using a lambda expression.
        
        The returned object is serializable if `function` is serializable.

        Arguments
        - function: the function to be used for loading values; must never return `null`

        Returns
        - a cache loader that loads values by passing each key to `function`
        """
        ...


    @staticmethod
    def from(supplier: "Supplier"["V"]) -> "CacheLoader"["Object", "V"]:
        """
        Returns a cache loader based on an *existing* supplier instance. Note that there's no need
        to create a *new* supplier just to pass it in here; just subclass `CacheLoader` and
        implement .load load instead.
        
        The returned object is serializable if `supplier` is serializable.

        Arguments
        - supplier: the supplier to be used for loading values; must never return `null`

        Returns
        - a cache loader that loads values by calling Supplier.get, irrespective of the
            key
        """
        ...


    @staticmethod
    def asyncReloading(loader: "CacheLoader"["K", "V"], executor: "Executor") -> "CacheLoader"["K", "V"]:
        """
        Returns a `CacheLoader` which wraps `loader`, executing calls to CacheLoader.reload using `executor`.
        
        This method is useful only when `loader.reload` has a synchronous implementation, such
        as .reload the default implementation.

        Since
        - 17.0
        """
        ...


    class UnsupportedLoadingOperationException(UnsupportedOperationException):
        """
        Exception thrown by `loadAll()` to indicate that it is not supported.

        Since
        - 19.0
        """




    class InvalidCacheLoadException(RuntimeException):
        """
        Thrown to indicate that an invalid response was returned from a call to CacheLoader.

        Since
        - 11.0
        """

        def __init__(self, message: str):
            ...
