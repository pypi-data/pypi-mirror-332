"""
Python module generated from Java source file org.bukkit.BanEntry

Java source file obtained from artifact spigot-api version 1.17.1-R0.1-20211121.234319-104

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import Date
from org.bukkit import *
from typing import Any, Callable, Iterable, Tuple


class BanEntry:
    """
    A single entry from a ban list. This may represent either a player ban or
    an IP ban.
    
    Ban entries include the following properties:
    <table border=1>
    <caption>Property information</caption>
    <tr>
        <th>Property</th>
        <th>Description</th>
    </tr><tr>
        <td>Target Name / IP Address</td>
        <td>The target name or IP address</td>
    </tr><tr>
        <td>Creation Date</td>
        <td>The creation date of the ban</td>
    </tr><tr>
        <td>Source</td>
        <td>The source of the ban, such as a player, console, plugin, etc</td>
    </tr><tr>
        <td>Expiration Date</td>
        <td>The expiration date of the ban</td>
    </tr><tr>
        <td>Reason</td>
        <td>The reason for the ban</td>
    </tr>
    </table>
    
    Unsaved information is not automatically written to the implementation's
    ban list, instead, the .save() method must be called to write the
    changes to the ban list. If this ban entry has expired (such as from an
    unban) and is no longer found in the list, the .save() call will
    re-add it to the list, therefore banning the victim specified.
    
    Likewise, changes to the associated BanList or other entries may or
    may not be reflected in this entry.
    """

    def getTarget(self) -> str:
        """
        Gets the target involved. This may be in the form of an IP or a player
        name.

        Returns
        - the target name or IP address
        """
        ...


    def getCreated(self) -> "Date":
        """
        Gets the date this ban entry was created.

        Returns
        - the creation date
        """
        ...


    def setCreated(self, created: "Date") -> None:
        """
        Sets the date this ban entry was created.

        Arguments
        - created: the new created date, cannot be null

        See
        - .save() saving changes
        """
        ...


    def getSource(self) -> str:
        """
        Gets the source of this ban.
        
        Note: A source is considered any String, although this is generally a
        player name.

        Returns
        - the source of the ban
        """
        ...


    def setSource(self, source: str) -> None:
        """
        Sets the source of this ban.
        
        Note: A source is considered any String, although this is generally a
        player name.

        Arguments
        - source: the new source where null values become empty strings

        See
        - .save() saving changes
        """
        ...


    def getExpiration(self) -> "Date":
        """
        Gets the date this ban expires on, or null for no defined end date.

        Returns
        - the expiration date
        """
        ...


    def setExpiration(self, expiration: "Date") -> None:
        """
        Sets the date this ban expires on. Null values are considered
        "infinite" bans.

        Arguments
        - expiration: the new expiration date, or null to indicate an
            eternity

        See
        - .save() saving changes
        """
        ...


    def getReason(self) -> str:
        """
        Gets the reason for this ban.

        Returns
        - the ban reason, or null if not set
        """
        ...


    def setReason(self, reason: str) -> None:
        """
        Sets the reason for this ban. Reasons must not be null.

        Arguments
        - reason: the new reason, null values assume the implementation
            default

        See
        - .save() saving changes
        """
        ...


    def save(self) -> None:
        """
        Saves the ban entry, overwriting any previous data in the ban list.
        
        Saving the ban entry of an unbanned player will cause the player to be
        banned once again.
        """
        ...
