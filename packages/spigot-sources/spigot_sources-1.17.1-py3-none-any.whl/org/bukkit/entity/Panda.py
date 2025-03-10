"""
Python module generated from Java source file org.bukkit.entity.Panda

Java source file obtained from artifact spigot-api version 1.17.1-R0.1-20211121.234319-104

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class Panda(Animals):
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
