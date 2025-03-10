"""
Python module generated from Java source file org.bukkit.metadata.Metadatable

Java source file obtained from artifact spigot-api version 1.16.5-R0.1-20210611.041013-99

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.metadata import *
from org.bukkit.plugin import Plugin
from typing import Any, Callable, Iterable, Tuple


class Metadatable:
    """
    This interface is implemented by all objects that can provide metadata
    about themselves.
    """

    def setMetadata(self, metadataKey: str, newMetadataValue: "MetadataValue") -> None:
        """
        Sets a metadata value in the implementing object's metadata store.

        Arguments
        - metadataKey: A unique key to identify this metadata.
        - newMetadataValue: The metadata value to apply.

        Raises
        - IllegalArgumentException: If value is null, or the owning plugin
            is null
        """
        ...


    def getMetadata(self, metadataKey: str) -> list["MetadataValue"]:
        """
        Returns a list of previously set metadata values from the implementing
        object's metadata store.

        Arguments
        - metadataKey: the unique metadata key being sought.

        Returns
        - A list of values, one for each plugin that has set the
            requested value.
        """
        ...


    def hasMetadata(self, metadataKey: str) -> bool:
        """
        Tests to see whether the implementing object contains the given
        metadata value in its metadata store.

        Arguments
        - metadataKey: the unique metadata key being queried.

        Returns
        - the existence of the metadataKey within subject.
        """
        ...


    def removeMetadata(self, metadataKey: str, owningPlugin: "Plugin") -> None:
        """
        Removes the given metadata value from the implementing object's
        metadata store.

        Arguments
        - metadataKey: the unique metadata key identifying the metadata to
            remove.
        - owningPlugin: This plugin's metadata value will be removed. All
            other values will be left untouched.

        Raises
        - IllegalArgumentException: If plugin is null
        """
        ...
