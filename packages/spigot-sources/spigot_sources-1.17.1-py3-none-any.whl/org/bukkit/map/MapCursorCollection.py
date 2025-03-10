"""
Python module generated from Java source file org.bukkit.map.MapCursorCollection

Java source file obtained from artifact spigot-api version 1.17.1-R0.1-20211121.234319-104

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.map import *
from typing import Any, Callable, Iterable, Tuple


class MapCursorCollection:
    """
    Represents all the map cursors on a MapCanvas. Like MapCanvas, a
    MapCursorCollection is linked to a specific MapRenderer.
    """

    def size(self) -> int:
        """
        Get the amount of cursors in this collection.

        Returns
        - The size of this collection.
        """
        ...


    def getCursor(self, index: int) -> "MapCursor":
        """
        Get a cursor from this collection.

        Arguments
        - index: The index of the cursor.

        Returns
        - The MapCursor.
        """
        ...


    def removeCursor(self, cursor: "MapCursor") -> bool:
        """
        Remove a cursor from the collection.

        Arguments
        - cursor: The MapCursor to remove.

        Returns
        - Whether the cursor was removed successfully.
        """
        ...


    def addCursor(self, cursor: "MapCursor") -> "MapCursor":
        """
        Add a cursor to the collection.

        Arguments
        - cursor: The MapCursor to add.

        Returns
        - The MapCursor that was passed.
        """
        ...


    def addCursor(self, x: int, y: int, direction: int) -> "MapCursor":
        """
        Add a cursor to the collection.

        Arguments
        - x: The x coordinate, from -128 to 127.
        - y: The y coordinate, from -128 to 127.
        - direction: The facing of the cursor, from 0 to 15.

        Returns
        - The newly added MapCursor.
        """
        ...


    def addCursor(self, x: int, y: int, direction: int, type: int) -> "MapCursor":
        """
        Add a cursor to the collection.

        Arguments
        - x: The x coordinate, from -128 to 127.
        - y: The y coordinate, from -128 to 127.
        - direction: The facing of the cursor, from 0 to 15.
        - type: The type (color/style) of the map cursor.

        Returns
        - The newly added MapCursor.

        Deprecated
        - Magic value
        """
        ...


    def addCursor(self, x: int, y: int, direction: int, type: int, visible: bool) -> "MapCursor":
        """
        Add a cursor to the collection.

        Arguments
        - x: The x coordinate, from -128 to 127.
        - y: The y coordinate, from -128 to 127.
        - direction: The facing of the cursor, from 0 to 15.
        - type: The type (color/style) of the map cursor.
        - visible: Whether the cursor is visible.

        Returns
        - The newly added MapCursor.

        Deprecated
        - Magic value
        """
        ...


    def addCursor(self, x: int, y: int, direction: int, type: int, visible: bool, caption: str) -> "MapCursor":
        """
        Add a cursor to the collection.

        Arguments
        - x: The x coordinate, from -128 to 127.
        - y: The y coordinate, from -128 to 127.
        - direction: The facing of the cursor, from 0 to 15.
        - type: The type (color/style) of the map cursor.
        - visible: Whether the cursor is visible.
        - caption: banner caption

        Returns
        - The newly added MapCursor.

        Deprecated
        - Magic value
        """
        ...
