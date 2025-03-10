"""
Python module generated from Java source file com.google.common.util.concurrent.ListenerCallQueue

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.base import Preconditions
from com.google.common.collect import Queues
from com.google.common.util.concurrent import *
from java.util import Queue
from java.util.concurrent import Executor
from javax.annotation.concurrent import GuardedBy
from typing import Any, Callable, Iterable, Tuple


class ListenerCallQueue(Runnable):
    """
    A special purpose queue/executor that executes listener callbacks serially on a configured
    executor. Each callback task can be enqueued and executed as separate phases.
    
    This class is very similar to SerializingExecutor with the exception that tasks can be
    enqueued without necessarily executing immediately.
    """

    def run(self) -> None:
        ...
