"""
Python module generated from Java source file java.net.InetSocketAddress

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import IOException
from java.io import InvalidObjectException
from java.io import ObjectInputStream
from java.io import ObjectOutputStream
from java.io import ObjectStreamException
from java.io import ObjectStreamField
from java.net import *
from typing import Any, Callable, Iterable, Tuple


class InetSocketAddress(SocketAddress):
    """
    This class implements an IP Socket Address (IP address + port number)
    It can also be a pair (hostname + port number), in which case an attempt
    will be made to resolve the hostname. If resolution fails then the address
    is said to be <I>unresolved</I> but can still be used on some circumstances
    like connecting through a proxy.
    
    It provides an immutable object used by sockets for binding, connecting, or
    as returned values.
    
    The *wildcard* is a special local IP address. It usually means "any"
    and can only be used for `bind` operations.

    See
    - java.net.ServerSocket

    Since
    - 1.4
    """

    def __init__(self, port: int):
        """
        Creates a socket address where the IP address is the wildcard address
        and the port number a specified value.
        
        A valid port value is between 0 and 65535.
        A port number of `zero` will let the system pick up an
        ephemeral port in a `bind` operation.

        Arguments
        - port: The port number

        Raises
        - IllegalArgumentException: if the port parameter is outside the specified
        range of valid port values.
        """
        ...


    def __init__(self, addr: "InetAddress", port: int):
        """
        Creates a socket address from an IP address and a port number.
        
        A valid port value is between 0 and 65535.
        A port number of `zero` will let the system pick up an
        ephemeral port in a `bind` operation.
        <P>
        A `null` address will assign the *wildcard* address.

        Arguments
        - addr: The IP address
        - port: The port number

        Raises
        - IllegalArgumentException: if the port parameter is outside the specified
        range of valid port values.
        """
        ...


    def __init__(self, hostname: str, port: int):
        """
        Creates a socket address from a hostname and a port number.
        
        An attempt will be made to resolve the hostname into an InetAddress.
        If that attempt fails, the address will be flagged as <I>unresolved</I>.
        
        If there is a security manager, its `checkConnect` method
        is called with the host name as its argument to check the permission
        to resolve it. This could result in a SecurityException.
        <P>
        A valid port value is between 0 and 65535.
        A port number of `zero` will let the system pick up an
        ephemeral port in a `bind` operation.

        Arguments
        - hostname: the Host name
        - port: The port number

        Raises
        - IllegalArgumentException: if the port parameter is outside the range
        of valid port values, or if the hostname parameter is `null`.
        - SecurityException: if a security manager is present and
                                  permission to resolve the host name is
                                  denied.

        See
        - .isUnresolved()
        """
        ...


    @staticmethod
    def createUnresolved(host: str, port: int) -> "InetSocketAddress":
        """
        Creates an unresolved socket address from a hostname and a port number.
        
        No attempt will be made to resolve the hostname into an InetAddress.
        The address will be flagged as <I>unresolved</I>.
        
        A valid port value is between 0 and 65535.
        A port number of `zero` will let the system pick up an
        ephemeral port in a `bind` operation.

        Arguments
        - host: the Host name
        - port: The port number

        Returns
        - an `InetSocketAddress` representing the unresolved
                 socket address

        Raises
        - IllegalArgumentException: if the port parameter is outside
                         the range of valid port values, or if the hostname
                         parameter is `null`.

        See
        - .isUnresolved()

        Since
        - 1.5
        """
        ...


    def getPort(self) -> int:
        """
        Gets the port number.

        Returns
        - the port number.
        """
        ...


    def getAddress(self) -> "InetAddress":
        """
        Gets the `InetAddress`.

        Returns
        - the InetAddress or `null` if it is unresolved.
        """
        ...


    def getHostName(self) -> str:
        """
        Gets the `hostname`.
        Note: This method may trigger a name service reverse lookup if the
        address was created with a literal IP address.

        Returns
        - the hostname part of the address.
        """
        ...


    def getHostString(self) -> str:
        """
        Returns the hostname, or the String form of the address if it
        doesn't have a hostname (it was created using a literal).
        This has the benefit of **not** attempting a reverse lookup.

        Returns
        - the hostname, or String representation of the address.

        Since
        - 1.7
        """
        ...


    def isUnresolved(self) -> bool:
        """
        Checks whether the address has been resolved or not.

        Returns
        - `True` if the hostname couldn't be resolved into
                 an `InetAddress`.
        """
        ...


    def toString(self) -> str:
        """
        Constructs a string representation of this InetSocketAddress.
        This string is constructed by calling InetAddress.toString()
        on the InetAddress and concatenating the port number (with a colon).
        
        If the address is an IPv6 address, the IPv6 literal is enclosed in
        square brackets, for example: `"localhost/[0:0:0:0:0:0:0:1]:80"`.
        If the address is .isUnresolved() unresolved,
        `<unresolved>` is displayed in place of the address literal, for
        example `"foo/<unresolved>:80"`.
        
        To retrieve a string representation of the hostname or the address, use
        .getHostString(), rather than parsing the string returned by this
        .toString() method.

        Returns
        - a string representation of this object.
        """
        ...


    def equals(self, obj: "Object") -> bool:
        """
        Compares this object against the specified object.
        The result is `True` if and only if the argument is
        not `null` and it represents the same address as
        this object.
        
        Two instances of `InetSocketAddress` represent the same
        address if both the InetAddresses (or hostnames if it is unresolved) and port
        numbers are equal.
        If both addresses are unresolved, then the hostname and the port number
        are compared.
        
        Note: Hostnames are case insensitive. e.g. "FooBar" and "foobar" are
        considered equal.

        Arguments
        - obj: the object to compare against.

        Returns
        - `True` if the objects are the same;
                 `False` otherwise.

        See
        - java.net.InetAddress.equals(java.lang.Object)
        """
        ...


    def hashCode(self) -> int:
        """
        Returns a hashcode for this socket address.

        Returns
        - a hash code value for this socket address.
        """
        ...
