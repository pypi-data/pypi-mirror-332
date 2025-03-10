"""
Python module generated from Java source file org.bukkit.map.MapCanvas

Java source file obtained from artifact spigot-api version 1.20.4-R0.1-20240423.152506-123

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.map import *
from typing import Any, Callable, Iterable, Tuple


class MapCanvas:
    """
    Represents a canvas for drawing to a map. Each canvas is associated with a
    specific MapRenderer and represents that renderer's layer on the
    map.
    """

    def getMapView(self) -> "MapView":
        """
        Get the map this canvas is attached to.

        Returns
        - The MapView this canvas is attached to.
        """
        ...


    def getCursors(self) -> "MapCursorCollection":
        """
        Get the cursor collection associated with this canvas.

        Returns
        - The MapCursorCollection associated with this canvas.
        """
        ...


    def setCursors(self, cursors: "MapCursorCollection") -> None:
        """
        Set the cursor collection associated with this canvas. This does not
        usually need to be called since a MapCursorCollection is already
        provided.

        Arguments
        - cursors: The MapCursorCollection to associate with this canvas.
        """
        ...


    def setPixelColor(self, x: int, y: int, color: "Color") -> None:
        """
        Draw a pixel to the canvas.
        
        The provided color might be converted to another color,
        which is in the map color range. This means, that
        .getPixelColor(int, int) might return another
        color than set.
        
        If null is used as color, then the color returned by
        .getBasePixelColor(int, int) is shown on the map.

        Arguments
        - x: The x coordinate, from 0 to 127.
        - y: The y coordinate, from 0 to 127.
        - color: The color.
        """
        ...


    def getPixelColor(self, x: int, y: int) -> "Color":
        """
        Get a pixel from the canvas.
        
        If no color is set at the given position for this canvas, then null is
        returned and the color returned by .getBasePixelColor(int, int)
        is shown on the map.

        Arguments
        - x: The x coordinate, from 0 to 127.
        - y: The y coordinate, from 0 to 127.

        Returns
        - The color, or null if no color is set.
        """
        ...


    def getBasePixelColor(self, x: int, y: int) -> "Color":
        """
        Get a pixel from the layers below this canvas.

        Arguments
        - x: The x coordinate, from 0 to 127.
        - y: The y coordinate, from 0 to 127.

        Returns
        - The color.
        """
        ...


    def setPixel(self, x: int, y: int, color: int) -> None:
        """
        Draw a pixel to the canvas.

        Arguments
        - x: The x coordinate, from 0 to 127.
        - y: The y coordinate, from 0 to 127.
        - color: The color. See MapPalette.

        Deprecated
        - Magic value, use .setPixelColor(int, int, Color)
        """
        ...


    def getPixel(self, x: int, y: int) -> int:
        """
        Get a pixel from the canvas.

        Arguments
        - x: The x coordinate, from 0 to 127.
        - y: The y coordinate, from 0 to 127.

        Returns
        - The color. See MapPalette.

        Deprecated
        - Magic value, use .getPixelColor(int, int)
        """
        ...


    def getBasePixel(self, x: int, y: int) -> int:
        """
        Get a pixel from the layers below this canvas.

        Arguments
        - x: The x coordinate, from 0 to 127.
        - y: The y coordinate, from 0 to 127.

        Returns
        - The color. See MapPalette.

        Deprecated
        - Magic value, use .getBasePixelColor(int, int)
        """
        ...


    def drawImage(self, x: int, y: int, image: "Image") -> None:
        """
        Draw an image to the map. The image will be clipped if necessary.

        Arguments
        - x: The x coordinate of the image.
        - y: The y coordinate of the image.
        - image: The Image to draw.
        """
        ...


    def drawText(self, x: int, y: int, font: "MapFont", text: str) -> None:
        """
        Render text to the map using fancy formatting. Newline (\n) characters
        will move down one line and return to the original column, and the text
        color can be changed using sequences such as "§12;", replacing 12 with
        the palette index of the color (see MapPalette).

        Arguments
        - x: The column to start rendering on.
        - y: The row to start rendering on.
        - font: The font to use.
        - text: The formatted text to render.
        """
        ...
