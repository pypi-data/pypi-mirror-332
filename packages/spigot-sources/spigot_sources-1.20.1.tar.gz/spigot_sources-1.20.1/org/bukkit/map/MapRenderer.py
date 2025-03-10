"""
Python module generated from Java source file org.bukkit.map.MapRenderer

Java source file obtained from artifact spigot-api version 1.20.1-R0.1-20230921.163938-66

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import Player
from org.bukkit.map import *
from typing import Any, Callable, Iterable, Tuple


class MapRenderer:
    """
    Represents a renderer for a map.
    """

    def __init__(self):
        """
        Initialize the map renderer base to be non-contextual. See .isContextual().
        """
        ...


    def __init__(self, contextual: bool):
        """
        Initialize the map renderer base with the given contextual status.

        Arguments
        - contextual: Whether the renderer is contextual. See .isContextual().
        """
        ...


    def isContextual(self) -> bool:
        """
        Get whether the renderer is contextual, i.e. has different canvases for
        different players.

        Returns
        - True if contextual, False otherwise.
        """
        ...


    def initialize(self, map: "MapView") -> None:
        """
        Initialize this MapRenderer for the given map.

        Arguments
        - map: The MapView being initialized.
        """
        ...


    def render(self, map: "MapView", canvas: "MapCanvas", player: "Player") -> None:
        """
        Render to the given map.

        Arguments
        - map: The MapView being rendered to.
        - canvas: The canvas to use for rendering.
        - player: The player who triggered the rendering.
        """
        ...
