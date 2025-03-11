"""
Python module generated from Java source file org.bukkit.util.io.BukkitObjectOutputStream

Java source file obtained from artifact spigot-api version 1.21.2-R0.1-20241023.084343-5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import IOException
from java.io import ObjectOutputStream
from java.io import OutputStream
from java.io import Serializable
from org.bukkit.configuration.serialization import ConfigurationSerializable
from org.bukkit.util.io import *
from typing import Any, Callable, Iterable, Tuple


class BukkitObjectOutputStream(ObjectOutputStream):
    """
    This class is designed to be used in conjunction with the ConfigurationSerializable API. It translates objects to an internal
    implementation for later deserialization using BukkitObjectInputStream.
    
    Behavior of implementations extending this class is not guaranteed across
    future versions.
    """

    def __init__(self, out: "OutputStream"):
        """
        Object output stream decoration constructor.

        Arguments
        - out: the stream to wrap

        Raises
        - IOException: if an I/O error occurs while writing stream header

        See
        - ObjectOutputStream.ObjectOutputStream(OutputStream)
        """
        ...
