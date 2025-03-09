"""
Python module generated from Java source file com.google.common.eventbus.SubscriberExceptionHandler

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.eventbus import *
from typing import Any, Callable, Iterable, Tuple


class SubscriberExceptionHandler:
    """
    Handler for exceptions thrown by event subscribers.

    Since
    - 16.0
    """

    def handleException(self, exception: "Throwable", context: "SubscriberExceptionContext") -> None:
        """
        Handles exceptions thrown by subscribers.
        """
        ...
