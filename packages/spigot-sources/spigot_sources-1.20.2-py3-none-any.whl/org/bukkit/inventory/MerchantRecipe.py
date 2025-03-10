"""
Python module generated from Java source file org.bukkit.inventory.MerchantRecipe

Java source file obtained from artifact spigot-api version 1.20.2-R0.1-20231205.164257-71

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from org.bukkit import Material
from org.bukkit.entity import Villager
from org.bukkit.inventory import *
from org.bukkit.potion import PotionEffectType
from org.bukkit.util import NumberConversions
from typing import Any, Callable, Iterable, Tuple


class MerchantRecipe(Recipe):
    """
    Represents a merchant's trade.
    
    Trades can take one or two ingredients, and provide one result. The
    ingredients' ItemStack amounts are respected in the trade.
    
    A trade has a maximum number of uses. A Villager may periodically
    replenish its trades by resetting the .getUses uses of its merchant
    recipes to `0`, allowing them to be used again.
    
    A trade may or may not reward experience for being completed.
    
    During trades, the MerchantRecipe dynamically adjusts the amount of
    its first ingredient based on the following criteria:
    
    - .getDemand() Demand: This value is periodically updated by the
    villager that owns this merchant recipe based on how often the recipe has
    been used since it has been last restocked in relation to its
    .getMaxUses maximum uses. The amount by which the demand influences
    the amount of the first ingredient is scaled by the recipe's
    .getPriceMultiplier price multiplier, and can never be below zero.
    - .getSpecialPrice() Special price: This value is dynamically
    updated whenever a player starts and stops trading with a villager that owns
    this merchant recipe. It is based on the player's individual reputation with
    the villager, and the player's currently active status effects (see
    PotionEffectType.HERO_OF_THE_VILLAGE). The influence of the player's
    reputation on the special price is scaled by the recipe's
    .getPriceMultiplier price multiplier.
    
    The adjusted amount of the first ingredient is calculated by adding up the
    original amount of the first ingredient, the demand scaled by the recipe's
    .getPriceMultiplier price multiplier and truncated to the next lowest
    integer value greater than or equal to 0, and the special price, and then
    constraining the resulting value between `1` and the item stack's
    ItemStack.getMaxStackSize() maximum stack size.
    """

    def __init__(self, result: "ItemStack", maxUses: int):
        ...


    def __init__(self, result: "ItemStack", uses: int, maxUses: int, experienceReward: bool):
        ...


    def __init__(self, result: "ItemStack", uses: int, maxUses: int, experienceReward: bool, villagerExperience: int, priceMultiplier: float):
        ...


    def __init__(self, result: "ItemStack", uses: int, maxUses: int, experienceReward: bool, villagerExperience: int, priceMultiplier: float, demand: int, specialPrice: int):
        ...


    def getResult(self) -> "ItemStack":
        ...


    def addIngredient(self, item: "ItemStack") -> None:
        ...


    def removeIngredient(self, index: int) -> None:
        ...


    def setIngredients(self, ingredients: list["ItemStack"]) -> None:
        ...


    def getIngredients(self) -> list["ItemStack"]:
        ...


    def getAdjustedIngredient1(self) -> "ItemStack":
        """
        Gets the .adjust(ItemStack) adjusted first ingredient.

        Returns
        - the adjusted first ingredient, or `null` if this
        recipe has no ingredients

        See
        - .adjust(ItemStack)
        """
        ...


    def adjust(self, itemStack: "ItemStack") -> None:
        """
        Modifies the amount of the given ItemStack in the same way as
        MerchantRecipe dynamically adjusts the amount of the first ingredient
        during trading.
        
        This is calculated by adding up the original amount of the item, the
        demand scaled by the recipe's
        .getPriceMultiplier price multiplier and truncated to the next
        lowest integer value greater than or equal to 0, and the special price,
        and then constraining the resulting value between `1` and the
        ItemStack's ItemStack.getMaxStackSize()
        maximum stack size.

        Arguments
        - itemStack: the item to adjust
        """
        ...


    def getDemand(self) -> int:
        """
        Get the demand for this trade.

        Returns
        - the demand
        """
        ...


    def setDemand(self, demand: int) -> None:
        """
        Set the demand for this trade.

        Arguments
        - demand: the new demand
        """
        ...


    def getSpecialPrice(self) -> int:
        """
        Get the special price for this trade.

        Returns
        - special price value
        """
        ...


    def setSpecialPrice(self, specialPrice: int) -> None:
        """
        Set the special price for this trade.

        Arguments
        - specialPrice: special price value
        """
        ...


    def getUses(self) -> int:
        """
        Get the number of times this trade has been used.

        Returns
        - the number of uses
        """
        ...


    def setUses(self, uses: int) -> None:
        """
        Set the number of times this trade has been used.

        Arguments
        - uses: the number of uses
        """
        ...


    def getMaxUses(self) -> int:
        """
        Get the maximum number of uses this trade has.

        Returns
        - the maximum number of uses
        """
        ...


    def setMaxUses(self, maxUses: int) -> None:
        """
        Set the maximum number of uses this trade has.

        Arguments
        - maxUses: the maximum number of time this trade can be used
        """
        ...


    def hasExperienceReward(self) -> bool:
        """
        Whether to reward experience to the player for the trade.

        Returns
        - whether to reward experience to the player for completing this
        trade
        """
        ...


    def setExperienceReward(self, flag: bool) -> None:
        """
        Set whether to reward experience to the player for the trade.

        Arguments
        - flag: whether to reward experience to the player for completing
        this trade
        """
        ...


    def getVillagerExperience(self) -> int:
        """
        Gets the amount of experience the villager earns from this trade.

        Returns
        - villager experience
        """
        ...


    def setVillagerExperience(self, villagerExperience: int) -> None:
        """
        Sets the amount of experience the villager earns from this trade.

        Arguments
        - villagerExperience: new experience amount
        """
        ...


    def getPriceMultiplier(self) -> float:
        """
        Gets the price multiplier for the cost of this trade.

        Returns
        - price multiplier
        """
        ...


    def setPriceMultiplier(self, priceMultiplier: float) -> None:
        """
        Sets the price multiplier for the cost of this trade.

        Arguments
        - priceMultiplier: new price multiplier
        """
        ...
