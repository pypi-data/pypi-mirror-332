"""
Python module generated from Java source file org.bukkit.Input

Java source file obtained from artifact spigot-api version 1.21.2-R0.1-20241023.084343-5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import *
from typing import Any, Callable, Iterable, Tuple


class Input:
    """
    Represents a movement input applied to an entity.
    """

    def isForward(self) -> bool:
        """
        Gets whether a forward input is applied.

        Returns
        - forward input
        """
        ...


    def isBackward(self) -> bool:
        """
        Gets whether a backward input is applied.

        Returns
        - backward input
        """
        ...


    def isLeft(self) -> bool:
        """
        Gets whether a left input is applied.

        Returns
        - left input
        """
        ...


    def isRight(self) -> bool:
        """
        Gets whether a right input is applied.

        Returns
        - right input
        """
        ...


    def isJump(self) -> bool:
        """
        Gets whether a jump input is applied.

        Returns
        - jump input
        """
        ...


    def isSneak(self) -> bool:
        """
        Gets whether a sneak input is applied.

        Returns
        - sneak input
        """
        ...


    def isSprint(self) -> bool:
        """
        Gets whether a sprint input is applied.

        Returns
        - sprint input
        """
        ...
