"""
Python module generated from Java source file org.bukkit.map.MapView

Java source file obtained from artifact spigot-api version 1.19.4-R0.1-20230607.155743-88

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit import World
from org.bukkit.inventory.meta import MapMeta
from org.bukkit.map import *
from typing import Any, Callable, Iterable, Tuple


class MapView:
    """
    Represents a map item.
    """

    def getId(self) -> int:
        """
        Get the ID of this map item for use with MapMeta.

        Returns
        - The ID of the map.
        """
        ...


    def isVirtual(self) -> bool:
        """
        Check whether this map is virtual. A map is virtual if its lowermost
        MapRenderer is plugin-provided.

        Returns
        - Whether the map is virtual.
        """
        ...


    def getScale(self) -> "Scale":
        """
        Get the scale of this map.

        Returns
        - The scale of the map.
        """
        ...


    def setScale(self, scale: "Scale") -> None:
        """
        Set the scale of this map.

        Arguments
        - scale: The scale to set.
        """
        ...


    def getCenterX(self) -> int:
        """
        Get the center X position of this map.

        Returns
        - The center X position.
        """
        ...


    def getCenterZ(self) -> int:
        """
        Get the center Z position of this map.

        Returns
        - The center Z position.
        """
        ...


    def setCenterX(self, x: int) -> None:
        """
        Set the center X position of this map.

        Arguments
        - x: The center X position.
        """
        ...


    def setCenterZ(self, z: int) -> None:
        """
        Set the center Z position of this map.

        Arguments
        - z: The center Z position.
        """
        ...


    def getWorld(self) -> "World":
        """
        Get the world that this map is associated with. Primarily used by the
        internal renderer, but may be used by external renderers. May return
        null if the world the map is associated with is not loaded.

        Returns
        - The World this map is associated with.
        """
        ...


    def setWorld(self, world: "World") -> None:
        """
        Set the world that this map is associated with. The world is used by
        the internal renderer, and may also be used by external renderers.

        Arguments
        - world: The World to associate this map with.
        """
        ...


    def getRenderers(self) -> list["MapRenderer"]:
        """
        Get a list of MapRenderers currently in effect.

        Returns
        - A `List<MapRenderer>` containing each map renderer.
        """
        ...


    def addRenderer(self, renderer: "MapRenderer") -> None:
        """
        Add a renderer to this map.

        Arguments
        - renderer: The MapRenderer to add.
        """
        ...


    def removeRenderer(self, renderer: "MapRenderer") -> bool:
        """
        Remove a renderer from this map.

        Arguments
        - renderer: The MapRenderer to remove.

        Returns
        - True if the renderer was successfully removed.
        """
        ...


    def isTrackingPosition(self) -> bool:
        """
        Gets whether a position cursor should be shown when the map is near its
        center.

        Returns
        - tracking status
        """
        ...


    def setTrackingPosition(self, trackingPosition: bool) -> None:
        """
        Sets whether a position cursor should be shown when the map is near its
        center.

        Arguments
        - trackingPosition: tracking status
        """
        ...


    def isUnlimitedTracking(self) -> bool:
        """
        Whether the map will show a smaller position cursor (True), or no
        position cursor (False) when cursor is outside of map's range.

        Returns
        - unlimited tracking state
        """
        ...


    def setUnlimitedTracking(self, unlimited: bool) -> None:
        """
        Whether the map will show a smaller position cursor (True), or no
        position cursor (False) when cursor is outside of map's range.

        Arguments
        - unlimited: tracking state
        """
        ...


    def isLocked(self) -> bool:
        """
        Gets whether the map is locked or not.
        
        A locked map may not be explored further.

        Returns
        - lock status
        """
        ...


    def setLocked(self, locked: bool) -> None:
        """
        Gets whether the map is locked or not.
        
        A locked map may not be explored further.

        Arguments
        - locked: status
        """
        ...


    class Scale(Enum):
        """
        An enum representing all possible scales a map can be set to.
        """

        CLOSEST = (0)
        CLOSE = (1)
        NORMAL = (2)
        FAR = (3)
        FARTHEST = (4)


        @staticmethod
        def valueOf(value: int) -> "Scale":
            """
            Get the scale given the raw value.

            Arguments
            - value: The raw scale

            Returns
            - The enum scale, or null for an invalid input

            Deprecated
            - Magic value
            """
            ...


        def getValue(self) -> int:
            """
            Get the raw value of this scale level.

            Returns
            - The scale value

            Deprecated
            - Magic value
            """
            ...
