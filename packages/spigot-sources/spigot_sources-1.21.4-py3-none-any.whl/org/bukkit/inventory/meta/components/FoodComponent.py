"""
Python module generated from Java source file org.bukkit.inventory.meta.components.FoodComponent

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.configuration.serialization import ConfigurationSerializable
from org.bukkit.inventory.meta.components import *
from org.bukkit.inventory.meta.components.consumable import ConsumableComponent
from typing import Any, Callable, Iterable, Tuple


class FoodComponent(ConfigurationSerializable):
    """
    Represents a component which can handle food stats in any item.
    
    **Note:** Items with food stats has no effect unless the item can be
    consumed, see ConsumableComponent.
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
