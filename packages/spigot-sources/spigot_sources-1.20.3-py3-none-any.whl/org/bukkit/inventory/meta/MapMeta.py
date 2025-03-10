"""
Python module generated from Java source file org.bukkit.inventory.meta.MapMeta

Java source file obtained from artifact spigot-api version 1.20.3-R0.1-20231207.085553-9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Color
from org.bukkit import UndefinedNullability
from org.bukkit.inventory.meta import *
from org.bukkit.map import MapView
from typing import Any, Callable, Iterable, Tuple


class MapMeta(ItemMeta):
    """
    Represents a map that can be scalable.
    """

    def hasMapId(self) -> bool:
        """
        Checks for existence of a map ID number.

        Returns
        - True if this has a map ID number.

        See
        - .hasMapView()

        Deprecated
        - These methods are poor API: They rely on the caller to pass
        in an only an integer property, and have poorly defined implementation
        behavior if that integer is not a valid map (the current implementation
        for example will generate a new map with a different ID). The xxxMapView
        family of methods should be used instead.
        """
        ...


    def getMapId(self) -> int:
        """
        Gets the map ID that is set. This is used to determine what map is
        displayed.
        
        Plugins should check that hasMapId() returns `True` before
        calling this method.

        Returns
        - the map ID that is set

        See
        - .getMapView()

        Deprecated
        - These methods are poor API: They rely on the caller to pass
        in an only an integer property, and have poorly defined implementation
        behavior if that integer is not a valid map (the current implementation
        for example will generate a new map with a different ID). The xxxMapView
        family of methods should be used instead.
        """
        ...


    def setMapId(self, id: int) -> None:
        """
        Sets the map ID. This is used to determine what map is displayed.

        Arguments
        - id: the map id to set

        See
        - .setMapView(org.bukkit.map.MapView)

        Deprecated
        - These methods are poor API: They rely on the caller to pass
        in an only an integer property, and have poorly defined implementation
        behavior if that integer is not a valid map (the current implementation
        for example will generate a new map with a different ID). The xxxMapView
        family of methods should be used instead.
        """
        ...


    def hasMapView(self) -> bool:
        """
        Checks for existence of an associated map.

        Returns
        - True if this item has an associated map
        """
        ...


    def getMapView(self) -> "MapView":
        """
        Gets the map view that is associated with this map item.
        
        
        Plugins should check that hasMapView() returns `True` before
        calling this method.

        Returns
        - the map view, or null if the item hasMapView(), but this map does
        not exist on the server
        """
        ...


    def setMapView(self, map: "MapView") -> None:
        """
        Sets the associated map. This is used to determine what map is displayed.
        
        
        The implementation **may** allow null to clear the associated map, but
        this is not required and is liable to generate a new (undefined) map when
        the item is first used.

        Arguments
        - map: the map to set
        """
        ...


    def isScaling(self) -> bool:
        """
        Checks to see if this map is scaling.

        Returns
        - True if this map is scaling
        """
        ...


    def setScaling(self, value: bool) -> None:
        """
        Sets if this map is scaling or not.

        Arguments
        - value: True to scale
        """
        ...


    def hasLocationName(self) -> bool:
        """
        Checks for existence of a location name.

        Returns
        - True if this has a location name

        Deprecated
        - This method does not have the expected effect and is
        actually an alias for ItemMeta.hasLocalizedName().
        """
        ...


    def getLocationName(self) -> str:
        """
        Gets the location name that is set.
        
        Plugins should check that hasLocationName() returns `True`
        before calling this method.

        Returns
        - the location name that is set

        Deprecated
        - This method does not have the expected effect and is
        actually an alias for ItemMeta.getLocalizedName().
        """
        ...


    def setLocationName(self, name: str) -> None:
        """
        Sets the location name.

        Arguments
        - name: the name to set

        Deprecated
        - This method does not have the expected effect and is
        actually an alias for ItemMeta.setLocalizedName(String).
        """
        ...


    def hasColor(self) -> bool:
        """
        Checks for existence of a map color.

        Returns
        - True if this has a custom map color
        """
        ...


    def getColor(self) -> "Color":
        """
        Gets the map color that is set. A custom map color will alter the display
        of the map in an inventory slot.
        
        Plugins should check that hasColor() returns `True` before
        calling this method.

        Returns
        - the map color that is set
        """
        ...


    def setColor(self, color: "Color") -> None:
        """
        Sets the map color. A custom map color will alter the display of the map
        in an inventory slot.

        Arguments
        - color: the color to set
        """
        ...


    def clone(self) -> "MapMeta":
        ...
