"""
Python module generated from Java source file org.bukkit.configuration.serialization.DelegateDeserialization

Java source file obtained from artifact spigot-api version 1.16.5-R0.1-20210611.041013-99

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.configuration.serialization import *
from typing import Any, Callable, Iterable, Tuple


class DelegateDeserialization:
    """
    Applies to a ConfigurationSerializable that will delegate all
    deserialization to another ConfigurationSerializable.
    """

    def value(self) -> type["ConfigurationSerializable"]:
        """
        Which class should be used as a delegate for this classes
        deserialization

        Returns
        - Delegate class
        """
        ...
