"""
Python module generated from Java source file org.bukkit.event.entity.EntitySpellCastEvent

Java source file obtained from artifact spigot-api version 1.20.1-R0.1-20230921.163938-66

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import Spellcaster
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import *
from typing import Any, Callable, Iterable, Tuple


class EntitySpellCastEvent(EntityEvent, Cancellable):
    """
    Called when a Spellcaster casts a spell.
    """

    def __init__(self, what: "Spellcaster", spell: "Spellcaster.Spell"):
        ...


    def getEntity(self) -> "Spellcaster":
        ...


    def getSpell(self) -> "Spellcaster.Spell":
        """
        Get the spell to be cast in this event.
        
        This is a convenience method equivalent to
        Spellcaster.getSpell().

        Returns
        - the spell to cast
        """
        ...


    def setCancelled(self, cancelled: bool) -> None:
        ...


    def isCancelled(self) -> bool:
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
