"""
Python module generated from Java source file org.joml.sampling.Callback2d

Java source file obtained from artifact joml version 1.10.8

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.joml.sampling import *
from typing import Any, Callable, Iterable, Tuple


class Callback2d:
    """
    Callback used for notifying about a new generated 2D sample.

    Author(s)
    - Kai Burjack
    """

    def onNewSample(self, x: float, y: float) -> None:
        """
        Will be called whenever a new sample with the given coordinates `(x, y)` is generated.

        Arguments
        - x: the x coordinate of the new sample point
        - y: the y coordinate of the new sample point
        """
        ...
