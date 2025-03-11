"""
Python module generated from Java source file org.bukkit.command.defaults.VersionCommand

Java source file obtained from artifact spigot-api version 1.20.6-R0.1-20240613.150924-57

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Charsets
from com.google.common.base import Preconditions
from com.google.common.collect import ImmutableList
from com.google.common.io import Resources
from com.google.gson import Gson
from com.google.gson import JsonObject
from com.google.gson import JsonSyntaxException
from java.io import BufferedReader
from java.io import IOException
from java.net import URL
from java.net import URLEncoder
from java.util import Arrays
from java.util import Locale
from java.util.concurrent.locks import ReentrantLock
from org.bukkit import Bukkit
from org.bukkit import ChatColor
from org.bukkit.command import CommandSender
from org.bukkit.command.defaults import *
from org.bukkit.plugin import Plugin
from org.bukkit.plugin import PluginDescriptionFile
from org.bukkit.util import StringUtil
from typing import Any, Callable, Iterable, Tuple


class VersionCommand(BukkitCommand):

    def __init__(self, name: str):
        ...


    def execute(self, sender: "CommandSender", currentAlias: str, args: list[str]) -> bool:
        ...


    def tabComplete(self, sender: "CommandSender", alias: str, args: list[str]) -> list[str]:
        ...
