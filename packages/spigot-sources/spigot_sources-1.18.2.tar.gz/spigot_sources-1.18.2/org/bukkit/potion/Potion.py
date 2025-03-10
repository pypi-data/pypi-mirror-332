"""
Python module generated from Java source file org.bukkit.potion.Potion

Java source file obtained from artifact spigot-api version 1.18.2-R0.1-20220607.160742-53

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.apache.commons.lang import Validate
from org.bukkit import Material
from org.bukkit.entity import LivingEntity
from org.bukkit.inventory import ItemStack
from org.bukkit.inventory.meta import PotionMeta
from org.bukkit.potion import *
from typing import Any, Callable, Iterable, Tuple


class Potion:
    """
    Potion Adapter for pre-1.9 data values
    see @PotionMeta for 1.9+
    """

    def __init__(self, type: "PotionType"):
        """
        Construct a new potion of the given type. Unless the type is PotionType.WATER, it will be level one, without extended duration.
        Don't use this constructor to create a no-effect potion other than
        water bottle.

        Arguments
        - type: The potion type
        """
        ...


    def __init__(self, type: "PotionType", level: int):
        """
        Create a new potion of the given type and level.

        Arguments
        - type: The type of potion.
        - level: The potion's level.
        """
        ...


    def __init__(self, type: "PotionType", level: int, splash: bool):
        """
        Create a new potion of the given type and level.

        Arguments
        - type: The type of potion.
        - level: The potion's level.
        - splash: Whether it is a splash potion.

        Deprecated
        - In favour of using .Potion(PotionType) with .splash().
        """
        ...


    def __init__(self, type: "PotionType", level: int, splash: bool, extended: bool):
        """
        Create a new potion of the given type and level.

        Arguments
        - type: The type of potion.
        - level: The potion's level.
        - splash: Whether it is a splash potion.
        - extended: Whether it has an extended duration.

        Deprecated
        - In favour of using .Potion(PotionType) with .extend() and possibly .splash().
        """
        ...


    def splash(self) -> "Potion":
        """
        Chain this to the constructor to make the potion a splash potion.

        Returns
        - The potion.
        """
        ...


    def extend(self) -> "Potion":
        """
        Chain this to the constructor to extend the potion's duration.

        Returns
        - The potion.
        """
        ...


    def apply(self, to: "ItemStack") -> None:
        """
        Applies the effects of this potion to the given ItemStack. The
        ItemStack must be a potion.

        Arguments
        - to: The itemstack to apply to
        """
        ...


    def apply(self, to: "LivingEntity") -> None:
        """
        Applies the effects that would be applied by this potion to the given
        LivingEntity.

        Arguments
        - to: The entity to apply the effects to

        See
        - LivingEntity.addPotionEffects(Collection)
        """
        ...


    def equals(self, obj: "Object") -> bool:
        ...


    def getEffects(self) -> Iterable["PotionEffect"]:
        """
        Returns a collection of PotionEffects that this Potion
        would confer upon a LivingEntity.

        Returns
        - The effects that this potion applies

        See
        - Potion.toDamageValue()
        """
        ...


    def getLevel(self) -> int:
        """
        Returns the level of this potion.

        Returns
        - The level of this potion
        """
        ...


    def getType(self) -> "PotionType":
        """
        Returns the PotionType of this potion.

        Returns
        - The type of this potion
        """
        ...


    def hasExtendedDuration(self) -> bool:
        """
        Returns whether this potion has an extended duration.

        Returns
        - Whether this potion has extended duration
        """
        ...


    def hashCode(self) -> int:
        ...


    def isSplash(self) -> bool:
        """
        Returns whether this potion is a splash potion.

        Returns
        - Whether this is a splash potion
        """
        ...


    def setHasExtendedDuration(self, isExtended: bool) -> None:
        """
        Set whether this potion has extended duration. This will cause the
        potion to have roughly 8/3 more duration than a regular potion.

        Arguments
        - isExtended: Whether the potion should have extended duration
        """
        ...


    def setSplash(self, isSplash: bool) -> None:
        """
        Sets whether this potion is a splash potion. Splash potions can be
        thrown for a radius effect.

        Arguments
        - isSplash: Whether this is a splash potion
        """
        ...


    def setType(self, type: "PotionType") -> None:
        """
        Sets the PotionType of this potion.

        Arguments
        - type: The new type of this potion
        """
        ...


    def setLevel(self, level: int) -> None:
        """
        Sets the level of this potion.

        Arguments
        - level: The new level of this potion
        """
        ...


    def toDamageValue(self) -> int:
        """
        Converts this potion to a valid potion damage short, usable for potion
        item stacks.

        Returns
        - The damage value of this potion

        Deprecated
        - Non-functional
        """
        ...


    def toItemStack(self, amount: int) -> "ItemStack":
        """
        Converts this potion to an ItemStack with the specified amount
        and a correct damage value.

        Arguments
        - amount: The amount of the ItemStack

        Returns
        - The created ItemStack
        """
        ...


    @staticmethod
    def fromDamage(damage: int) -> "Potion":
        """
        Gets the potion from its damage value.

        Arguments
        - damage: the damage value

        Returns
        - the produced potion
        """
        ...


    @staticmethod
    def fromItemStack(item: "ItemStack") -> "Potion":
        ...


    @staticmethod
    def getBrewer() -> "PotionBrewer":
        """
        Returns an instance of PotionBrewer.

        Returns
        - An instance of PotionBrewer
        """
        ...


    @staticmethod
    def setPotionBrewer(other: "PotionBrewer") -> None:
        """
        Sets the current instance of PotionBrewer. Generally not to be
        used from within a plugin.

        Arguments
        - other: The new PotionBrewer
        """
        ...


    def getNameId(self) -> int:
        """
        Gets the potion from its name id.

        Returns
        - the name id

        Deprecated
        - Non-functional
        """
        ...
