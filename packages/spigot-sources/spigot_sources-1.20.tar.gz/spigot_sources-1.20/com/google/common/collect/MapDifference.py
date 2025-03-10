"""
Python module generated from Java source file com.google.common.collect.MapDifference

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.collect import *
from com.google.errorprone.annotations import DoNotMock
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class MapDifference:
    """
    An object representing the differences between two maps.

    Author(s)
    - Kevin Bourrillion

    Since
    - 2.0
    """

    def areEqual(self) -> bool:
        """
        Returns `True` if there are no differences between the two maps; that is, if the maps are
        equal.
        """
        ...


    def entriesOnlyOnLeft(self) -> dict["K", "V"]:
        """
        Returns an unmodifiable map containing the entries from the left map whose keys are not present
        in the right map.
        """
        ...


    def entriesOnlyOnRight(self) -> dict["K", "V"]:
        """
        Returns an unmodifiable map containing the entries from the right map whose keys are not
        present in the left map.
        """
        ...


    def entriesInCommon(self) -> dict["K", "V"]:
        """
        Returns an unmodifiable map containing the entries that appear in both maps; that is, the
        intersection of the two maps.
        """
        ...


    def entriesDiffering(self) -> dict["K", "ValueDifference"["V"]]:
        """
        Returns an unmodifiable map describing keys that appear in both maps, but with different
        values.
        """
        ...


    def equals(self, object: "Object") -> bool:
        """
        Compares the specified object with this instance for equality. Returns `True` if the
        given object is also a `MapDifference` and the values returned by the .entriesOnlyOnLeft(), .entriesOnlyOnRight(), .entriesInCommon() and .entriesDiffering() of the two instances are equal.
        """
        ...


    def hashCode(self) -> int:
        """
        Returns the hash code for this instance. This is defined as the hash code of
        
        ````Arrays.asList(entriesOnlyOnLeft(), entriesOnlyOnRight(),
            entriesInCommon(), entriesDiffering())````
        """
        ...
