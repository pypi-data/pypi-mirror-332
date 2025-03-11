"""
Python module generated from Java source file org.bukkit.inventory.view.builder.InventoryViewBuilder

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import HumanEntity
from org.bukkit.inventory import InventoryView
from org.bukkit.inventory.view.builder import *
from typing import Any, Callable, Iterable, Tuple


class InventoryViewBuilder:
    """
    Generic Builder for InventoryView's with no special attributes or parameters
    
    Type `<V>`: the type of InventoryView created from this builder
    """

    def copy(self) -> "InventoryViewBuilder"["V"]:
        """
        Makes a copy of this builder

        Returns
        - a copy of this builder
        """
        ...


    def title(self, title: str) -> "InventoryViewBuilder"["V"]:
        """
        Sets the title of the builder

        Arguments
        - title: the title

        Returns
        - this builder
        """
        ...


    def build(self, player: "HumanEntity") -> "V":
        """
        Builds this builder into a InventoryView

        Arguments
        - player: the player to assign to the view

        Returns
        - the created InventoryView
        """
        ...
