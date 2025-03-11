"""
Python module generated from Java source file java.util.concurrent.RunnableFuture

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util.concurrent import *
from typing import Any, Callable, Iterable, Tuple


class RunnableFuture(Runnable, Future):
    """
    A Future that is Runnable. Successful execution of
    the `run` method causes completion of the `Future`
    and allows access to its results.
    
    Type `<V>`: The result type returned by this Future's `get` method

    Author(s)
    - Doug Lea

    See
    - Executor

    Since
    - 1.6
    """

    def run(self) -> None:
        """
        Sets this Future to the result of its computation
        unless it has been cancelled.
        """
        ...
