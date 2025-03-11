"""
Python module generated from Java source file org.bukkit.entity.memory.MemoryKey

Java source file obtained from artifact spigot-api version 1.21.1-R0.1-20241022.152140-54

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import UUID
from org.bukkit import Keyed
from org.bukkit import Location
from org.bukkit import NamespacedKey
from org.bukkit.entity.memory import *
from typing import Any, Callable, Iterable, Tuple


class MemoryKey(Keyed):
    """
    Represents a key used for accessing memory values of a
    org.bukkit.entity.LivingEntity.
    
    Type `<T>`: the class type of the memory value
    """

    HOME = MemoryKey<>(NamespacedKey.minecraft("home"), Location.class)
    POTENTIAL_JOB_SITE = MemoryKey<>(NamespacedKey.minecraft("potential_job_site"), Location.class)
    JOB_SITE = MemoryKey<>(NamespacedKey.minecraft("job_site"), Location.class)
    MEETING_POINT = MemoryKey<>(NamespacedKey.minecraft("meeting_point"), Location.class)
    GOLEM_DETECTED_RECENTLY = MemoryKey<>(NamespacedKey.minecraft("golem_detected_recently"), Boolean.class)
    LAST_SLEPT = MemoryKey<>(NamespacedKey.minecraft("last_slept"), Long.class)
    LAST_WOKEN = MemoryKey<>(NamespacedKey.minecraft("last_woken"), Long.class)
    LAST_WORKED_AT_POI = MemoryKey<>(NamespacedKey.minecraft("last_worked_at_poi"), Long.class)
    UNIVERSAL_ANGER = MemoryKey<>(NamespacedKey.minecraft("universal_anger"), Boolean.class)
    ANGRY_AT = MemoryKey<>(NamespacedKey.minecraft("angry_at"), UUID.class)
    ADMIRING_ITEM = MemoryKey<>(NamespacedKey.minecraft("admiring_item"), Boolean.class)
    ADMIRING_DISABLED = MemoryKey<>(NamespacedKey.minecraft("admiring_disabled"), Boolean.class)
    HUNTED_RECENTLY = MemoryKey<>(NamespacedKey.minecraft("hunted_recently"), Boolean.class)
    PLAY_DEAD_TICKS = MemoryKey<>(NamespacedKey.minecraft("play_dead_ticks"), Integer.class)
    TEMPTATION_COOLDOWN_TICKS = MemoryKey<>(NamespacedKey.minecraft("temptation_cooldown_ticks"), Integer.class)
    IS_TEMPTED = MemoryKey<>(NamespacedKey.minecraft("is_tempted"), Boolean.class)
    LONG_JUMP_COOLING_DOWN = MemoryKey<>(NamespacedKey.minecraft("long_jump_cooling_down"), Integer.class)
    HAS_HUNTING_COOLDOWN = MemoryKey<>(NamespacedKey.minecraft("has_hunting_cooldown"), Boolean.class)
    RAM_COOLDOWN_TICKS = MemoryKey<>(NamespacedKey.minecraft("ram_cooldown_ticks"), Integer.class)
    LIKED_PLAYER = MemoryKey<>(NamespacedKey.minecraft("liked_player"), UUID.class)
    LIKED_NOTEBLOCK_POSITION = MemoryKey<>(NamespacedKey.minecraft("liked_noteblock"), Location.class)
    LIKED_NOTEBLOCK_COOLDOWN_TICKS = MemoryKey<>(NamespacedKey.minecraft("liked_noteblock_cooldown_ticks"), Integer.class)
    ITEM_PICKUP_COOLDOWN_TICKS = MemoryKey<>(NamespacedKey.minecraft("item_pickup_cooldown_ticks"), Integer.class)
    SNIFFER_EXPLORED_POSITIONS = MemoryKey<>(NamespacedKey.minecraft("sniffer_explored_positions"), Location.class)


    def getKey(self) -> "NamespacedKey":
        ...


    def getMemoryClass(self) -> type["T"]:
        """
        Gets the class of values associated with this memory.

        Returns
        - the class of value objects
        """
        ...


    @staticmethod
    def getByKey(namespacedKey: "NamespacedKey") -> "MemoryKey":
        """
        Returns a MemoryKey by a NamespacedKey.

        Arguments
        - namespacedKey: the NamespacedKey referencing a
        MemoryKey

        Returns
        - the MemoryKey or null when no MemoryKey is
        available under that key
        """
        ...


    @staticmethod
    def values() -> set["MemoryKey"]:
        """
        Returns the set of all MemoryKeys.

        Returns
        - the memoryKeys
        """
        ...
