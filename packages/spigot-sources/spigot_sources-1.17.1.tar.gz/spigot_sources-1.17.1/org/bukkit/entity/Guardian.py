"""
Python module generated from Java source file org.bukkit.entity.Guardian

Java source file obtained from artifact spigot-api version 1.17.1-R0.1-20211121.234319-104

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
