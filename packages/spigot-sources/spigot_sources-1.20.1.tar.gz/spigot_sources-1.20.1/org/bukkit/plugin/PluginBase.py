"""
Python module generated from Java source file org.bukkit.plugin.PluginBase

Java source file obtained from artifact spigot-api version 1.20.1-R0.1-20230921.163938-66

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.plugin import *
from typing import Any, Callable, Iterable, Tuple


class PluginBase(Plugin):
    """
    Represents a base Plugin
    
    Extend this class if your plugin is not a org.bukkit.plugin.java.JavaPlugin
    """

    def hashCode(self) -> int:
        ...


    def equals(self, obj: "Object") -> bool:
        ...


    def getName(self) -> str:
        ...
