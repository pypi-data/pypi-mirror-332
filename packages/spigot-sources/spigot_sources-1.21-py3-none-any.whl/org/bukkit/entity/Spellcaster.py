"""
Python module generated from Java source file org.bukkit.entity.Spellcaster

Java source file obtained from artifact spigot-api version 1.21-R0.1-20240807.214924-87

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class Spellcaster(Illager):
    """
    Represents a spell casting "Illager".
    """

    def getSpell(self) -> "Spell":
        """
        Gets the Spell the entity is currently using.

        Returns
        - the current spell
        """
        ...


    def setSpell(self, spell: "Spell") -> None:
        """
        Sets the Spell the entity is currently using.

        Arguments
        - spell: the spell the entity should be using
        """
        ...


    class Spell(Enum):
        """
        Represents the current spell the entity is using.
        """

        NONE = 0
        """
        No spell is being used..
        """
        SUMMON_VEX = 1
        """
        The spell that summons Vexes.
        """
        FANGS = 2
        """
        The spell that summons Fangs.
        """
        WOLOLO = 3
        """
        The "wololo" spell.
        """
        DISAPPEAR = 4
        """
        The spell that makes the casting entity invisible.
        """
        BLINDNESS = 5
        """
        The spell that makes the target blind.
        """
