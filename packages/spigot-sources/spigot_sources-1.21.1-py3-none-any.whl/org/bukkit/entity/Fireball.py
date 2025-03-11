"""
Python module generated from Java source file org.bukkit.entity.Fireball

Java source file obtained from artifact spigot-api version 1.21.1-R0.1-20241022.152140-54

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import *
from org.bukkit.util import Vector
from typing import Any, Callable, Iterable, Tuple


class Fireball(Projectile, Explosive):
    """
    Represents a Fireball.
    """

    def setDirection(self, direction: "Vector") -> None:
        """
        Sets the direction the fireball should be flying towards.
        
        This is a convenience method, it will change the velocity direction and
        acceleration direction, while keeping the power the same.
        
        **Note:** This method only uses the direction of the vector and will
        normalize (a copy of) it.
        
        **Special Case:** When the given direction is
        Vector.isZero() zero, the velocity and acceleration will also be
        set to zero without keeping the power.

        Arguments
        - direction: the direction this fireball should be flying towards

        See
        - .setAcceleration(Vector)
        """
        ...


    def getDirection(self) -> "Vector":
        """
        Retrieve the direction this fireball is heading toward.
        The returned vector is not normalized.

        Returns
        - the direction

        See
        - .getAcceleration()

        Deprecated
        - badly named method, returns the value of
        .getAcceleration()
        """
        ...


    def setAcceleration(self, acceleration: "Vector") -> None:
        """
        Sets the acceleration of the fireball.
        
        The acceleration gets applied to the velocity every tick, depending on
        the specific type of the fireball a damping / drag factor is applied so
        that the velocity does not grow into infinity.
        
        **Note:** that the client may not respect non-default acceleration
        power and will therefore mispredict the location of the fireball, causing
        visual stutter.

        Arguments
        - acceleration: the acceleration
        """
        ...


    def getAcceleration(self) -> "Vector":
        """
        Retrieve the acceleration of this fireball.

        Returns
        - the acceleration
        """
        ...
