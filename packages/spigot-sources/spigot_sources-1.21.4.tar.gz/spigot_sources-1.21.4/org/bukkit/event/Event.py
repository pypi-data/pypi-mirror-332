"""
Python module generated from Java source file org.bukkit.event.Event

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.event import *
from org.bukkit.plugin import Plugin
from org.bukkit.plugin import PluginManager
from typing import Any, Callable, Iterable, Tuple


class Event:
    """
    Represents an event.
    
    All events require a static method named getHandlerList() which returns the same HandlerList as .getHandlers().

    See
    - PluginManager.registerEvents(Listener,Plugin)
    """

    def __init__(self):
        """
        The default constructor is defined for cleaner code. This constructor
        assumes the event is synchronous.
        """
        ...


    def __init__(self, isAsync: bool):
        """
        This constructor is used to explicitly declare an event as synchronous
        or asynchronous.

        Arguments
        - isAsync: True indicates the event will fire asynchronously, False
            by default from default constructor
        """
        ...


    def getEventName(self) -> str:
        """
        Convenience method for providing a user-friendly identifier. By
        default, it is the event's class's Class.getSimpleName()
        simple name.

        Returns
        - name of this event
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    def isAsynchronous(self) -> bool:
        """
        Any custom event that should not by synchronized with other events must
        use the specific constructor. These are the caveats of using an
        asynchronous event:
        
        - The event is never fired from inside code triggered by a
            synchronous event. Attempting to do so results in an java.lang.IllegalStateException.
        - However, asynchronous event handlers may fire synchronous or
            asynchronous events
        - The event may be fired multiple times simultaneously and in any
            order.
        - Any newly registered or unregistered handler is ignored after an
            event starts execution.
        - The handlers for this event may block for any length of time.
        - Some implementations may selectively declare a specific event use
            as asynchronous. This behavior should be clearly defined.
        - Asynchronous calls are not calculated in the plugin timing system.

        Returns
        - False by default, True if the event fires asynchronously
        """
        ...


    class Result(Enum):

        DENY = 0
        """
        Deny the event. Depending on the event, the action indicated by the
        event will either not take place or will be reverted. Some actions
        may not be denied.
        """
        DEFAULT = 1
        """
        Neither deny nor allow the event. The server will proceed with its
        normal handling.
        """
        ALLOW = 2
        """
        Allow / Force the event. The action indicated by the event will
        take place if possible, even if the server would not normally allow
        the action. Some actions may not be allowed.
        """
