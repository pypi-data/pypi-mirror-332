"""
Python module generated from Java source file org.bukkit.plugin.TimedRegisteredListener

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.event import Event
from org.bukkit.event import EventException
from org.bukkit.event import EventPriority
from org.bukkit.event import Listener
from org.bukkit.plugin import *
from typing import Any, Callable, Iterable, Tuple


class TimedRegisteredListener(RegisteredListener):
    """
    Extends RegisteredListener to include timing information
    """

    def __init__(self, pluginListener: "Listener", eventExecutor: "EventExecutor", eventPriority: "EventPriority", registeredPlugin: "Plugin", listenCancelled: bool):
        ...


    def callEvent(self, event: "Event") -> None:
        ...


    def reset(self) -> None:
        """
        Resets the call count and total time for this listener
        """
        ...


    def getCount(self) -> int:
        """
        Gets the total times this listener has been called

        Returns
        - Times this listener has been called
        """
        ...


    def getTotalTime(self) -> int:
        """
        Gets the total time calls to this listener have taken

        Returns
        - Total time for all calls of this listener
        """
        ...


    def getEventClass(self) -> type["Event"]:
        """
        Gets the class of the events this listener handled. If it handled
        multiple classes of event, the closest shared superclass will be
        returned, such that for any event this listener has handled,
        `this.getEventClass().isAssignableFrom(event.getClass())`
        and no class `this.getEventClass().isAssignableFrom(clazz)
        && this.getEventClass() != clazz &&
        event.getClass().isAssignableFrom(clazz)` for all handled events.

        Returns
        - the event class handled by this RegisteredListener
        """
        ...


    def hasMultiple(self) -> bool:
        """
        Gets whether this listener has handled multiple events, such that for
        some two events, `eventA.getClass() != eventB.getClass()`.

        Returns
        - True if this listener has handled multiple events
        """
        ...
