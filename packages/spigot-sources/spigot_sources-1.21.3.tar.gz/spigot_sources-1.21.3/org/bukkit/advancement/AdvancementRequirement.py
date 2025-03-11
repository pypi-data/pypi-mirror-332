"""
Python module generated from Java source file org.bukkit.advancement.AdvancementRequirement

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.advancement import *
from typing import Any, Callable, Iterable, Tuple


class AdvancementRequirement:

    def getRequiredCriteria(self) -> list[str]:
        """
        Get all required criteria.

        Returns
        - the list of required criteria for this requirement.
        """
        ...


    def isStrict(self) -> bool:
        """
        Check if the requirement is strict.

        Returns
        - True if requirement list contains one criteria, False if
        multiple.
        """
        ...
