"""
Python module generated from Java source file org.bukkit.event.player.PlayerRecipeBookSettingsChangeEvent

Java source file obtained from artifact spigot-api version 1.21-R0.1-20240807.214924-87

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.entity import Player
from org.bukkit.event import HandlerList
from org.bukkit.event.player import *
from typing import Any, Callable, Iterable, Tuple


class PlayerRecipeBookSettingsChangeEvent(PlayerEvent):
    """
    Called when a player changes recipe book settings.
    """

    def __init__(self, player: "Player", recipeBookType: "RecipeBookType", open: bool, filtering: bool):
        ...


    def getRecipeBookType(self) -> "RecipeBookType":
        """
        Gets the type of recipe book the player is changing the settings for.

        Returns
        - the type of recipe book
        """
        ...


    def isOpen(self) -> bool:
        """
        Checks if the recipe book is being opened or closed.

        Returns
        - True if opening
        """
        ...


    def isFiltering(self) -> bool:
        """
        Checks if the recipe book filter is being enabled or disabled.

        Returns
        - True if enabling
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...


    class RecipeBookType(Enum):
        """
        Enum representing the various types of recipe book.
        
        Different types of recipe book are shown in different GUIs.
        """

        CRAFTING = 0
        """
        Recipe book seen in crafting table and player inventory.
        """
        FURNACE = 1
        """
        Recipe book seen in furnace.
        """
        BLAST_FURNACE = 2
        """
        Recipe book seen in blast furnace.
        """
        SMOKER = 3
        """
        Recipe book seen in smoker.
        """
