"""
Python module generated from Java source file org.bukkit.util.ChatPaginator

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import Arrays
from org.bukkit import ChatColor
from org.bukkit.util import *
from typing import Any, Callable, Iterable, Tuple


class ChatPaginator:
    """
    The ChatPaginator takes a raw string of arbitrary length and breaks it down
    into an array of strings appropriate for displaying on the Minecraft player
    console.
    """

    GUARANTEED_NO_WRAP_CHAT_PAGE_WIDTH = 55
    AVERAGE_CHAT_PAGE_WIDTH = 65
    UNBOUNDED_PAGE_WIDTH = Integer.MAX_VALUE
    OPEN_CHAT_PAGE_HEIGHT = 20
    CLOSED_CHAT_PAGE_HEIGHT = 10
    UNBOUNDED_PAGE_HEIGHT = Integer.MAX_VALUE


    @staticmethod
    def paginate(unpaginatedString: str, pageNumber: int) -> "ChatPage":
        """
        Breaks a raw string up into pages using the default width and height.

        Arguments
        - unpaginatedString: The raw string to break.
        - pageNumber: The page number to fetch.

        Returns
        - A single chat page.
        """
        ...


    @staticmethod
    def paginate(unpaginatedString: str, pageNumber: int, lineLength: int, pageHeight: int) -> "ChatPage":
        """
        Breaks a raw string up into pages using a provided width and height.

        Arguments
        - unpaginatedString: The raw string to break.
        - pageNumber: The page number to fetch.
        - lineLength: The desired width of a chat line.
        - pageHeight: The desired number of lines in a page.

        Returns
        - A single chat page.
        """
        ...


    @staticmethod
    def wordWrap(rawString: str, lineLength: int) -> list[str]:
        """
        Breaks a raw string up into a series of lines. Words are wrapped using
        spaces as decimeters and the newline character is respected.

        Arguments
        - rawString: The raw string to break.
        - lineLength: The length of a line of text.

        Returns
        - An array of word-wrapped lines.
        """
        ...


    class ChatPage:

        def __init__(self, lines: list[str], pageNumber: int, totalPages: int):
            ...


        def getPageNumber(self) -> int:
            ...


        def getTotalPages(self) -> int:
            ...


        def getLines(self) -> list[str]:
            ...
