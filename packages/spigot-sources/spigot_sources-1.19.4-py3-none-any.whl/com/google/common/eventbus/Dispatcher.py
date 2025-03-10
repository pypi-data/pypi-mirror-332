"""
Python module generated from Java source file com.google.common.eventbus.Dispatcher

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.collect import Queues
from com.google.common.eventbus import *
from java.util import Iterator
from java.util import Queue
from java.util.concurrent import ConcurrentLinkedQueue
from typing import Any, Callable, Iterable, Tuple


class Dispatcher:
    """
    Handler for dispatching events to subscribers, providing different event ordering guarantees that
    make sense for different situations.
    
    **Note:** The dispatcher is orthogonal to the subscriber's `Executor`. The dispatcher
    controls the order in which events are dispatched, while the executor controls how (i.e. on which
    thread) the subscriber is actually called when an event is dispatched to it.

    Author(s)
    - Colin Decker
    """


