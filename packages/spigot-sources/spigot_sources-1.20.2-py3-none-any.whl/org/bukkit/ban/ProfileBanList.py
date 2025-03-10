"""
Python module generated from Java source file org.bukkit.ban.ProfileBanList

Java source file obtained from artifact spigot-api version 1.20.2-R0.1-20231205.164257-71

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import Date
from org.bukkit import BanEntry
from org.bukkit import BanList
from org.bukkit.ban import *
from org.bukkit.profile import PlayerProfile
from typing import Any, Callable, Iterable, Tuple


class ProfileBanList(BanList):
    """
    A BanList targeting player profile bans.
    """

    def addBan(self, target: "PlayerProfile", reason: str, expires: "Date", source: str) -> "BanEntry"["PlayerProfile"]:
        """
        Arguments
        - target: the target of the ban
        - reason: reason for the ban, null indicates implementation default
        - expires: date for the ban's expiration (unban), or null to imply
            forever
        - source: source of the ban, null indicates implementation default

        Returns
        - the entry for the newly created ban, or the entry for the
            (updated) previous ban

        Raises
        - IllegalArgumentException: if ProfilePlayer has an invalid UUID
        """
        ...
