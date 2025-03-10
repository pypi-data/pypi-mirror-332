"""
Python module generated from Java source file org.bukkit.entity.Guardian

Java source file obtained from artifact spigot-api version 1.20.4-R0.1-20240423.152506-123

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class Guardian(Monster):

    def setLaser(self, activated: bool) -> bool:
        """
        Sets whether the guardian laser should show or not.
        
        A target must be present. If no target is present the laser will not show
        and the method will return False.

        Arguments
        - activated: whether the laser is active

        Returns
        - True if the laser was activated otherwise False

        See
        - .setTarget(LivingEntity)
        """
        ...


    def hasLaser(self) -> bool:
        """
        Gets whether the guardian laser is active or not.

        Returns
        - True if the laser is active otherwise False
        """
        ...


    def getLaserDuration(self) -> int:
        """
        Get the duration (in ticks) that a laser attack takes.

        Returns
        - the laser duration in ticks
        """
        ...


    def setLaserTicks(self, ticks: int) -> None:
        """
        Set the amount of ticks that have elapsed since this guardian has initiated
        a laser attack. If set to .getLaserDuration() or greater, the guardian
        will inflict damage upon its target and the laser attack will complete.
        
        For this value to have any effect, the guardian must have an active target
        (see .setTarget(LivingEntity)) and be charging a laser attack (where
        .hasLaser() is True). The client may display a different animation of
        the guardian laser than the set ticks.

        Arguments
        - ticks: the ticks to set. Must be at least -10
        """
        ...


    def getLaserTicks(self) -> int:
        """
        Get the amount of ticks that have elapsed since this guardian has initiated
        a laser attack.
        
        This value may or may not be significant depending on whether or not the guardian
        has an active target (.getTarget()) and is charging a laser attack
        (.hasLaser()). This value is not reset after a successful attack nor used
        in the next and will be reset to the minimum value when the guardian initiates a
        new one.

        Returns
        - the laser ticks ranging from -10 to .getLaserDuration()
        """
        ...


    def isElder(self) -> bool:
        """
        Check if the Guardian is an elder Guardian

        Returns
        - True if the Guardian is an Elder Guardian, False if not

        Deprecated
        - should check if instance of ElderGuardian.
        """
        ...


    def setElder(self, shouldBeElder: bool) -> None:
        """
        Arguments
        - shouldBeElder: shouldBeElder

        Deprecated
        - Must spawn a new ElderGuardian.
        """
        ...


    def isMoving(self) -> bool:
        """
        Check whether or not this guardian is moving.
        
        While moving, the guardian's spikes are retracted and will not inflict thorns
        damage upon entities that attack it. Additionally, a moving guardian cannot
        attack another entity. If stationary (i.e. this method returns `False`),
        thorns damage is guaranteed and the guardian may initiate laser attacks.

        Returns
        - True if moving, False if stationary
        """
        ...
