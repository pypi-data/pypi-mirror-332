"""
Python module generated from Java source file org.bukkit.util.OldEnum

Java source file obtained from artifact spigot-api version 1.21-R0.1-20240807.214924-87

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.util import *
from typing import Any, Callable, Iterable, Tuple


class OldEnum(Comparable):
    """
    Class which holds common methods which are present in an enum.
    
    Type `<T>`: the type of the old enum.

    Deprecated
    - only for backwards compatibility.
    """

    def compareTo(self, other: "T") -> int:
        """
        Arguments
        - other: to compare to.

        Returns
        - negative if this old enum is lower, zero if equal and positive if
        higher than the given old enum.

        Deprecated
        - only for backwards compatibility, old enums can not be
        compared.
        """
        ...


    def name(self) -> str:
        """
        Returns
        - the name of the old enum.

        Deprecated
        - only for backwards compatibility.
        """
        ...


    def ordinal(self) -> int:
        """
        Returns
        - the ordinal of the old enum.

        Deprecated
        - only for backwards compatibility, it is not guaranteed that
        an old enum always has the same ordinal.
        """
        ...
