"""
Python module generated from Java source file org.bukkit.BanList

Java source file obtained from artifact spigot-api version 1.21-R0.1-20240807.214924-87

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from java.time import Duration
from java.time import Instant
from java.util import Date
from org.bukkit import *
from typing import Any, Callable, Iterable, Tuple


class BanList:
    """
    A ban list, containing bans of some Type.
    
    Type `<T>`: The ban target
    """

    def getBanEntry(self, target: str) -> "BanEntry"["T"]:
        """
        Gets a BanEntry by target.

        Arguments
        - target: entry parameter to search for

        Returns
        - the corresponding entry, or null if none found

        Deprecated
        - see .getBanEntry(Object)
        """
        ...


    def getBanEntry(self, target: "T") -> "BanEntry"["T"]:
        """
        Gets a BanEntry by target.

        Arguments
        - target: entry parameter to search for

        Returns
        - the corresponding entry, or null if none found
        """
        ...


    def addBan(self, target: str, reason: str, expires: "Date", source: str) -> "BanEntry"["T"]:
        """
        Adds a ban to this list. If a previous ban exists, this will
        update the previous entry.

        Arguments
        - target: the target of the ban
        - reason: reason for the ban, null indicates implementation default
        - expires: date for the ban's expiration (unban), or null to imply
            forever
        - source: source of the ban, null indicates implementation default

        Returns
        - the entry for the newly created ban, or the entry for the
            (updated) previous ban

        Deprecated
        - see .addBan(Object, String, Date, String)
        """
        ...


    def addBan(self, target: "T", reason: str, expires: "Date", source: str) -> "BanEntry"["T"]:
        """
        Adds a ban to this list. If a previous ban exists, this will
        update the previous entry.

        Arguments
        - target: the target of the ban
        - reason: reason for the ban, null indicates implementation default
        - expires: date for the ban's expiration (unban), or null to imply
            forever
        - source: source of the ban, null indicates implementation default

        Returns
        - the entry for the newly created ban, or the entry for the
            (updated) previous ban
        """
        ...


    def addBan(self, target: "T", reason: str, expires: "Instant", source: str) -> "BanEntry"["T"]:
        """
        Adds a ban to this list. If a previous ban exists, this will
        update the previous entry.

        Arguments
        - target: the target of the ban
        - reason: reason for the ban, null indicates implementation default
        - expires: instant for the ban's expiration (unban), or null to imply
            forever
        - source: source of the ban, null indicates implementation default

        Returns
        - the entry for the newly created ban, or the entry for the
            (updated) previous ban
        """
        ...


    def addBan(self, target: "T", reason: str, duration: "Duration", source: str) -> "BanEntry"["T"]:
        """
        Adds a ban to this list. If a previous ban exists, this will
        update the previous entry.

        Arguments
        - target: the target of the ban
        - reason: reason for the ban, null indicates implementation default
        - duration: the duration of the ban, or null to imply
            forever
        - source: source of the ban, null indicates implementation default

        Returns
        - the entry for the newly created ban, or the entry for the
            (updated) previous ban
        """
        ...


    def getBanEntries(self) -> set["BanEntry"]:
        """
        Gets a set containing every BanEntry in this list.

        Returns
        - an immutable set containing every entry tracked by this list

        Deprecated
        - This return a generic class, prefer use .getEntries()
        """
        ...


    def getEntries(self) -> set["BanEntry"["T"]]:
        """
        Gets a set containing every BanEntry in this list.

        Returns
        - an immutable set containing every entry tracked by this list
        """
        ...


    def isBanned(self, target: "T") -> bool:
        """
        Gets if a BanEntry exists for the target, indicating an active
        ban status.

        Arguments
        - target: the target to find

        Returns
        - True if a BanEntry exists for the target, indicating an
            active ban status, False otherwise
        """
        ...


    def isBanned(self, target: str) -> bool:
        """
        Gets if a BanEntry exists for the target, indicating an active
        ban status.

        Arguments
        - target: the target to find

        Returns
        - True if a BanEntry exists for the target, indicating an
            active ban status, False otherwise

        Deprecated
        - see .isBanned(Object)
        """
        ...


    def pardon(self, target: "T") -> None:
        """
        Removes the specified target from this list, therefore indicating a
        "not banned" status.

        Arguments
        - target: the target to remove from this list
        """
        ...


    def pardon(self, target: str) -> None:
        """
        Removes the specified target from this list, therefore indicating a
        "not banned" status.

        Arguments
        - target: the target to remove from this list

        Deprecated
        - see .pardon(Object)
        """
        ...


    class Type(Enum):
        """
        Represents a ban-type that a BanList may track.
        """

        NAME = 0
        """
        Banned player names

        Deprecated
        - deprecated in favor of .PROFILE
        """
        IP = 1
        """
        Banned IP addresses
        """
        PROFILE = 2
        """
        Banned player profiles
        """
