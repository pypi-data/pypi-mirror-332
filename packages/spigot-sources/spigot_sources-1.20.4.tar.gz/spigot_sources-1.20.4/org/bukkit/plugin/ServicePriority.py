"""
Python module generated from Java source file org.bukkit.plugin.ServicePriority

Java source file obtained from artifact spigot-api version 1.20.4-R0.1-20240423.152506-123

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.plugin import *
from typing import Any, Callable, Iterable, Tuple


class ServicePriority(Enum):
    """
    Represents various priorities of a provider.
    """

    Lowest = 0
    Low = 1
    Normal = 2
    High = 3
    Highest = 4
