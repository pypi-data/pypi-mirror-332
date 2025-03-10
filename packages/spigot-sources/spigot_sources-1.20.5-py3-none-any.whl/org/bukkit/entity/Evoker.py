"""
Python module generated from Java source file org.bukkit.entity.Evoker

Java source file obtained from artifact spigot-api version 1.20.5-R0.1-20240429.101539-37

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class Evoker(Spellcaster):
    """
    Represents an Evoker "Illager".
    """

    def getCurrentSpell(self) -> "Spell":
        """
        Gets the Spell the Evoker is currently using.

        Returns
        - the current spell

        Deprecated
        - future versions of Minecraft have additional spell casting
        entities.
        """
        ...


    def setCurrentSpell(self, spell: "Spell") -> None:
        """
        Sets the Spell the Evoker is currently using.

        Arguments
        - spell: the spell the evoker should be using

        Deprecated
        - future versions of Minecraft have additional spell casting
        entities.
        """
        ...


    class Spell(Enum):
        """
        Represents the current spell the Evoker is using.

        Deprecated
        - future versions of Minecraft have additional spell casting
        entities.
        """

        NONE = 0
        """
        No spell is being evoked.
        """
        SUMMON = 1
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
