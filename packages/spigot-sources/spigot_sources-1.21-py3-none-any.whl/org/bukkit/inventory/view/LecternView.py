"""
Python module generated from Java source file org.bukkit.inventory.view.LecternView

Java source file obtained from artifact spigot-api version 1.21-R0.1-20240807.214924-87

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.inventory import InventoryView
from org.bukkit.inventory.view import *
from typing import Any, Callable, Iterable, Tuple


class LecternView(InventoryView):
    """
    An instance of InventoryView which provides extra methods related to
    lectern view data.
    """

    def getPage(self) -> int:
        """
        Gets the page that the LecternView is on.

        Returns
        - The page the book is on
        """
        ...


    def setPage(self, page: int) -> None:
        """
        Sets the page of the lectern book.

        Arguments
        - page: the lectern book page
        """
        ...
