"""
Python module generated from Java source file org.bukkit.util.io.BukkitObjectInputStream

Java source file obtained from artifact spigot-api version 1.19.4-R0.1-20230607.155743-88

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import IOException
from java.io import InputStream
from java.io import ObjectInputStream
from org.bukkit.configuration.serialization import ConfigurationSerializable
from org.bukkit.configuration.serialization import ConfigurationSerialization
from org.bukkit.util.io import *
from typing import Any, Callable, Iterable, Tuple


class BukkitObjectInputStream(ObjectInputStream):
    """
    This class is designed to be used in conjunction with the ConfigurationSerializable API. It translates objects back to their
    original implementation after being serialized by BukkitObjectInputStream.
    
    Behavior of implementations extending this class is not guaranteed across
    future versions.
    """

    def __init__(self, in: "InputStream"):
        """
        Object input stream decoration constructor.

        Arguments
        - in: the input stream to wrap

        Raises
        - IOException: if an I/O error occurs while reading stream header

        See
        - ObjectInputStream.ObjectInputStream(InputStream)
        """
        ...
