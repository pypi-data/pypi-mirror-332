"""
Python module generated from Java source file com.google.common.net.HostSpecifier

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtIncompatible
from com.google.common.base import Preconditions
from com.google.common.net import *
from java.net import InetAddress
from java.text import ParseException
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class HostSpecifier:
    """
    A syntactically valid host specifier, suitable for use in a URI. This may be either a numeric IP
    address in IPv4 or IPv6 notation, or a domain name.
    
    Because this class is intended to represent host specifiers which can reasonably be used in a
    URI, the domain name case is further restricted to include only those domain names which end in a
    recognized public suffix; see InternetDomainName.isPublicSuffix() for details.
    
    Note that no network lookups are performed by any `HostSpecifier` methods. No attempt is
    made to verify that a provided specifier corresponds to a real or accessible host. Only syntactic
    and pattern-based checks are performed.
    
    If you know that a given string represents a numeric IP address, use InetAddresses to
    obtain and manipulate a java.net.InetAddress instance from it rather than using this
    class. Similarly, if you know that a given string represents a domain name, use InternetDomainName rather than this class.

    Author(s)
    - Craig Berry

    Since
    - 5.0
    """

    @staticmethod
    def fromValid(specifier: str) -> "HostSpecifier":
        """
        Returns a `HostSpecifier` built from the provided `specifier`, which is already
        known to be valid. If the `specifier` might be invalid, use .from(String)
        instead.
        
        The specifier must be in one of these formats:
        
        
          - A domain name, like `google.com`
          - A IPv4 address string, like `127.0.0.1`
          - An IPv6 address string with or without brackets, like `[2001:db8::1]` or `2001:db8::1`

        Raises
        - IllegalArgumentException: if the specifier is not valid.
        """
        ...


    @staticmethod
    def from(specifier: str) -> "HostSpecifier":
        """
        Attempts to return a `HostSpecifier` for the given string, throwing an exception if
        parsing fails. Always use this method in preference to .fromValid(String) for a
        specifier that is not already known to be valid.

        Raises
        - ParseException: if the specifier is not valid.
        """
        ...


    @staticmethod
    def isValid(specifier: str) -> bool:
        """
        Determines whether `specifier` represents a valid HostSpecifier as described in
        the documentation for .fromValid(String).
        """
        ...


    def equals(self, other: "Object") -> bool:
        ...


    def hashCode(self) -> int:
        ...


    def toString(self) -> str:
        """
        Returns a string representation of the host specifier suitable for inclusion in a URI. If the
        host specifier is a domain name, the string will be normalized to all lower case. If the
        specifier was an IPv6 address without brackets, brackets are added so that the result will be
        usable in the host part of a URI.
        """
        ...
