"""
Python module generated from Java source file org.bukkit.inventory.meta.BookMeta

Java source file obtained from artifact spigot-api version 1.20.2-R0.1-20231205.164257-71

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from net.md_5.bungee.api.chat import BaseComponent
from org.bukkit import Material
from org.bukkit.inventory.meta import *
from typing import Any, Callable, Iterable, Tuple


class BookMeta(ItemMeta):
    """
    Represents a book (Material.WRITABLE_BOOK or Material.WRITTEN_BOOK) that can have a title, an author, and pages.
    """

    def hasTitle(self) -> bool:
        """
        Checks for the existence of a title in the book.

        Returns
        - True if the book has a title
        """
        ...


    def getTitle(self) -> str:
        """
        Gets the title of the book.
        
        Plugins should check that hasTitle() returns True before calling this
        method.

        Returns
        - the title of the book
        """
        ...


    def setTitle(self, title: str) -> bool:
        """
        Sets the title of the book.
        
        Limited to 32 characters. Removes title when given null.

        Arguments
        - title: the title to set

        Returns
        - True if the title was successfully set
        """
        ...


    def hasAuthor(self) -> bool:
        """
        Checks for the existence of an author in the book.

        Returns
        - True if the book has an author
        """
        ...


    def getAuthor(self) -> str:
        """
        Gets the author of the book.
        
        Plugins should check that hasAuthor() returns True before calling this
        method.

        Returns
        - the author of the book
        """
        ...


    def setAuthor(self, author: str) -> None:
        """
        Sets the author of the book. Removes author when given null.

        Arguments
        - author: the author to set
        """
        ...


    def hasGeneration(self) -> bool:
        """
        Checks for the existence of generation level in the book.

        Returns
        - True if the book has a generation level
        """
        ...


    def getGeneration(self) -> "Generation":
        """
        Gets the generation of the book.
        
        Plugins should check that hasGeneration() returns True before calling
        this method.

        Returns
        - the generation of the book
        """
        ...


    def setGeneration(self, generation: "Generation") -> None:
        """
        Sets the generation of the book. Removes generation when given null.

        Arguments
        - generation: the generation to set
        """
        ...


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
        
        The data can be up to 256 characters in length, additional characters
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
        pages. Maximum 100 pages with 256 characters per page.

        Arguments
        - pages: A list of pages to set the book to use
        """
        ...


    def setPages(self, *pages: Tuple[str, ...]) -> None:
        """
        Clears the existing book pages, and sets the book to use the provided
        pages. Maximum 50 pages with 256 characters per page.

        Arguments
        - pages: A list of strings, each being a page
        """
        ...


    def addPage(self, *pages: Tuple[str, ...]) -> None:
        """
        Adds new pages to the end of the book. Up to a maximum of 50 pages with
        256 characters per page.

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


    def clone(self) -> "BookMeta":
        ...


    def spigot(self) -> "Spigot":
        ...


    class Spigot:

        def getPage(self, page: int) -> list["BaseComponent"]:
            """
            Gets the specified page in the book. The given page must exist.

            Arguments
            - page: the page number to get

            Returns
            - the page from the book
            """
            ...


        def setPage(self, page: int, *data: Tuple["BaseComponent", ...]) -> None:
            """
            Sets the specified page in the book. Pages of the book must be
            contiguous.
            
            The data can be up to 256 characters in length, additional characters
            are truncated.

            Arguments
            - page: the page number to set
            - data: the data to set for that page
            """
            ...


        def getPages(self) -> list[list["BaseComponent"]]:
            """
            Gets all the pages in the book.

            Returns
            - list of all the pages in the book
            """
            ...


        def setPages(self, pages: list[list["BaseComponent"]]) -> None:
            """
            Clears the existing book pages, and sets the book to use the provided
            pages. Maximum 50 pages with 256 characters per page.

            Arguments
            - pages: A list of pages to set the book to use
            """
            ...


        def setPages(self, *pages: Tuple[list["BaseComponent"], ...]) -> None:
            """
            Clears the existing book pages, and sets the book to use the provided
            pages. Maximum 50 pages with 256 characters per page.

            Arguments
            - pages: A list of component arrays, each being a page
            """
            ...


        def addPage(self, *pages: Tuple[list["BaseComponent"], ...]) -> None:
            """
            Adds new pages to the end of the book. Up to a maximum of 50 pages
            with 256 characters per page.

            Arguments
            - pages: A list of component arrays, each being a page
            """
            ...
