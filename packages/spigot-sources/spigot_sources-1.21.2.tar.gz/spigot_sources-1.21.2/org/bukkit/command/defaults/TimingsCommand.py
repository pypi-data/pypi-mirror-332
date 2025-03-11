"""
Python module generated from Java source file org.bukkit.command.defaults.TimingsCommand

Java source file obtained from artifact spigot-api version 1.21.2-R0.1-20241023.084343-5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from com.google.common.collect import ImmutableList
from java.io import ByteArrayOutputStream
from java.io import File
from java.io import IOException
from java.io import OutputStream
from java.io import PrintStream
from java.net import HttpURLConnection
from java.net import URL
from org.bukkit import Bukkit
from org.bukkit import ChatColor
from org.bukkit.command import CommandSender
from org.bukkit.command import RemoteConsoleCommandSender
from org.bukkit.command.defaults import *
from org.bukkit.event import Event
from org.bukkit.event import HandlerList
from org.bukkit.plugin import Plugin
from org.bukkit.plugin import RegisteredListener
from org.bukkit.plugin import SimplePluginManager
from org.bukkit.plugin import TimedRegisteredListener
from org.bukkit.util import StringUtil
from org.spigotmc import CustomTimingsHandler
from typing import Any, Callable, Iterable, Tuple


class TimingsCommand(BukkitCommand):

    timingStart = 0


    def __init__(self, name: str):
        ...


    def executeSpigotTimings(self, sender: "CommandSender", args: list[str]) -> None:
        ...


    def execute(self, sender: "CommandSender", currentAlias: str, args: list[str]) -> bool:
        ...


    def tabComplete(self, sender: "CommandSender", alias: str, args: list[str]) -> list[str]:
        ...
