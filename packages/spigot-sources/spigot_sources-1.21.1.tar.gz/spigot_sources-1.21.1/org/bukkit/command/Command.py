"""
Python module generated from Java source file org.bukkit.command.Command

Java source file obtained from artifact spigot-api version 1.21.1-R0.1-20241022.152140-54

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from com.google.common.collect import ImmutableList
from java.util import Collections
from org.bukkit import Bukkit
from org.bukkit import ChatColor
from org.bukkit import GameRule
from org.bukkit import Location
from org.bukkit import Server
from org.bukkit.command import *
from org.bukkit.entity import Player
from org.bukkit.entity.minecart import CommandMinecart
from org.bukkit.permissions import Permissible
from org.bukkit.plugin import PluginDescriptionFile
from org.bukkit.util import StringUtil
from typing import Any, Callable, Iterable, Tuple


class Command:
    """
    Represents a Command, which executes various tasks upon user input
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


    def tabComplete(self, sender: "CommandSender", alias: str, args: list[str]) -> list[str]:
        """
        Executed on tab completion for this command, returning a list of
        options the player can tab through.

        Arguments
        - sender: Source object which is executing this command
        - alias: the alias being used
        - args: All arguments passed to the command, split via ' '

        Returns
        - a list of tab-completions for the specified arguments. This
            will never be null. List may be immutable.

        Raises
        - IllegalArgumentException: if sender, alias, or args is null
        """
        ...


    def tabComplete(self, sender: "CommandSender", alias: str, args: list[str], location: "Location") -> list[str]:
        """
        Executed on tab completion for this command, returning a list of
        options the player can tab through.

        Arguments
        - sender: Source object which is executing this command
        - alias: the alias being used
        - args: All arguments passed to the command, split via ' '
        - location: The position looked at by the sender, or null if none

        Returns
        - a list of tab-completions for the specified arguments. This
            will never be null. List may be immutable.

        Raises
        - IllegalArgumentException: if sender, alias, or args is null
        """
        ...


    def getName(self) -> str:
        """
        Returns the name of this command

        Returns
        - Name of this command
        """
        ...


    def setName(self, name: str) -> bool:
        """
        Sets the name of this command.
        
        May only be used before registering the command.
        Will return True if the new name is set, and False
        if the command has already been registered.

        Arguments
        - name: New command name

        Returns
        - returns True if the name change happened instantly or False if
            the command was already registered
        """
        ...


    def getPermission(self) -> str:
        """
        Gets the permission required by users to be able to perform this
        command

        Returns
        - Permission name, or null if none
        """
        ...


    def setPermission(self, permission: str) -> None:
        """
        Sets the permission required by users to be able to perform this
        command

        Arguments
        - permission: Permission name or null
        """
        ...


    def testPermission(self, target: "CommandSender") -> bool:
        """
        Tests the given CommandSender to see if they can perform this
        command.
        
        If they do not have permission, they will be informed that they cannot
        do this.

        Arguments
        - target: User to test

        Returns
        - True if they can use it, otherwise False
        """
        ...


    def testPermissionSilent(self, target: "CommandSender") -> bool:
        """
        Tests the given CommandSender to see if they can perform this
        command.
        
        No error is sent to the sender.

        Arguments
        - target: User to test

        Returns
        - True if they can use it, otherwise False
        """
        ...


    def getLabel(self) -> str:
        """
        Returns the label for this command

        Returns
        - Label of this command
        """
        ...


    def setLabel(self, name: str) -> bool:
        """
        Sets the label of this command.
        
        May only be used before registering the command.
        Will return True if the new name is set, and False
        if the command has already been registered.

        Arguments
        - name: The command's name

        Returns
        - returns True if the name change happened instantly or False if
            the command was already registered
        """
        ...


    def register(self, commandMap: "CommandMap") -> bool:
        """
        Registers this command to a CommandMap.
        Once called it only allows changes the registered CommandMap

        Arguments
        - commandMap: the CommandMap to register this command to

        Returns
        - True if the registration was successful (the current registered
            CommandMap was the passed CommandMap or null) False otherwise
        """
        ...


    def unregister(self, commandMap: "CommandMap") -> bool:
        """
        Unregisters this command from the passed CommandMap applying any
        outstanding changes

        Arguments
        - commandMap: the CommandMap to unregister

        Returns
        - True if the unregistration was successful (the current
            registered CommandMap was the passed CommandMap or null) False
            otherwise
        """
        ...


    def isRegistered(self) -> bool:
        """
        Returns the current registered state of this command

        Returns
        - True if this command is currently registered False otherwise
        """
        ...


    def getAliases(self) -> list[str]:
        """
        Returns a list of active aliases of this command

        Returns
        - List of aliases
        """
        ...


    def getPermissionMessage(self) -> str:
        """
        Returns a message to be displayed on a failed permission check for this
        command

        Returns
        - Permission check failed message

        Deprecated
        - permission messages have not worked for player-executed
        commands since 1.13 as clients without permission to execute a command
        are unaware of its existence and therefore will not send an unknown
        command execution to the server. This message will only ever be shown to
        consoles or when this command is executed with
        Bukkit.dispatchCommand(CommandSender, String).
        """
        ...


    def getDescription(self) -> str:
        """
        Gets a brief description of this command

        Returns
        - Description of this command
        """
        ...


    def getUsage(self) -> str:
        """
        Gets an example usage of this command

        Returns
        - One or more example usages
        """
        ...


    def setAliases(self, aliases: list[str]) -> "Command":
        """
        Sets the list of aliases to request on registration for this command.
        This is not effective outside of defining aliases in the PluginDescriptionFile.getCommands() (under the
        ``aliases`' node) is equivalent to this method.

        Arguments
        - aliases: aliases to register to this command

        Returns
        - this command object, for chaining
        """
        ...


    def setDescription(self, description: str) -> "Command":
        """
        Sets a brief description of this command. Defining a description in the
        PluginDescriptionFile.getCommands() (under the
        ``description`' node) is equivalent to this method.

        Arguments
        - description: new command description

        Returns
        - this command object, for chaining
        """
        ...


    def setPermissionMessage(self, permissionMessage: str) -> "Command":
        """
        Sets the message sent when a permission check fails

        Arguments
        - permissionMessage: new permission message, null to indicate
            default message, or an empty string to indicate no message

        Returns
        - this command object, for chaining

        Deprecated
        - permission messages have not worked for player-executed
        commands since 1.13 as clients without permission to execute a command
        are unaware of its existence and therefore will not send an unknown
        command execution to the server. This message will only ever be shown to
        consoles or when this command is executed with
        Bukkit.dispatchCommand(CommandSender, String).
        """
        ...


    def setUsage(self, usage: str) -> "Command":
        """
        Sets the example usage of this command

        Arguments
        - usage: new example usage

        Returns
        - this command object, for chaining
        """
        ...


    @staticmethod
    def broadcastCommandMessage(source: "CommandSender", message: str) -> None:
        ...


    @staticmethod
    def broadcastCommandMessage(source: "CommandSender", message: str, sendToSource: bool) -> None:
        ...


    def toString(self) -> str:
        ...
