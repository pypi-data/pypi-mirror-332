"""
Python module generated from Java source file org.bukkit.enchantments.Enchantment

Java source file obtained from artifact spigot-api version 1.21.2-R0.1-20241023.084343-5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.collect import Lists
from java.util import Locale
from org.bukkit import Keyed
from org.bukkit import NamespacedKey
from org.bukkit import Registry
from org.bukkit import Translatable
from org.bukkit.enchantments import *
from org.bukkit.inventory import ItemStack
from typing import Any, Callable, Iterable, Tuple


class Enchantment(Keyed, Translatable):
    """
    The various type of enchantments that may be added to armour or weapons
    """

    PROTECTION = getEnchantment("protection")
    """
    Provides protection against environmental damage
    """
    FIRE_PROTECTION = getEnchantment("fire_protection")
    """
    Provides protection against fire damage
    """
    FEATHER_FALLING = getEnchantment("feather_falling")
    """
    Provides protection against fall damage
    """
    BLAST_PROTECTION = getEnchantment("blast_protection")
    """
    Provides protection against explosive damage
    """
    PROJECTILE_PROTECTION = getEnchantment("projectile_protection")
    """
    Provides protection against projectile damage
    """
    RESPIRATION = getEnchantment("respiration")
    """
    Decreases the rate of air loss whilst underwater
    """
    AQUA_AFFINITY = getEnchantment("aqua_affinity")
    """
    Increases the speed at which a player may mine underwater
    """
    THORNS = getEnchantment("thorns")
    """
    Damages the attacker
    """
    DEPTH_STRIDER = getEnchantment("depth_strider")
    """
    Increases walking speed while in water
    """
    FROST_WALKER = getEnchantment("frost_walker")
    """
    Freezes any still water adjacent to ice / frost which player is walking on
    """
    BINDING_CURSE = getEnchantment("binding_curse")
    """
    Item cannot be removed
    """
    SHARPNESS = getEnchantment("sharpness")
    """
    Increases damage against all targets
    """
    SMITE = getEnchantment("smite")
    """
    Increases damage against undead targets
    """
    BANE_OF_ARTHROPODS = getEnchantment("bane_of_arthropods")
    """
    Increases damage against arthropod targets
    """
    KNOCKBACK = getEnchantment("knockback")
    """
    All damage to other targets will knock them back when hit
    """
    FIRE_ASPECT = getEnchantment("fire_aspect")
    """
    When attacking a target, has a chance to set them on fire
    """
    LOOTING = getEnchantment("looting")
    """
    Provides a chance of gaining extra loot when killing monsters
    """
    SWEEPING_EDGE = getEnchantment("sweeping_edge")
    """
    Increases damage against targets when using a sweep attack
    """
    EFFICIENCY = getEnchantment("efficiency")
    """
    Increases the rate at which you mine/dig
    """
    SILK_TOUCH = getEnchantment("silk_touch")
    """
    Allows blocks to drop themselves instead of fragments (for example,
    stone instead of cobblestone)
    """
    UNBREAKING = getEnchantment("unbreaking")
    """
    Decreases the rate at which a tool looses durability
    """
    FORTUNE = getEnchantment("fortune")
    """
    Provides a chance of gaining extra loot when destroying blocks
    """
    POWER = getEnchantment("power")
    """
    Provides extra damage when shooting arrows from bows
    """
    PUNCH = getEnchantment("punch")
    """
    Provides a knockback when an entity is hit by an arrow from a bow
    """
    FLAME = getEnchantment("flame")
    """
    Sets entities on fire when hit by arrows shot from a bow
    """
    INFINITY = getEnchantment("infinity")
    """
    Provides infinite arrows when shooting a bow
    """
    LUCK_OF_THE_SEA = getEnchantment("luck_of_the_sea")
    """
    Decreases odds of catching worthless junk
    """
    LURE = getEnchantment("lure")
    """
    Increases rate of fish biting your hook
    """
    LOYALTY = getEnchantment("loyalty")
    """
    Causes a thrown trident to return to the player who threw it
    """
    IMPALING = getEnchantment("impaling")
    """
    Deals more damage to mobs that live in the ocean
    """
    RIPTIDE = getEnchantment("riptide")
    """
    When it is rainy, launches the player in the direction their trident is thrown
    """
    CHANNELING = getEnchantment("channeling")
    """
    Strikes lightning when a mob is hit with a trident if conditions are
    stormy
    """
    MULTISHOT = getEnchantment("multishot")
    """
    Shoot multiple arrows from crossbows
    """
    QUICK_CHARGE = getEnchantment("quick_charge")
    """
    Charges crossbows quickly
    """
    PIERCING = getEnchantment("piercing")
    """
    Crossbow projectiles pierce entities
    """
    DENSITY = getEnchantment("density")
    """
    Increases fall damage of maces
    """
    BREACH = getEnchantment("breach")
    """
    Reduces armor effectiveness against maces
    """
    WIND_BURST = getEnchantment("wind_burst")
    """
    Emits wind burst upon hitting enemy
    """
    MENDING = getEnchantment("mending")
    """
    Allows mending the item using experience orbs
    """
    VANISHING_CURSE = getEnchantment("vanishing_curse")
    """
    Item disappears instead of dropping
    """
    SOUL_SPEED = getEnchantment("soul_speed")
    """
    Walk quicker on soul blocks
    """
    SWIFT_SNEAK = getEnchantment("swift_sneak")
    """
    Walk quicker while sneaking
    """


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

        Deprecated
        - enchantment groupings are now managed by tags, not categories
        """
        ...


    def isTreasure(self) -> bool:
        """
        Checks if this enchantment is a treasure enchantment.
        
        Treasure enchantments can only be received via looting, trading, or
        fishing.

        Returns
        - True if the enchantment is a treasure enchantment

        Deprecated
        - enchantment types are now managed by tags
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


    @staticmethod
    def getByKey(key: "NamespacedKey") -> "Enchantment":
        """
        Gets the Enchantment at the specified key

        Arguments
        - key: key to fetch

        Returns
        - Resulting Enchantment, or null if not found

        Deprecated
        - only for backwards compatibility, use Registry.get(NamespacedKey) instead
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

        Deprecated
        - use Registry.iterator() Registry.ENCHANTMENT.iterator()
        """
        ...
