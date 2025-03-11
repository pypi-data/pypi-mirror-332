"""
Python module generated from Java source file org.bukkit.inventory.meta.components.FoodComponent

Java source file obtained from artifact spigot-api version 1.21.1-R0.1-20241022.152140-54

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.configuration.serialization import ConfigurationSerializable
from org.bukkit.inventory import ItemStack
from org.bukkit.inventory.meta.components import *
from org.bukkit.potion import PotionEffect
from typing import Any, Callable, Iterable, Tuple


class FoodComponent(ConfigurationSerializable):
    """
    Represents a component which can turn any item into food.
    """

    def getNutrition(self) -> int:
        """
        Gets the food restored by this item when eaten.

        Returns
        - nutrition value
        """
        ...


    def setNutrition(self, nutrition: int) -> None:
        """
        Sets the food restored by this item when eaten.

        Arguments
        - nutrition: new nutrition value, must be non-negative
        """
        ...


    def getSaturation(self) -> float:
        """
        Gets the saturation restored by this item when eaten.

        Returns
        - saturation value
        """
        ...


    def setSaturation(self, saturation: float) -> None:
        """
        Sets the saturation restored by this item when eaten.

        Arguments
        - saturation: new saturation value
        """
        ...


    def canAlwaysEat(self) -> bool:
        """
        Gets if this item can be eaten even when not hungry.

        Returns
        - True if always edible
        """
        ...


    def setCanAlwaysEat(self, canAlwaysEat: bool) -> None:
        """
        Sets if this item can be eaten even when not hungry.

        Arguments
        - canAlwaysEat: whether always edible
        """
        ...


    def getEatSeconds(self) -> float:
        """
        Gets the time in seconds it will take for this item to be eaten.

        Returns
        - eat time
        """
        ...


    def setEatSeconds(self, eatSeconds: float) -> None:
        """
        Sets the time in seconds it will take for this item to be eaten.

        Arguments
        - eatSeconds: new eat time
        """
        ...


    def getUsingConvertsTo(self) -> "ItemStack":
        """
        Gets the item this food will convert to once eaten.

        Returns
        - converted item
        """
        ...


    def setUsingConvertsTo(self, item: "ItemStack") -> None:
        """
        Sets the item this food will convert to once eaten.

        Arguments
        - item: converted item
        """
        ...


    def getEffects(self) -> list["FoodEffect"]:
        """
        Gets the effects which may be applied by this item when eaten.

        Returns
        - food effects
        """
        ...


    def setEffects(self, effects: list["FoodEffect"]) -> None:
        """
        Sets the effects which may be applied by this item when eaten.

        Arguments
        - effects: new effects
        """
        ...


    def addEffect(self, effect: "PotionEffect", probability: float) -> "FoodEffect":
        """
        Adds an effect which may be applied by this item when eaten.

        Arguments
        - effect: the effect
        - probability: the probability of the effect being applied

        Returns
        - the added effect
        """
        ...


    class FoodEffect(ConfigurationSerializable):
        """
        An effect which may be applied by this item when eaten.
        """

        def getEffect(self) -> "PotionEffect":
            """
            Gets the effect which may be applied.

            Returns
            - the effect
            """
            ...


        def setEffect(self, effect: "PotionEffect") -> None:
            """
            Sets the effect which may be applied.

            Arguments
            - effect: the new effect
            """
            ...


        def getProbability(self) -> float:
            """
            Gets the probability of this effect being applied.

            Returns
            - probability
            """
            ...


        def setProbability(self, probability: float) -> None:
            """
            Sets the probability of this effect being applied.

            Arguments
            - probability: between 0 and 1 inclusive.
            """
            ...
