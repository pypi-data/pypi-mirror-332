"""
Python module generated from Java source file java.net.InetAddress

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import File
from java.io import IOException
from java.io import InvalidObjectException
from java.io import ObjectInputStream
from java.io.ObjectInputStream import GetField
from java.io import ObjectOutputStream
from java.io.ObjectOutputStream import PutField
from java.io import ObjectStreamException
from java.io import ObjectStreamField
from java.net import *
from java.util import Arrays
from java.util import NavigableSet
from java.util import Objects
from java.util import Scanner
from java.util.concurrent import ConcurrentHashMap
from java.util.concurrent import ConcurrentMap
from java.util.concurrent import ConcurrentSkipListSet
from java.util.concurrent.atomic import AtomicLong
from jdk.internal.access import JavaNetInetAddressAccess
from jdk.internal.access import SharedSecrets
from sun.net import InetAddressCachePolicy
from sun.net.util import IPAddressUtil
from sun.nio.cs import UTF_8
from sun.security.action import *
from typing import Any, Callable, Iterable, Tuple


class InetAddress(Serializable):
    """
    This class represents an Internet Protocol (IP) address.
    
     An IP address is either a 32-bit or 128-bit unsigned number
    used by IP, a lower-level protocol on which protocols like UDP and
    TCP are built. The IP address architecture is defined by <a
    href="http://www.ietf.org/rfc/rfc790.txt">*RFC&nbsp;790:
    Assigned Numbers*</a>, <a
    href="http://www.ietf.org/rfc/rfc1918.txt"> *RFC&nbsp;1918:
    Address Allocation for Private Internets*</a>, <a
    href="http://www.ietf.org/rfc/rfc2365.txt">*RFC&nbsp;2365:
    Administratively Scoped IP Multicast*</a>, and <a
    href="http://www.ietf.org/rfc/rfc2373.txt">*RFC&nbsp;2373: IP
    Version 6 Addressing Architecture*</a>. An instance of an
    InetAddress consists of an IP address and possibly its
    corresponding host name (depending on whether it is constructed
    with a host name or whether it has already done reverse host name
    resolution).
    
    <h2> Address types </h2>
    
    <table class="striped" style="margin-left:2em">
      <caption style="display:none">Description of unicast and multicast address types</caption>
      <thead>
      <tr><th scope="col">Address Type</th><th scope="col">Description</th></tr>
      </thead>
      <tbody>
      <tr><th scope="row" style="vertical-align:top">unicast</th>
          <td>An identifier for a single interface. A packet sent to
            a unicast address is delivered to the interface identified by
            that address.
    
             The Unspecified Address -- Also called anylocal or wildcard
            address. It must never be assigned to any node. It indicates the
            absence of an address. One example of its use is as the target of
            bind, which allows a server to accept a client connection on any
            interface, in case the server host has multiple interfaces.
    
             The *unspecified* address must not be used as
            the destination address of an IP packet.
    
             The *Loopback* Addresses -- This is the address
            assigned to the loopback interface. Anything sent to this
            IP address loops around and becomes IP input on the local
            host. This address is often used when testing a
            client.</td></tr>
      <tr><th scope="row" style="vertical-align:top">multicast</th>
          <td>An identifier for a set of interfaces (typically belonging
            to different nodes). A packet sent to a multicast address is
            delivered to all interfaces identified by that address.</td></tr>
    </tbody>
    </table>
    
    <h3> IP address scope </h3>
    
     *Link-local* addresses are designed to be used for addressing
    on a single link for purposes such as auto-address configuration,
    neighbor discovery, or when no routers are present.
    
     *Site-local* addresses are designed to be used for addressing
    inside of a site without the need for a global prefix.
    
     *Global* addresses are unique across the internet.
    
    <h3> Textual representation of IP addresses </h3>
    
    The textual representation of an IP address is address family specific.
    
    
    
    For IPv4 address format, please refer to <A
    HREF="Inet4Address.html#format">Inet4Address#format</A>; For IPv6
    address format, please refer to <A
    HREF="Inet6Address.html#format">Inet6Address#format</A>.
    
    <P>There is a <a href="doc-files/net-properties.html#Ipv4IPv6">couple of
    System Properties</a> affecting how IPv4 and IPv6 addresses are used.</P>
    
    <h3> Host Name Resolution </h3>
    
    Host name-to-IP address *resolution* is accomplished through
    the use of a combination of local machine configuration information
    and network naming services such as the Domain Name System (DNS)
    and Network Information Service(NIS). The particular naming
    services(s) being used is by default the local machine configured
    one. For any host name, its corresponding IP address is returned.
    
     *Reverse name resolution* means that for any IP address,
    the host associated with the IP address is returned.
    
     The InetAddress class provides methods to resolve host names to
    their IP addresses and vice versa.
    
    <h3> InetAddress Caching </h3>
    
    The InetAddress class has a cache to store successful as well as
    unsuccessful host name resolutions.
    
     By default, when a security manager is installed, in order to
    protect against DNS spoofing attacks,
    the result of positive host name resolutions are
    cached forever. When a security manager is not installed, the default
    behavior is to cache entries for a finite (implementation dependent)
    period of time. The result of unsuccessful host
    name resolution is cached for a very short period of time (10
    seconds) to improve performance.
    
     If the default behavior is not desired, then a Java security property
    can be set to a different Time-to-live (TTL) value for positive
    caching. Likewise, a system admin can configure a different
    negative caching TTL value when needed.
    
     Two Java security properties control the TTL values used for
     positive and negative host name resolution caching:
    
    <dl style="margin-left:2em">
    <dt>**networkaddress.cache.ttl**</dt>
    <dd>Indicates the caching policy for successful name lookups from
    the name service. The value is specified as an integer to indicate
    the number of seconds to cache the successful lookup. The default
    setting is to cache for an implementation specific period of time.
    
    A value of -1 indicates "cache forever".
    </dd>
    <dt>**networkaddress.cache.negative.ttl** (default: 10)</dt>
    <dd>Indicates the caching policy for un-successful name lookups
    from the name service. The value is specified as an integer to
    indicate the number of seconds to cache the failure for
    un-successful lookups.
    
    A value of 0 indicates "never cache".
    A value of -1 indicates "cache forever".
    </dd>
    </dl>

    Author(s)
    - Chris Warth

    See
    - java.net.InetAddress.getLocalHost()

    Since
    - 1.0
    """

    def isMulticastAddress(self) -> bool:
        """
        Utility routine to check if the InetAddress is an
        IP multicast address.

        Returns
        - a `boolean` indicating if the InetAddress is
        an IP multicast address

        Since
        - 1.1
        """
        ...


    def isAnyLocalAddress(self) -> bool:
        """
        Utility routine to check if the InetAddress is a wildcard address.

        Returns
        - a `boolean` indicating if the InetAddress is
                a wildcard address.

        Since
        - 1.4
        """
        ...


    def isLoopbackAddress(self) -> bool:
        """
        Utility routine to check if the InetAddress is a loopback address.

        Returns
        - a `boolean` indicating if the InetAddress is
        a loopback address; or False otherwise.

        Since
        - 1.4
        """
        ...


    def isLinkLocalAddress(self) -> bool:
        """
        Utility routine to check if the InetAddress is an link local address.

        Returns
        - a `boolean` indicating if the InetAddress is
        a link local address; or False if address is not a link local unicast address.

        Since
        - 1.4
        """
        ...


    def isSiteLocalAddress(self) -> bool:
        """
        Utility routine to check if the InetAddress is a site local address.

        Returns
        - a `boolean` indicating if the InetAddress is
        a site local address; or False if address is not a site local unicast address.

        Since
        - 1.4
        """
        ...


    def isMCGlobal(self) -> bool:
        """
        Utility routine to check if the multicast address has global scope.

        Returns
        - a `boolean` indicating if the address has
                is a multicast address of global scope, False if it is not
                of global scope or it is not a multicast address

        Since
        - 1.4
        """
        ...


    def isMCNodeLocal(self) -> bool:
        """
        Utility routine to check if the multicast address has node scope.

        Returns
        - a `boolean` indicating if the address has
                is a multicast address of node-local scope, False if it is not
                of node-local scope or it is not a multicast address

        Since
        - 1.4
        """
        ...


    def isMCLinkLocal(self) -> bool:
        """
        Utility routine to check if the multicast address has link scope.

        Returns
        - a `boolean` indicating if the address has
                is a multicast address of link-local scope, False if it is not
                of link-local scope or it is not a multicast address

        Since
        - 1.4
        """
        ...


    def isMCSiteLocal(self) -> bool:
        """
        Utility routine to check if the multicast address has site scope.

        Returns
        - a `boolean` indicating if the address has
                is a multicast address of site-local scope, False if it is not
                of site-local scope or it is not a multicast address

        Since
        - 1.4
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

        Since
        - 1.4
        """
        ...


    def isReachable(self, timeout: int) -> bool:
        """
        Test whether that address is reachable. Best effort is made by the
        implementation to try to reach the host, but firewalls and server
        configuration may block requests resulting in a unreachable status
        while some specific ports may be accessible.
        A typical implementation will use ICMP ECHO REQUESTs if the
        privilege can be obtained, otherwise it will try to establish
        a TCP connection on port 7 (Echo) of the destination host.
        
        The timeout value, in milliseconds, indicates the maximum amount of time
        the try should take. If the operation times out before getting an
        answer, the host is deemed unreachable. A negative value will result
        in an IllegalArgumentException being thrown.

        Arguments
        - timeout: the time, in milliseconds, before the call aborts

        Returns
        - a `boolean` indicating if the address is reachable.

        Raises
        - IOException: if a network error occurs
        - IllegalArgumentException: if `timeout` is negative.

        Since
        - 1.5
        """
        ...


    def isReachable(self, netif: "NetworkInterface", ttl: int, timeout: int) -> bool:
        """
        Test whether that address is reachable. Best effort is made by the
        implementation to try to reach the host, but firewalls and server
        configuration may block requests resulting in a unreachable status
        while some specific ports may be accessible.
        A typical implementation will use ICMP ECHO REQUESTs if the
        privilege can be obtained, otherwise it will try to establish
        a TCP connection on port 7 (Echo) of the destination host.
        
        The `network interface` and `ttl` parameters
        let the caller specify which network interface the test will go through
        and the maximum number of hops the packets should go through.
        A negative value for the `ttl` will result in an
        IllegalArgumentException being thrown.
        
        The timeout value, in milliseconds, indicates the maximum amount of time
        the try should take. If the operation times out before getting an
        answer, the host is deemed unreachable. A negative value will result
        in an IllegalArgumentException being thrown.

        Arguments
        - netif: the NetworkInterface through which the
                           test will be done, or null for any interface
        - ttl: the maximum numbers of hops to try or 0 for the
                         default
        - timeout: the time, in milliseconds, before the call aborts

        Returns
        - a `boolean` indicating if the address is reachable.

        Raises
        - IllegalArgumentException: if either `timeout`
                                 or `ttl` are negative.
        - IOException: if a network error occurs

        Since
        - 1.5
        """
        ...


    def getHostName(self) -> str:
        """
        Gets the host name for this IP address.
        
        If this InetAddress was created with a host name,
        this host name will be remembered and returned;
        otherwise, a reverse name lookup will be performed
        and the result will be returned based on the system
        configured name lookup service. If a lookup of the name service
        is required, call
        .getCanonicalHostName() getCanonicalHostName.
        
        If there is a security manager, its
        `checkConnect` method is first called
        with the hostname and `-1`
        as its arguments to see if the operation is allowed.
        If the operation is not allowed, it will return
        the textual representation of the IP address.

        Returns
        - the host name for this IP address, or if the operation
           is not allowed by the security check, the textual
           representation of the IP address.

        See
        - SecurityManager.checkConnect
        """
        ...


    def getCanonicalHostName(self) -> str:
        """
        Gets the fully qualified domain name for this IP address.
        Best effort method, meaning we may not be able to return
        the FQDN depending on the underlying system configuration.
        
        If there is a security manager, this method first
        calls its `checkConnect` method
        with the hostname and `-1`
        as its arguments to see if the calling code is allowed to know
        the hostname for this IP address, i.e., to connect to the host.
        If the operation is not allowed, it will return
        the textual representation of the IP address.

        Returns
        - the fully qualified domain name for this IP address,
           or if the operation is not allowed by the security check,
           the textual representation of the IP address.

        See
        - SecurityManager.checkConnect

        Since
        - 1.4
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
        Returns the IP address string in textual presentation.

        Returns
        - the raw IP address in a string format.

        Since
        - 1.0.2
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


    def toString(self) -> str:
        """
        Converts this IP address to a `String`. The
        string returned is of the form: hostname / literal IP
        address.
        
        If the host name is unresolved, no reverse name service lookup
        is performed. The hostname part will be represented by an empty string.

        Returns
        - a string representation of this IP address.
        """
        ...


    @staticmethod
    def getByAddress(host: str, addr: list[int]) -> "InetAddress":
        """
        Creates an InetAddress based on the provided host name and IP address.
        No name service is checked for the validity of the address.
        
         The host name can either be a machine name, such as
        "`www.example.com`", or a textual representation of its IP
        address.
         No validity checking is done on the host name either.
        
         If addr specifies an IPv4 address an instance of Inet4Address
        will be returned; otherwise, an instance of Inet6Address
        will be returned.
        
         IPv4 address byte array must be 4 bytes long and IPv6 byte array
        must be 16 bytes long

        Arguments
        - host: the specified host
        - addr: the raw IP address in network byte order

        Returns
        - an InetAddress object created from the raw IP address.

        Raises
        - UnknownHostException: if IP address is of illegal length

        Since
        - 1.4
        """
        ...


    @staticmethod
    def getByName(host: str) -> "InetAddress":
        """
        Determines the IP address of a host, given the host's name.
        
         The host name can either be a machine name, such as
        "`www.example.com`", or a textual representation of its
        IP address. If a literal IP address is supplied, only the
        validity of the address format is checked.
        
         For `host` specified in literal IPv6 address,
        either the form defined in RFC 2732 or the literal IPv6 address
        format defined in RFC 2373 is accepted. IPv6 scoped addresses are also
        supported. See <a href="Inet6Address.html#scoped">here</a> for a description of IPv6
        scoped addresses.
        
         If the host is `null` or `host.length()` is equal
        to zero, then an `InetAddress` representing an address of the
        loopback interface is returned.
        See <a href="http://www.ietf.org/rfc/rfc3330.txt">RFC&nbsp;3330</a>
        section&nbsp;2 and <a href="http://www.ietf.org/rfc/rfc2373.txt">RFC&nbsp;2373</a>
        section&nbsp;2.5.3.
        
         If there is a security manager, and `host` is not `null`
        or `host.length()` is not equal to zero, the security manager's
        `checkConnect` method is called with the hostname and `-1`
        as its arguments to determine if the operation is allowed.

        Arguments
        - host: the specified host, or `null`.

        Returns
        - an IP address for the given host name.

        Raises
        - UnknownHostException: if no IP address for the
                      `host` could be found, or if a scope_id was specified
                      for a global IPv6 address.
        - SecurityException: if a security manager exists
                    and its checkConnect method doesn't allow the operation
        """
        ...


    @staticmethod
    def getAllByName(host: str) -> list["InetAddress"]:
        """
        Given the name of a host, returns an array of its IP addresses,
        based on the configured name service on the system.
        
         The host name can either be a machine name, such as
        "`www.example.com`", or a textual representation of its IP
        address. If a literal IP address is supplied, only the
        validity of the address format is checked.
        
         For `host` specified in *literal IPv6 address*,
        either the form defined in RFC 2732 or the literal IPv6 address
        format defined in RFC 2373 is accepted. A literal IPv6 address may
        also be qualified by appending a scoped zone identifier or scope_id.
        The syntax and usage of scope_ids is described
        <a href="Inet6Address.html#scoped">here</a>.
        
         If the host is `null` or `host.length()` is equal
        to zero, then an `InetAddress` representing an address of the
        loopback interface is returned.
        See <a href="http://www.ietf.org/rfc/rfc3330.txt">RFC&nbsp;3330</a>
        section&nbsp;2 and <a href="http://www.ietf.org/rfc/rfc2373.txt">RFC&nbsp;2373</a>
        section&nbsp;2.5.3. 
        
         If there is a security manager, and `host` is not `null`
        or `host.length()` is not equal to zero, the security manager's
        `checkConnect` method is called with the hostname and `-1`
        as its arguments to determine if the operation is allowed.

        Arguments
        - host: the name of the host, or `null`.

        Returns
        - an array of all the IP addresses for a given host name.

        Raises
        - UnknownHostException: if no IP address for the
                      `host` could be found, or if a scope_id was specified
                      for a global IPv6 address.
        - SecurityException: if a security manager exists and its
                      `checkConnect` method doesn't allow the operation.

        See
        - SecurityManager.checkConnect
        """
        ...


    @staticmethod
    def getLoopbackAddress() -> "InetAddress":
        """
        Returns the loopback address.
        
        The InetAddress returned will represent the IPv4
        loopback address, 127.0.0.1, or the IPv6 loopback
        address, ::1. The IPv4 loopback address returned
        is only one of many in the form 127.*.*.*

        Returns
        - the InetAddress loopback instance.

        Since
        - 1.7
        """
        ...


    @staticmethod
    def getByAddress(addr: list[int]) -> "InetAddress":
        """
        Returns an `InetAddress` object given the raw IP address .
        The argument is in network byte order: the highest order
        byte of the address is in `getAddress()[0]`.
        
         This method doesn't block, i.e. no reverse name service lookup
        is performed.
        
         IPv4 address byte array must be 4 bytes long and IPv6 byte array
        must be 16 bytes long

        Arguments
        - addr: the raw IP address in network byte order

        Returns
        - an InetAddress object created from the raw IP address.

        Raises
        - UnknownHostException: if IP address is of illegal length

        Since
        - 1.4
        """
        ...


    @staticmethod
    def getLocalHost() -> "InetAddress":
        """
        Returns the address of the local host. This is achieved by retrieving
        the name of the host from the system, then resolving that name into
        an `InetAddress`.
        
        <P>Note: The resolved address may be cached for a short period of time.
        </P>
        
        If there is a security manager, its
        `checkConnect` method is called
        with the local host name and `-1`
        as its arguments to see if the operation is allowed.
        If the operation is not allowed, an InetAddress representing
        the loopback address is returned.

        Returns
        - the address of the local host.

        Raises
        - UnknownHostException: if the local host name could not
                    be resolved into an address.

        See
        - java.net.InetAddress.getByName(java.lang.String)
        """
        ...
