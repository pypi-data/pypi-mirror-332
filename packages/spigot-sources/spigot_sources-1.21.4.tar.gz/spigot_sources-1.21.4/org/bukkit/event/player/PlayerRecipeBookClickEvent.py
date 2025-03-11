"""
Python module generated from Java source file org.bukkit.event.player.PlayerRecipeBookClickEvent

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from org.bukkit.entity import Player
from org.bukkit.event import HandlerList
from org.bukkit.event.player import *
from org.bukkit.inventory import CraftingRecipe
from org.bukkit.inventory import Recipe
from typing import Any, Callable, Iterable, Tuple


class PlayerRecipeBookClickEvent(PlayerEvent):
    """
    Called when a player clicks a recipe in the recipe book.
    """

    def __init__(self, player: "Player", recipe: "Recipe", shiftClick: bool):
        ...


    def getOriginalRecipe(self) -> "Recipe":
        """
        Gets the original recipe the player was trying to craft. 
        This *will not* reflect any changes made with setRecipe.

        Returns
        - the original recipe
        """
        ...


    def getRecipe(self) -> "Recipe":
        """
        Gets the recipe the player is trying to craft. 
        This *will* reflect changes made with setRecipe.

        Returns
        - the recipe
        """
        ...


    def setRecipe(self, recipe: "Recipe") -> None:
        """
        Set the recipe that will be used. 
        The game will attempt to move the ingredients for this recipe into the
        appropriate slots.
        
        If the original recipe is a CraftingRecipe the provided recipe
        must also be a CraftingRecipe, otherwise the provided recipe must
        be of the same type as the original recipe.

        Arguments
        - recipe: the recipe to be used
        """
        ...


    def isShiftClick(self) -> bool:
        """
        If True the game will attempt to move the ingredients for as many copies
        of this recipe as possible into the appropriate slots, otherwise only 1
        copy will be moved.

        Returns
        - whether as many copies as possible should be moved
        """
        ...


    def setShiftClick(self, shiftClick: bool) -> None:
        """
        Sets if the game will attempt to move the ingredients for as many copies
        of this recipe as possible into the appropriate slots.

        Arguments
        - shiftClick: whether as many copies as possible should be moved
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
