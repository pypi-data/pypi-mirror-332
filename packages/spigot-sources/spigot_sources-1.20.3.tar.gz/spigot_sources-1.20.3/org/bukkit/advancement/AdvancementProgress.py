"""
Python module generated from Java source file org.bukkit.advancement.AdvancementProgress

Java source file obtained from artifact spigot-api version 1.20.3-R0.1-20231207.085553-9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import Date
from org.bukkit.advancement import *
from typing import Any, Callable, Iterable, Tuple


class AdvancementProgress:
    """
    The individual status of an advancement for a player. This class is not
    reference safe as the underlying advancement may be reloaded.
    """

    def getAdvancement(self) -> "Advancement":
        """
        The advancement this progress is concerning.

        Returns
        - the relevant advancement
        """
        ...


    def isDone(self) -> bool:
        """
        Check if all criteria for this advancement have been met.

        Returns
        - True if this advancement is done
        """
        ...


    def awardCriteria(self, criteria: str) -> bool:
        """
        Mark the specified criteria as awarded at the current time.

        Arguments
        - criteria: the criteria to mark

        Returns
        - True if awarded, False if criteria does not exist or already
        awarded.
        """
        ...


    def revokeCriteria(self, criteria: str) -> bool:
        """
        Mark the specified criteria as uncompleted.

        Arguments
        - criteria: the criteria to mark

        Returns
        - True if removed, False if criteria does not exist or not awarded
        """
        ...


    def getDateAwarded(self, criteria: str) -> "Date":
        """
        Get the date the specified criteria was awarded.

        Arguments
        - criteria: the criteria to check

        Returns
        - date awarded or null if unawarded or criteria does not exist
        """
        ...


    def getRemainingCriteria(self) -> Iterable[str]:
        """
        Get the criteria which have not been awarded.

        Returns
        - unmodifiable copy of criteria remaining
        """
        ...


    def getAwardedCriteria(self) -> Iterable[str]:
        """
        Gets the criteria which have been awarded.

        Returns
        - unmodifiable copy of criteria awarded
        """
        ...
