"""
Python module generated from Java source file org.bukkit.entity.Painting

Java source file obtained from artifact spigot-api version 1.17.1-R0.1-20211121.234319-104

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Art
from org.bukkit.entity import *
from org.bukkit.event.hanging import HangingBreakEvent
from typing import Any, Callable, Iterable, Tuple


class Painting(Hanging):
    """
    Represents a Painting.
    """

    def getArt(self) -> "Art":
        """
        Get the art on this painting

        Returns
        - The art
        """
        ...


    def setArt(self, art: "Art") -> bool:
        """
        Set the art on this painting

        Arguments
        - art: The new art

        Returns
        - False if the new art won't fit at the painting's current
            location
        """
        ...


    def setArt(self, art: "Art", force: bool) -> bool:
        """
        Set the art on this painting

        Arguments
        - art: The new art
        - force: If True, force the new art regardless of whether it fits
            at the current location. Note that forcing it where it can't fit
            normally causes it to drop as an item unless you override this by
            catching the HangingBreakEvent.

        Returns
        - False if force was False and the new art won't fit at the
            painting's current location
        """
        ...
