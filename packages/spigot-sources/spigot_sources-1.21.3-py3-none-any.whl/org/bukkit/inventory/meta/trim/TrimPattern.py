"""
Python module generated from Java source file org.bukkit.inventory.meta.trim.TrimPattern

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

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
from typing import Any, Callable, Iterable, Tuple


class TrimPattern(Keyed, Translatable):
    """
    Represents a pattern that may be used in an ArmorTrim.
    """

    SENTRY = getTrimPattern("sentry")
    """
    Material.SENTRY_ARMOR_TRIM_SMITHING_TEMPLATE.
    """
    DUNE = getTrimPattern("dune")
    """
    Material.DUNE_ARMOR_TRIM_SMITHING_TEMPLATE.
    """
    COAST = getTrimPattern("coast")
    """
    Material.COAST_ARMOR_TRIM_SMITHING_TEMPLATE.
    """
    WILD = getTrimPattern("wild")
    """
    Material.WILD_ARMOR_TRIM_SMITHING_TEMPLATE.
    """
    WARD = getTrimPattern("ward")
    """
    Material.WARD_ARMOR_TRIM_SMITHING_TEMPLATE.
    """
    EYE = getTrimPattern("eye")
    """
    Material.EYE_ARMOR_TRIM_SMITHING_TEMPLATE.
    """
    VEX = getTrimPattern("vex")
    """
    Material.VEX_ARMOR_TRIM_SMITHING_TEMPLATE.
    """
    TIDE = getTrimPattern("tide")
    """
    Material.TIDE_ARMOR_TRIM_SMITHING_TEMPLATE.
    """
    SNOUT = getTrimPattern("snout")
    """
    Material.SNOUT_ARMOR_TRIM_SMITHING_TEMPLATE.
    """
    RIB = getTrimPattern("rib")
    """
    Material.RIB_ARMOR_TRIM_SMITHING_TEMPLATE.
    """
    SPIRE = getTrimPattern("spire")
    """
    Material.SPIRE_ARMOR_TRIM_SMITHING_TEMPLATE.
    """
    WAYFINDER = getTrimPattern("wayfinder")
    """
    Material.WAYFINDER_ARMOR_TRIM_SMITHING_TEMPLATE.
    """
    SHAPER = getTrimPattern("shaper")
    """
    Material.SHAPER_ARMOR_TRIM_SMITHING_TEMPLATE.
    """
    SILENCE = getTrimPattern("silence")
    """
    Material.SILENCE_ARMOR_TRIM_SMITHING_TEMPLATE.
    """
    RAISER = getTrimPattern("raiser")
    """
    Material.RAISER_ARMOR_TRIM_SMITHING_TEMPLATE.
    """
    HOST = getTrimPattern("host")
    """
    Material.HOST_ARMOR_TRIM_SMITHING_TEMPLATE.
    """
    FLOW = getTrimPattern("flow")
    """
    Material.FLOW_ARMOR_TRIM_SMITHING_TEMPLATE.
    """
    BOLT = getTrimPattern("bolt")
    """
    Material.BOLT_ARMOR_TRIM_SMITHING_TEMPLATE.
    """


    @staticmethod
    def getTrimPattern(key: str) -> "TrimPattern":
        ...
