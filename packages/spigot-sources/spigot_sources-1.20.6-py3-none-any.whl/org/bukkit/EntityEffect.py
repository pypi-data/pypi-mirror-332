"""
Python module generated from Java source file org.bukkit.EntityEffect

Java source file obtained from artifact spigot-api version 1.20.6-R0.1-20240613.150924-57

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from enum import Enum
from org.bukkit import *
from org.bukkit.entity import Ageable
from org.bukkit.entity import ArmorStand
from org.bukkit.entity import Cat
from org.bukkit.entity import Dolphin
from org.bukkit.entity import Egg
from org.bukkit.entity import Entity
from org.bukkit.entity import EvokerFangs
from org.bukkit.entity import Firework
from org.bukkit.entity import Fox
from org.bukkit.entity import Goat
from org.bukkit.entity import Guardian
from org.bukkit.entity import Hoglin
from org.bukkit.entity import IronGolem
from org.bukkit.entity import LivingEntity
from org.bukkit.entity import Player
from org.bukkit.entity import Rabbit
from org.bukkit.entity import Ravager
from org.bukkit.entity import Sheep
from org.bukkit.entity import Sniffer
from org.bukkit.entity import Snowball
from org.bukkit.entity import Squid
from org.bukkit.entity import Tameable
from org.bukkit.entity import TippedArrow
from org.bukkit.entity import Villager
from org.bukkit.entity import Warden
from org.bukkit.entity import Witch
from org.bukkit.entity import Wolf
from org.bukkit.entity import Zoglin
from org.bukkit.entity import ZombieVillager
from org.bukkit.entity.minecart import ExplosiveMinecart
from org.bukkit.entity.minecart import SpawnerMinecart
from typing import Any, Callable, Iterable, Tuple


class EntityEffect(Enum):
    """
    A list of all Effects that can happen to entities.
    """

    ARROW_PARTICLES = (0, TippedArrow)
    """
    Colored particles from a tipped arrow.
    """
    RABBIT_JUMP = (1, Rabbit)
    """
    Rabbit jumping.
    """
    RESET_SPAWNER_MINECART_DELAY = (1, SpawnerMinecart)
    """
    Resets a spawner minecart's delay to 200. Does not effect actual spawning
    delay, only the speed at which the entity in the spawner spins
    """
    HURT = (2, LivingEntity)
    """
    When mobs get hurt.

    Deprecated
    - Use LivingEntity.playHurtAnimation(float)
    """
    DEATH = (3, Entity)
    """
    When a mob dies.
    
    **This will cause client-glitches!**

    See
    - .ENTITY_DEATH

    Deprecated
    - split into individual effects
    """
    EGG_BREAK = (3, Egg)
    """
    Spawns the egg breaking particles
    """
    SNOWBALL_BREAK = (3, Snowball)
    """
    Spawns the snowball breaking particles
    """
    ENTITY_DEATH = (3, LivingEntity)
    """
    Plays the entity death sound and animation
    
    **This will cause client-glitches!**
    """
    FANG_ATTACK = (4, EvokerFangs)
    """
    Plays the fang attack animation
    """
    HOGLIN_ATTACK = (4, Hoglin)
    """
    Plays the hoglin attack animation
    """
    IRON_GOLEN_ATTACK = (4, IronGolem)
    """
    Plays the iron golem attack animation
    """
    RAVAGER_ATTACK = (4, Ravager)
    """
    Plays the ravager attack animation
    """
    WARDEN_ATTACK = (4, Warden)
    """
    Plays the warden attack animation
    """
    ZOGLIN_ATTACK = (4, Zoglin)
    """
    Plays the zoglin attack animation
    """
    WOLF_SMOKE = (6, Tameable)
    """
    The smoke when taming an entity fails.
    """
    WOLF_HEARTS = (7, Tameable)
    """
    The hearts when taming an entity succeeds.
    """
    WOLF_SHAKE = (8, Wolf)
    """
    When a wolf shakes (after being wet).

    See
    - EntityEffect.WOLF_SHAKE_STOP
    """
    SHEEP_EAT = (10, Entity)
    """
    When an entity eats a LONG_GRASS block.

    See
    - .TNT_MINECART_IGNITE

    Deprecated
    - split into individual effects
    """
    SHEEP_EAT_GRASS = (10, Sheep)
    """
    Plays the sheep eating grass animation
    """
    TNT_MINECART_IGNITE = (10, ExplosiveMinecart)
    """
    Causes the TNT minecart to ignite, does not play the ignition sound
    
    **This will cause client-glitches!**
    """
    IRON_GOLEM_ROSE = (11, IronGolem)
    """
    When an Iron Golem gives a rose.
    """
    VILLAGER_HEART = (12, Villager)
    """
    Hearts from a villager.
    """
    VILLAGER_ANGRY = (13, Villager)
    """
    When a villager is angry.
    """
    VILLAGER_HAPPY = (14, Villager)
    """
    Happy particles from a villager.
    """
    WITCH_MAGIC = (15, Witch)
    """
    Magic particles from a witch.
    """
    ZOMBIE_TRANSFORM = (16, ZombieVillager)
    """
    When a zombie transforms into a villager by shaking violently.
    """
    FIREWORK_EXPLODE = (17, Firework)
    """
    When a firework explodes.
    """
    LOVE_HEARTS = (18, Ageable)
    """
    Hearts from a breeding entity.
    """
    SQUID_ROTATE = (19, Squid)
    """
    Resets squid rotation.
    """
    ENTITY_POOF = (20, LivingEntity)
    """
    Silverfish entering block, spawner spawning.
    """
    GUARDIAN_TARGET = (21, Guardian)
    """
    Guardian plays the attack sound effect.
    """
    SHIELD_BLOCK = (29, LivingEntity)
    """
    Shield blocks attack.
    """
    SHIELD_BREAK = (30, LivingEntity)
    """
    Shield breaks.
    """
    ARMOR_STAND_HIT = (32, ArmorStand)
    """
    Armor stand is hit.
    """
    THORNS_HURT = (33, LivingEntity)
    """
    Entity hurt by thorns attack.
    """
    IRON_GOLEM_SHEATH = (34, IronGolem)
    """
    Iron golem puts away rose.
    """
    TOTEM_RESURRECT = (35, LivingEntity)
    """
    Totem prevents entity death.
    """
    HURT_DROWN = (36, LivingEntity)
    """
    Entity hurt due to drowning damage.
    """
    HURT_EXPLOSION = (37, LivingEntity)
    """
    Entity hurt due to explosion damage.
    """
    DOLPHIN_FED = (38, Dolphin)
    """
    Dolphin has been fed and is locating a structure.
    """
    RAVAGER_STUNNED = (39, Ravager)
    """
    Ravager has been stunned for 40 ticks.
    """
    CAT_TAME_FAIL = (40, Cat)
    """
    Cat taming failed.
    """
    CAT_TAME_SUCCESS = (41, Cat)
    """
    Cat taming succeeded.
    """
    VILLAGER_SPLASH = (42, Villager)
    """
    Villager splashes particles during a raid.
    """
    PLAYER_BAD_OMEN_RAID = (43, Player)
    """
    Player's bad omen effect removed to start or increase raid difficult.
    """
    HURT_BERRY_BUSH = (44, LivingEntity)
    """
    Entity hurt due to berry bush. Prickly!
    """
    FOX_CHEW = (45, Fox)
    """
    Fox chews the food in its mouth
    """
    TELEPORT_ENDER = (46, LivingEntity)
    """
    Entity teleported as a result of chorus fruit or as an enderman
    """
    BREAK_EQUIPMENT_MAIN_HAND = (47, LivingEntity)
    """
    Entity breaks item in main hand
    """
    BREAK_EQUIPMENT_OFF_HAND = (48, LivingEntity)
    """
    Entity breaks item in off hand
    """
    BREAK_EQUIPMENT_HELMET = (49, LivingEntity)
    """
    Entity breaks item in helmet slot
    """
    BREAK_EQUIPMENT_CHESTPLATE = (50, LivingEntity)
    """
    Entity breaks item in chestplate slot
    """
    BREAK_EQUIPMENT_LEGGINGS = (51, LivingEntity)
    """
    Entity breaks item in legging slot
    """
    BREAK_EQUIPMENT_BOOTS = (52, LivingEntity)
    """
    Entity breaks item in boot slot
    """
    HONEY_BLOCK_SLIDE_PARTICLES = (53, Entity)
    """
    Spawns honey block slide particles at the entity's feet
    """
    HONEY_BLOCK_FALL_PARTICLES = (54, LivingEntity)
    """
    Spawns honey block fall particles at the entity's feet
    """
    SWAP_HAND_ITEMS = (55, LivingEntity)
    """
    Entity swaps the items in their hand and offhand
    """
    WOLF_SHAKE_STOP = (56, Wolf)
    """
    Stops a wolf that is currently shaking

    See
    - EntityEffect.WOLF_SHAKE
    """
    GOAT_LOWER_HEAD = (58, Goat)
    """
    Goat lowers its head for ramming

    See
    - .GOAT_RAISE_HEAD
    """
    GOAT_RAISE_HEAD = (59, Goat)
    """
    Goat raises its head

    See
    - .GOAT_LOWER_HEAD
    """
    SPAWN_DEATH_SMOKE = (60, LivingEntity)
    """
    Spawns death smoke particles
    """
    WARDEN_TENDRIL_SHAKE = (61, Warden)
    """
    Warden shakes its tendrils
    """
    WARDEN_SONIC_ATTACK = (62, Warden)
    """
    Warden performs sonic attack animation 
    Does not play the sound or fire the beam
    """
    SNIFFER_DIG = (63, Sniffer)
    """
    Plays sniffer digging sound 
    Sniffer must have a target and be in Sniffer.State.SEARCHING or
    Sniffer.State.DIGGING
    """


    def getData(self) -> int:
        """
        Gets the data value of this EntityEffect, may not be unique.

        Returns
        - The data value

        Deprecated
        - Magic value
        """
        ...


    def getApplicable(self) -> type["Entity"]:
        """
        Gets entity superclass which this affect is applicable to.

        Returns
        - applicable class
        """
        ...


    def isApplicableTo(self, entity: "Entity") -> bool:
        """
        Checks if this effect is applicable to the given entity.

        Arguments
        - entity: the entity to check

        Returns
        - True if applicable
        """
        ...


    def isApplicableTo(self, clazz: type["Entity"]) -> bool:
        """
        Checks if this effect is applicable to the given entity class.

        Arguments
        - clazz: the entity class to check

        Returns
        - True if applicable
        """
        ...
