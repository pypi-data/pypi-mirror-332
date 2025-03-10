"""
Python module generated from Java source file org.bukkit.command.PluginIdentifiableCommand

Java source file obtained from artifact spigot-api version 1.20.1-R0.1-20230921.163938-66

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.command import *
from org.bukkit.plugin import Plugin
from typing import Any, Callable, Iterable, Tuple


class PluginIdentifiableCommand:
    """
    This interface is used by the help system to group commands into
    sub-indexes based on the Plugin they are a part of. Custom command
    implementations will need to implement this interface to have a sub-index
    automatically generated on the plugin's behalf.
    """

    def getPlugin(self) -> "Plugin":
        """
        Gets the owner of this PluginIdentifiableCommand.

        Returns
        - Plugin that owns this PluginIdentifiableCommand.
        """
        ...
