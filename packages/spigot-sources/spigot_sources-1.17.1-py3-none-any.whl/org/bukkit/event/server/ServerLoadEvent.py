"""
Python module generated from Java source file org.bukkit.event.server.ServerLoadEvent

Java source file obtained from artifact spigot-api version 1.17.1-R0.1-20211121.234319-104

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.event import HandlerList
from org.bukkit.event.server import *
from typing import Any, Callable, Iterable, Tuple


class ServerLoadEvent(ServerEvent):
    """
    This event is called when either the server startup or reload has completed.
    """

    def __init__(self, type: "LoadType"):
        """
        Creates a `ServerLoadEvent` with a given loading type.

        Arguments
        - type: the context in which the server was loaded
        """
        ...


    def getType(self) -> "LoadType":
        """
        Gets the context in which the server was loaded.

        Returns
        - the context in which the server was loaded
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...


    class LoadType(Enum):
        """
        Represents the context in which the enclosing event has been completed.
        """

        STARTUP = 0
        RELOAD = 1
