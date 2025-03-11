"""
Python module generated from Java source file org.bukkit.block.data.type.Candle

Java source file obtained from artifact spigot-api version 1.21.1-R0.1-20241022.152140-54

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block.data import Lightable
from org.bukkit.block.data import Waterlogged
from org.bukkit.block.data.type import *
from typing import Any, Callable, Iterable, Tuple


class Candle(Lightable, Waterlogged):
    """
    'candles' represents the number of candles which are present.
    """

    def getCandles(self) -> int:
        """
        Gets the value of the 'candles' property.

        Returns
        - the 'candles' value
        """
        ...


    def setCandles(self, candles: int) -> None:
        """
        Sets the value of the 'candles' property.

        Arguments
        - candles: the new 'candles' value
        """
        ...


    def getMaximumCandles(self) -> int:
        """
        Gets the maximum allowed value of the 'candles' property.

        Returns
        - the maximum 'candles' value
        """
        ...
