"""
Python module generated from Java source file org.bukkit.advancement.AdvancementDisplay

Java source file obtained from artifact spigot-api version 1.19.4-R0.1-20230607.155743-88

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.advancement import *
from org.bukkit.inventory import ItemStack
from typing import Any, Callable, Iterable, Tuple


class AdvancementDisplay:
    """
    Holds information about how the advancement is displayed by the game.
    """

    def getTitle(self) -> str:
        """
        Gets the title of the advancement.

        Returns
        - The advancement title without colour codes.
        """
        ...


    def getDescription(self) -> str:
        """
        Gets the visible description of the advancement.

        Returns
        - The advancement description without colour codes.
        """
        ...


    def getIcon(self) -> "ItemStack":
        """
        The icon that is used for this advancement.

        Returns
        - an ItemStack that represents the advancement.
        """
        ...


    def shouldShowToast(self) -> bool:
        """
        Whether to show a toast to the player when this advancement has been
        completed.

        Returns
        - True if a toast is shown.
        """
        ...


    def shouldAnnounceChat(self) -> bool:
        """
        Whether to announce in the chat when this advancement has been completed.

        Returns
        - True if announced in chat.
        """
        ...


    def isHidden(self) -> bool:
        """
        Whether to hide this advancement and all its children from the
        advancement screen until this advancement have been completed.
        
        Has no effect on root advancements themselves, but still affects all
        their children.

        Returns
        - True if hidden.
        """
        ...


    def getX(self) -> float:
        """
        The X position of the advancement in the advancement screen.

        Returns
        - the X coordinate as float
        """
        ...


    def getY(self) -> float:
        """
        The Y position of the advancement in the advancement screen.

        Returns
        - the Y coordinate as float
        """
        ...


    def getType(self) -> "AdvancementDisplayType":
        """
        The display type of this advancement.

        Returns
        - an enum representing the type.
        """
        ...
