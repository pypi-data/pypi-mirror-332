"""
Python module generated from Java source file org.bukkit.FireworkEffect

Java source file obtained from artifact spigot-api version 1.20.1-R0.1-20230921.163938-66

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from com.google.common.collect import ImmutableList
from com.google.common.collect import ImmutableMap
from enum import Enum
from org.bukkit import *
from org.bukkit.configuration.serialization import ConfigurationSerializable
from org.bukkit.configuration.serialization import SerializableAs
from typing import Any, Callable, Iterable, Tuple


class FireworkEffect(ConfigurationSerializable):
    """
    Represents a single firework effect.
    """

    @staticmethod
    def builder() -> "Builder":
        """
        Construct a firework effect.

        Returns
        - A utility object for building a firework effect
        """
        ...


    def hasFlicker(self) -> bool:
        """
        Get whether the firework effect flickers.

        Returns
        - True if it flickers, False if not
        """
        ...


    def hasTrail(self) -> bool:
        """
        Get whether the firework effect has a trail.

        Returns
        - True if it has a trail, False if not
        """
        ...


    def getColors(self) -> list["Color"]:
        """
        Get the primary colors of the firework effect.

        Returns
        - An immutable list of the primary colors
        """
        ...


    def getFadeColors(self) -> list["Color"]:
        """
        Get the fade colors of the firework effect.

        Returns
        - An immutable list of the fade colors
        """
        ...


    def getType(self) -> "Type":
        """
        Get the type of the firework effect.

        Returns
        - The effect type
        """
        ...


    @staticmethod
    def deserialize(map: dict[str, "Object"]) -> "ConfigurationSerializable":
        """
        Arguments
        - map: the map to deserialize

        Returns
        - the resulting serializable

        See
        - ConfigurationSerializable
        """
        ...


    def serialize(self) -> dict[str, "Object"]:
        ...


    def toString(self) -> str:
        ...


    def hashCode(self) -> int:
        ...


    def equals(self, obj: "Object") -> bool:
        ...


    class Builder:
        """
        This is a builder for FireworkEffects.

        See
        - FireworkEffect.builder()
        """

        def with(self, type: "Type") -> "Builder":
            """
            Specify the type of the firework effect.

            Arguments
            - type: The effect type

            Returns
            - This object, for chaining

            Raises
            - IllegalArgumentException: If type is null
            """
            ...


        def withFlicker(self) -> "Builder":
            """
            Add a flicker to the firework effect.

            Returns
            - This object, for chaining
            """
            ...


        def flicker(self, flicker: bool) -> "Builder":
            """
            Set whether the firework effect should flicker.

            Arguments
            - flicker: True if it should flicker, False if not

            Returns
            - This object, for chaining
            """
            ...


        def withTrail(self) -> "Builder":
            """
            Add a trail to the firework effect.

            Returns
            - This object, for chaining
            """
            ...


        def trail(self, trail: bool) -> "Builder":
            """
            Set whether the firework effect should have a trail.

            Arguments
            - trail: True if it should have a trail, False for no trail

            Returns
            - This object, for chaining
            """
            ...


        def withColor(self, color: "Color") -> "Builder":
            """
            Add a primary color to the firework effect.

            Arguments
            - color: The color to add

            Returns
            - This object, for chaining

            Raises
            - IllegalArgumentException: If color is null
            """
            ...


        def withColor(self, *colors: Tuple["Color", ...]) -> "Builder":
            """
            Add several primary colors to the firework effect.

            Arguments
            - colors: The colors to add

            Returns
            - This object, for chaining

            Raises
            - IllegalArgumentException: If colors is null
            - IllegalArgumentException: If any color is null (may be
                thrown after changes have occurred)
            """
            ...


        def withColor(self, colors: Iterable[Any]) -> "Builder":
            """
            Add several primary colors to the firework effect.

            Arguments
            - colors: An iterable object whose iterator yields the desired
                colors

            Returns
            - This object, for chaining

            Raises
            - IllegalArgumentException: If colors is null
            - IllegalArgumentException: If any color is null (may be
                thrown after changes have occurred)
            """
            ...


        def withFade(self, color: "Color") -> "Builder":
            """
            Add a fade color to the firework effect.

            Arguments
            - color: The color to add

            Returns
            - This object, for chaining

            Raises
            - IllegalArgumentException: If colors is null
            - IllegalArgumentException: If any color is null (may be
                thrown after changes have occurred)
            """
            ...


        def withFade(self, *colors: Tuple["Color", ...]) -> "Builder":
            """
            Add several fade colors to the firework effect.

            Arguments
            - colors: The colors to add

            Returns
            - This object, for chaining

            Raises
            - IllegalArgumentException: If colors is null
            - IllegalArgumentException: If any color is null (may be
                thrown after changes have occurred)
            """
            ...


        def withFade(self, colors: Iterable[Any]) -> "Builder":
            """
            Add several fade colors to the firework effect.

            Arguments
            - colors: An iterable object whose iterator yields the desired
                colors

            Returns
            - This object, for chaining

            Raises
            - IllegalArgumentException: If colors is null
            - IllegalArgumentException: If any color is null (may be
                thrown after changes have occurred)
            """
            ...


        def build(self) -> "FireworkEffect":
            """
            Create a FireworkEffect from the current contents of this
            builder.
            
            To successfully build, you must have specified at least one color.

            Returns
            - The representative firework effect
            """
            ...


    class Type(Enum):
        """
        The type or shape of the effect.
        """

        BALL = 0
        """
        A small ball effect.
        """
        BALL_LARGE = 1
        """
        A large ball effect.
        """
        STAR = 2
        """
        A star-shaped effect.
        """
        BURST = 3
        """
        A burst effect.
        """
        CREEPER = 4
        """
        A creeper-face effect.
        """
