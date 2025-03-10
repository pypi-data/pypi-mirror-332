"""
Python module generated from Java source file org.bukkit.help.HelpMap

Java source file obtained from artifact spigot-api version 1.19.4-R0.1-20230607.155743-88

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.help import *
from typing import Any, Callable, Iterable, Tuple


class HelpMap:
    """
    The HelpMap tracks all help topics registered in a Bukkit server. When the
    server starts up or is reloaded, help is processed and topics are added in
    the following order:
    
    <ol>
    - General topics are loaded from the help.yml
    - Plugins load and optionally call `addTopic()`
    - Registered plugin commands are processed by HelpTopicFactory
        objects to create topics
    - Topic contents are amended as directed in help.yml
    </ol>
    """

    def getHelpTopic(self, topicName: str) -> "HelpTopic":
        """
        Returns a help topic for a given topic name.

        Arguments
        - topicName: The help topic name to look up.

        Returns
        - A HelpTopic object matching the topic name or null if
            none can be found.
        """
        ...


    def getHelpTopics(self) -> Iterable["HelpTopic"]:
        """
        Returns a collection of all the registered help topics.

        Returns
        - All the registered help topics.
        """
        ...


    def addTopic(self, topic: "HelpTopic") -> None:
        """
        Adds a topic to the server's help index.

        Arguments
        - topic: The new help topic to add.
        """
        ...


    def clear(self) -> None:
        """
        Clears out the contents of the help index. Normally called during
        server reload.
        """
        ...


    def registerHelpTopicFactory(self, commandClass: type[Any], factory: "HelpTopicFactory"[Any]) -> None:
        """
        Associates a HelpTopicFactory object with given command base
        class. Plugins typically call this method during `onLoad()`. Once
        registered, the custom HelpTopicFactory will be used to create a custom
        HelpTopic for all commands deriving from the `commandClass` base class, or all commands deriving from org.bukkit.command.PluginCommand who's executor derives from `commandClass` base class.

        Arguments
        - commandClass: The class for which the custom HelpTopicFactory
            applies. Must derive from either org.bukkit.command.Command
            or org.bukkit.command.CommandExecutor.
        - factory: The HelpTopicFactory implementation to associate
            with the `commandClass`.

        Raises
        - IllegalArgumentException: Thrown if `commandClass` does
            not derive from a legal base class.
        """
        ...


    def getIgnoredPlugins(self) -> list[str]:
        """
        Gets the list of plugins the server administrator has chosen to exclude
        from the help index. Plugin authors who choose to directly extend
        org.bukkit.command.Command instead of org.bukkit.command.PluginCommand will need to check this collection in
        their HelpTopicFactory implementations to ensure they meet the
        server administrator's expectations.

        Returns
        - A list of plugins that should be excluded from the help index.
        """
        ...
