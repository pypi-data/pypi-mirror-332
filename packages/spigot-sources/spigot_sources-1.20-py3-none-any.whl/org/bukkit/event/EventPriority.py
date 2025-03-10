"""
Python module generated from Java source file org.bukkit.event.EventPriority

Java source file obtained from artifact spigot-api version 1.20-R0.1-20230612.113428-32

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.event import *
from typing import Any, Callable, Iterable, Tuple


class EventPriority(Enum):
    """
    Represents an event's priority in execution.
    
    Listeners with lower priority are called first
    will listeners with higher priority are called last.
    
    Listeners are called in following order:
    .LOWEST -> .LOW -> .NORMAL -> .HIGH -> .HIGHEST -> .MONITOR
    """

    LOWEST = (0)
    """
    Event call is of very low importance and should be run first, to allow
    other plugins to further customise the outcome
    """
    LOW = (1)
    """
    Event call is of low importance
    """
    NORMAL = (2)
    """
    Event call is neither important nor unimportant, and may be run
    normally
    """
    HIGH = (3)
    """
    Event call is of high importance
    """
    HIGHEST = (4)
    """
    Event call is critical and must have the final say in what happens
    to the event
    """
    MONITOR = (5)
    """
    Event is listened to purely for monitoring the outcome of an event.
    
    No modifications to the event should be made under this priority
    """


    def getSlot(self) -> int:
        ...
