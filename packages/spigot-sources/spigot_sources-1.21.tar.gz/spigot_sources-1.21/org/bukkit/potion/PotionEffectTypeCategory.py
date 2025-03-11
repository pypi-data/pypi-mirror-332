"""
Python module generated from Java source file org.bukkit.potion.PotionEffectTypeCategory

Java source file obtained from artifact spigot-api version 1.21-R0.1-20240807.214924-87

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.potion import *
from typing import Any, Callable, Iterable, Tuple


class PotionEffectTypeCategory(Enum):
    """
    Represents a category of PotionEffectType and its effect on an entity.
    """

    BENEFICIAL = 0
    """
    Beneficial effects that positively impact an entity, such as Regeneration,
    Absorption, or Fire Resistance.
    """
    HARMFUL = 1
    """
    Harmful effects that negatively impact an entity, such as Blindness, Wither,
    or Levitation.
    """
    NEUTRAL = 2
    """
    Neutral effects that have neither a positive nor negative effect on an
    entity, such as Glowing or Bad Omen.
    """
