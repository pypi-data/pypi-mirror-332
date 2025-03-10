"""
Python module generated from Java source file org.bukkit.event.entity.EntityDamageEvent

Java source file obtained from artifact spigot-api version 1.20.5-R0.1-20240429.101539-37

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Function
from com.google.common.base import Functions
from com.google.common.base import Preconditions
from com.google.common.collect import ImmutableMap
from enum import Enum
from java.util import EnumMap
from java.util import Objects
from org.bukkit import Material
from org.bukkit import WorldBorder
from org.bukkit.damage import DamageSource
from org.bukkit.damage import DamageType
from org.bukkit.entity import Entity
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import *
from typing import Any, Callable, Iterable, Tuple


class EntityDamageEvent(EntityEvent, Cancellable):
    """
    Stores data for damage events
    """

    def __init__(self, damagee: "Entity", cause: "DamageCause", damage: float):
        ...


    def __init__(self, damagee: "Entity", cause: "DamageCause", damageSource: "DamageSource", damage: float):
        ...


    def __init__(self, damagee: "Entity", cause: "DamageCause", modifiers: dict["DamageModifier", "Double"], modifierFunctions: dict["DamageModifier", "Function"["Double", "Double"]]):
        ...


    def __init__(self, damagee: "Entity", cause: "DamageCause", damageSource: "DamageSource", modifiers: dict["DamageModifier", "Double"], modifierFunctions: dict["DamageModifier", "Function"["Double", "Double"]]):
        ...


    def isCancelled(self) -> bool:
        ...


    def setCancelled(self, cancel: bool) -> None:
        ...


    def getOriginalDamage(self, type: "DamageModifier") -> float:
        """
        Gets the original damage for the specified modifier, as defined at this
        event's construction.

        Arguments
        - type: the modifier

        Returns
        - the original damage

        Raises
        - IllegalArgumentException: if type is null
        """
        ...


    def setDamage(self, type: "DamageModifier", damage: float) -> None:
        """
        Sets the damage for the specified modifier.

        Arguments
        - type: the damage modifier
        - damage: the scalar value of the damage's modifier

        Raises
        - IllegalArgumentException: if type is null
        - UnsupportedOperationException: if the caller does not support
            the particular DamageModifier, or to rephrase, when .isApplicable(DamageModifier) returns False

        See
        - .getFinalDamage()
        """
        ...


    def getDamage(self, type: "DamageModifier") -> float:
        """
        Gets the damage change for some modifier

        Arguments
        - type: the damage modifier

        Returns
        - The raw amount of damage caused by the event

        Raises
        - IllegalArgumentException: if type is null

        See
        - DamageModifier.BASE
        """
        ...


    def isApplicable(self, type: "DamageModifier") -> bool:
        """
        This checks to see if a particular modifier is valid for this event's
        caller, such that, .setDamage(DamageModifier, double) will not
        throw an UnsupportedOperationException.
        
        DamageModifier.BASE is always applicable.

        Arguments
        - type: the modifier

        Returns
        - True if the modifier is supported by the caller, False otherwise

        Raises
        - IllegalArgumentException: if type is null
        """
        ...


    def getDamage(self) -> float:
        """
        Gets the raw amount of damage caused by the event

        Returns
        - The raw amount of damage caused by the event

        See
        - DamageModifier.BASE
        """
        ...


    def getFinalDamage(self) -> float:
        """
        Gets the amount of damage caused by the event after all damage
        reduction is applied.

        Returns
        - the amount of damage caused by the event
        """
        ...


    def setDamage(self, damage: float) -> None:
        """
        Sets the raw amount of damage caused by the event.
        
        For compatibility this also recalculates the modifiers and scales
        them by the difference between the modifier for the previous damage
        value and the new one.

        Arguments
        - damage: The raw amount of damage caused by the event
        """
        ...


    def getCause(self) -> "DamageCause":
        """
        Gets the cause of the damage.
        
        While a DamageCause may indicate a specific Bukkit-assigned cause of damage,
        .getDamageSource() may expose additional types of damage such as custom
        damage types provided by data packs, as well as any direct or indirect entities,
        locations, or other contributing factors to the damage being inflicted. The
        alternative is generally preferred, but DamageCauses provided to this event
        should largely encompass most common use cases for developers if a simple cause
        is required.

        Returns
        - a DamageCause value detailing the cause of the damage.
        """
        ...


    def getDamageSource(self) -> "DamageSource":
        """
        Get the source of damage.

        Returns
        - a DamageSource detailing the source of the damage.
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...


    class DamageModifier(Enum):
        """
        An enum to specify the types of modifier

        Deprecated
        - This API is responsible for a large number of implementation
        problems and is in general unsustainable to maintain. It is likely to be
        removed very soon in a subsequent release. Please see
        <a href="https://www.spigotmc.org/threads/194446/">this thread</a> for more information.
        """

        BASE = 0
        """
        This represents the amount of damage being done, also known as the
        raw EntityDamageEvent.getDamage().
        """
        HARD_HAT = 1
        """
        This represents the damage reduced by a wearing a helmet when hit
        by a falling block.
        """
        BLOCKING = 2
        """
        This represents  the damage reduction caused by blocking, only present for
        Player Players.
        """
        ARMOR = 3
        """
        This represents the damage reduction caused by wearing armor.
        """
        RESISTANCE = 4
        """
        This represents the damage reduction caused by the Resistance potion effect.
        """
        MAGIC = 5
        """
        This represents the damage reduction caused by the combination of:
        
        - 
            Armor enchantments
        - 
            Witch's potion resistance
        
        """
        ABSORPTION = 6
        """
        This represents the damage reduction caused by the absorption potion
        effect.
        """


    class DamageCause(Enum):
        """
        An enum to specify the cause of the damage
        """

        KILL = 0
        """
        Damage caused by /kill command
        
        Damage: Float.MAX_VALUE
        """
        WORLD_BORDER = 1
        """
        Damage caused by the World Border
        
        Damage: WorldBorder.getDamageAmount()
        """
        CONTACT = 2
        """
        Damage caused when an entity contacts a block such as a Cactus,
        Dripstone (Stalagmite) or Berry Bush.
        
        Damage: variable
        """
        ENTITY_ATTACK = 3
        """
        Damage caused when an entity attacks another entity.
        
        Damage: variable
        """
        ENTITY_SWEEP_ATTACK = 4
        """
        Damage caused when an entity attacks another entity in a sweep attack.
        
        Damage: variable
        """
        PROJECTILE = 5
        """
        Damage caused when attacked by a projectile.
        
        Damage: variable
        """
        SUFFOCATION = 6
        """
        Damage caused by being put in a block
        
        Damage: 1
        """
        FALL = 7
        """
        Damage caused when an entity falls a distance greater than 3 blocks
        
        Damage: fall height - 3.0
        """
        FIRE = 8
        """
        Damage caused by direct exposure to fire
        
        Damage: 1
        """
        FIRE_TICK = 9
        """
        Damage caused due to burns caused by fire
        
        Damage: 1
        """
        MELTING = 10
        """
        Damage caused due to a snowman melting
        
        Damage: 1
        """
        LAVA = 11
        """
        Damage caused by direct exposure to lava
        
        Damage: 4
        """
        DROWNING = 12
        """
        Damage caused by running out of air while in water
        
        Damage: 2
        """
        BLOCK_EXPLOSION = 13
        """
        Damage caused by being in the area when a block explodes.
        
        Damage: variable
        """
        ENTITY_EXPLOSION = 14
        """
        Damage caused by being in the area when an entity, such as a
        Creeper, explodes.
        
        Damage: variable
        """
        VOID = 15
        """
        Damage caused by falling into the void
        
        Damage: 4 for players
        """
        LIGHTNING = 16
        """
        Damage caused by being struck by lightning
        
        Damage: 5
        """
        SUICIDE = 17
        """
        Damage caused by committing suicide.
        
        **Note:** This is currently only used by plugins, default commands
        like /minecraft:kill use .KILL to damage players.
        
        Damage: variable
        """
        STARVATION = 18
        """
        Damage caused by starving due to having an empty hunger bar
        
        Damage: 1
        """
        POISON = 19
        """
        Damage caused due to an ongoing poison effect
        
        Damage: 1
        """
        MAGIC = 20
        """
        Damage caused by being hit by a damage potion or spell
        
        Damage: variable
        """
        WITHER = 21
        """
        Damage caused by Wither potion effect
        """
        FALLING_BLOCK = 22
        """
        Damage caused by being hit by a falling block which deals damage
        
        **Note:** Not every block deals damage
        
        Damage: variable
        """
        THORNS = 23
        """
        Damage caused in retaliation to another attack by the Thorns
        enchantment.
        
        Damage: 1-4 (Thorns)
        """
        DRAGON_BREATH = 24
        """
        Damage caused by a dragon breathing fire.
        
        Damage: variable
        """
        CUSTOM = 25
        """
        Custom damage.
        
        Damage: variable
        """
        FLY_INTO_WALL = 26
        """
        Damage caused when an entity runs into a wall.
        
        Damage: variable
        """
        HOT_FLOOR = 27
        """
        Damage caused when an entity steps on Material.MAGMA_BLOCK.
        
        Damage: 1
        """
        CRAMMING = 28
        """
        Damage caused when an entity is colliding with too many entities due
        to the maxEntityCramming game rule.
        
        Damage: 6
        """
        DRYOUT = 29
        """
        Damage caused when an entity that should be in water is not.
        
        Damage: 1
        """
        FREEZE = 30
        """
        Damage caused from freezing.
        
        Damage: 1 or 5
        """
        SONIC_BOOM = 31
        """
        Damage caused by the Sonic Boom attack from org.bukkit.entity.Warden
        
        Damage: 10
        """
