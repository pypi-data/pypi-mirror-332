"""
Python module generated from Java source file org.bukkit.entity.Guardian

Java source file obtained from artifact spigot-api version 1.16.5-R0.1-20210611.041013-99

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class Guardian(Monster):

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
