"""
Python module generated from Java source file org.bukkit.map.MapCursor

Java source file obtained from artifact spigot-api version 1.20.6-R0.1-20240613.150924-57

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit import Keyed
from org.bukkit import NamespacedKey
from org.bukkit.map import *
from typing import Any, Callable, Iterable, Tuple


class MapCursor:
    """
    Represents a cursor on a map.
    """

    def __init__(self, x: int, y: int, direction: int, type: int, visible: bool):
        """
        Initialize the map cursor.

        Arguments
        - x: The x coordinate, from -128 to 127.
        - y: The y coordinate, from -128 to 127.
        - direction: The facing of the cursor, from 0 to 15.
        - type: The type (color/style) of the map cursor.
        - visible: Whether the cursor is visible by default.

        Deprecated
        - Magic value
        """
        ...


    def __init__(self, x: int, y: int, direction: int, type: "Type", visible: bool):
        """
        Initialize the map cursor.

        Arguments
        - x: The x coordinate, from -128 to 127.
        - y: The y coordinate, from -128 to 127.
        - direction: The facing of the cursor, from 0 to 15.
        - type: The type (color/style) of the map cursor.
        - visible: Whether the cursor is visible by default.
        """
        ...


    def __init__(self, x: int, y: int, direction: int, type: int, visible: bool, caption: str):
        """
        Initialize the map cursor.

        Arguments
        - x: The x coordinate, from -128 to 127.
        - y: The y coordinate, from -128 to 127.
        - direction: The facing of the cursor, from 0 to 15.
        - type: The type (color/style) of the map cursor.
        - visible: Whether the cursor is visible by default.
        - caption: cursor caption

        Deprecated
        - Magic value
        """
        ...


    def __init__(self, x: int, y: int, direction: int, type: "Type", visible: bool, caption: str):
        """
        Initialize the map cursor.

        Arguments
        - x: The x coordinate, from -128 to 127.
        - y: The y coordinate, from -128 to 127.
        - direction: The facing of the cursor, from 0 to 15.
        - type: The type (color/style) of the map cursor.
        - visible: Whether the cursor is visible by default.
        - caption: cursor caption
        """
        ...


    def getX(self) -> int:
        """
        Get the X position of this cursor.

        Returns
        - The X coordinate.
        """
        ...


    def getY(self) -> int:
        """
        Get the Y position of this cursor.

        Returns
        - The Y coordinate.
        """
        ...


    def getDirection(self) -> int:
        """
        Get the direction of this cursor.

        Returns
        - The facing of the cursor, from 0 to 15.
        """
        ...


    def getType(self) -> "Type":
        """
        Get the type of this cursor.

        Returns
        - The type (color/style) of the map cursor.
        """
        ...


    def getRawType(self) -> int:
        """
        Get the type of this cursor.

        Returns
        - The type (color/style) of the map cursor.

        Deprecated
        - Magic value
        """
        ...


    def isVisible(self) -> bool:
        """
        Get the visibility status of this cursor.

        Returns
        - True if visible, False otherwise.
        """
        ...


    def setX(self, x: int) -> None:
        """
        Set the X position of this cursor.

        Arguments
        - x: The X coordinate.
        """
        ...


    def setY(self, y: int) -> None:
        """
        Set the Y position of this cursor.

        Arguments
        - y: The Y coordinate.
        """
        ...


    def setDirection(self, direction: int) -> None:
        """
        Set the direction of this cursor.

        Arguments
        - direction: The facing of the cursor, from 0 to 15.
        """
        ...


    def setType(self, type: "Type") -> None:
        """
        Set the type of this cursor.

        Arguments
        - type: The type (color/style) of the map cursor.
        """
        ...


    def setRawType(self, type: int) -> None:
        """
        Set the type of this cursor.

        Arguments
        - type: The type (color/style) of the map cursor.

        Deprecated
        - Magic value
        """
        ...


    def setVisible(self, visible: bool) -> None:
        """
        Set the visibility status of this cursor.

        Arguments
        - visible: True if visible.
        """
        ...


    def getCaption(self) -> str:
        """
        Gets the caption on this cursor.

        Returns
        - caption
        """
        ...


    def setCaption(self, caption: str) -> None:
        """
        Sets the caption on this cursor.

        Arguments
        - caption: new caption
        """
        ...


    class Type(Enum):
        """
        Represents the standard types of map cursors. More may be made
        available by resource packs - the value is used by the client as an
        index in the file './assets/minecraft/textures/map/map_icons.png' from minecraft.jar or from a
        resource pack.
        """

        PLAYER = (0, "player")
        FRAME = (1, "frame")
        RED_MARKER = (2, "red_marker")
        BLUE_MARKER = (3, "blue_marker")
        TARGET_X = (4, "target_x")
        TARGET_POINT = (5, "target_point")
        PLAYER_OFF_MAP = (6, "player_off_map")
        PLAYER_OFF_LIMITS = (7, "player_off_limits")
        MANSION = (8, "mansion")
        MONUMENT = (9, "monument")
        BANNER_WHITE = (10, "banner_white")
        BANNER_ORANGE = (11, "banner_orange")
        BANNER_MAGENTA = (12, "banner_magenta")
        BANNER_LIGHT_BLUE = (13, "banner_light_blue")
        BANNER_YELLOW = (14, "banner_yellow")
        BANNER_LIME = (15, "banner_lime")
        BANNER_PINK = (16, "banner_pink")
        BANNER_GRAY = (17, "banner_gray")
        BANNER_LIGHT_GRAY = (18, "banner_light_gray")
        BANNER_CYAN = (19, "banner_cyan")
        BANNER_PURPLE = (20, "banner_purple")
        BANNER_BLUE = (21, "banner_blue")
        BANNER_BROWN = (22, "banner_brown")
        BANNER_GREEN = (23, "banner_green")
        BANNER_RED = (24, "banner_red")
        BANNER_BLACK = (25, "banner_black")
        RED_X = (26, "red_x")
        VILLAGE_DESERT = (27, "village_desert")
        VILLAGE_PLAINS = (28, "village_plains")
        VILLAGE_SAVANNA = (29, "village_savanna")
        VILLAGE_SNOWY = (30, "village_snowy")
        VILLAGE_TAIGA = (31, "village_taiga")
        JUNGLE_TEMPLE = (32, "jungle_temple")
        SWAMP_HUT = (33, "swamp_hut")
        TRIAL_CHAMBERS = (34, "trial_chambers")


        def getKey(self) -> "NamespacedKey":
            ...


        def getValue(self) -> int:
            """
            Gets the internal value of the cursor.

            Returns
            - the value

            Deprecated
            - Magic value
            """
            ...


        @staticmethod
        def byValue(value: int) -> "Type":
            """
            Get a cursor by its internal value.

            Arguments
            - value: the value

            Returns
            - the matching type

            Deprecated
            - Magic value
            """
            ...
