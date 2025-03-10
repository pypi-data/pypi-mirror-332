"""
Python module generated from Java source file org.bukkit.inventory.meta.trim.TrimPattern

Java source file obtained from artifact spigot-api version 1.19.4-R0.1-20230607.155743-88

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Keyed
from org.bukkit import Material
from org.bukkit import MinecraftExperimental
from org.bukkit import NamespacedKey
from org.bukkit import Registry
from org.bukkit.inventory.meta.trim import *
from typing import Any, Callable, Iterable, Tuple


class TrimPattern(Keyed):
    """
    Represents a pattern that may be used in an ArmorTrim.

    Unknown Tags
    - Armor trims are part of an experimental feature of Minecraft and
    hence subject to change. Constants in this class may be null if a data pack
    is not present to enable these features.
    """

    SENTRY = Registry.TRIM_PATTERN.get(NamespacedKey.minecraft("sentry"))
    """
    Material.SENTRY_ARMOR_TRIM_SMITHING_TEMPLATE.
    """
    DUNE = Registry.TRIM_PATTERN.get(NamespacedKey.minecraft("dune"))
    """
    Material.DUNE_ARMOR_TRIM_SMITHING_TEMPLATE.
    """
    COAST = Registry.TRIM_PATTERN.get(NamespacedKey.minecraft("coast"))
    """
    Material.COAST_ARMOR_TRIM_SMITHING_TEMPLATE.
    """
    WILD = Registry.TRIM_PATTERN.get(NamespacedKey.minecraft("wild"))
    """
    Material.WILD_ARMOR_TRIM_SMITHING_TEMPLATE.
    """
    WARD = Registry.TRIM_PATTERN.get(NamespacedKey.minecraft("ward"))
    """
    Material.WARD_ARMOR_TRIM_SMITHING_TEMPLATE.
    """
    EYE = Registry.TRIM_PATTERN.get(NamespacedKey.minecraft("eye"))
    """
    Material.EYE_ARMOR_TRIM_SMITHING_TEMPLATE.
    """
    VEX = Registry.TRIM_PATTERN.get(NamespacedKey.minecraft("vex"))
    """
    Material.VEX_ARMOR_TRIM_SMITHING_TEMPLATE.
    """
    TIDE = Registry.TRIM_PATTERN.get(NamespacedKey.minecraft("tide"))
    """
    Material.TIDE_ARMOR_TRIM_SMITHING_TEMPLATE.
    """
    SNOUT = Registry.TRIM_PATTERN.get(NamespacedKey.minecraft("snout"))
    """
    Material.SNOUT_ARMOR_TRIM_SMITHING_TEMPLATE.
    """
    RIB = Registry.TRIM_PATTERN.get(NamespacedKey.minecraft("rib"))
    """
    Material.RIB_ARMOR_TRIM_SMITHING_TEMPLATE.
    """
    SPIRE = Registry.TRIM_PATTERN.get(NamespacedKey.minecraft("spire"))
    """
    Material.SPIRE_ARMOR_TRIM_SMITHING_TEMPLATE.
    """
