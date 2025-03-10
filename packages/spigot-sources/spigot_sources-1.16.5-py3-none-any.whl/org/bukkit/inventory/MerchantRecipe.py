"""
Python module generated from Java source file org.bukkit.inventory.MerchantRecipe

Java source file obtained from artifact spigot-api version 1.16.5-R0.1-20210611.041013-99

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from org.bukkit.inventory import *
from typing import Any, Callable, Iterable, Tuple


class MerchantRecipe(Recipe):
    """
    Represents a merchant's trade.
    
    Trades can take one or two ingredients, and provide one result. The
    ingredients' ItemStack amounts are respected in the trade.
    
    A trade has a limited number of uses, after which the trade can no longer be
    used, unless the player uses a different trade, which will cause its maximum
    uses to increase.
    
    A trade may or may not reward experience for being completed.

    See
    - org.bukkit.event.entity.VillagerReplenishTradeEvent
    """

    def __init__(self, result: "ItemStack", maxUses: int):
        ...


    def __init__(self, result: "ItemStack", uses: int, maxUses: int, experienceReward: bool):
        ...


    def __init__(self, result: "ItemStack", uses: int, maxUses: int, experienceReward: bool, villagerExperience: int, priceMultiplier: float):
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
        
        The maximum uses of this trade may increase when a player trades with the
        owning merchant.

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
        Gets the additive price multiplier for the cost of this trade.

        Returns
        - price multiplier
        """
        ...


    def setPriceMultiplier(self, priceMultiplier: float) -> None:
        """
        Sets the additive price multiplier for the cost of this trade.

        Arguments
        - priceMultiplier: new price multiplier
        """
        ...
