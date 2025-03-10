"""
Python module generated from Java source file org.bukkit.inventory.meta.ColorableArmorMeta

Java source file obtained from artifact spigot-api version 1.20.3-R0.1-20231207.085553-9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.inventory.meta import *
from typing import Any, Callable, Iterable, Tuple


class ColorableArmorMeta(ArmorMeta, LeatherArmorMeta):
    """
    Represents armor that an entity can equip and can also be colored.
    """

    def clone(self) -> "ColorableArmorMeta":
        ...
