"""
Python module generated from Java source file org.bukkit.event.EventHandler

Java source file obtained from artifact spigot-api version 1.17.1-R0.1-20211121.234319-104

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.event import *
from typing import Any, Callable, Iterable, Tuple


class EventHandler:
    """
    An annotation to mark methods as being event handler methods
    """

    def priority(self) -> "EventPriority":
        """
        Define the priority of the event.
        
        First priority to the last priority executed:
        <ol>
        - LOWEST
        - LOW
        - NORMAL
        - HIGH
        - HIGHEST
        - MONITOR
        </ol>

        Returns
        - the priority
        """
        return EventPriority.NORMAL


    def ignoreCancelled(self) -> bool:
        """
        Define if the handler ignores a cancelled event.
        
        If ignoreCancelled is True and the event is cancelled, the method is
        not called. Otherwise, the method is always called.

        Returns
        - whether cancelled events should be ignored
        """
        return False
