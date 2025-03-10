"""
Python module generated from Java source file org.bukkit.event.Cancellable

Java source file obtained from artifact spigot-api version 1.17.1-R0.1-20211121.234319-104

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.event import *
from typing import Any, Callable, Iterable, Tuple


class Cancellable:

    def isCancelled(self) -> bool:
        """
        Gets the cancellation state of this event. A cancelled event will not
        be executed in the server, but will still pass to other plugins

        Returns
        - True if this event is cancelled
        """
        ...


    def setCancelled(self, cancel: bool) -> None:
        """
        Sets the cancellation state of this event. A cancelled event will not
        be executed in the server, but will still pass to other plugins.

        Arguments
        - cancel: True if you wish to cancel this event
        """
        ...
