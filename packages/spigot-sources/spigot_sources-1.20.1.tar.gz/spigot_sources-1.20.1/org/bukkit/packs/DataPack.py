"""
Python module generated from Java source file org.bukkit.packs.DataPack

Java source file obtained from artifact spigot-api version 1.20.1-R0.1-20230921.163938-66

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit import FeatureFlag
from org.bukkit import Keyed
from org.bukkit.packs import *
from typing import Any, Callable, Iterable, Tuple


class DataPack(Keyed):
    """
    Represents a data pack.
    """

    def getTitle(self) -> str:
        """
        Gets the title of the data pack.

        Returns
        - the title
        """
        ...


    def getDescription(self) -> str:
        """
        Gets the description of the data pack.

        Returns
        - the description
        """
        ...


    def getPackFormat(self) -> int:
        """
        Gets the pack version.
        
        This is related to the server version to work.

        Returns
        - the pack version
        """
        ...


    def isEnabled(self) -> bool:
        """
        Gets if the data pack is enabled on the server.

        Returns
        - True if is enabled
        """
        ...


    def isRequired(self) -> bool:
        """
        Gets if the data pack is required on the server.

        Returns
        - True if is required
        """
        ...


    def getCompatibility(self) -> "Compatibility":
        """
        Gets the compatibility of this data pack with the server.

        Returns
        - an enum
        """
        ...


    def getRequestedFeatures(self) -> set["FeatureFlag"]:
        """
        Gets a set of features requested by this data pack.

        Returns
        - a set of features
        """
        ...


    def getSource(self) -> "Source":
        """
        Gets the source of this data pack.

        Returns
        - the source
        """
        ...


    class Compatibility(Enum):
        """
        Show the compatibility of the data pack with the server.
        """

        NEW = 0
        """
        It's newer than the server pack version.
        """
        OLD = 1
        """
        It's older than the server pack version.
        """
        COMPATIBLE = 2
        """
        Its compatible with the server pack version.
        """


    class Source(Enum):
        """
        Represent the source of a data pack.
        """

        DEFAULT = 0
        BUILT_IN = 1
        FEATURE = 2
        WORLD = 3
        SERVER = 4
