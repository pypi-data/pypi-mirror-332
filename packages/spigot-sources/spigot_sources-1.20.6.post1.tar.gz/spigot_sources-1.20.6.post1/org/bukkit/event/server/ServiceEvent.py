"""
Python module generated from Java source file org.bukkit.event.server.ServiceEvent

Java source file obtained from artifact spigot-api version 1.20.6-R0.1-20240613.150924-57

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.event.server import *
from org.bukkit.plugin import RegisteredServiceProvider
from typing import Any, Callable, Iterable, Tuple


class ServiceEvent(ServerEvent):
    """
    An event relating to a registered service. This is called in a org.bukkit.plugin.ServicesManager
    """

    def __init__(self, provider: "RegisteredServiceProvider"[Any]):
        ...


    def getProvider(self) -> "RegisteredServiceProvider"[Any]:
        ...
