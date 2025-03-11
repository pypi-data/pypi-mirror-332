"""
Python module generated from Java source file org.bukkit.inventory.meta.trim.TrimMaterial

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Keyed
from org.bukkit import Material
from org.bukkit import NamespacedKey
from org.bukkit import Registry
from org.bukkit import Translatable
from org.bukkit.inventory.meta.trim import *
from org.bukkit.registry import RegistryAware
from typing import Any, Callable, Iterable, Tuple


class TrimMaterial(Keyed, Translatable, RegistryAware):
    """
    Represents a material that may be used in an ArmorTrim.
    """

    QUARTZ = getTrimMaterial("quartz")
    """
    Material.QUARTZ.
    """
    IRON = getTrimMaterial("iron")
    """
    Material.IRON_INGOT.
    """
    NETHERITE = getTrimMaterial("netherite")
    """
    Material.NETHERITE_INGOT.
    """
    REDSTONE = getTrimMaterial("redstone")
    """
    Material.REDSTONE.
    """
    COPPER = getTrimMaterial("copper")
    """
    Material.COPPER_INGOT.
    """
    GOLD = getTrimMaterial("gold")
    """
    Material.GOLD_INGOT.
    """
    EMERALD = getTrimMaterial("emerald")
    """
    Material.EMERALD.
    """
    DIAMOND = getTrimMaterial("diamond")
    """
    Material.DIAMOND.
    """
    LAPIS = getTrimMaterial("lapis")
    """
    Material.LAPIS_LAZULI.
    """
    AMETHYST = getTrimMaterial("amethyst")
    """
    Material.AMETHYST_SHARD.
    """
    RESIN = getTrimMaterial("resin")
    """
    Material.RESIN_BRICK.
    """


    @staticmethod
    def getTrimMaterial(key: str) -> "TrimMaterial":
        ...


    def getKey(self) -> "NamespacedKey":
        """
        See
        - .isRegistered()

        Deprecated
        - A key might not always be present, use .getKeyOrThrow() instead.
        """
        ...
