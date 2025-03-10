"""
Python module generated from Java source file org.bukkit.configuration.SectionPathData

Java source file obtained from artifact spigot-api version 1.19.4-R0.1-20230607.155743-88

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import Collections
from org.bukkit.configuration import *
from typing import Any, Callable, Iterable, Tuple


class SectionPathData:

    def __init__(self, data: "Object"):
        ...


    def getData(self) -> "Object":
        ...


    def setData(self, data: "Object") -> None:
        ...


    def getComments(self) -> list[str]:
        """
        If no comments exist, an empty list will be returned. A null entry in the
        list represents an empty line and an empty String represents an empty
        comment line.

        Returns
        - A unmodifiable list of the requested comments, every entry
        represents one line.
        """
        ...


    def setComments(self, comments: list[str]) -> None:
        """
        Represents the comments on a ConfigurationSection entry.
        
        A null entry in the List is an empty line and an empty String entry is an
        empty comment line. Any existing comments will be replaced, regardless of
        what the new comments are.

        Arguments
        - comments: New comments to set every entry represents one line.
        """
        ...


    def getInlineComments(self) -> list[str]:
        """
        If no comments exist, an empty list will be returned. A null entry in the
        list represents an empty line and an empty String represents an empty
        comment line.

        Returns
        - A unmodifiable list of the requested comments, every entry
        represents one line.
        """
        ...


    def setInlineComments(self, inlineComments: list[str]) -> None:
        """
        Represents the comments on a ConfigurationSection entry.
        
        A null entry in the List is an empty line and an empty String entry is an
        empty comment line. Any existing comments will be replaced, regardless of
        what the new comments are.

        Arguments
        - inlineComments: New comments to set every entry represents one
        line.
        """
        ...
