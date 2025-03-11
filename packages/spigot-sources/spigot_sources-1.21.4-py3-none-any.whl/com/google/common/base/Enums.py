"""
Python module generated from Java source file com.google.common.base.Enums

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import J2ktIncompatible
from com.google.common.base import *
from java.io import Serializable
from java.lang.ref import WeakReference
from java.lang.reflect import Field
from java.util import EnumSet
from java.util import WeakHashMap
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class Enums:
    """
    Utility methods for working with Enum instances.

    Author(s)
    - Steve McKay

    Since
    - 9.0
    """

    @staticmethod
    def getField(enumValue: "Enum"[Any]) -> "Field":
        """
        Returns the Field in which `enumValue` is defined. For example, to get the `Description` annotation on the `GOLF` constant of enum `Sport`, use `Enums.getField(Sport.GOLF).getAnnotation(Description.class)`.

        Since
        - 12.0
        """
        ...


    @staticmethod
    def getIfPresent(enumClass: type["T"], value: str) -> "Optional"["T"]:
        """
        Returns an optional enum constant for the given type, using Enum.valueOf. If the
        constant does not exist, Optional.absent is returned. A common use case is for parsing
        user input or falling back to a default enum constant. For example, `Enums.getIfPresent(Country.class, countryInput).or(Country.DEFAULT);`

        Since
        - 12.0
        """
        ...


    @staticmethod
    def stringConverter(enumClass: type["T"]) -> "Converter"[str, "T"]:
        """
        Returns a serializable converter that converts between strings and `enum` values of type
        `enumClass` using Enum.valueOf(Class, String) and Enum.name(). The
        converter will throw an `IllegalArgumentException` if the argument is not the name of any
        enum constant in the specified enum.

        Since
        - 16.0
        """
        ...
