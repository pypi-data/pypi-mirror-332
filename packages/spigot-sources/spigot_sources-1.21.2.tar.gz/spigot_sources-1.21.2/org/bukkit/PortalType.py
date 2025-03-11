"""
Python module generated from Java source file org.bukkit.PortalType

Java source file obtained from artifact spigot-api version 1.21.2-R0.1-20241023.084343-5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit import *
from typing import Any, Callable, Iterable, Tuple


class PortalType(Enum):
    """
    Represents various types of portals that can be made in a world.
    """

    NETHER = 0
    """
    This is a Nether portal, made of obsidian.
    """
    ENDER = 1
    """
    This is an Ender portal.
    """
    CUSTOM = 2
    """
    This is a custom Plugin portal.
    """
