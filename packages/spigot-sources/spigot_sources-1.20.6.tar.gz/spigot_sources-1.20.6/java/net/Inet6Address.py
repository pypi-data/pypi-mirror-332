"""
Python module generated from Java source file java.net.Inet6Address

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import IOException
from java.io import InvalidObjectException
from java.io import ObjectInputStream
from java.io import ObjectOutputStream
from java.io import ObjectStreamField
from java.net import *
from java.util import Arrays
from java.util import Enumeration
from typing import Any, Callable, Iterable, Tuple


class Inet6Address(InetAddress):

    @staticmethod
    def getByAddress(host: str, addr: list[int], nif: "NetworkInterface") -> "Inet6Address":
        """
        Create an Inet6Address in the exact manner of InetAddress.getByAddress(String,byte[]) except that the IPv6 scope_id is
        set to the value corresponding to the given interface for the address
        type specified in `addr`. The call will fail with an
        UnknownHostException if the given interface does not have a numeric
        scope_id assigned for the given address type (e.g. link-local or site-local).
        See <a href="Inet6Address.html#scoped">here</a> for a description of IPv6
        scoped addresses.

        Arguments
        - host: the specified host
        - addr: the raw IP address in network byte order
        - nif: an interface this address must be associated with.

        Returns
        - an Inet6Address object created from the raw IP address.

        Raises
        - UnknownHostException: if IP address is of illegal length, or if the interface does not
                 have a numeric scope_id assigned for the given address type.

        Since
        - 1.5
        """
        ...


    @staticmethod
    def getByAddress(host: str, addr: list[int], scope_id: int) -> "Inet6Address":
        """
        Create an Inet6Address in the exact manner of InetAddress.getByAddress(String,byte[]) except that the IPv6 scope_id is
        set to the given numeric value. The scope_id is not checked to determine
        if it corresponds to any interface on the system.
        See <a href="Inet6Address.html#scoped">here</a> for a description of IPv6
        scoped addresses.

        Arguments
        - host: the specified host
        - addr: the raw IP address in network byte order
        - scope_id: the numeric scope_id for the address.

        Returns
        - an Inet6Address object created from the raw IP address.

        Raises
        - UnknownHostException: if IP address is of illegal length.

        Since
        - 1.5
        """
        ...


    def isMulticastAddress(self) -> bool:
        """
        Utility routine to check if the InetAddress is an IP multicast
        address. 11111111 at the start of the address identifies the
        address as being a multicast address.

        Returns
        - a `boolean` indicating if the InetAddress is an IP
                multicast address
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
        - a `boolean` indicating if the InetAddress is a loopback
                address; or False otherwise.
        """
        ...


    def isLinkLocalAddress(self) -> bool:
        """
        Utility routine to check if the InetAddress is an link local address.

        Returns
        - a `boolean` indicating if the InetAddress is a link local
                address; or False if address is not a link local unicast address.
        """
        ...


    def isSiteLocalAddress(self) -> bool:
        """
        Utility routine to check if the InetAddress is a site local address.

        Returns
        - a `boolean` indicating if the InetAddress is a site local
                address; or False if address is not a site local unicast address.
        """
        ...


    def isMCGlobal(self) -> bool:
        """
        Utility routine to check if the multicast address has global scope.

        Returns
        - a `boolean` indicating if the address has is a multicast
                address of global scope, False if it is not of global scope or
                it is not a multicast address
        """
        ...


    def isMCNodeLocal(self) -> bool:
        """
        Utility routine to check if the multicast address has node scope.

        Returns
        - a `boolean` indicating if the address has is a multicast
                address of node-local scope, False if it is not of node-local
                scope or it is not a multicast address
        """
        ...


    def isMCLinkLocal(self) -> bool:
        """
        Utility routine to check if the multicast address has link scope.

        Returns
        - a `boolean` indicating if the address has is a multicast
                address of link-local scope, False if it is not of link-local
                scope or it is not a multicast address
        """
        ...


    def isMCSiteLocal(self) -> bool:
        """
        Utility routine to check if the multicast address has site scope.

        Returns
        - a `boolean` indicating if the address has is a multicast
                address of site-local scope, False if it is not  of site-local
                scope or it is not a multicast address
        """
        ...


    def isMCOrgLocal(self) -> bool:
        """
        Utility routine to check if the multicast address has organization scope.

        Returns
        - a `boolean` indicating if the address has is a multicast
                address of organization-local scope, False if it is not of
                organization-local scope or it is not a multicast address
        """
        ...


    def getAddress(self) -> list[int]:
        """
        Returns the raw IP address of this `InetAddress` object. The result
        is in network byte order: the highest order byte of the address is in
        `getAddress()[0]`.

        Returns
        - the raw IP address of this object.
        """
        ...


    def getScopeId(self) -> int:
        """
        Returns the numeric scopeId, if this instance is associated with
        an interface. If no scoped_id is set, the returned value is zero.

        Returns
        - the scopeId, or zero if not set.

        Since
        - 1.5
        """
        ...


    def getScopedInterface(self) -> "NetworkInterface":
        """
        Returns the scoped interface, if this instance was created with
        a scoped interface.

        Returns
        - the scoped interface, or null if not set.

        Since
        - 1.5
        """
        ...


    def getHostAddress(self) -> str:
        """
        Returns the IP address string in textual presentation. If the instance
        was created specifying a scope identifier then the scope id is appended
        to the IP address preceded by a "%" (per-cent) character. This can be
        either a numeric value or a string, depending on which was used to create
        the instance.

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
        Compares this object against the specified object. The result is `True` if and only if the argument is not `null` and it represents
        the same IP address as this object.
        
         Two instances of `InetAddress` represent the same IP address
        if the length of the byte arrays returned by `getAddress` is the
        same for both, and each of the array components is the same for the byte
        arrays.

        Arguments
        - obj: the object to compare against.

        Returns
        - `True` if the objects are the same; `False` otherwise.

        See
        - java.net.InetAddress.getAddress()
        """
        ...


    def isIPv4CompatibleAddress(self) -> bool:
        """
        Utility routine to check if the InetAddress is an
        IPv4 compatible IPv6 address.

        Returns
        - a `boolean` indicating if the InetAddress is an IPv4
                compatible IPv6 address; or False if address is IPv4 address.
        """
        ...
