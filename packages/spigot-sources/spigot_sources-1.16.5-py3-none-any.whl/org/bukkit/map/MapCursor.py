"""
Python module generated from Java source file org.bukkit.map.MapCursor

Java source file obtained from artifact spigot-api version 1.16.5-R0.1-20210611.041013-99

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
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
        index in the file './misc/mapicons.png' from minecraft.jar or from a
        resource pack.
        """

        WHITE_POINTER = (0)
        GREEN_POINTER = (1)
        RED_POINTER = (2)
        BLUE_POINTER = (3)
        WHITE_CROSS = (4)
        RED_MARKER = (5)
        WHITE_CIRCLE = (6)
        SMALL_WHITE_CIRCLE = (7)
        MANSION = (8)
        TEMPLE = (9)
        BANNER_WHITE = (10)
        BANNER_ORANGE = (11)
        BANNER_MAGENTA = (12)
        BANNER_LIGHT_BLUE = (13)
        BANNER_YELLOW = (14)
        BANNER_LIME = (15)
        BANNER_PINK = (16)
        BANNER_GRAY = (17)
        BANNER_LIGHT_GRAY = (18)
        BANNER_CYAN = (19)
        BANNER_PURPLE = (20)
        BANNER_BLUE = (21)
        BANNER_BROWN = (22)
        BANNER_GREEN = (23)
        BANNER_RED = (24)
        BANNER_BLACK = (25)
        RED_X = (26)


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
