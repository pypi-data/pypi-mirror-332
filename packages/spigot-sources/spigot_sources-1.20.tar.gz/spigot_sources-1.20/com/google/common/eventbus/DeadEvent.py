"""
Python module generated from Java source file com.google.common.eventbus.DeadEvent

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import MoreObjects
from com.google.common.eventbus import *
from typing import Any, Callable, Iterable, Tuple


class DeadEvent:
    """
    Wraps an event that was posted, but which had no subscribers and thus could not be delivered.
    
    Registering a DeadEvent subscriber is useful for debugging or logging, as it can detect
    misconfigurations in a system's event distribution.

    Author(s)
    - Cliff Biffle

    Since
    - 10.0
    """

    def __init__(self, source: "Object", event: "Object"):
        """
        Creates a new DeadEvent.

        Arguments
        - source: object broadcasting the DeadEvent (generally the EventBus).
        - event: the event that could not be delivered.
        """
        ...


    def getSource(self) -> "Object":
        """
        Returns the object that originated this event (*not* the object that originated the
        wrapped event). This is generally an EventBus.

        Returns
        - the source of this event.
        """
        ...


    def getEvent(self) -> "Object":
        """
        Returns the wrapped, 'dead' event, which the system was unable to deliver to any registered
        subscriber.

        Returns
        - the 'dead' event that could not be delivered.
        """
        ...


    def toString(self) -> str:
        ...
