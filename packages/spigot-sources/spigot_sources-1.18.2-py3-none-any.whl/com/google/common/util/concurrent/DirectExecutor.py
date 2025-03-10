"""
Python module generated from Java source file com.google.common.util.concurrent.DirectExecutor

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.util.concurrent import *
from enum import Enum
from java.util.concurrent import Executor
from typing import Any, Callable, Iterable, Tuple


class DirectExecutor(Enum):
    """
    An Executor that runs each task in the thread that invokes Executor.execute
    execute.
    """

    INSTANCE = 0


    def execute(self, command: "Runnable") -> None:
        ...


    def toString(self) -> str:
        ...
