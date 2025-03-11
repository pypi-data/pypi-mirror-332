"""
Python module generated from Java source file org.bukkit.inventory.meta.ArmorMeta

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.inventory.meta import *
from org.bukkit.inventory.meta.trim import ArmorTrim
from typing import Any, Callable, Iterable, Tuple


class ArmorMeta(ItemMeta):
    """
    Represents armor that an entity can equip.
    
    <strong>Note: Armor trims are part of an experimental feature of Minecraft
    and hence subject to change.</strong>
    """

    def hasTrim(self) -> bool:
        """
        Check whether or not this item has an armor trim.

        Returns
        - True if has a trim, False otherwise
        """
        ...


    def setTrim(self, trim: "ArmorTrim") -> None:
        """
        Set the ArmorTrim.

        Arguments
        - trim: the trim to set, or null to remove it
        """
        ...


    def getTrim(self) -> "ArmorTrim":
        """
        Get the ArmorTrim.

        Returns
        - the armor trim, or null if none
        """
        ...


    def clone(self) -> "ArmorMeta":
        ...
