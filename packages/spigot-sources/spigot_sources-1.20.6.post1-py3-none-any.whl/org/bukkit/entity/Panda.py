"""
Python module generated from Java source file org.bukkit.entity.Panda

Java source file obtained from artifact spigot-api version 1.20.6-R0.1-20240613.150924-57

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class Panda(Animals, Sittable):
    """
    Panda entity.
    """

    def getMainGene(self) -> "Gene":
        """
        Gets this Panda's main gene.

        Returns
        - main gene
        """
        ...


    def setMainGene(self, gene: "Gene") -> None:
        """
        Sets this Panda's main gene.

        Arguments
        - gene: main gene
        """
        ...


    def getHiddenGene(self) -> "Gene":
        """
        Gets this Panda's hidden gene.

        Returns
        - hidden gene
        """
        ...


    def setHiddenGene(self, gene: "Gene") -> None:
        """
        Sets this Panda's hidden gene.

        Arguments
        - gene: hidden gene
        """
        ...


    def isRolling(self) -> bool:
        """
        Gets whether the Panda is rolling

        Returns
        - Whether the Panda is rolling
        """
        ...


    def setRolling(self, flag: bool) -> None:
        """
        Sets whether the Panda is rolling

        Arguments
        - flag: Whether the Panda is rolling
        """
        ...


    def isSneezing(self) -> bool:
        """
        Gets whether the Panda is sneezing

        Returns
        - Whether the Panda is sneezing
        """
        ...


    def setSneezing(self, flag: bool) -> None:
        """
        Sets whether the Panda is sneezing

        Arguments
        - flag: Whether the Panda is sneezing
        """
        ...


    def isOnBack(self) -> bool:
        """
        Gets whether the Panda is on its back

        Returns
        - Whether the Panda is on its back
        """
        ...


    def setOnBack(self, flag: bool) -> None:
        """
        Sets whether the Panda is on its back

        Arguments
        - flag: Whether the Panda is on its back
        """
        ...


    def isEating(self) -> bool:
        """
        Gets whether the Panda is eating

        Returns
        - Whether the Panda is eating
        """
        ...


    def setEating(self, flag: bool) -> None:
        """
        Sets the Panda's eating status. The panda must be holding food for this to work

        Arguments
        - flag: Whether the Panda is eating
        """
        ...


    def isScared(self) -> bool:
        """
        Gets whether the Panda is scared

        Returns
        - Whether the Panda is scared
        """
        ...


    def getUnhappyTicks(self) -> int:
        """
        Gets how many ticks the panda will be unhappy for

        Returns
        - The number of ticks the panda will be unhappy for
        """
        ...


    class Gene(Enum):

        NORMAL = (False)
        LAZY = (False)
        WORRIED = (False)
        PLAYFUL = (False)
        BROWN = (True)
        WEAK = (True)
        AGGRESSIVE = (False)


        def isRecessive(self) -> bool:
            """
            Gets whether this gene is recessive, i.e. required in both parents to
            propagate to children.

            Returns
            - recessive status
            """
            ...
