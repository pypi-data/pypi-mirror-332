"""
Python module generated from Java source file org.bukkit.Statistic

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from java.util import Locale
from org.bukkit import *
from typing import Any, Callable, Iterable, Tuple


class Statistic(Enum):
    """
    Represents a countable statistic, which is tracked by the server.
    """

    DAMAGE_DEALT = 0
    DAMAGE_TAKEN = 1
    DEATHS = 2
    MOB_KILLS = 3
    PLAYER_KILLS = 4
    FISH_CAUGHT = 5
    ANIMALS_BRED = 6
    LEAVE_GAME = 7
    JUMP = 8
    DROP_COUNT = 9
    DROP = (Type.ITEM)
    PICKUP = (Type.ITEM)
    PLAY_ONE_MINUTE = 12
    """
    Name is misleading, actually records ticks played.
    """
    TOTAL_WORLD_TIME = 13
    WALK_ONE_CM = 14
    WALK_ON_WATER_ONE_CM = 15
    FALL_ONE_CM = 16
    SNEAK_TIME = 17
    CLIMB_ONE_CM = 18
    FLY_ONE_CM = 19
    WALK_UNDER_WATER_ONE_CM = 20
    MINECART_ONE_CM = 21
    BOAT_ONE_CM = 22
    PIG_ONE_CM = 23
    HORSE_ONE_CM = 24
    SPRINT_ONE_CM = 25
    CROUCH_ONE_CM = 26
    AVIATE_ONE_CM = 27
    MINE_BLOCK = (Type.BLOCK)
    USE_ITEM = (Type.ITEM)
    BREAK_ITEM = (Type.ITEM)
    CRAFT_ITEM = (Type.ITEM)
    KILL_ENTITY = (Type.ENTITY)
    ENTITY_KILLED_BY = (Type.ENTITY)
    TIME_SINCE_DEATH = 34
    TALKED_TO_VILLAGER = 35
    TRADED_WITH_VILLAGER = 36
    CAKE_SLICES_EATEN = 37
    CAULDRON_FILLED = 38
    CAULDRON_USED = 39
    ARMOR_CLEANED = 40
    BANNER_CLEANED = 41
    BREWINGSTAND_INTERACTION = 42
    BEACON_INTERACTION = 43
    DROPPER_INSPECTED = 44
    HOPPER_INSPECTED = 45
    DISPENSER_INSPECTED = 46
    NOTEBLOCK_PLAYED = 47
    NOTEBLOCK_TUNED = 48
    FLOWER_POTTED = 49
    TRAPPED_CHEST_TRIGGERED = 50
    ENDERCHEST_OPENED = 51
    ITEM_ENCHANTED = 52
    RECORD_PLAYED = 53
    FURNACE_INTERACTION = 54
    CRAFTING_TABLE_INTERACTION = 55
    CHEST_OPENED = 56
    SLEEP_IN_BED = 57
    SHULKER_BOX_OPENED = 58
    TIME_SINCE_REST = 59
    SWIM_ONE_CM = 60
    DAMAGE_DEALT_ABSORBED = 61
    DAMAGE_DEALT_RESISTED = 62
    DAMAGE_BLOCKED_BY_SHIELD = 63
    DAMAGE_ABSORBED = 64
    DAMAGE_RESISTED = 65
    CLEAN_SHULKER_BOX = 66
    OPEN_BARREL = 67
    INTERACT_WITH_BLAST_FURNACE = 68
    INTERACT_WITH_SMOKER = 69
    INTERACT_WITH_LECTERN = 70
    INTERACT_WITH_CAMPFIRE = 71
    INTERACT_WITH_CARTOGRAPHY_TABLE = 72
    INTERACT_WITH_LOOM = 73
    INTERACT_WITH_STONECUTTER = 74
    BELL_RING = 75
    RAID_TRIGGER = 76
    RAID_WIN = 77
    INTERACT_WITH_ANVIL = 78
    INTERACT_WITH_GRINDSTONE = 79
    TARGET_HIT = 80
    INTERACT_WITH_SMITHING_TABLE = 81
    STRIDER_ONE_CM = 82


    def getType(self) -> "Type":
        """
        Gets the type of this statistic.

        Returns
        - the type of this statistic
        """
        ...


    def isSubstatistic(self) -> bool:
        """
        Checks if this is a substatistic.
        
        A substatistic exists en masse for each block, item, or entitytype, depending on
        .getType().
        
        This is a redundant method and equivalent to checking
        `getType() != Type.UNTYPED`

        Returns
        - True if this is a substatistic
        """
        ...


    def isBlock(self) -> bool:
        """
        Checks if this is a substatistic dealing with blocks.
        
        This is a redundant method and equivalent to checking
        `getType() == Type.BLOCK`

        Returns
        - True if this deals with blocks
        """
        ...


    def getKey(self) -> "NamespacedKey":
        ...


    class Type(Enum):
        """
        The type of statistic.
        """

        UNTYPED = 0
        """
        Statistics of this type do not require a qualifier.
        """
        ITEM = 1
        """
        Statistics of this type require an Item Material qualifier.
        """
        BLOCK = 2
        """
        Statistics of this type require a Block Material qualifier.
        """
        ENTITY = 3
        """
        Statistics of this type require an EntityType qualifier.
        """
