"""
Python module generated from Java source file java.net.NetworkInterface

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.net import *
from java.util import Arrays
from java.util import Enumeration
from java.util import NoSuchElementException
from java.util import Spliterator
from java.util.stream import Stream
from java.util.stream import StreamSupport
from typing import Any, Callable, Iterable, Tuple


class NetworkInterface:
    """
    This class represents a Network Interface made up of a name,
    and a list of IP addresses assigned to this interface.
    It is used to identify the local interface on which a multicast group
    is joined.
    
    Interfaces are normally known by names such as "le0".

    Since
    - 1.4
    """

    def getName(self) -> str:
        """
        Get the name of this network interface.

        Returns
        - the name of this network interface
        """
        ...


    def getInetAddresses(self) -> "Enumeration"["InetAddress"]:
        """
        Get an Enumeration with all or a subset of the InetAddresses bound to
        this network interface.
        
        If there is a security manager, its `checkConnect`
        method is called for each InetAddress. Only InetAddresses where
        the `checkConnect` doesn't throw a SecurityException
        will be returned in the Enumeration. However, if the caller has the
        NetPermission("getNetworkInformation") permission, then all
        InetAddresses are returned.

        Returns
        - an Enumeration object with all or a subset of the InetAddresses
        bound to this network interface

        See
        - .inetAddresses()
        """
        ...


    def inetAddresses(self) -> "Stream"["InetAddress"]:
        """
        Get a Stream of all or a subset of the InetAddresses bound to this
        network interface.
        
        If there is a security manager, its `checkConnect`
        method is called for each InetAddress. Only InetAddresses where
        the `checkConnect` doesn't throw a SecurityException will be
        returned in the Stream. However, if the caller has the
        NetPermission("getNetworkInformation") permission, then all
        InetAddresses are returned.

        Returns
        - a Stream object with all or a subset of the InetAddresses
        bound to this network interface

        Since
        - 9
        """
        ...


    def getInterfaceAddresses(self) -> "java.util.List"["InterfaceAddress"]:
        """
        Get a List of all or a subset of the `InterfaceAddresses`
        of this network interface.
        
        If there is a security manager, its `checkConnect`
        method is called with the InetAddress for each InterfaceAddress.
        Only InterfaceAddresses where the `checkConnect` doesn't throw
        a SecurityException will be returned in the List.

        Returns
        - a `List` object with all or a subset of the
                InterfaceAddress of this network interface

        Since
        - 1.6
        """
        ...


    def getSubInterfaces(self) -> "Enumeration"["NetworkInterface"]:
        """
        Get an Enumeration with all the subinterfaces (also known as virtual
        interfaces) attached to this network interface.
        
        For instance eth0:1 will be a subinterface to eth0.

        Returns
        - an Enumeration object with all of the subinterfaces
        of this network interface

        See
        - .subInterfaces()

        Since
        - 1.6
        """
        ...


    def subInterfaces(self) -> "Stream"["NetworkInterface"]:
        """
        Get a Stream of all subinterfaces (also known as virtual
        interfaces) attached to this network interface.

        Returns
        - a Stream object with all of the subinterfaces
        of this network interface

        Since
        - 9
        """
        ...


    def getParent(self) -> "NetworkInterface":
        """
        Returns the parent NetworkInterface of this interface if this is
        a subinterface, or `null` if it is a physical
        (non virtual) interface or has no parent.

        Returns
        - The `NetworkInterface` this interface is attached to.

        Since
        - 1.6
        """
        ...


    def getIndex(self) -> int:
        """
        Returns the index of this network interface. The index is an integer greater
        or equal to zero, or `-1` for unknown. This is a system specific value
        and interfaces with the same name can have different indexes on different
        machines.

        Returns
        - the index of this network interface or `-1` if the index is
                unknown

        See
        - .getByIndex(int)

        Since
        - 1.7
        """
        ...


    def getDisplayName(self) -> str:
        """
        Get the display name of this network interface.
        A display name is a human readable String describing the network
        device.

        Returns
        - a non-empty string representing the display name of this network
                interface, or null if no display name is available.
        """
        ...


    @staticmethod
    def getByName(name: str) -> "NetworkInterface":
        """
        Searches for the network interface with the specified name.

        Arguments
        - name: The name of the network interface.

        Returns
        - A `NetworkInterface` with the specified name,
                 or `null` if there is no network interface
                 with the specified name.

        Raises
        - SocketException: If an I/O error occurs.
        - NullPointerException: If the specified name is `null`.
        """
        ...


    @staticmethod
    def getByIndex(index: int) -> "NetworkInterface":
        """
        Get a network interface given its index.

        Arguments
        - index: an integer, the index of the interface

        Returns
        - the NetworkInterface obtained from its index, or `null` if
                there is no interface with such an index on the system

        Raises
        - SocketException: if an I/O error occurs.
        - IllegalArgumentException: if index has a negative value

        See
        - .getIndex()

        Since
        - 1.7
        """
        ...


    @staticmethod
    def getByInetAddress(addr: "InetAddress") -> "NetworkInterface":
        """
        Convenience method to search for a network interface that
        has the specified Internet Protocol (IP) address bound to
        it.
        
        If the specified IP address is bound to multiple network
        interfaces it is not defined which network interface is
        returned.

        Arguments
        - addr: The `InetAddress` to search with.

        Returns
        - A `NetworkInterface`
                 or `null` if there is no network interface
                 with the specified IP address.

        Raises
        - SocketException: If an I/O error occurs.
        - NullPointerException: If the specified address is `null`.
        """
        ...


    @staticmethod
    def getNetworkInterfaces() -> "Enumeration"["NetworkInterface"]:
        """
        Returns an `Enumeration` of all the interfaces on this machine. The
        `Enumeration` contains at least one element, possibly representing
        a loopback interface that only supports communication between entities on
        this machine.

        Returns
        - an Enumeration of NetworkInterfaces found on this machine

        Raises
        - SocketException: if an I/O error occurs,
                    or if the platform does not have at least one configured
                    network interface.

        See
        - .networkInterfaces()

        Unknown Tags
        - this method can be used in combination with
        .getInetAddresses() to obtain all IP addresses for this node
        """
        ...


    @staticmethod
    def networkInterfaces() -> "Stream"["NetworkInterface"]:
        """
        Returns a `Stream` of all the interfaces on this machine.  The
        `Stream` contains at least one interface, possibly representing a
        loopback interface that only supports communication between entities on
        this machine.

        Returns
        - a Stream of NetworkInterfaces found on this machine

        Raises
        - SocketException: if an I/O error occurs,
                    or if the platform does not have at least one configured
                    network interface.

        Since
        - 9

        Unknown Tags
        - this method can be used in combination with
        .inetAddresses()} to obtain a stream of all IP addresses for
        this node, for example:
        ``` `Stream<InetAddress> addrs = NetworkInterface.networkInterfaces()
            .flatMap(NetworkInterface::inetAddresses);````
        """
        ...


    def isUp(self) -> bool:
        ...


    def isLoopback(self) -> bool:
        ...


    def isPointToPoint(self) -> bool:
        ...


    def supportsMulticast(self) -> bool:
        ...


    def getHardwareAddress(self) -> list[int]:
        """
        Returns the hardware address (usually MAC) of the interface if it
        has one and if it can be accessed given the current privileges.
        If a security manager is set, then the caller must have
        the permission NetPermission("getNetworkInformation").

        Returns
        - a byte array containing the address, or `null` if
                 the address doesn't exist, is not accessible or a security
                 manager is set and the caller does not have the permission
                 NetPermission("getNetworkInformation")

        Raises
        - SocketException: if an I/O error occurs.

        Since
        - 1.6
        """
        ...


    def getMTU(self) -> int:
        """
        Returns the Maximum Transmission Unit (MTU) of this interface.

        Returns
        - the value of the MTU for that interface.

        Raises
        - SocketException: if an I/O error occurs.

        Since
        - 1.6
        """
        ...


    def isVirtual(self) -> bool:
        """
        Returns whether this interface is a virtual interface (also called
        subinterface).
        Virtual interfaces are, on some systems, interfaces created as a child
        of a physical interface and given different settings (like address or
        MTU). Usually the name of the interface will the name of the parent
        followed by a colon (:) and a number identifying the child since there
        can be several virtual interfaces attached to a single physical
        interface.

        Returns
        - `True` if this interface is a virtual interface.

        Since
        - 1.6
        """
        ...


    def equals(self, obj: "Object") -> bool:
        """
        Compares this object against the specified object.
        The result is `True` if and only if the argument is
        not `null` and it represents the same NetworkInterface
        as this object.
        
        Two instances of `NetworkInterface` represent the same
        NetworkInterface if both the name and the set of `InetAddress`es
        bound to the interfaces are equal.

        Arguments
        - obj: the object to compare against.

        Returns
        - `True` if the objects are the same;
                 `False` otherwise.

        See
        - java.net.InetAddress.getAddress()

        Unknown Tags
        - two `NetworkInterface` objects referring to the same
        underlying interface may not compare equal if the addresses
        of the underlying interface are being dynamically updated by
        the system.
        """
        ...


    def hashCode(self) -> int:
        ...


    def toString(self) -> str:
        ...
