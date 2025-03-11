"""
Python module generated from Java source file org.joml.RoundingMode

Java source file obtained from artifact joml version 1.10.8

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.joml import *
from typing import Any, Callable, Iterable, Tuple


class RoundingMode:
    """
    Rounding modes.

    Author(s)
    - Kai Burjack
    """

    TRUNCATE = 0
    """
    Discards the fractional part.
    """
    CEILING = 1
    """
    Round towards positive infinity.
    """
    FLOOR = 2
    """
    Round towards negative infinity.
    """
    HALF_EVEN = 3
    """
    Round towards the nearest neighbor. If both neighbors are equidistant, round
    towards the even neighbor.
    """
    HALF_DOWN = 4
    """
    Round towards the nearest neighbor. If both neighbors are equidistant, round
    down.
    """
    HALF_UP = 5
    """
    Round towards the nearest neighbor. If both neighbors are equidistant, round
    up.
    """
