"""
Python module generated from Java source file org.bukkit.enchantments.Enchantment

Java source file obtained from artifact spigot-api version 1.20.1-R0.1-20230921.163938-66

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Keyed
from org.bukkit import NamespacedKey
from org.bukkit.enchantments import *
from org.bukkit.inventory import ItemStack
from typing import Any, Callable, Iterable, Tuple


class Enchantment(Keyed):
    """
    The various type of enchantments that may be added to armour or weapons
    """

    PROTECTION_ENVIRONMENTAL = EnchantmentWrapper("protection")
    """
    Provides protection against environmental damage
    """
    PROTECTION_FIRE = EnchantmentWrapper("fire_protection")
    """
    Provides protection against fire damage
    """
    PROTECTION_FALL = EnchantmentWrapper("feather_falling")
    """
    Provides protection against fall damage
    """
    PROTECTION_EXPLOSIONS = EnchantmentWrapper("blast_protection")
    """
    Provides protection against explosive damage
    """
    PROTECTION_PROJECTILE = EnchantmentWrapper("projectile_protection")
    """
    Provides protection against projectile damage
    """
    OXYGEN = EnchantmentWrapper("respiration")
    """
    Decreases the rate of air loss whilst underwater
    """
    WATER_WORKER = EnchantmentWrapper("aqua_affinity")
    """
    Increases the speed at which a player may mine underwater
    """
    THORNS = EnchantmentWrapper("thorns")
    """
    Damages the attacker
    """
    DEPTH_STRIDER = EnchantmentWrapper("depth_strider")
    """
    Increases walking speed while in water
    """
    FROST_WALKER = EnchantmentWrapper("frost_walker")
    """
    Freezes any still water adjacent to ice / frost which player is walking on
    """
    BINDING_CURSE = EnchantmentWrapper("binding_curse")
    """
    Item cannot be removed
    """
    DAMAGE_ALL = EnchantmentWrapper("sharpness")
    """
    Increases damage against all targets
    """
    DAMAGE_UNDEAD = EnchantmentWrapper("smite")
    """
    Increases damage against undead targets
    """
    DAMAGE_ARTHROPODS = EnchantmentWrapper("bane_of_arthropods")
    """
    Increases damage against arthropod targets
    """
    KNOCKBACK = EnchantmentWrapper("knockback")
    """
    All damage to other targets will knock them back when hit
    """
    FIRE_ASPECT = EnchantmentWrapper("fire_aspect")
    """
    When attacking a target, has a chance to set them on fire
    """
    LOOT_BONUS_MOBS = EnchantmentWrapper("looting")
    """
    Provides a chance of gaining extra loot when killing monsters
    """
    SWEEPING_EDGE = EnchantmentWrapper("sweeping")
    """
    Increases damage against targets when using a sweep attack
    """
    DIG_SPEED = EnchantmentWrapper("efficiency")
    """
    Increases the rate at which you mine/dig
    """
    SILK_TOUCH = EnchantmentWrapper("silk_touch")
    """
    Allows blocks to drop themselves instead of fragments (for example,
    stone instead of cobblestone)
    """
    DURABILITY = EnchantmentWrapper("unbreaking")
    """
    Decreases the rate at which a tool looses durability
    """
    LOOT_BONUS_BLOCKS = EnchantmentWrapper("fortune")
    """
    Provides a chance of gaining extra loot when destroying blocks
    """
    ARROW_DAMAGE = EnchantmentWrapper("power")
    """
    Provides extra damage when shooting arrows from bows
    """
    ARROW_KNOCKBACK = EnchantmentWrapper("punch")
    """
    Provides a knockback when an entity is hit by an arrow from a bow
    """
    ARROW_FIRE = EnchantmentWrapper("flame")
    """
    Sets entities on fire when hit by arrows shot from a bow
    """
    ARROW_INFINITE = EnchantmentWrapper("infinity")
    """
    Provides infinite arrows when shooting a bow
    """
    LUCK = EnchantmentWrapper("luck_of_the_sea")
    """
    Decreases odds of catching worthless junk
    """
    LURE = EnchantmentWrapper("lure")
    """
    Increases rate of fish biting your hook
    """
    LOYALTY = EnchantmentWrapper("loyalty")
    """
    Causes a thrown trident to return to the player who threw it
    """
    IMPALING = EnchantmentWrapper("impaling")
    """
    Deals more damage to mobs that live in the ocean
    """
    RIPTIDE = EnchantmentWrapper("riptide")
    """
    When it is rainy, launches the player in the direction their trident is thrown
    """
    CHANNELING = EnchantmentWrapper("channeling")
    """
    Strikes lightning when a mob is hit with a trident if conditions are
    stormy
    """
    MULTISHOT = EnchantmentWrapper("multishot")
    """
    Shoot multiple arrows from crossbows
    """
    QUICK_CHARGE = EnchantmentWrapper("quick_charge")
    """
    Charges crossbows quickly
    """
    PIERCING = EnchantmentWrapper("piercing")
    """
    Crossbow projectiles pierce entities
    """
    MENDING = EnchantmentWrapper("mending")
    """
    Allows mending the item using experience orbs
    """
    VANISHING_CURSE = EnchantmentWrapper("vanishing_curse")
    """
    Item disappears instead of dropping
    """
    SOUL_SPEED = EnchantmentWrapper("soul_speed")
    """
    Walk quicker on soul blocks
    """
    SWIFT_SNEAK = EnchantmentWrapper("swift_sneak")
    """
    Walk quicker while sneaking
    """


    def __init__(self, key: "NamespacedKey"):
        ...


    def getKey(self) -> "NamespacedKey":
        ...


    def getName(self) -> str:
        """
        Gets the unique name of this enchantment

        Returns
        - Unique name

        Deprecated
        - enchantments are badly named, use .getKey().
        """
        ...


    def getMaxLevel(self) -> int:
        """
        Gets the maximum level that this Enchantment may become.

        Returns
        - Maximum level of the Enchantment
        """
        ...


    def getStartLevel(self) -> int:
        """
        Gets the level that this Enchantment should start at

        Returns
        - Starting level of the Enchantment
        """
        ...


    def getItemTarget(self) -> "EnchantmentTarget":
        """
        Gets the type of ItemStack that may fit this Enchantment.

        Returns
        - Target type of the Enchantment
        """
        ...


    def isTreasure(self) -> bool:
        """
        Checks if this enchantment is a treasure enchantment.
        
        Treasure enchantments can only be received via looting, trading, or
        fishing.

        Returns
        - True if the enchantment is a treasure enchantment
        """
        ...


    def isCursed(self) -> bool:
        """
        Checks if this enchantment is a cursed enchantment
        
        Cursed enchantments are found the same way treasure enchantments are

        Returns
        - True if the enchantment is cursed

        Deprecated
        - cursed enchantments are no longer special. Will return True
        only for Enchantment.BINDING_CURSE and
        Enchantment.VANISHING_CURSE.
        """
        ...


    def conflictsWith(self, other: "Enchantment") -> bool:
        """
        Check if this enchantment conflicts with another enchantment.

        Arguments
        - other: The enchantment to check against

        Returns
        - True if there is a conflict.
        """
        ...


    def canEnchantItem(self, item: "ItemStack") -> bool:
        """
        Checks if this Enchantment may be applied to the given ItemStack.
        
        This does not check if it conflicts with any enchantments already
        applied to the item.

        Arguments
        - item: Item to test

        Returns
        - True if the enchantment may be applied, otherwise False
        """
        ...


    def equals(self, obj: "Object") -> bool:
        ...


    def hashCode(self) -> int:
        ...


    def toString(self) -> str:
        ...


    @staticmethod
    def registerEnchantment(enchantment: "Enchantment") -> None:
        """
        Registers an enchantment with the given ID and object.
        
        Generally not to be used from within a plugin.

        Arguments
        - enchantment: Enchantment to register
        """
        ...


    @staticmethod
    def isAcceptingRegistrations() -> bool:
        """
        Checks if this is accepting Enchantment registrations.

        Returns
        - True if the server Implementation may add enchantments
        """
        ...


    @staticmethod
    def stopAcceptingRegistrations() -> None:
        """
        Stops accepting any enchantment registrations
        """
        ...


    @staticmethod
    def getByKey(key: "NamespacedKey") -> "Enchantment":
        """
        Gets the Enchantment at the specified key

        Arguments
        - key: key to fetch

        Returns
        - Resulting Enchantment, or null if not found
        """
        ...


    @staticmethod
    def getByName(name: str) -> "Enchantment":
        """
        Gets the Enchantment at the specified name

        Arguments
        - name: Name to fetch

        Returns
        - Resulting Enchantment, or null if not found

        Deprecated
        - enchantments are badly named, use .getByKey(org.bukkit.NamespacedKey).
        """
        ...


    @staticmethod
    def values() -> list["Enchantment"]:
        """
        Gets an array of all the registered Enchantments

        Returns
        - Array of enchantments
        """
        ...
