"""
Python module generated from Java source file org.bukkit.event.server.ServiceRegisterEvent

Java source file obtained from artifact spigot-api version 1.20.1-R0.1-20230921.163938-66

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.event import HandlerList
from org.bukkit.event.server import *
from org.bukkit.plugin import RegisteredServiceProvider
from typing import Any, Callable, Iterable, Tuple


class ServiceRegisterEvent(ServiceEvent):
    """
    This event is called when a service is registered.
    
    Warning: The order in which register and unregister events are called
    should not be relied upon.
    """

    def __init__(self, registeredProvider: "RegisteredServiceProvider"[Any]):
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
