"""
Python module generated from Java source file org.bukkit.Particle

Java source file obtained from artifact spigot-api version 1.21.2-R0.1-20241023.084343-5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from enum import Enum
from org.bukkit import *
from org.bukkit.block.data import BlockData
from org.bukkit.inventory import ItemStack
from typing import Any, Callable, Iterable, Tuple


class Particle(Enum):

    POOF = ("poof")
    EXPLOSION = ("explosion")
    EXPLOSION_EMITTER = ("explosion_emitter")
    FIREWORK = ("firework")
    BUBBLE = ("bubble")
    SPLASH = ("splash")
    FISHING = ("fishing")
    UNDERWATER = ("underwater")
    CRIT = ("crit")
    ENCHANTED_HIT = ("enchanted_hit")
    SMOKE = ("smoke")
    LARGE_SMOKE = ("large_smoke")
    EFFECT = ("effect")
    INSTANT_EFFECT = ("instant_effect")
    ENTITY_EFFECT = ("entity_effect", Color)
    """
    Uses Color as DataType
    """
    WITCH = ("witch")
    DRIPPING_WATER = ("dripping_water")
    DRIPPING_LAVA = ("dripping_lava")
    ANGRY_VILLAGER = ("angry_villager")
    HAPPY_VILLAGER = ("happy_villager")
    MYCELIUM = ("mycelium")
    NOTE = ("note")
    PORTAL = ("portal")
    ENCHANT = ("enchant")
    FLAME = ("flame")
    LAVA = ("lava")
    CLOUD = ("cloud")
    DUST = ("dust", DustOptions)
    """
    Uses Particle.DustOptions as DataType
    """
    ITEM_SNOWBALL = ("item_snowball")
    ITEM_SLIME = ("item_slime")
    HEART = ("heart")
    ITEM = ("item", ItemStack)
    """
    Uses ItemStack as DataType
    """
    BLOCK = ("block", BlockData)
    """
    Uses BlockData as DataType
    """
    RAIN = ("rain")
    ELDER_GUARDIAN = ("elder_guardian")
    DRAGON_BREATH = ("dragon_breath")
    END_ROD = ("end_rod")
    DAMAGE_INDICATOR = ("damage_indicator")
    SWEEP_ATTACK = ("sweep_attack")
    FALLING_DUST = ("falling_dust", BlockData)
    """
    Uses BlockData as DataType
    """
    TOTEM_OF_UNDYING = ("totem_of_undying")
    SPIT = ("spit")
    SQUID_INK = ("squid_ink")
    BUBBLE_POP = ("bubble_pop")
    CURRENT_DOWN = ("current_down")
    BUBBLE_COLUMN_UP = ("bubble_column_up")
    NAUTILUS = ("nautilus")
    DOLPHIN = ("dolphin")
    SNEEZE = ("sneeze")
    CAMPFIRE_COSY_SMOKE = ("campfire_cosy_smoke")
    CAMPFIRE_SIGNAL_SMOKE = ("campfire_signal_smoke")
    COMPOSTER = ("composter")
    FLASH = ("flash")
    FALLING_LAVA = ("falling_lava")
    LANDING_LAVA = ("landing_lava")
    FALLING_WATER = ("falling_water")
    DRIPPING_HONEY = ("dripping_honey")
    FALLING_HONEY = ("falling_honey")
    LANDING_HONEY = ("landing_honey")
    FALLING_NECTAR = ("falling_nectar")
    SOUL_FIRE_FLAME = ("soul_fire_flame")
    ASH = ("ash")
    CRIMSON_SPORE = ("crimson_spore")
    WARPED_SPORE = ("warped_spore")
    SOUL = ("soul")
    DRIPPING_OBSIDIAN_TEAR = ("dripping_obsidian_tear")
    FALLING_OBSIDIAN_TEAR = ("falling_obsidian_tear")
    LANDING_OBSIDIAN_TEAR = ("landing_obsidian_tear")
    REVERSE_PORTAL = ("reverse_portal")
    WHITE_ASH = ("white_ash")
    DUST_COLOR_TRANSITION = ("dust_color_transition", DustTransition)
    """
    Uses DustTransition as DataType
    """
    VIBRATION = ("vibration", Vibration)
    """
    Uses Vibration as DataType
    """
    FALLING_SPORE_BLOSSOM = ("falling_spore_blossom")
    SPORE_BLOSSOM_AIR = ("spore_blossom_air")
    SMALL_FLAME = ("small_flame")
    SNOWFLAKE = ("snowflake")
    DRIPPING_DRIPSTONE_LAVA = ("dripping_dripstone_lava")
    FALLING_DRIPSTONE_LAVA = ("falling_dripstone_lava")
    DRIPPING_DRIPSTONE_WATER = ("dripping_dripstone_water")
    FALLING_DRIPSTONE_WATER = ("falling_dripstone_water")
    GLOW_SQUID_INK = ("glow_squid_ink")
    GLOW = ("glow")
    WAX_ON = ("wax_on")
    WAX_OFF = ("wax_off")
    ELECTRIC_SPARK = ("electric_spark")
    SCRAPE = ("scrape")
    SONIC_BOOM = ("sonic_boom")
    SCULK_SOUL = ("sculk_soul")
    SCULK_CHARGE = ("sculk_charge", Float)
    """
    Use Float as DataType
    """
    SCULK_CHARGE_POP = ("sculk_charge_pop")
    SHRIEK = ("shriek", Integer)
    """
    Use Integer as DataType
    """
    CHERRY_LEAVES = ("cherry_leaves")
    EGG_CRACK = ("egg_crack")
    DUST_PLUME = ("dust_plume")
    WHITE_SMOKE = ("white_smoke")
    GUST = ("gust")
    SMALL_GUST = ("small_gust")
    GUST_EMITTER_LARGE = ("gust_emitter_large")
    GUST_EMITTER_SMALL = ("gust_emitter_small")
    TRIAL_SPAWNER_DETECTION = ("trial_spawner_detection")
    TRIAL_SPAWNER_DETECTION_OMINOUS = ("trial_spawner_detection_ominous")
    VAULT_CONNECTION = ("vault_connection")
    INFESTED = ("infested")
    ITEM_COBWEB = ("item_cobweb")
    DUST_PILLAR = ("dust_pillar", BlockData)
    """
    Uses BlockData as DataType
    """
    BLOCK_CRUMBLE = ("block_crumble", BlockData)
    """
    Uses BlockData as DataType
    """
    TRAIL = ("trail", TargetColor)
    """
    Uses TargetColor as DataType
    """
    OMINOUS_SPAWNING = ("ominous_spawning")
    RAID_OMEN = ("raid_omen")
    TRIAL_OMEN = ("trial_omen")
    BLOCK_MARKER = ("block_marker", BlockData)
    """
    Uses BlockData as DataType
    """


    def getDataType(self) -> type[Any]:
        """
        Returns the required data type for the particle

        Returns
        - the required data type
        """
        ...


    def getKey(self) -> "NamespacedKey":
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


    class TargetColor:
        """
        Options which can be applied to trail particles - a location and color.
        """

        def __init__(self, target: "Location", color: "Color"):
            ...


        def getTarget(self) -> "Location":
            """
            The target of the particles to be displayed.

            Returns
            - particle target
            """
            ...


        def getColor(self) -> "Color":
            """
            The color of the particles to be displayed.

            Returns
            - particle color
            """
            ...
