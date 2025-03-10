"""
Python module generated from Java source file org.bukkit.event.inventory.ClickType

Java source file obtained from artifact spigot-api version 1.20.1-R0.1-20230921.163938-66

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.event.inventory import *
from typing import Any, Callable, Iterable, Tuple


class ClickType(Enum):
    """
    What the client did to trigger this action (not the result).
    """

    LEFT = 0
    """
    The left (or primary) mouse button.
    """
    SHIFT_LEFT = 1
    """
    Holding shift while pressing the left mouse button.
    """
    RIGHT = 2
    """
    The right mouse button.
    """
    SHIFT_RIGHT = 3
    """
    Holding shift while pressing the right mouse button.
    """
    WINDOW_BORDER_LEFT = 4
    """
    Clicking the left mouse button on the grey area around the inventory.
    """
    WINDOW_BORDER_RIGHT = 5
    """
    Clicking the right mouse button on the grey area around the inventory.
    """
    MIDDLE = 6
    """
    The middle mouse button, or a "scrollwheel click".
    """
    NUMBER_KEY = 7
    """
    One of the number keys 1-9, correspond to slots on the hotbar.
    """
    DOUBLE_CLICK = 8
    """
    Pressing the left mouse button twice in quick succession.
    """
    DROP = 9
    """
    The "Drop" key (defaults to Q).
    """
    CONTROL_DROP = 10
    """
    Holding Ctrl while pressing the "Drop" key (defaults to Q).
    """
    CREATIVE = 11
    """
    Any action done with the Creative inventory open.
    """
    SWAP_OFFHAND = 12
    """
    The "swap item with offhand" key (defaults to F).
    """
    UNKNOWN = 13
    """
    A type of inventory manipulation not yet recognized by Bukkit.
    
    This is only for transitional purposes on a new Minecraft update, and
    should never be relied upon.
    
    Any ClickType.UNKNOWN is called on a best-effort basis.
    """


    def isKeyboardClick(self) -> bool:
        """
        Gets whether this ClickType represents the pressing of a key on a
        keyboard.

        Returns
        - True if this ClickType represents the pressing of a key
        """
        ...


    def isMouseClick(self) -> bool:
        """
        Gets whether this ClickType represents the pressing of a mouse button

        Returns
        - True if this ClickType represents the pressing of a mouse button
        """
        ...


    def isCreativeAction(self) -> bool:
        """
        Gets whether this ClickType represents an action that can only be
        performed by a Player in creative mode.

        Returns
        - True if this action requires Creative mode
        """
        ...


    def isRightClick(self) -> bool:
        """
        Gets whether this ClickType represents a right click.

        Returns
        - True if this ClickType represents a right click
        """
        ...


    def isLeftClick(self) -> bool:
        """
        Gets whether this ClickType represents a left click.

        Returns
        - True if this ClickType represents a left click
        """
        ...


    def isShiftClick(self) -> bool:
        """
        Gets whether this ClickType indicates that the shift key was pressed
        down when the click was made.

        Returns
        - True if the action uses Shift.
        """
        ...
