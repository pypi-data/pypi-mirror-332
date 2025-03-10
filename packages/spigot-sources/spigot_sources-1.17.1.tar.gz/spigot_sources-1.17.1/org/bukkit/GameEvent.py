"""
Python module generated from Java source file org.bukkit.GameEvent

Java source file obtained from artifact spigot-api version 1.17.1-R0.1-20211121.234319-104

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import Collections
from org.bukkit import *
from typing import Any, Callable, Iterable, Tuple


class GameEvent(Keyed):
    """
    Represents a generic Mojang game event.
    """

    BLOCK_ATTACH = getEvent("block_attach")
    BLOCK_CHANGE = getEvent("block_change")
    BLOCK_CLOSE = getEvent("block_close")
    BLOCK_DESTROY = getEvent("block_destroy")
    BLOCK_DETACH = getEvent("block_detach")
    BLOCK_OPEN = getEvent("block_open")
    BLOCK_PLACE = getEvent("block_place")
    BLOCK_PRESS = getEvent("block_press")
    BLOCK_SWITCH = getEvent("block_switch")
    BLOCK_UNPRESS = getEvent("block_unpress")
    BLOCK_UNSWITCH = getEvent("block_unswitch")
    CONTAINER_CLOSE = getEvent("container_close")
    CONTAINER_OPEN = getEvent("container_open")
    DISPENSE_FAIL = getEvent("dispense_fail")
    DRINKING_FINISH = getEvent("drinking_finish")
    EAT = getEvent("eat")
    ELYTRA_FREE_FALL = getEvent("elytra_free_fall")
    ENTITY_DAMAGED = getEvent("entity_damaged")
    ENTITY_KILLED = getEvent("entity_killed")
    ENTITY_PLACE = getEvent("entity_place")
    EQUIP = getEvent("equip")
    EXPLODE = getEvent("explode")
    FISHING_ROD_CAST = getEvent("fishing_rod_cast")
    FISHING_ROD_REEL_IN = getEvent("fishing_rod_reel_in")
    FLAP = getEvent("flap")
    FLUID_PICKUP = getEvent("fluid_pickup")
    FLUID_PLACE = getEvent("fluid_place")
    HIT_GROUND = getEvent("hit_ground")
    LIGHTNING_STRIKE = getEvent("lightning_strike")
    MINECART_MOVING = getEvent("minecart_moving")
    MOB_INTERACT = getEvent("mob_interact")
    PISTON_CONTRACT = getEvent("piston_contract")
    PISTON_EXTEND = getEvent("piston_extend")
    PRIME_FUSE = getEvent("prime_fuse")
    PROJECTILE_LAND = getEvent("projectile_land")
    PROJECTILE_SHOOT = getEvent("projectile_shoot")
    RAVAGER_ROAR = getEvent("ravager_roar")
    RING_BELL = getEvent("ring_bell")
    SHEAR = getEvent("shear")
    SHULKER_CLOSE = getEvent("shulker_close")
    SHULKER_OPEN = getEvent("shulker_open")
    SPLASH = getEvent("splash")
    STEP = getEvent("step")
    SWIM = getEvent("swim")
    WOLF_SHAKING = getEvent("wolf_shaking")


    def getKey(self) -> "NamespacedKey":
        ...


    @staticmethod
    def getByKey(namespacedKey: "NamespacedKey") -> "GameEvent":
        """
        Returns a GameEvent by a NamespacedKey.

        Arguments
        - namespacedKey: the key

        Returns
        - the event or null
        """
        ...


    @staticmethod
    def values() -> Iterable["GameEvent"]:
        """
        Returns the set of all GameEvents.

        Returns
        - the memoryKeys
        """
        ...
