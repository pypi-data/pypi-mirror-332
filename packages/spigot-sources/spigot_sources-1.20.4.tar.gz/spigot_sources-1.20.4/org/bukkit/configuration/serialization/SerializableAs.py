"""
Python module generated from Java source file org.bukkit.configuration.serialization.SerializableAs

Java source file obtained from artifact spigot-api version 1.20.4-R0.1-20240423.152506-123

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.configuration.serialization import *
from typing import Any, Callable, Iterable, Tuple


class SerializableAs:
    """
    Represents an "alias" that a ConfigurationSerializable may be
    stored as.
    If this is not present on a ConfigurationSerializable class, it
    will use the fully qualified name of the class.
    
    This value will be stored in the configuration so that the configuration
    deserialization can determine what type it is.
    
    Using this annotation on any other class than a ConfigurationSerializable will have no effect.

    See
    - ConfigurationSerialization.registerClass(Class, String)
    """

    def value(self) -> str:
        """
        This is the name your class will be stored and retrieved as.
        
        This name MUST be unique. We recommend using names such as
        "MyPluginThing" instead of "Thing".

        Returns
        - Name to serialize the class as.
        """
        ...
