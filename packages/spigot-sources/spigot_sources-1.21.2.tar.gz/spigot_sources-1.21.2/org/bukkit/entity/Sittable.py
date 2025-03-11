"""
Python module generated from Java source file org.bukkit.entity.Sittable

Java source file obtained from artifact spigot-api version 1.21.2-R0.1-20241023.084343-5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class Sittable:
    """
    An animal that can sit still.
    """

    def isSitting(self) -> bool:
        """
        Checks if this animal is sitting

        Returns
        - True if sitting
        """
        ...


    def setSitting(self, sitting: bool) -> None:
        """
        Sets if this animal is sitting. Will remove any path that the animal
        was following beforehand.

        Arguments
        - sitting: True if sitting
        """
        ...
