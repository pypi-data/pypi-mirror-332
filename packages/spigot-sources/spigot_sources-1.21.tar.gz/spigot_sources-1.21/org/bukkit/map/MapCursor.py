"""
Python module generated from Java source file org.bukkit.map.MapCursor

Java source file obtained from artifact spigot-api version 1.21-R0.1-20240807.214924-87

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from com.google.common.collect import Lists
from java.util import Locale
from org.bukkit import Keyed
from org.bukkit import NamespacedKey
from org.bukkit import Registry
from org.bukkit.map import *
from org.bukkit.util import OldEnum
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
        - Magic value, use .MapCursor(byte, byte, byte, Type, boolean, String)
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


    class Type(OldEnum, Keyed):
        """
        Represents the standard types of map cursors. More may be made
        available by resource packs - the value is used by the client as an
        index in the file './assets/minecraft/textures/map/map_icons.png' from minecraft.jar or from a
        resource pack.
        """

        PLAYER = getType("player")
        FRAME = getType("frame")
        RED_MARKER = getType("red_marker")
        BLUE_MARKER = getType("blue_marker")
        TARGET_X = getType("target_x")
        TARGET_POINT = getType("target_point")
        PLAYER_OFF_MAP = getType("player_off_map")
        PLAYER_OFF_LIMITS = getType("player_off_limits")
        MANSION = getType("mansion")
        MONUMENT = getType("monument")
        BANNER_WHITE = getType("banner_white")
        BANNER_ORANGE = getType("banner_orange")
        BANNER_MAGENTA = getType("banner_magenta")
        BANNER_LIGHT_BLUE = getType("banner_light_blue")
        BANNER_YELLOW = getType("banner_yellow")
        BANNER_LIME = getType("banner_lime")
        BANNER_PINK = getType("banner_pink")
        BANNER_GRAY = getType("banner_gray")
        BANNER_LIGHT_GRAY = getType("banner_light_gray")
        BANNER_CYAN = getType("banner_cyan")
        BANNER_PURPLE = getType("banner_purple")
        BANNER_BLUE = getType("banner_blue")
        BANNER_BROWN = getType("banner_brown")
        BANNER_GREEN = getType("banner_green")
        BANNER_RED = getType("banner_red")
        BANNER_BLACK = getType("banner_black")
        RED_X = getType("red_x")
        VILLAGE_DESERT = getType("village_desert")
        VILLAGE_PLAINS = getType("village_plains")
        VILLAGE_SAVANNA = getType("village_savanna")
        VILLAGE_SNOWY = getType("village_snowy")
        VILLAGE_TAIGA = getType("village_taiga")
        JUNGLE_TEMPLE = getType("jungle_temple")
        SWAMP_HUT = getType("swamp_hut")
        TRIAL_CHAMBERS = getType("trial_chambers")


        @staticmethod
        def getType(key: str) -> "Type":
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


        @staticmethod
        def valueOf(name: str) -> "Type":
            """
            Arguments
            - name: of the type.

            Returns
            - the type with the given name.

            Deprecated
            - only for backwards compatibility, use Registry.get(NamespacedKey) instead.
            """
            ...


        @staticmethod
        def values() -> list["Type"]:
            """
            Returns
            - an array of all known map cursor types.

            Deprecated
            - use Registry.iterator().
            """
            ...
