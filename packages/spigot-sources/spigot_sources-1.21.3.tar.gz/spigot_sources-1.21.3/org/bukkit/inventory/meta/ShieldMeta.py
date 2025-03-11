"""
Python module generated from Java source file org.bukkit.inventory.meta.ShieldMeta

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import DyeColor
from org.bukkit.inventory.meta import *
from typing import Any, Callable, Iterable, Tuple


class ShieldMeta(BannerMeta):

    def getBaseColor(self) -> "DyeColor":
        """
        Gets the base color for this shield.

        Returns
        - the base color or null
        """
        ...


    def setBaseColor(self, color: "DyeColor") -> None:
        """
        Sets the base color for this shield.
        
        **Note:** If the shield contains a
        org.bukkit.block.banner.Pattern, then a null base color will
        retain the pattern but default the base color to DyeColor.WHITE.

        Arguments
        - color: the base color or null
        """
        ...
