"""
Python module generated from Java source file org.bukkit.metadata.MetadataStore

Java source file obtained from artifact spigot-api version 1.20.2-R0.1-20231205.164257-71

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.metadata import *
from org.bukkit.plugin import Plugin
from typing import Any, Callable, Iterable, Tuple


class MetadataStore:

    def setMetadata(self, subject: "T", metadataKey: str, newMetadataValue: "MetadataValue") -> None:
        """
        Adds a metadata value to an object.

        Arguments
        - subject: The object receiving the metadata.
        - metadataKey: A unique key to identify this metadata.
        - newMetadataValue: The metadata value to apply.

        Raises
        - IllegalArgumentException: If value is null, or the owning plugin
            is null
        """
        ...


    def getMetadata(self, subject: "T", metadataKey: str) -> list["MetadataValue"]:
        """
        Returns all metadata values attached to an object. If multiple plugins
        have attached metadata, each will value will be included.

        Arguments
        - subject: the object being interrogated.
        - metadataKey: the unique metadata key being sought.

        Returns
        - A list of values, one for each plugin that has set the
            requested value.
        """
        ...


    def hasMetadata(self, subject: "T", metadataKey: str) -> bool:
        """
        Tests to see if a metadata attribute has been set on an object.

        Arguments
        - subject: the object upon which the has-metadata test is
            performed.
        - metadataKey: the unique metadata key being queried.

        Returns
        - the existence of the metadataKey within subject.
        """
        ...


    def removeMetadata(self, subject: "T", metadataKey: str, owningPlugin: "Plugin") -> None:
        """
        Removes a metadata item owned by a plugin from a subject.

        Arguments
        - subject: the object to remove the metadata from.
        - metadataKey: the unique metadata key identifying the metadata to
            remove.
        - owningPlugin: the plugin attempting to remove a metadata item.

        Raises
        - IllegalArgumentException: If plugin is null
        """
        ...


    def invalidateAll(self, owningPlugin: "Plugin") -> None:
        """
        Invalidates all metadata in the metadata store that originates from the
        given plugin. Doing this will force each invalidated metadata item to
        be recalculated the next time it is accessed.

        Arguments
        - owningPlugin: the plugin requesting the invalidation.

        Raises
        - IllegalArgumentException: If plugin is null
        """
        ...
