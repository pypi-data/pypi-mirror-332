"""
Python module generated from Java source file org.bukkit.metadata.LazyMetadataValue

Java source file obtained from artifact spigot-api version 1.17.1-R0.1-20211121.234319-104

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from java.lang.ref import SoftReference
from java.util.concurrent import Callable
from org.apache.commons.lang import Validate
from org.bukkit.metadata import *
from org.bukkit.plugin import Plugin
from typing import Any, Callable, Iterable, Tuple


class LazyMetadataValue(MetadataValueAdapter):
    """
    The LazyMetadataValue class implements a type of metadata that is not
    computed until another plugin asks for it.
    
    By making metadata values lazy, no computation is done by the providing
    plugin until absolutely necessary (if ever). Additionally,
    LazyMetadataValue objects cache their values internally unless overridden
    by a CacheStrategy or invalidated at the individual or plugin
    level. Once invalidated, the LazyMetadataValue will recompute its value
    when asked.
    """

    def __init__(self, owningPlugin: "Plugin", lazyValue: "Callable"["Object"]):
        """
        Initialized a LazyMetadataValue object with the default
        CACHE_AFTER_FIRST_EVAL cache strategy.

        Arguments
        - owningPlugin: the Plugin that created this metadata
            value.
        - lazyValue: the lazy value assigned to this metadata value.
        """
        ...


    def __init__(self, owningPlugin: "Plugin", cacheStrategy: "CacheStrategy", lazyValue: "Callable"["Object"]):
        """
        Initializes a LazyMetadataValue object with a specific cache strategy.

        Arguments
        - owningPlugin: the Plugin that created this metadata
            value.
        - cacheStrategy: determines the rules for caching this metadata
            value.
        - lazyValue: the lazy value assigned to this metadata value.
        """
        ...


    def value(self) -> "Object":
        ...


    def invalidate(self) -> None:
        ...


    class CacheStrategy(Enum):
        """
        Describes possible caching strategies for metadata.
        """

        CACHE_AFTER_FIRST_EVAL = 0
        """
        Once the metadata value has been evaluated, do not re-evaluate the
        value until it is manually invalidated.
        """
        NEVER_CACHE = 1
        """
        Re-evaluate the metadata item every time it is requested
        """
        CACHE_ETERNALLY = 2
        """
        Once the metadata value has been evaluated, do not re-evaluate the
        value in spite of manual invalidation.
        """
