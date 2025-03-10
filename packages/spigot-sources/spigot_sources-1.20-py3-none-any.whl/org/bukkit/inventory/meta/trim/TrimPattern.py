"""
Python module generated from Java source file org.bukkit.inventory.meta.trim.TrimPattern

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


class TrimPattern(Keyed):
    """
    Represents a pattern that may be used in an ArmorTrim.
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
    WAYFINDER = Registry.TRIM_PATTERN.get(NamespacedKey.minecraft("wayfinder"))
    """
    Material.WAYFINDER_ARMOR_TRIM_SMITHING_TEMPLATE.
    """
    SHAPER = Registry.TRIM_PATTERN.get(NamespacedKey.minecraft("shaper"))
    """
    Material.SHAPER_ARMOR_TRIM_SMITHING_TEMPLATE.
    """
    SILENCE = Registry.TRIM_PATTERN.get(NamespacedKey.minecraft("silence"))
    """
    Material.SILENCE_ARMOR_TRIM_SMITHING_TEMPLATE.
    """
    RAISER = Registry.TRIM_PATTERN.get(NamespacedKey.minecraft("raiser"))
    """
    Material.RAISER_ARMOR_TRIM_SMITHING_TEMPLATE.
    """
    HOST = Registry.TRIM_PATTERN.get(NamespacedKey.minecraft("host"))
    """
    Material.HOST_ARMOR_TRIM_SMITHING_TEMPLATE.
    """
