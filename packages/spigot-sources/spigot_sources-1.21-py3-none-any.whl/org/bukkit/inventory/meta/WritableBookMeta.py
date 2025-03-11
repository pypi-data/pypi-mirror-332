"""
Python module generated from Java source file org.bukkit.inventory.meta.WritableBookMeta

Java source file obtained from artifact spigot-api version 1.21-R0.1-20240807.214924-87

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Material
from org.bukkit.inventory.meta import *
from typing import Any, Callable, Iterable, Tuple


class WritableBookMeta(ItemMeta):
    """
    Represents a book (Material.WRITABLE_BOOK or Material.WRITTEN_BOOK) that can have pages.
    """

    def hasPages(self) -> bool:
        """
        Checks for the existence of pages in the book.

        Returns
        - True if the book has pages
        """
        ...


    def getPage(self, page: int) -> str:
        """
        Gets the specified page in the book. The given page must exist.
        
        Pages are 1-indexed.

        Arguments
        - page: the page number to get, in range [1, getPageCount()]

        Returns
        - the page from the book
        """
        ...


    def setPage(self, page: int, data: str) -> None:
        """
        Sets the specified page in the book. Pages of the book must be
        contiguous.
        
        The data can be up to 1024 characters in length, additional characters
        are truncated.
        
        Pages are 1-indexed.

        Arguments
        - page: the page number to set, in range [1, getPageCount()]
        - data: the data to set for that page
        """
        ...


    def getPages(self) -> list[str]:
        """
        Gets all the pages in the book.

        Returns
        - list of all the pages in the book
        """
        ...


    def setPages(self, pages: list[str]) -> None:
        """
        Clears the existing book pages, and sets the book to use the provided
        pages. Maximum 100 pages with 1024 characters per page.

        Arguments
        - pages: A list of pages to set the book to use
        """
        ...


    def setPages(self, *pages: Tuple[str, ...]) -> None:
        """
        Clears the existing book pages, and sets the book to use the provided
        pages. Maximum 100 pages with 1024 characters per page.

        Arguments
        - pages: A list of strings, each being a page
        """
        ...


    def addPage(self, *pages: Tuple[str, ...]) -> None:
        """
        Adds new pages to the end of the book. Up to a maximum of 100 pages with
        1024 characters per page.

        Arguments
        - pages: A list of strings, each being a page
        """
        ...


    def getPageCount(self) -> int:
        """
        Gets the number of pages in the book.

        Returns
        - the number of pages in the book
        """
        ...


    def clone(self) -> "WritableBookMeta":
        ...
