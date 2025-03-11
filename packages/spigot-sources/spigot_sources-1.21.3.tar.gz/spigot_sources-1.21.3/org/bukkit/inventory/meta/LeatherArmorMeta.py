"""
Python module generated from Java source file org.bukkit.inventory.meta.LeatherArmorMeta

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Color
from org.bukkit import Material
from org.bukkit.inventory import ItemFactory
from org.bukkit.inventory.meta import *
from typing import Any, Callable, Iterable, Tuple


class LeatherArmorMeta(ItemMeta):
    """
    Represents leather armor (Material.LEATHER_BOOTS, Material.LEATHER_CHESTPLATE, Material.LEATHER_HELMET, or Material.LEATHER_LEGGINGS) that can be colored.
    """

    def getColor(self) -> "Color":
        """
        Gets the color of the armor. If it has not been set otherwise, it will
        be ItemFactory.getDefaultLeatherColor().

        Returns
        - the color of the armor, never null
        """
        ...


    def setColor(self, color: "Color") -> None:
        """
        Sets the color of the armor.

        Arguments
        - color: the color to set. Setting it to null is equivalent to
            setting it to ItemFactory.getDefaultLeatherColor().
        """
        ...


    def clone(self) -> "LeatherArmorMeta":
        ...
