"""
Python module generated from Java source file org.spigotmc.CustomTimingsHandler

Java source file obtained from artifact spigot-api version 1.20-R0.1-20230612.113428-32

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import PrintStream
from java.util import Queue
from java.util.concurrent import ConcurrentLinkedQueue
from org.bukkit import Bukkit
from org.bukkit import World
from org.bukkit.command.defaults import TimingsCommand
from org.spigotmc import *
from typing import Any, Callable, Iterable, Tuple


class CustomTimingsHandler:
    """
    Provides custom timing sections for /timings merged.
    """

    def __init__(self, name: str):
        ...


    def __init__(self, name: str, parent: "CustomTimingsHandler"):
        ...


    @staticmethod
    def printTimings(printStream: "PrintStream") -> None:
        """
        Prints the timings and extra data to the given stream.

        Arguments
        - printStream: output stream
        """
        ...


    @staticmethod
    def reload() -> None:
        """
        Resets all timings.
        """
        ...


    @staticmethod
    def tick() -> None:
        """
        Ticked every tick by CraftBukkit to count the number of times a timer
        caused TPS loss.
        """
        ...


    def startTiming(self) -> None:
        """
        Starts timing to track a section of code.
        """
        ...


    def stopTiming(self) -> None:
        """
        Stops timing a section of code.
        """
        ...


    def reset(self) -> None:
        """
        Reset this timer, setting all values to zero.
        """
        ...
