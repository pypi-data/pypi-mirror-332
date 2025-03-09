"""
Python module generated from Java source file java.net.Inet4Address

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import ObjectStreamException
from java.net import *
from typing import Any, Callable, Iterable, Tuple


class Inet4Address(InetAddress):

    def isMulticastAddress(self) -> bool:
        """
        Utility routine to check if the InetAddress is an
        IP multicast address. IP multicast address is a Class D
        address i.e first four bits of the address are 1110.

        Returns
        - a `boolean` indicating if the InetAddress is
        an IP multicast address
        """
        ...


    def isAnyLocalAddress(self) -> bool:
        """
        Utility routine to check if the InetAddress is a wildcard address.

        Returns
        - a `boolean` indicating if the InetAddress is
                a wildcard address.
        """
        ...


    def isLoopbackAddress(self) -> bool:
        """
        Utility routine to check if the InetAddress is a loopback address.

        Returns
        - a `boolean` indicating if the InetAddress is
        a loopback address; or False otherwise.
        """
        ...


    def isLinkLocalAddress(self) -> bool:
        """
        Utility routine to check if the InetAddress is an link local address.

        Returns
        - a `boolean` indicating if the InetAddress is
        a link local address; or False if address is not a link local unicast address.
        """
        ...


    def isSiteLocalAddress(self) -> bool:
        """
        Utility routine to check if the InetAddress is a site local address.

        Returns
        - a `boolean` indicating if the InetAddress is
        a site local address; or False if address is not a site local unicast address.
        """
        ...


    def isMCGlobal(self) -> bool:
        """
        Utility routine to check if the multicast address has global scope.

        Returns
        - a `boolean` indicating if the address has
                is a multicast address of global scope, False if it is not
                of global scope or it is not a multicast address
        """
        ...


    def isMCNodeLocal(self) -> bool:
        """
        Utility routine to check if the multicast address has node scope.

        Returns
        - a `boolean` indicating if the address has
                is a multicast address of node-local scope, False if it is not
                of node-local scope or it is not a multicast address
        """
        ...


    def isMCLinkLocal(self) -> bool:
        """
        Utility routine to check if the multicast address has link scope.

        Returns
        - a `boolean` indicating if the address has
                is a multicast address of link-local scope, False if it is not
                of link-local scope or it is not a multicast address
        """
        ...


    def isMCSiteLocal(self) -> bool:
        """
        Utility routine to check if the multicast address has site scope.

        Returns
        - a `boolean` indicating if the address has
                is a multicast address of site-local scope, False if it is not
                of site-local scope or it is not a multicast address
        """
        ...


    def isMCOrgLocal(self) -> bool:
        """
        Utility routine to check if the multicast address has organization scope.

        Returns
        - a `boolean` indicating if the address has
                is a multicast address of organization-local scope,
                False if it is not of organization-local scope
                or it is not a multicast address
        """
        ...


    def getAddress(self) -> list[int]:
        """
        Returns the raw IP address of this `InetAddress`
        object. The result is in network byte order: the highest order
        byte of the address is in `getAddress()[0]`.

        Returns
        - the raw IP address of this object.
        """
        ...


    def getHostAddress(self) -> str:
        """
        Returns the IP address string in textual presentation form.

        Returns
        - the raw IP address in a string format.
        """
        ...


    def hashCode(self) -> int:
        """
        Returns a hashcode for this IP address.

        Returns
        - a hash code value for this IP address.
        """
        ...


    def equals(self, obj: "Object") -> bool:
        """
        Compares this object against the specified object.
        The result is `True` if and only if the argument is
        not `null` and it represents the same IP address as
        this object.
        
        Two instances of `InetAddress` represent the same IP
        address if the length of the byte arrays returned by
        `getAddress` is the same for both, and each of the
        array components is the same for the byte arrays.

        Arguments
        - obj: the object to compare against.

        Returns
        - `True` if the objects are the same;
                 `False` otherwise.

        See
        - java.net.InetAddress.getAddress()
        """
        ...
