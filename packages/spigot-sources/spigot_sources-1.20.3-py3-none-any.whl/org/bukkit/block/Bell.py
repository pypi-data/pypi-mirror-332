"""
Python module generated from Java source file org.bukkit.block.Bell

Java source file obtained from artifact spigot-api version 1.20.3-R0.1-20231207.085553-9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import *
from org.bukkit.entity import Entity
from org.bukkit.event.block import BellRingEvent
from typing import Any, Callable, Iterable, Tuple


class Bell(TileState):
    """
    Represents a captured state of Bell.
    """

    def ring(self, entity: "Entity", direction: "BlockFace") -> bool:
        """
        Ring this bell. This will call a BellRingEvent.

        Arguments
        - entity: the entity ringing the bell
        - direction: the direction from which the bell was rung or null to
        ring in the direction that the bell is facing

        Returns
        - True if rung successfully, False if the event was cancelled
        """
        ...


    def ring(self, entity: "Entity") -> bool:
        """
        Ring this bell in the direction that the bell is facing. This will call a
        BellRingEvent.

        Arguments
        - entity: the entity ringing the bell

        Returns
        - True if rung successfully, False if the event was cancelled
        """
        ...


    def ring(self, direction: "BlockFace") -> bool:
        """
        Ring this bell. This will call a BellRingEvent.

        Arguments
        - direction: the direction from which the bell was rung or null to
        ring in the direction that the bell is facing

        Returns
        - True if rung successfully, False if the event was cancelled
        """
        ...


    def ring(self) -> bool:
        """
        Ring this bell in the direction that the bell is facing. This will call a
        BellRingEvent.

        Returns
        - True if rung successfully, False if the event was cancelled
        """
        ...


    def isShaking(self) -> bool:
        """
        Check whether or not this bell is shaking. A bell is considered to be
        shaking if it was recently rung.
        
        A bell will typically shake for 50 ticks.

        Returns
        - True if shaking, False otherwise
        """
        ...


    def getShakingTicks(self) -> int:
        """
        Get the amount of ticks since this bell has been shaking, or 0 if the
        bell is not currently shaking.
        
        A bell will typically shake for 50 ticks.

        Returns
        - the time in ticks since the bell was rung, or 0 if not shaking
        """
        ...


    def isResonating(self) -> bool:
        """
        Check whether or not this bell is resonating. A bell is considered to be
        resonating if .isShaking() while shaking, raiders were detected
        in the area and are ready to be highlighted to nearby players.
        
        A bell will typically resonate for 40 ticks.

        Returns
        - True if resonating, False otherwise
        """
        ...


    def getResonatingTicks(self) -> int:
        """
        Get the amount of ticks since this bell has been resonating, or 0 if the
        bell is not currently resonating.
        
        A bell will typically resonate for 40 ticks.

        Returns
        - the time in ticks since the bell has been resonating, or 0 if not
        resonating
        """
        ...
