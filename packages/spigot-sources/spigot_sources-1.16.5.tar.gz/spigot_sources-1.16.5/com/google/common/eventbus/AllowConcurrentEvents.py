"""
Python module generated from Java source file com.google.common.eventbus.AllowConcurrentEvents

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.eventbus import *
from typing import Any, Callable, Iterable, Tuple


class AllowConcurrentEvents:
    """
    Marks an event subscriber method as being thread-safe. This annotation indicates that EventBus
    may invoke the event subscriber simultaneously from multiple threads.
    
    This does not mark the method, and so should be used in combination with Subscribe.

    Author(s)
    - Cliff Biffle

    Since
    - 10.0
    """


