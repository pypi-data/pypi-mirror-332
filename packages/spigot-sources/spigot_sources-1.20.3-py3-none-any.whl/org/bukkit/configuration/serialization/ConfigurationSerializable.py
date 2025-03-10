"""
Python module generated from Java source file org.bukkit.configuration.serialization.ConfigurationSerializable

Java source file obtained from artifact spigot-api version 1.20.3-R0.1-20231207.085553-9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.configuration.serialization import *
from typing import Any, Callable, Iterable, Tuple


class ConfigurationSerializable:
    """
    Represents an object that may be serialized.
    
    These objects MUST implement one of the following, in addition to the
    methods as defined by this interface:
    
    - A static method "deserialize" that accepts a single Map&lt;
    String, Object&gt; and returns the class.
    - A static method "valueOf" that accepts a single Map&lt;String, Object&gt; and returns the class.
    - A constructor that accepts a single Map&lt;String,
    Object&gt;.
    
    In addition to implementing this interface, you must register the class
    with ConfigurationSerialization.registerClass(Class).

    See
    - SerializableAs
    """

    def serialize(self) -> dict[str, "Object"]:
        """
        Creates a Map representation of this class.
        
        This class must provide a method to restore this class, as defined in
        the ConfigurationSerializable interface javadocs.

        Returns
        - Map containing the current state of this class
        """
        ...
