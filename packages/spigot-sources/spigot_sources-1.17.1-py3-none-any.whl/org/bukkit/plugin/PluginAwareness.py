"""
Python module generated from Java source file org.bukkit.plugin.PluginAwareness

Java source file obtained from artifact spigot-api version 1.17.1-R0.1-20211121.234319-104

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.plugin import *
from typing import Any, Callable, Iterable, Tuple


class PluginAwareness:
    """
    Represents a concept that a plugin is aware of.
    
    The internal representation may be singleton, or be a parameterized
    instance, but must be immutable.
    """

    class Flags(Enum):
        """
        Each entry here represents a particular plugin's awareness. These can
        be checked by using PluginDescriptionFile.getAwareness().Set.contains(Object) contains(flag).
        """

        UTF8 = 0
        """
        This specifies that all (text) resources stored in a plugin's jar
        use UTF-8 encoding.

        Deprecated
        - all plugins are now assumed to be UTF-8 aware.
        """
