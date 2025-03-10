"""
Python module generated from Java source file java.util.concurrent.AbstractExecutorService

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import Iterator
from java.util.concurrent import *
from typing import Any, Callable, Iterable, Tuple


class AbstractExecutorService(ExecutorService):
    """
    Provides default implementations of ExecutorService
    execution methods. This class implements the `submit`,
    `invokeAny` and `invokeAll` methods using a
    RunnableFuture returned by `newTaskFor`, which defaults
    to the FutureTask class provided in this package.  For example,
    the implementation of `submit(Runnable)` creates an
    associated `RunnableFuture` that is executed and
    returned. Subclasses may override the `newTaskFor` methods
    to return `RunnableFuture` implementations other than
    `FutureTask`.
    
    **Extension example.** Here is a sketch of a class
    that customizes ThreadPoolExecutor to use
    a `CustomTask` class instead of the default `FutureTask`:
    ``` `public class CustomThreadPoolExecutor extends ThreadPoolExecutor {
    
      static class CustomTask<V> implements RunnableFuture<V> { ...`
    
      protected <V> RunnableFuture<V> newTaskFor(Callable<V> c) {
          return new CustomTask<V>(c);
      }
      protected <V> RunnableFuture<V> newTaskFor(Runnable r, V v) {
          return new CustomTask<V>(r, v);
      }
      // ... add constructors, etc.
    }}```

    Author(s)
    - Doug Lea

    Since
    - 1.5
    """

    def __init__(self):
        """
        Constructor for subclasses to call.
        """
        ...


    def submit(self, task: "Runnable") -> "Future"[Any]:
        """
        Raises
        - RejectedExecutionException: 
        - NullPointerException: 
        """
        ...


    def submit(self, task: "Runnable", result: "T") -> "Future"["T"]:
        """
        Raises
        - RejectedExecutionException: 
        - NullPointerException: 
        """
        ...


    def submit(self, task: "Callable"["T"]) -> "Future"["T"]:
        """
        Raises
        - RejectedExecutionException: 
        - NullPointerException: 
        """
        ...


    def invokeAny(self, tasks: Iterable["Callable"["T"]]) -> "T":
        ...


    def invokeAny(self, tasks: Iterable["Callable"["T"]], timeout: int, unit: "TimeUnit") -> "T":
        ...


    def invokeAll(self, tasks: Iterable["Callable"["T"]]) -> list["Future"["T"]]:
        ...


    def invokeAll(self, tasks: Iterable["Callable"["T"]], timeout: int, unit: "TimeUnit") -> list["Future"["T"]]:
        ...
