"""
Python module generated from Java source file org.bukkit.command.CommandMap

Java source file obtained from artifact spigot-api version 1.17.1-R0.1-20211121.234319-104

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Location
from org.bukkit.command import *
from typing import Any, Callable, Iterable, Tuple


class CommandMap:

    def registerAll(self, fallbackPrefix: str, commands: list["Command"]) -> None:
        """
        Registers all the commands belonging to a certain plugin.
        
        Caller can use:-
        
        - command.getName() to determine the label registered for this
            command
        - command.getAliases() to determine the aliases which where
            registered

        Arguments
        - fallbackPrefix: a prefix which is prepended to each command with
            a ':' one or more times to make the command unique
        - commands: a list of commands to register
        """
        ...


    def register(self, label: str, fallbackPrefix: str, command: "Command") -> bool:
        """
        Registers a command. Returns True on success; False if name is already
        taken and fallback had to be used.
        
        Caller can use:-
        
        - command.getName() to determine the label registered for this
            command
        - command.getAliases() to determine the aliases which where
            registered

        Arguments
        - label: the label of the command, without the '/'-prefix.
        - fallbackPrefix: a prefix which is prepended to the command with a
            ':' one or more times to make the command unique
        - command: the command to register

        Returns
        - True if command was registered with the passed in label, False
            otherwise, which indicates the fallbackPrefix was used one or more
            times
        """
        ...


    def register(self, fallbackPrefix: str, command: "Command") -> bool:
        """
        Registers a command. Returns True on success; False if name is already
        taken and fallback had to be used.
        
        Caller can use:-
        
        - command.getName() to determine the label registered for this
            command
        - command.getAliases() to determine the aliases which where
            registered

        Arguments
        - fallbackPrefix: a prefix which is prepended to the command with a
            ':' one or more times to make the command unique
        - command: the command to register, from which label is determined
            from the command name

        Returns
        - True if command was registered with the passed in label, False
            otherwise, which indicates the fallbackPrefix was used one or more
            times
        """
        ...


    def dispatch(self, sender: "CommandSender", cmdLine: str) -> bool:
        """
        Looks for the requested command and executes it if found.

        Arguments
        - sender: The command's sender
        - cmdLine: command + arguments. Example: "/test abc 123"

        Returns
        - returns False if no target is found, True otherwise.

        Raises
        - CommandException: Thrown when the executor for the given command
            fails with an unhandled exception
        """
        ...


    def clearCommands(self) -> None:
        """
        Clears all registered commands.
        """
        ...


    def getCommand(self, name: str) -> "Command":
        """
        Gets the command registered to the specified name

        Arguments
        - name: Name of the command to retrieve

        Returns
        - Command with the specified name or null if a command with that
            label doesn't exist
        """
        ...


    def tabComplete(self, sender: "CommandSender", cmdLine: str) -> list[str]:
        """
        Looks for the requested command and executes an appropriate
        tab-completer if found. This method will also tab-complete partial
        commands.

        Arguments
        - sender: The command's sender.
        - cmdLine: The entire command string to tab-complete, excluding
            initial slash.

        Returns
        - a list of possible tab-completions. This list may be immutable.
            Will be null if no matching command of which sender has permission.

        Raises
        - CommandException: Thrown when the tab-completer for the given
            command fails with an unhandled exception
        - IllegalArgumentException: if either sender or cmdLine are null
        """
        ...


    def tabComplete(self, sender: "CommandSender", cmdLine: str, location: "Location") -> list[str]:
        """
        Looks for the requested command and executes an appropriate
        tab-completer if found. This method will also tab-complete partial
        commands.

        Arguments
        - sender: The command's sender.
        - cmdLine: The entire command string to tab-complete, excluding
            initial slash.
        - location: The position looked at by the sender, or null if none

        Returns
        - a list of possible tab-completions. This list may be immutable.
            Will be null if no matching command of which sender has permission.

        Raises
        - CommandException: Thrown when the tab-completer for the given
            command fails with an unhandled exception
        - IllegalArgumentException: if either sender or cmdLine are null
        """
        ...
