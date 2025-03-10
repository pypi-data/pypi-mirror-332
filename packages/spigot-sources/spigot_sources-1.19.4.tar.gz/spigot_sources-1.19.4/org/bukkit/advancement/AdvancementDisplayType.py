"""
Python module generated from Java source file org.bukkit.advancement.AdvancementDisplayType

Java source file obtained from artifact spigot-api version 1.19.4-R0.1-20230607.155743-88

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit import ChatColor
from org.bukkit.advancement import *
from typing import Any, Callable, Iterable, Tuple


class AdvancementDisplayType(Enum):
    """
    Advancements are displayed in different ways depending on their display type.
    
    This enum contains information about these types and how they are
    represented.
    """

    TASK = (ChatColor.GREEN)
    """
    Task or normal icons have a square icon frame.
    """
    CHALLENGE = (ChatColor.DARK_PURPLE)
    """
    Challenge icons have a stylised icon frame.
    """
    GOAL = (ChatColor.GREEN)
    """
    Goal icons have a rounded icon frame.
    """


    def getColor(self) -> "ChatColor":
        """
        The chat color used by Minecraft for this advancement.

        Returns
        - The chat color used by this advancement type.
        """
        ...
