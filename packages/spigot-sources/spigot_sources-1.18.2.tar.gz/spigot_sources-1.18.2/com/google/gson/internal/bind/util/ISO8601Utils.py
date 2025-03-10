"""
Python module generated from Java source file com.google.gson.internal.bind.util.ISO8601Utils

Java source file obtained from artifact gson version 2.8.9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson.internal.bind.util import *
from java.text import ParseException
from java.text import ParsePosition
from java.util import *
from typing import Any, Callable, Iterable, Tuple


class ISO8601Utils:

    @staticmethod
    def format(date: "Date") -> str:
        """
        Format a date into 'yyyy-MM-ddThh:mm:ssZ' (default timezone, no milliseconds precision)

        Arguments
        - date: the date to format

        Returns
        - the date formatted as 'yyyy-MM-ddThh:mm:ssZ'
        """
        ...


    @staticmethod
    def format(date: "Date", millis: bool) -> str:
        """
        Format a date into 'yyyy-MM-ddThh:mm:ss[.sss]Z' (GMT timezone)

        Arguments
        - date: the date to format
        - millis: True to include millis precision otherwise False

        Returns
        - the date formatted as 'yyyy-MM-ddThh:mm:ss[.sss]Z'
        """
        ...


    @staticmethod
    def format(date: "Date", millis: bool, tz: "TimeZone") -> str:
        """
        Format date into yyyy-MM-ddThh:mm:ss[.sss][Z|[+-]hh:mm]

        Arguments
        - date: the date to format
        - millis: True to include millis precision otherwise False
        - tz: timezone to use for the formatting (UTC will produce 'Z')

        Returns
        - the date formatted as yyyy-MM-ddThh:mm:ss[.sss][Z|[+-]hh:mm]
        """
        ...


    @staticmethod
    def parse(date: str, pos: "ParsePosition") -> "Date":
        """
        Parse a date from ISO-8601 formatted string. It expects a format
        [yyyy-MM-dd|yyyyMMdd][T(hh:mm[:ss[.sss]]|hhmm[ss[.sss]])]?[Z|[+-]hh[:mm]]]

        Arguments
        - date: ISO string to parse in the appropriate format.
        - pos: The position to start parsing from, updated to where parsing stopped.

        Returns
        - the parsed date

        Raises
        - ParseException: if the date is not in the appropriate format
        """
        ...
