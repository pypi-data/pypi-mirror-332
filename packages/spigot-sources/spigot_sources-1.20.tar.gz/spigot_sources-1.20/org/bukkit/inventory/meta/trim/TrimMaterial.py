"""
Python module generated from Java source file org.bukkit.inventory.meta.trim.TrimMaterial

Java source file obtained from artifact spigot-api version 1.20-R0.1-20230612.113428-32

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Keyed
from org.bukkit import Material
from org.bukkit import NamespacedKey
from org.bukkit import Registry
from org.bukkit.inventory.meta.trim import *
from typing import Any, Callable, Iterable, Tuple


class TrimMaterial(Keyed):
    """
    Represents a material that may be used in an ArmorTrim.
    """

    QUARTZ = Registry.TRIM_MATERIAL.get(NamespacedKey.minecraft("quartz"))
    """
    Material.QUARTZ.
    """
    IRON = Registry.TRIM_MATERIAL.get(NamespacedKey.minecraft("iron"))
    """
    Material.IRON_INGOT.
    """
    NETHERITE = Registry.TRIM_MATERIAL.get(NamespacedKey.minecraft("netherite"))
    """
    Material.NETHERITE_INGOT.
    """
    REDSTONE = Registry.TRIM_MATERIAL.get(NamespacedKey.minecraft("redstone"))
    """
    Material.REDSTONE.
    """
    COPPER = Registry.TRIM_MATERIAL.get(NamespacedKey.minecraft("copper"))
    """
    Material.COPPER_INGOT.
    """
    GOLD = Registry.TRIM_MATERIAL.get(NamespacedKey.minecraft("gold"))
    """
    Material.GOLD_INGOT.
    """
    EMERALD = Registry.TRIM_MATERIAL.get(NamespacedKey.minecraft("emerald"))
    """
    Material.EMERALD.
    """
    DIAMOND = Registry.TRIM_MATERIAL.get(NamespacedKey.minecraft("diamond"))
    """
    Material.DIAMOND.
    """
    LAPIS = Registry.TRIM_MATERIAL.get(NamespacedKey.minecraft("lapis"))
    """
    Material.LAPIS_LAZULI.
    """
    AMETHYST = Registry.TRIM_MATERIAL.get(NamespacedKey.minecraft("amethyst"))
    """
    Material.AMETHYST_SHARD.
    """
