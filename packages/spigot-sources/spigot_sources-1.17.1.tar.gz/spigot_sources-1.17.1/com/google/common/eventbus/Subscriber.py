"""
Python module generated from Java source file com.google.common.eventbus.Subscriber

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import VisibleForTesting
from com.google.common.eventbus import *
from com.google.j2objc.annotations import Weak
from java.lang.reflect import InvocationTargetException
from java.lang.reflect import Method
from java.util.concurrent import Executor
from javax.annotation import Nullable
from typing import Any, Callable, Iterable, Tuple


class Subscriber:
    """
    A subscriber method on a specific object, plus the executor that should be used for dispatching
    events to it.
    
    Two subscribers are equivalent when they refer to the same method on the same object (not
    class). This property is used to ensure that no subscriber method is registered more than once.

    Author(s)
    - Colin Decker
    """

    def hashCode(self) -> int:
        ...


    def equals(self, obj: "Object") -> bool:
        ...
