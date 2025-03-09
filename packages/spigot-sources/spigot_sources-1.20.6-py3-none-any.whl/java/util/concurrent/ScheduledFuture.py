"""
Python module generated from Java source file java.util.concurrent.ScheduledFuture

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util.concurrent import *
from typing import Any, Callable, Iterable, Tuple


class ScheduledFuture(Delayed, Future):
    """
    A delayed result-bearing action that can be cancelled.
    Usually a scheduled future is the result of scheduling
    a task with a ScheduledExecutorService.
    
    Type `<V>`: The result type returned by this Future

    Author(s)
    - Doug Lea

    Since
    - 1.5
    """


