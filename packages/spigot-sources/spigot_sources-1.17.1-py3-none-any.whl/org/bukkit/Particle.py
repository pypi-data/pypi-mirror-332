"""
Python module generated from Java source file org.bukkit.Particle

Java source file obtained from artifact spigot-api version 1.17.1-R0.1-20211121.234319-104

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from enum import Enum
from org.bukkit import *
from org.bukkit.block.data import BlockData
from org.bukkit.inventory import ItemStack
from org.bukkit.material import MaterialData
from typing import Any, Callable, Iterable, Tuple


class Particle(Enum):

    EXPLOSION_NORMAL = 0
    EXPLOSION_LARGE = 1
    EXPLOSION_HUGE = 2
    FIREWORKS_SPARK = 3
    WATER_BUBBLE = 4
    WATER_SPLASH = 5
    WATER_WAKE = 6
    SUSPENDED = 7
    SUSPENDED_DEPTH = 8
    CRIT = 9
    CRIT_MAGIC = 10
    SMOKE_NORMAL = 11
    SMOKE_LARGE = 12
    SPELL = 13
    SPELL_INSTANT = 14
    SPELL_MOB = 15
    SPELL_MOB_AMBIENT = 16
    SPELL_WITCH = 17
    DRIP_WATER = 18
    DRIP_LAVA = 19
    VILLAGER_ANGRY = 20
    VILLAGER_HAPPY = 21
    TOWN_AURA = 22
    NOTE = 23
    PORTAL = 24
    ENCHANTMENT_TABLE = 25
    FLAME = 26
    LAVA = 27
    CLOUD = 28
    REDSTONE = (DustOptions)
    SNOWBALL = 30
    SNOW_SHOVEL = 31
    SLIME = 32
    HEART = 33
    BARRIER = 34
    ITEM_CRACK = (ItemStack)
    BLOCK_CRACK = (BlockData)
    BLOCK_DUST = (BlockData)
    WATER_DROP = 38
    MOB_APPEARANCE = 39
    DRAGON_BREATH = 40
    END_ROD = 41
    DAMAGE_INDICATOR = 42
    SWEEP_ATTACK = 43
    FALLING_DUST = (BlockData)
    TOTEM = 45
    SPIT = 46
    SQUID_INK = 47
    BUBBLE_POP = 48
    CURRENT_DOWN = 49
    BUBBLE_COLUMN_UP = 50
    NAUTILUS = 51
    DOLPHIN = 52
    SNEEZE = 53
    CAMPFIRE_COSY_SMOKE = 54
    CAMPFIRE_SIGNAL_SMOKE = 55
    COMPOSTER = 56
    FLASH = 57
    FALLING_LAVA = 58
    LANDING_LAVA = 59
    FALLING_WATER = 60
    DRIPPING_HONEY = 61
    FALLING_HONEY = 62
    LANDING_HONEY = 63
    FALLING_NECTAR = 64
    SOUL_FIRE_FLAME = 65
    ASH = 66
    CRIMSON_SPORE = 67
    WARPED_SPORE = 68
    SOUL = 69
    DRIPPING_OBSIDIAN_TEAR = 70
    FALLING_OBSIDIAN_TEAR = 71
    LANDING_OBSIDIAN_TEAR = 72
    REVERSE_PORTAL = 73
    WHITE_ASH = 74
    LIGHT = 75
    DUST_COLOR_TRANSITION = (DustTransition)
    VIBRATION = (Vibration)
    FALLING_SPORE_BLOSSOM = 78
    SPORE_BLOSSOM_AIR = 79
    SMALL_FLAME = 80
    SNOWFLAKE = 81
    DRIPPING_DRIPSTONE_LAVA = 82
    FALLING_DRIPSTONE_LAVA = 83
    DRIPPING_DRIPSTONE_WATER = 84
    FALLING_DRIPSTONE_WATER = 85
    GLOW_SQUID_INK = 86
    GLOW = 87
    WAX_ON = 88
    WAX_OFF = 89
    ELECTRIC_SPARK = 90
    SCRAPE = 91
    LEGACY_BLOCK_CRACK = (MaterialData)
    LEGACY_BLOCK_DUST = (MaterialData)
    LEGACY_FALLING_DUST = (MaterialData)


    def getDataType(self) -> type[Any]:
        """
        Returns the required data type for the particle

        Returns
        - the required data type
        """
        ...


    class DustOptions:
        """
        Options which can be applied to redstone dust particles - a particle
        color and size.
        """

        def __init__(self, color: "Color", size: float):
            ...


        def getColor(self) -> "Color":
            """
            The color of the particles to be displayed.

            Returns
            - particle color
            """
            ...


        def getSize(self) -> float:
            """
            Relative size of the particle.

            Returns
            - relative particle size
            """
            ...


    class DustTransition(DustOptions):
        """
        Options which can be applied to a color transitioning dust particles.
        """

        def __init__(self, fromColor: "Color", toColor: "Color", size: float):
            ...


        def getToColor(self) -> "Color":
            """
            The final of the particles to be displayed.

            Returns
            - final particle color
            """
            ...
