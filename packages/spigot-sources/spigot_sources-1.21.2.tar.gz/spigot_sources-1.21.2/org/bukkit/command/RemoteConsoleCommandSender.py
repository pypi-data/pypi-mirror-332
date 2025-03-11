"""
Python module generated from Java source file org.bukkit.command.RemoteConsoleCommandSender

Java source file obtained from artifact spigot-api version 1.21.2-R0.1-20241023.084343-5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.net import SocketAddress
from org.bukkit.command import *
from typing import Any, Callable, Iterable, Tuple


class RemoteConsoleCommandSender(CommandSender):

    def getAddress(self) -> "SocketAddress":
        """
        Gets the socket address of this remote sender.

        Returns
        - the remote sender's address
        """
        ...
