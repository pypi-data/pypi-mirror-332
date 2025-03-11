"""
Python module generated from Java source file org.bukkit.plugin.RegisteredServiceProvider

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.plugin import *
from typing import Any, Callable, Iterable, Tuple


class RegisteredServiceProvider(Comparable):
    """
    A registered service provider.
    
    Type `<T>`: Service
    """

    def __init__(self, service: type["T"], provider: "T", priority: "ServicePriority", plugin: "Plugin"):
        ...


    def getService(self) -> type["T"]:
        ...


    def getPlugin(self) -> "Plugin":
        ...


    def getProvider(self) -> "T":
        ...


    def getPriority(self) -> "ServicePriority":
        ...


    def compareTo(self, other: "RegisteredServiceProvider"[Any]) -> int:
        ...
