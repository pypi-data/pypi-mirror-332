"""
Python module generated from Java source file org.bukkit.map.MapPalette

Java source file obtained from artifact spigot-api version 1.20.4-R0.1-20240423.152506-123

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from org.bukkit.map import *
from typing import Any, Callable, Iterable, Tuple


class MapPalette:
    """
    Represents the palette that map items use.
    
    These fields are hee base color ranges. Each entry corresponds to four
    colors of varying shades with values entry to entry + 3.
    """

    TRANSPARENT = 0
    """
    Deprecated
    - Magic value
    """
    LIGHT_GREEN = 4
    """
    Deprecated
    - Magic value
    """
    LIGHT_BROWN = 8
    """
    Deprecated
    - Magic value
    """
    GRAY_1 = 12
    """
    Deprecated
    - Magic value
    """
    RED = 16
    """
    Deprecated
    - Magic value
    """
    PALE_BLUE = 20
    """
    Deprecated
    - Magic value
    """
    GRAY_2 = 24
    """
    Deprecated
    - Magic value
    """
    DARK_GREEN = 28
    """
    Deprecated
    - Magic value
    """
    WHITE = 32
    """
    Deprecated
    - Magic value
    """
    LIGHT_GRAY = 36
    """
    Deprecated
    - Magic value
    """
    BROWN = 40
    """
    Deprecated
    - Magic value
    """
    DARK_GRAY = 44
    """
    Deprecated
    - Magic value
    """
    BLUE = 48
    """
    Deprecated
    - Magic value
    """
    DARK_BROWN = 52
    """
    Deprecated
    - Magic value
    """


    @staticmethod
    def resizeImage(image: "Image") -> "BufferedImage":
        """
        Resize an image to 128x128.

        Arguments
        - image: The image to resize.

        Returns
        - The resized image.
        """
        ...


    @staticmethod
    def imageToBytes(image: "Image") -> list[int]:
        """
        Convert an Image to a byte[] using the palette.

        Arguments
        - image: The image to convert.

        Returns
        - A byte[] containing the pixels of the image.

        Deprecated
        - Magic value
        """
        ...


    @staticmethod
    def matchColor(r: int, g: int, b: int) -> int:
        """
        Get the index of the closest matching color in the palette to the given
        color.

        Arguments
        - r: The red component of the color.
        - b: The blue component of the color.
        - g: The green component of the color.

        Returns
        - The index in the palette.

        Deprecated
        - Magic value
        """
        ...


    @staticmethod
    def matchColor(color: "Color") -> int:
        """
        Get the index of the closest matching color in the palette to the given
        color.

        Arguments
        - color: The Color to match.

        Returns
        - The index in the palette.

        Deprecated
        - Magic value
        """
        ...


    @staticmethod
    def getColor(index: int) -> "Color":
        """
        Get the value of the given color in the palette.

        Arguments
        - index: The index in the palette.

        Returns
        - The Color of the palette entry.

        Deprecated
        - Magic value
        """
        ...


    @staticmethod
    def setMapColorCache(mapColorCache: "MapColorCache") -> None:
        """
        Sets the given MapColorCache.

        Arguments
        - mapColorCache: The map color cache to set
        """
        ...


    class MapColorCache:
        """
        Holds cached information for matching map colors of a given RBG color.
        """

        def isCached(self) -> bool:
            """
            Returns True if the MapColorCache has values cached, if not it will
            return False.
            A case where it might return False is when the cache is not build jet.

            Returns
            - True if this MapColorCache has values cached otherwise False
            """
            ...


        def matchColor(self, color: "Color") -> int:
            """
            Get the cached index of the closest matching color in the palette to the given
            color.

            Arguments
            - color: The Color to match.

            Returns
            - The index in the palette.

            Raises
            - IllegalStateException: if .isCached() returns False

            Deprecated
            - Magic value
            """
            ...
