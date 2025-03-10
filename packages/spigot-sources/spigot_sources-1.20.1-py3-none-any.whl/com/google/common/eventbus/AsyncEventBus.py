"""
Python module generated from Java source file com.google.common.eventbus.AsyncEventBus

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.eventbus import *
from java.util.concurrent import Executor
from typing import Any, Callable, Iterable, Tuple


class AsyncEventBus(EventBus):
    """
    An EventBus that takes the Executor of your choice and uses it to dispatch events,
    allowing dispatch to occur asynchronously.

    Author(s)
    - Cliff Biffle

    Since
    - 10.0
    """

    def __init__(self, identifier: str, executor: "Executor"):
        """
        Creates a new AsyncEventBus that will use `executor` to dispatch events. Assigns `identifier` as the bus's name for logging purposes.

        Arguments
        - identifier: short name for the bus, for logging purposes.
        - executor: Executor to use to dispatch events. It is the caller's responsibility to shut
            down the executor after the last event has been posted to this event bus.
        """
        ...


    def __init__(self, executor: "Executor", subscriberExceptionHandler: "SubscriberExceptionHandler"):
        """
        Creates a new AsyncEventBus that will use `executor` to dispatch events.

        Arguments
        - executor: Executor to use to dispatch events. It is the caller's responsibility to shut
            down the executor after the last event has been posted to this event bus.
        - subscriberExceptionHandler: Handler used to handle exceptions thrown from subscribers.
            See SubscriberExceptionHandler for more information.

        Since
        - 16.0
        """
        ...


    def __init__(self, executor: "Executor"):
        """
        Creates a new AsyncEventBus that will use `executor` to dispatch events.

        Arguments
        - executor: Executor to use to dispatch events. It is the caller's responsibility to shut
            down the executor after the last event has been posted to this event bus.
        """
        ...
