"""
Python module generated from Java source file org.bukkit.GameEvent

Java source file obtained from artifact spigot-api version 1.20.5-R0.1-20240429.101539-37

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from com.google.common.collect import Lists
from java.util import Collections
from org.bukkit import *
from typing import Any, Callable, Iterable, Tuple


class GameEvent(Keyed):
    """
    Represents a generic Mojang game event.
    """

    BLOCK_ACTIVATE = getEvent("block_activate")
    BLOCK_ATTACH = getEvent("block_attach")
    BLOCK_CHANGE = getEvent("block_change")
    BLOCK_CLOSE = getEvent("block_close")
    BLOCK_DEACTIVATE = getEvent("block_deactivate")
    BLOCK_DESTROY = getEvent("block_destroy")
    BLOCK_DETACH = getEvent("block_detach")
    BLOCK_OPEN = getEvent("block_open")
    BLOCK_PLACE = getEvent("block_place")
    BLOCK_PRESS = getEvent("block_activate")
    BLOCK_SWITCH = getEvent("block_activate")
    BLOCK_UNPRESS = getEvent("block_deactivate")
    BLOCK_UNSWITCH = getEvent("block_deactivate")
    CONTAINER_CLOSE = getEvent("container_close")
    CONTAINER_OPEN = getEvent("container_open")
    DISPENSE_FAIL = getEvent("block_activate")
    DRINK = getEvent("drink")
    DRINKING_FINISH = getEvent("drink")
    EAT = getEvent("eat")
    ELYTRA_FREE_FALL = getEvent("elytra_glide")
    ELYTRA_GLIDE = getEvent("elytra_glide")
    ENTITY_DAMAGE = getEvent("entity_damage")
    ENTITY_DAMAGED = getEvent("entity_damage")
    ENTITY_DIE = getEvent("entity_die")
    ENTITY_DISMOUNT = getEvent("entity_dismount")
    ENTITY_DYING = getEvent("entity_die")
    ENTITY_INTERACT = getEvent("entity_interact")
    ENTITY_MOUNT = getEvent("entity_mount")
    ENTITY_KILLED = getEvent("entity_die")
    ENTITY_PLACE = getEvent("entity_place")
    ENTITY_ACTION = getEvent("entity_action")
    ENTITY_ROAR = getEvent("entity_action")
    ENTITY_SHAKE = getEvent("entity_action")
    EQUIP = getEvent("equip")
    EXPLODE = getEvent("explode")
    FLAP = getEvent("flap")
    FLUID_PICKUP = getEvent("fluid_pickup")
    FLUID_PLACE = getEvent("fluid_place")
    HIT_GROUND = getEvent("hit_ground")
    INSTRUMENT_PLAY = getEvent("instrument_play")
    ITEM_INTERACT_FINISH = getEvent("item_interact_finish")
    ITEM_INTERACT_START = getEvent("item_interact_start")
    JUKEBOX_PLAY = getEvent("jukebox_play")
    JUKEBOX_STOP_PLAY = getEvent("jukebox_stop_play")
    LIGHTNING_STRIKE = getEvent("lightning_strike")
    MOB_INTERACT = getEvent("entity_interact")
    NOTE_BLOCK_PLAY = getEvent("note_block_play")
    PISTON_CONTRACT = getEvent("block_deactivate")
    PISTON_EXTEND = getEvent("block_activate")
    PRIME_FUSE = getEvent("prime_fuse")
    PROJECTILE_LAND = getEvent("projectile_land")
    PROJECTILE_SHOOT = getEvent("projectile_shoot")
    RAVAGER_ROAR = getEvent("entity_action")
    RING_BELL = getEvent("block_change")
    SCULK_SENSOR_TENDRILS_CLICKING = getEvent("sculk_sensor_tendrils_clicking")
    SHEAR = getEvent("shear")
    SHRIEK = getEvent("shriek")
    SHULKER_CLOSE = getEvent("container_close")
    SHULKER_OPEN = getEvent("container_open")
    SPLASH = getEvent("splash")
    STEP = getEvent("step")
    SWIM = getEvent("swim")
    TELEPORT = getEvent("teleport")
    UNEQUIP = getEvent("unequip")
    WOLF_SHAKING = getEvent("entity_action")
    RESONATE_1 = getEvent("resonate_1")
    RESONATE_2 = getEvent("resonate_2")
    RESONATE_3 = getEvent("resonate_3")
    RESONATE_4 = getEvent("resonate_4")
    RESONATE_5 = getEvent("resonate_5")
    RESONATE_6 = getEvent("resonate_6")
    RESONATE_7 = getEvent("resonate_7")
    RESONATE_8 = getEvent("resonate_8")
    RESONATE_9 = getEvent("resonate_9")
    RESONATE_10 = getEvent("resonate_10")
    RESONATE_11 = getEvent("resonate_11")
    RESONATE_12 = getEvent("resonate_12")
    RESONATE_13 = getEvent("resonate_13")
    RESONATE_14 = getEvent("resonate_14")
    RESONATE_15 = getEvent("resonate_15")


    @staticmethod
    def getByKey(namespacedKey: "NamespacedKey") -> "GameEvent":
        """
        Returns a GameEvent by a NamespacedKey.

        Arguments
        - namespacedKey: the key

        Returns
        - the event or null

        Deprecated
        - Use Registry.get(NamespacedKey) instead.
        """
        ...


    @staticmethod
    def values() -> Iterable["GameEvent"]:
        """
        Returns the set of all GameEvents.

        Returns
        - the memoryKeys

        Deprecated
        - use Registry.iterator().
        """
        ...
