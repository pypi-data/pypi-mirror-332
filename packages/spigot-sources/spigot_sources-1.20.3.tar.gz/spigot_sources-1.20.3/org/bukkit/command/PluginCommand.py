"""
Python module generated from Java source file org.bukkit.command.PluginCommand

Java source file obtained from artifact spigot-api version 1.20.3-R0.1-20231207.085553-9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from org.bukkit.command import *
from org.bukkit.plugin import Plugin
from typing import Any, Callable, Iterable, Tuple


class PluginCommand(Command, PluginIdentifiableCommand):
    """
    Represents a Command belonging to a plugin
    """

    def execute(self, sender: "CommandSender", commandLabel: str, args: list[str]) -> bool:
        """
        Executes the command, returning its success

        Arguments
        - sender: Source object which is executing this command
        - commandLabel: The alias of the command used
        - args: All arguments passed to the command, split via ' '

        Returns
        - True if the command was successful, otherwise False
        """
        ...


    def setExecutor(self, executor: "CommandExecutor") -> None:
        """
        Sets the CommandExecutor to run when parsing this command

        Arguments
        - executor: New executor to run
        """
        ...


    def getExecutor(self) -> "CommandExecutor":
        """
        Gets the CommandExecutor associated with this command

        Returns
        - CommandExecutor object linked to this command
        """
        ...


    def setTabCompleter(self, completer: "TabCompleter") -> None:
        """
        Sets the TabCompleter to run when tab-completing this command.
        
        If no TabCompleter is specified, and the command's executor implements
        TabCompleter, then the executor will be used for tab completion.

        Arguments
        - completer: New tab completer
        """
        ...


    def getTabCompleter(self) -> "TabCompleter":
        """
        Gets the TabCompleter associated with this command.

        Returns
        - TabCompleter object linked to this command
        """
        ...


    def getPlugin(self) -> "Plugin":
        """
        Gets the owner of this PluginCommand

        Returns
        - Plugin that owns this command
        """
        ...


    def tabComplete(self, sender: "CommandSender", alias: str, args: list[str]) -> "java.util.List"[str]:
        """
        
        
        Delegates to the tab completer if present.
        
        If it is not present or returns null, will delegate to the current
        command executor if it implements TabCompleter. If a non-null
        list has not been found, will default to standard player name
        completion in Command.tabComplete(CommandSender, String, String[]).
        
        This method does not consider permissions.

        Raises
        - CommandException: if the completer or executor throw an
            exception during the process of tab-completing.
        - IllegalArgumentException: if sender, alias, or args is null
        """
        ...


    def toString(self) -> str:
        ...
