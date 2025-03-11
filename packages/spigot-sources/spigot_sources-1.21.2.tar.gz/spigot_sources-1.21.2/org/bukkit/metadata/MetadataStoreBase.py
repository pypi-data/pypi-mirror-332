"""
Python module generated from Java source file org.bukkit.metadata.MetadataStoreBase

Java source file obtained from artifact spigot-api version 1.21.2-R0.1-20241023.084343-5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from java.util import Collections
from java.util import WeakHashMap
from org.bukkit.metadata import *
from org.bukkit.plugin import Plugin
from typing import Any, Callable, Iterable, Tuple


class MetadataStoreBase:

    def setMetadata(self, subject: "T", metadataKey: str, newMetadataValue: "MetadataValue") -> None:
        """
        Adds a metadata value to an object. Each metadata value is owned by a
        specific Plugin. If a plugin has already added a metadata value
        to an object, that value will be replaced with the value of `newMetadataValue`. Multiple plugins can set independent values for the
        same `metadataKey` without conflict.
        
        Implementation note: I considered using a java.util.concurrent.locks.ReadWriteLock for controlling access to
        `metadataMap`, but decided that the added overhead wasn't worth
        the finer grained access control.
        
        Bukkit is almost entirely single threaded so locking overhead shouldn't
        pose a problem.

        Arguments
        - subject: The object receiving the metadata.
        - metadataKey: A unique key to identify this metadata.
        - newMetadataValue: The metadata value to apply.

        Raises
        - IllegalArgumentException: If value is null, or the owning plugin
            is null

        See
        - MetadataStore.setMetadata(Object, String, MetadataValue)
        """
        ...


    def getMetadata(self, subject: "T", metadataKey: str) -> list["MetadataValue"]:
        """
        Returns all metadata values attached to an object. If multiple
        have attached metadata, each will value will be included.

        Arguments
        - subject: the object being interrogated.
        - metadataKey: the unique metadata key being sought.

        Returns
        - A list of values, one for each plugin that has set the
            requested value.

        See
        - MetadataStore.getMetadata(Object, String)
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

        See
        - MetadataStore.removeMetadata(Object, String,
            org.bukkit.plugin.Plugin)
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

        See
        - MetadataStore.invalidateAll(org.bukkit.plugin.Plugin)
        """
        ...
