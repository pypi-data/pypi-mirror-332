"""
Python module generated from Java source file org.bukkit.packs.DataPack

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

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

    See
    - <a href="https://minecraft.wiki/w/Data_pack">Minecraft wiki</a>
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
        Gets the pack format.
        
        Pack formats are non-standard and unrelated to the version of Minecraft. For
        a list of known pack versions, see the
        <a href="https://minecraft.wiki/w/Data_pack#Pack_format">Minecraft Wiki</a>.

        Returns
        - the pack version

        See
        - .getMaxSupportedPackFormat()
        """
        ...


    def getMinSupportedPackFormat(self) -> int:
        """
        Gets the minimum supported pack format. If the data pack does not specify a
        minimum supported format, .getPackFormat() is returned.
        
        Pack formats are non-standard and unrelated to the version of Minecraft. For
        a list of known pack versions, see the
        <a href="https://minecraft.wiki/w/Data_pack#Pack_format">Minecraft Wiki</a>.

        Returns
        - the min pack version supported
        """
        ...


    def getMaxSupportedPackFormat(self) -> int:
        """
        Gets the maximum supported pack format. If the data pack does not specify a
        maximum supported format, .getPackFormat() is returned.
        
        Pack formats are non-standard and unrelated to the version of Minecraft. For
        a list of known pack versions, see the
        <a href="https://minecraft.wiki/w/Data_pack#Pack_format">Minecraft Wiki</a>.

        Returns
        - the max pack version supported
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
