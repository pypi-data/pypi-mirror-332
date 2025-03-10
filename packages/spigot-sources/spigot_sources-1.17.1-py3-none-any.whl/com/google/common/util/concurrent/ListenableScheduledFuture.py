"""
Python module generated from Java source file com.google.common.util.concurrent.ListenableScheduledFuture

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtIncompatible
from com.google.common.util.concurrent import *
from java.util.concurrent import ScheduledFuture
from typing import Any, Callable, Iterable, Tuple


class ListenableScheduledFuture(ScheduledFuture, ListenableFuture):
    """
    Helper interface to implement both ListenableFuture and ScheduledFuture.

    Author(s)
    - Anthony Zana

    Since
    - 15.0
    """


