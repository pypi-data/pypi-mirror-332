"""
Python module generated from Java source file org.bukkit.block.data.BlockData

Java source file obtained from artifact spigot-api version 1.16.5-R0.1-20210611.041013-99

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Material
from org.bukkit import Server
from org.bukkit import SoundGroup
from org.bukkit.block.data import *
from typing import Any, Callable, Iterable, Tuple


class BlockData(Cloneable):

    def getMaterial(self) -> "Material":
        """
        Get the Material represented by this block data.

        Returns
        - the material
        """
        ...


    def getAsString(self) -> str:
        """
        Gets a string, which when passed into a method such as
        Server.createBlockData(java.lang.String) will unambiguously
        recreate this instance.

        Returns
        - serialized data string for this block
        """
        ...


    def getAsString(self, hideUnspecified: bool) -> str:
        """
        Gets a string, which when passed into a method such as
        Server.createBlockData(java.lang.String) will recreate this or a
        similar instance where unspecified states (if any) may be optionally
        omitted. If this instance was parsed and states are omitted, this exact
        instance will be creatable when parsed again, else their equality cannot
        be guaranteed.
        
        This method will only take effect for BlockData instances created by
        methods such as Server.createBlockData(String) or any similar
        method whereby states are optionally defined. If otherwise, the result of
        .getAsString() will be returned. The following behaviour would be
        expected:
        ````String dataString = "minecraft:chest[waterlogged=True]"
        BlockData data = Bukkit.createBlockData(dataString);
        dataString.equals(data.getAsString(True)); // This would return True
        dataString.equals(data.getAsString(False)); // This would return False as all states are present
        dataString.equals(data.getAsString()); // This is equivalent to the above, "getAsString(False)"````

        Arguments
        - hideUnspecified: True if unspecified states should be omitted,
        False if they are to be shown as performed by .getAsString().

        Returns
        - serialized data string for this block
        """
        ...


    def merge(self, data: "BlockData") -> "BlockData":
        """
        Merges all explicitly set states from the given data with this BlockData.
        
        Note that the given data MUST have been created from one of the String
        parse methods, e.g. Server.createBlockData(java.lang.String) and
        not have been subsequently modified.
        
        Note also that the block types must match identically.

        Arguments
        - data: the data to merge from

        Returns
        - a new instance of this blockdata with the merged data
        """
        ...


    def matches(self, data: "BlockData") -> bool:
        """
        Checks if the specified BlockData matches this block data.
        
        The semantics of this method are such that for manually created or
        modified BlockData it has the same effect as
        Object.equals(java.lang.Object), whilst for parsed data (that to
        which .merge(org.bukkit.block.data.BlockData) applies, it will
        return True when the type and all explicitly set states match.
        
        **Note that these semantics mean that a.matches(b) may not be the same
        as b.matches(a)**

        Arguments
        - data: the data to match against (normally a parsed constant)

        Returns
        - if there is a match
        """
        ...


    def clone(self) -> "BlockData":
        """
        Returns a copy of this BlockData.

        Returns
        - a copy of the block data
        """
        ...


    def getSoundGroup(self) -> "SoundGroup":
        """
        Gets the block's SoundGroup which can be used to get its step
        sound, hit sound, and others.

        Returns
        - the sound effect group
        """
        ...
