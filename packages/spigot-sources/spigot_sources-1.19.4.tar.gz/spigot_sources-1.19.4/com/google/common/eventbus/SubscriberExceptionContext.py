"""
Python module generated from Java source file com.google.common.eventbus.SubscriberExceptionContext

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.eventbus import *
from java.lang.reflect import Method
from typing import Any, Callable, Iterable, Tuple


class SubscriberExceptionContext:
    """
    Context for an exception thrown by a subscriber.

    Since
    - 16.0
    """

    def getEventBus(self) -> "EventBus":
        """
        Returns
        - The EventBus that handled the event and the subscriber. Useful for broadcasting
            a new event based on the error.
        """
        ...


    def getEvent(self) -> "Object":
        """
        Returns
        - The event object that caused the subscriber to throw.
        """
        ...


    def getSubscriber(self) -> "Object":
        """
        Returns
        - The object context that the subscriber was called on.
        """
        ...


    def getSubscriberMethod(self) -> "Method":
        """
        Returns
        - The subscribed method that threw the exception.
        """
        ...
