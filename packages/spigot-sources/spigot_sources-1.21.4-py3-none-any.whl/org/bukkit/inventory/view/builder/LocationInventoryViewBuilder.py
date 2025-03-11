"""
Python module generated from Java source file org.bukkit.inventory.view.builder.LocationInventoryViewBuilder

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Location
from org.bukkit.inventory import InventoryView
from org.bukkit.inventory.view.builder import *
from typing import Any, Callable, Iterable, Tuple


class LocationInventoryViewBuilder(InventoryViewBuilder):
    """
    An InventoryViewBuilder that can be bound by location within the world
    
    Type `<V>`: the type of InventoryView created from this builder
    """

    def copy(self) -> "LocationInventoryViewBuilder"["V"]:
        ...


    def title(self, title: str) -> "LocationInventoryViewBuilder"["V"]:
        ...


    def checkReachable(self, checkReachable: bool) -> "LocationInventoryViewBuilder"["V"]:
        """
        Determines whether or not the server should check if the player can reach
        the location.
        
        Not providing a location but setting checkReachable to True will
        automatically close the view when opened.
        
        If checkReachable is set to False and a location is set on the builder if
        the target block exists and this builder is the correct menu for that
        block, e.g. MenuType.GENERIC_9X3 builder and target block set to chest,
        if that block is destroyed the view would persist.

        Arguments
        - checkReachable: whether or not to check if the view is "reachable"

        Returns
        - this builder
        """
        ...


    def location(self, location: "Location") -> "LocationInventoryViewBuilder"["V"]:
        """
        Binds a location to this builder.
        
        By binding a location in an unloaded chunk to this builder it is likely
        that the given chunk the location is will load. That means that when,
        building this view it may come with the costs associated with chunk
        loading.
        
        Providing a location of a tile entity with a non matching menu comes with
        extra costs associated with ensuring that the correct view is created.

        Arguments
        - location: the location to bind to this view

        Returns
        - this builder
        """
        ...
