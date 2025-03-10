"""
Python module generated from Java source file org.bukkit.Particle

Java source file obtained from artifact spigot-api version 1.20-R0.1-20230612.113428-32

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
    """
    Uses Particle.DustOptions as DataType
    """
    SNOWBALL = 30
    SNOW_SHOVEL = 31
    SLIME = 32
    HEART = 33
    ITEM_CRACK = (ItemStack)
    """
    Uses ItemStack as DataType
    """
    BLOCK_CRACK = (BlockData)
    """
    Uses BlockData as DataType
    """
    BLOCK_DUST = (BlockData)
    """
    Uses BlockData as DataType
    """
    WATER_DROP = 37
    MOB_APPEARANCE = 38
    DRAGON_BREATH = 39
    END_ROD = 40
    DAMAGE_INDICATOR = 41
    SWEEP_ATTACK = 42
    FALLING_DUST = (BlockData)
    """
    Uses BlockData as DataType
    """
    TOTEM = 44
    SPIT = 45
    SQUID_INK = 46
    BUBBLE_POP = 47
    CURRENT_DOWN = 48
    BUBBLE_COLUMN_UP = 49
    NAUTILUS = 50
    DOLPHIN = 51
    SNEEZE = 52
    CAMPFIRE_COSY_SMOKE = 53
    CAMPFIRE_SIGNAL_SMOKE = 54
    COMPOSTER = 55
    FLASH = 56
    FALLING_LAVA = 57
    LANDING_LAVA = 58
    FALLING_WATER = 59
    DRIPPING_HONEY = 60
    FALLING_HONEY = 61
    LANDING_HONEY = 62
    FALLING_NECTAR = 63
    SOUL_FIRE_FLAME = 64
    ASH = 65
    CRIMSON_SPORE = 66
    WARPED_SPORE = 67
    SOUL = 68
    DRIPPING_OBSIDIAN_TEAR = 69
    FALLING_OBSIDIAN_TEAR = 70
    LANDING_OBSIDIAN_TEAR = 71
    REVERSE_PORTAL = 72
    WHITE_ASH = 73
    DUST_COLOR_TRANSITION = (DustTransition)
    """
    Uses DustTransition as DataType
    """
    VIBRATION = (Vibration)
    """
    Uses Vibration as DataType
    """
    FALLING_SPORE_BLOSSOM = 76
    SPORE_BLOSSOM_AIR = 77
    SMALL_FLAME = 78
    SNOWFLAKE = 79
    DRIPPING_DRIPSTONE_LAVA = 80
    FALLING_DRIPSTONE_LAVA = 81
    DRIPPING_DRIPSTONE_WATER = 82
    FALLING_DRIPSTONE_WATER = 83
    GLOW_SQUID_INK = 84
    GLOW = 85
    WAX_ON = 86
    WAX_OFF = 87
    ELECTRIC_SPARK = 88
    SCRAPE = 89
    SONIC_BOOM = 90
    SCULK_SOUL = 91
    SCULK_CHARGE = (Float)
    SCULK_CHARGE_POP = 93
    SHRIEK = (Integer)
    CHERRY_LEAVES = 95
    EGG_CRACK = 96
    BLOCK_MARKER = (BlockData)
    """
    Uses BlockData as DataType
    """
    LEGACY_BLOCK_CRACK = (MaterialData)
    """
    Uses MaterialData as DataType
    """
    LEGACY_BLOCK_DUST = (MaterialData)
    """
    Uses MaterialData as DataType
    """
    LEGACY_FALLING_DUST = (MaterialData)
    """
    Uses MaterialData as DataType
    """


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
