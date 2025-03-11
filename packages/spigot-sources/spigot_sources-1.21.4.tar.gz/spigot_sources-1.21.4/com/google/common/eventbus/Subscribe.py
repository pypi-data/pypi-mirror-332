"""
Python module generated from Java source file com.google.common.eventbus.Subscribe

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.eventbus import *
from typing import Any, Callable, Iterable, Tuple


class Subscribe:
    """
    Marks a method as an event subscriber.
    
    The type of event will be indicated by the method's first (and only) parameter, which cannot
    be primitive. If this annotation is applied to methods with zero parameters, or more than one
    parameter, the object containing the method will not be able to register for event delivery from
    the EventBus.
    
    Unless also annotated with @AllowConcurrentEvents, event subscriber methods will be
    invoked serially by each event bus that they are registered with.

    Author(s)
    - Cliff Biffle

    Since
    - 10.0
    """


