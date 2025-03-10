"""
Python module generated from Java source file com.google.common.util.concurrent.Atomics

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.util.concurrent import *
from java.util.concurrent.atomic import AtomicReference
from java.util.concurrent.atomic import AtomicReferenceArray
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class Atomics:
    """
    Static utility methods pertaining to classes in the `java.util.concurrent.atomic` package.

    Author(s)
    - Kurt Alfred Kluever

    Since
    - 10.0
    """

    @staticmethod
    def newReference() -> "AtomicReference"["V"]:
        """
        Creates an `AtomicReference` instance with no initial value.

        Returns
        - a new `AtomicReference` with no initial value
        """
        ...


    @staticmethod
    def newReference(initialValue: "V") -> "AtomicReference"["V"]:
        """
        Creates an `AtomicReference` instance with the given initial value.

        Arguments
        - initialValue: the initial value

        Returns
        - a new `AtomicReference` with the given initial value
        """
        ...


    @staticmethod
    def newReferenceArray(length: int) -> "AtomicReferenceArray"["E"]:
        """
        Creates an `AtomicReferenceArray` instance of given length.

        Arguments
        - length: the length of the array

        Returns
        - a new `AtomicReferenceArray` with the given length
        """
        ...


    @staticmethod
    def newReferenceArray(array: list["E"]) -> "AtomicReferenceArray"["E"]:
        """
        Creates an `AtomicReferenceArray` instance with the same length as, and all elements
        copied from, the given array.

        Arguments
        - array: the array to copy elements from

        Returns
        - a new `AtomicReferenceArray` copied from the given array
        """
        ...
