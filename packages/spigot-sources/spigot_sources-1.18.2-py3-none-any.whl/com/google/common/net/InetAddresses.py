"""
Python module generated from Java source file com.google.common.net.InetAddresses

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtIncompatible
from com.google.common.base import CharMatcher
from com.google.common.base import MoreObjects
from com.google.common.hash import Hashing
from com.google.common.io import ByteStreams
from com.google.common.net import *
from com.google.common.primitives import Ints
from java.math import BigInteger
from java.net import Inet4Address
from java.net import Inet6Address
from java.net import InetAddress
from java.net import UnknownHostException
from java.util import Arrays
from java.util import Locale
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class InetAddresses:
    """
    Static utility methods pertaining to InetAddress instances.
    
    **Important note:** Unlike `InetAddress.getByName()`, the methods of this class never
    cause DNS services to be accessed. For this reason, you should prefer these methods as much as
    possible over their JDK equivalents whenever you are expecting to handle only IP address string
    literals -- there is no blocking DNS penalty for a malformed string.
    
    When dealing with Inet4Address and Inet6Address objects as byte arrays (vis.
    `InetAddress.getAddress()`) they are 4 and 16 bytes in length, respectively, and represent
    the address in network byte order.
    
    Examples of IP addresses and their byte representations:
    
    <dl>
      <dt>The IPv4 loopback address, `"127.0.0.1"`.
      <dd>`7f 00 00 01`
      <dt>The IPv6 loopback address, `"::1"`.
      <dd>`00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01`
      <dt>From the IPv6 reserved documentation prefix (`2001:db8::/32`), `"2001:db8::1"`.
      <dd>`20 01 0d b8 00 00 00 00 00 00 00 00 00 00 00 01`
      <dt>An IPv6 "IPv4 compatible" (or "compat") address, `"::192.168.0.1"`.
      <dd>`00 00 00 00 00 00 00 00 00 00 00 00 c0 a8 00 01`
      <dt>An IPv6 "IPv4 mapped" address, `"::ffff:192.168.0.1"`.
      <dd>`00 00 00 00 00 00 00 00 00 00 ff ff c0 a8 00 01`
    </dl>
    
    A few notes about IPv6 "IPv4 mapped" addresses and their observed use in Java.
    
    "IPv4 mapped" addresses were originally a representation of IPv4 addresses for use on an IPv6
    socket that could receive both IPv4 and IPv6 connections (by disabling the `IPV6_V6ONLY`
    socket option on an IPv6 socket). Yes, it's confusing. Nevertheless, these "mapped" addresses
    were never supposed to be seen on the wire. That assumption was dropped, some say mistakenly, in
    later RFCs with the apparent aim of making IPv4-to-IPv6 transition simpler.
    
    Technically one *can* create a 128bit IPv6 address with the wire format of a "mapped"
    address, as shown above, and transmit it in an IPv6 packet header. However, Java's InetAddress
    creation methods appear to adhere doggedly to the original intent of the "mapped" address: all
    "mapped" addresses return Inet4Address objects.
    
    For added safety, it is common for IPv6 network operators to filter all packets where either
    the source or destination address appears to be a "compat" or "mapped" address. Filtering
    suggestions usually recommend discarding any packets with source or destination addresses in the
    invalid range `::/3`, which includes both of these bizarre address formats. For more
    information on "bogons", including lists of IPv6 bogon space, see:
    
    
      - <a target="_parent"
          href="http://en.wikipedia.org/wiki/Bogon_filtering">http://en.wikipedia.
          org/wiki/Bogon_filtering</a>
      - <a target="_parent"
          href="http://www.cymru.com/Bogons/ipv6.txt">http://www.cymru.com/Bogons/ ipv6.txt</a>
      - <a target="_parent" href="http://www.cymru.com/Bogons/v6bogon.html">http://www.cymru.com/
          Bogons/v6bogon.html</a>
      - <a target="_parent" href="http://www.space.net/~gert/RIPE/ipv6-filters.html">http://www.
          space.net/~gert/RIPE/ipv6-filters.html</a>

    Author(s)
    - Erik Kline

    Since
    - 5.0
    """

    @staticmethod
    def forString(ipString: str) -> "InetAddress":
        """
        Returns the InetAddress having the given string representation.
        
        This deliberately avoids all nameservice lookups (e.g. no DNS).
        
        Anything after a `%` in an IPv6 address is ignored (assumed to be a Scope ID).
        
        This method accepts non-ASCII digits, for example `"１９２.１６８.０.１"` (those are fullwidth
        characters). That is consistent with InetAddress, but not with various RFCs. If you
        want to accept ASCII digits only, you can use something like `CharMatcher.ascii().matchesAllOf(ipString)`.

        Arguments
        - ipString: `String` containing an IPv4 or IPv6 string literal, e.g. `"192.168.0.1"` or `"2001:db8::1"`

        Returns
        - InetAddress representing the argument

        Raises
        - IllegalArgumentException: if the argument is not a valid IP string literal
        """
        ...


    @staticmethod
    def isInetAddress(ipString: str) -> bool:
        """
        Returns `True` if the supplied string is a valid IP string literal, `False`
        otherwise.
        
        This method accepts non-ASCII digits, for example `"１９２.１６８.０.１"` (those are fullwidth
        characters). That is consistent with InetAddress, but not with various RFCs. If you
        want to accept ASCII digits only, you can use something like `CharMatcher.ascii().matchesAllOf(ipString)`.

        Arguments
        - ipString: `String` to evaluated as an IP string literal

        Returns
        - `True` if the argument is a valid IP string literal
        """
        ...


    @staticmethod
    def toAddrString(ip: "InetAddress") -> str:
        """
        Returns the string representation of an InetAddress.
        
        For IPv4 addresses, this is identical to InetAddress.getHostAddress(), but for IPv6
        addresses, the output follows <a href="http://tools.ietf.org/html/rfc5952">RFC 5952</a> section
        4. The main difference is that this method uses "::" for zero compression, while Java's version
        uses the uncompressed form.
        
        This method uses hexadecimal for all IPv6 addresses, including IPv4-mapped IPv6 addresses
        such as "::c000:201". The output does not include a Scope ID.

        Arguments
        - ip: InetAddress to be converted to an address string

        Returns
        - `String` containing the text-formatted IP address

        Since
        - 10.0
        """
        ...


    @staticmethod
    def toUriString(ip: "InetAddress") -> str:
        """
        Returns the string representation of an InetAddress suitable for inclusion in a URI.
        
        For IPv4 addresses, this is identical to InetAddress.getHostAddress(), but for IPv6
        addresses it compresses zeroes and surrounds the text with square brackets; for example `"[2001:db8::1]"`.
        
        Per section 3.2.2 of <a target="_parent"
        href="http://tools.ietf.org/html/rfc3986#section-3.2.2">RFC 3986</a>, a URI containing an IPv6
        string literal is of the form `"http://[2001:db8::1]:8888/index.html"`.
        
        Use of either InetAddresses.toAddrString, InetAddress.getHostAddress(), or
        this method is recommended over InetAddress.toString() when an IP address string
        literal is desired. This is because InetAddress.toString() prints the hostname and the
        IP address string joined by a "/".

        Arguments
        - ip: InetAddress to be converted to URI string literal

        Returns
        - `String` containing URI-safe string literal
        """
        ...


    @staticmethod
    def forUriString(hostAddr: str) -> "InetAddress":
        """
        Returns an InetAddress representing the literal IPv4 or IPv6 host portion of a URL, encoded in
        the format specified by RFC 3986 section 3.2.2.
        
        This method is similar to InetAddresses.forString(String), however, it requires that
        IPv6 addresses are surrounded by square brackets.
        
        This method is the inverse of InetAddresses.toUriString(java.net.InetAddress).
        
        This method accepts non-ASCII digits, for example `"１９２.１６８.０.１"` (those are fullwidth
        characters). That is consistent with InetAddress, but not with various RFCs. If you
        want to accept ASCII digits only, you can use something like `CharMatcher.ascii().matchesAllOf(ipString)`.

        Arguments
        - hostAddr: A RFC 3986 section 3.2.2 encoded IPv4 or IPv6 address

        Returns
        - an InetAddress representing the address in `hostAddr`

        Raises
        - IllegalArgumentException: if `hostAddr` is not a valid IPv4 address, or IPv6
            address surrounded by square brackets
        """
        ...


    @staticmethod
    def isUriInetAddress(ipString: str) -> bool:
        """
        Returns `True` if the supplied string is a valid URI IP string literal, `False`
        otherwise.
        
        This method accepts non-ASCII digits, for example `"１９２.１６８.０.１"` (those are fullwidth
        characters). That is consistent with InetAddress, but not with various RFCs. If you
        want to accept ASCII digits only, you can use something like `CharMatcher.ascii().matchesAllOf(ipString)`.

        Arguments
        - ipString: `String` to evaluated as an IP URI host string literal

        Returns
        - `True` if the argument is a valid IP URI host
        """
        ...


    @staticmethod
    def isCompatIPv4Address(ip: "Inet6Address") -> bool:
        """
        Evaluates whether the argument is an IPv6 "compat" address.
        
        An "IPv4 compatible", or "compat", address is one with 96 leading bits of zero, with the
        remaining 32 bits interpreted as an IPv4 address. These are conventionally represented in
        string literals as `"::192.168.0.1"`, though `"::c0a8:1"` is also considered an
        IPv4 compatible address (and equivalent to `"::192.168.0.1"`).
        
        For more on IPv4 compatible addresses see section 2.5.5.1 of <a target="_parent"
        href="http://tools.ietf.org/html/rfc4291#section-2.5.5.1">RFC 4291</a>.
        
        NOTE: This method is different from Inet6Address.isIPv4CompatibleAddress in that it
        more correctly classifies `"::"` and `"::1"` as proper IPv6 addresses (which they
        are), NOT IPv4 compatible addresses (which they are generally NOT considered to be).

        Arguments
        - ip: Inet6Address to be examined for embedded IPv4 compatible address format

        Returns
        - `True` if the argument is a valid "compat" address
        """
        ...


    @staticmethod
    def getCompatIPv4Address(ip: "Inet6Address") -> "Inet4Address":
        """
        Returns the IPv4 address embedded in an IPv4 compatible address.

        Arguments
        - ip: Inet6Address to be examined for an embedded IPv4 address

        Returns
        - Inet4Address of the embedded IPv4 address

        Raises
        - IllegalArgumentException: if the argument is not a valid IPv4 compatible address
        """
        ...


    @staticmethod
    def is6to4Address(ip: "Inet6Address") -> bool:
        """
        Evaluates whether the argument is a 6to4 address.
        
        6to4 addresses begin with the `"2002::/16"` prefix. The next 32 bits are the IPv4
        address of the host to which IPv6-in-IPv4 tunneled packets should be routed.
        
        For more on 6to4 addresses see section 2 of <a target="_parent"
        href="http://tools.ietf.org/html/rfc3056#section-2">RFC 3056</a>.

        Arguments
        - ip: Inet6Address to be examined for 6to4 address format

        Returns
        - `True` if the argument is a 6to4 address
        """
        ...


    @staticmethod
    def get6to4IPv4Address(ip: "Inet6Address") -> "Inet4Address":
        """
        Returns the IPv4 address embedded in a 6to4 address.

        Arguments
        - ip: Inet6Address to be examined for embedded IPv4 in 6to4 address

        Returns
        - Inet4Address of embedded IPv4 in 6to4 address

        Raises
        - IllegalArgumentException: if the argument is not a valid IPv6 6to4 address
        """
        ...


    @staticmethod
    def isTeredoAddress(ip: "Inet6Address") -> bool:
        """
        Evaluates whether the argument is a Teredo address.
        
        Teredo addresses begin with the `"2001::/32"` prefix.

        Arguments
        - ip: Inet6Address to be examined for Teredo address format

        Returns
        - `True` if the argument is a Teredo address
        """
        ...


    @staticmethod
    def getTeredoInfo(ip: "Inet6Address") -> "TeredoInfo":
        """
        Returns the Teredo information embedded in a Teredo address.

        Arguments
        - ip: Inet6Address to be examined for embedded Teredo information

        Returns
        - extracted `TeredoInfo`

        Raises
        - IllegalArgumentException: if the argument is not a valid IPv6 Teredo address
        """
        ...


    @staticmethod
    def isIsatapAddress(ip: "Inet6Address") -> bool:
        """
        Evaluates whether the argument is an ISATAP address.
        
        From RFC 5214: "ISATAP interface identifiers are constructed in Modified EUI-64 format [...]
        by concatenating the 24-bit IANA OUI (00-00-5E), the 8-bit hexadecimal value 0xFE, and a 32-bit
        IPv4 address in network byte order [...]"
        
        For more on ISATAP addresses see section 6.1 of <a target="_parent"
        href="http://tools.ietf.org/html/rfc5214#section-6.1">RFC 5214</a>.

        Arguments
        - ip: Inet6Address to be examined for ISATAP address format

        Returns
        - `True` if the argument is an ISATAP address
        """
        ...


    @staticmethod
    def getIsatapIPv4Address(ip: "Inet6Address") -> "Inet4Address":
        """
        Returns the IPv4 address embedded in an ISATAP address.

        Arguments
        - ip: Inet6Address to be examined for embedded IPv4 in ISATAP address

        Returns
        - Inet4Address of embedded IPv4 in an ISATAP address

        Raises
        - IllegalArgumentException: if the argument is not a valid IPv6 ISATAP address
        """
        ...


    @staticmethod
    def hasEmbeddedIPv4ClientAddress(ip: "Inet6Address") -> bool:
        """
        Examines the Inet6Address to determine if it is an IPv6 address of one of the specified address
        types that contain an embedded IPv4 address.
        
        NOTE: ISATAP addresses are explicitly excluded from this method due to their trivial
        spoofability. With other transition addresses spoofing involves (at least) infection of one's
        BGP routing table.

        Arguments
        - ip: Inet6Address to be examined for embedded IPv4 client address

        Returns
        - `True` if there is an embedded IPv4 client address

        Since
        - 7.0
        """
        ...


    @staticmethod
    def getEmbeddedIPv4ClientAddress(ip: "Inet6Address") -> "Inet4Address":
        """
        Examines the Inet6Address to extract the embedded IPv4 client address if the InetAddress is an
        IPv6 address of one of the specified address types that contain an embedded IPv4 address.
        
        NOTE: ISATAP addresses are explicitly excluded from this method due to their trivial
        spoofability. With other transition addresses spoofing involves (at least) infection of one's
        BGP routing table.

        Arguments
        - ip: Inet6Address to be examined for embedded IPv4 client address

        Returns
        - Inet4Address of embedded IPv4 client address

        Raises
        - IllegalArgumentException: if the argument does not have a valid embedded IPv4 address
        """
        ...


    @staticmethod
    def isMappedIPv4Address(ipString: str) -> bool:
        """
        Evaluates whether the argument is an "IPv4 mapped" IPv6 address.
        
        An "IPv4 mapped" address is anything in the range ::ffff:0:0/96 (sometimes written as
        ::ffff:0.0.0.0/96), with the last 32 bits interpreted as an IPv4 address.
        
        For more on IPv4 mapped addresses see section 2.5.5.2 of <a target="_parent"
        href="http://tools.ietf.org/html/rfc4291#section-2.5.5.2">RFC 4291</a>.
        
        Note: This method takes a `String` argument because InetAddress automatically
        collapses mapped addresses to IPv4. (It is actually possible to avoid this using one of the
        obscure Inet6Address methods, but it would be unwise to depend on such a
        poorly-documented feature.)
        
        This method accepts non-ASCII digits. That is consistent with InetAddress, but not
        with various RFCs. If you want to accept ASCII digits only, you can use something like `CharMatcher.ascii().matchesAllOf(ipString)`.

        Arguments
        - ipString: `String` to be examined for embedded IPv4-mapped IPv6 address format

        Returns
        - `True` if the argument is a valid "mapped" address

        Since
        - 10.0
        """
        ...


    @staticmethod
    def getCoercedIPv4Address(ip: "InetAddress") -> "Inet4Address":
        """
        Coerces an IPv6 address into an IPv4 address.
        
        HACK: As long as applications continue to use IPv4 addresses for indexing into tables,
        accounting, et cetera, it may be necessary to **coerce** IPv6 addresses into IPv4 addresses.
        This method does so by hashing 64 bits of the IPv6 address into `224.0.0.0/3` (64 bits
        into 29 bits):
        
        
          - If the IPv6 address contains an embedded IPv4 address, the function hashes that.
          - Otherwise, it hashes the upper 64 bits of the IPv6 address.
        
        
        A "coerced" IPv4 address is equivalent to itself.
        
        NOTE: This method is failsafe for security purposes: ALL IPv6 addresses (except localhost
        (::1)) are hashed to avoid the security risk associated with extracting an embedded IPv4
        address that might permit elevated privileges.

        Arguments
        - ip: InetAddress to "coerce"

        Returns
        - Inet4Address represented "coerced" address

        Since
        - 7.0
        """
        ...


    @staticmethod
    def coerceToInteger(ip: "InetAddress") -> int:
        """
        Returns an integer representing an IPv4 address regardless of whether the supplied argument is
        an IPv4 address or not.
        
        IPv6 addresses are **coerced** to IPv4 addresses before being converted to integers.
        
        As long as there are applications that assume that all IP addresses are IPv4 addresses and
        can therefore be converted safely to integers (for whatever purpose) this function can be used
        to handle IPv6 addresses as well until the application is suitably fixed.
        
        NOTE: an IPv6 address coerced to an IPv4 address can only be used for such purposes as
        rudimentary identification or indexing into a collection of real InetAddresses. They
        cannot be used as real addresses for the purposes of network communication.

        Arguments
        - ip: InetAddress to convert

        Returns
        - `int`, "coerced" if ip is not an IPv4 address

        Since
        - 7.0
        """
        ...


    @staticmethod
    def toBigInteger(address: "InetAddress") -> "BigInteger":
        """
        Returns a BigInteger representing the address.
        
        Unlike `coerceToInteger`, IPv6 addresses are not coerced to IPv4 addresses.

        Arguments
        - address: InetAddress to convert

        Returns
        - `BigInteger` representation of the address

        Since
        - 28.2
        """
        ...


    @staticmethod
    def fromInteger(address: int) -> "Inet4Address":
        """
        Returns an Inet4Address having the integer value specified by the argument.

        Arguments
        - address: `int`, the 32bit integer address to be converted

        Returns
        - Inet4Address equivalent of the argument
        """
        ...


    @staticmethod
    def fromIPv4BigInteger(address: "BigInteger") -> "Inet4Address":
        """
        Returns the `Inet4Address` corresponding to a given `BigInteger`.

        Arguments
        - address: BigInteger representing the IPv4 address

        Returns
        - Inet4Address representation of the given BigInteger

        Raises
        - IllegalArgumentException: if the BigInteger is not between 0 and 2^32-1

        Since
        - 28.2
        """
        ...


    @staticmethod
    def fromIPv6BigInteger(address: "BigInteger") -> "Inet6Address":
        """
        Returns the `Inet6Address` corresponding to a given `BigInteger`.

        Arguments
        - address: BigInteger representing the IPv6 address

        Returns
        - Inet6Address representation of the given BigInteger

        Raises
        - IllegalArgumentException: if the BigInteger is not between 0 and 2^128-1

        Since
        - 28.2
        """
        ...


    @staticmethod
    def fromLittleEndianByteArray(addr: list[int]) -> "InetAddress":
        """
        Returns an address from a **little-endian ordered** byte array (the opposite of what InetAddress.getByAddress expects).
        
        IPv4 address byte array must be 4 bytes long and IPv6 byte array must be 16 bytes long.

        Arguments
        - addr: the raw IP address in little-endian byte order

        Returns
        - an InetAddress object created from the raw IP address

        Raises
        - UnknownHostException: if IP address is of illegal length
        """
        ...


    @staticmethod
    def decrement(address: "InetAddress") -> "InetAddress":
        """
        Returns a new InetAddress that is one less than the passed in address. This method works for
        both IPv4 and IPv6 addresses.

        Arguments
        - address: the InetAddress to decrement

        Returns
        - a new InetAddress that is one less than the passed in address

        Raises
        - IllegalArgumentException: if InetAddress is at the beginning of its range

        Since
        - 18.0
        """
        ...


    @staticmethod
    def increment(address: "InetAddress") -> "InetAddress":
        """
        Returns a new InetAddress that is one more than the passed in address. This method works for
        both IPv4 and IPv6 addresses.

        Arguments
        - address: the InetAddress to increment

        Returns
        - a new InetAddress that is one more than the passed in address

        Raises
        - IllegalArgumentException: if InetAddress is at the end of its range

        Since
        - 10.0
        """
        ...


    @staticmethod
    def isMaximum(address: "InetAddress") -> bool:
        """
        Returns True if the InetAddress is either 255.255.255.255 for IPv4 or
        ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff for IPv6.

        Returns
        - True if the InetAddress is either 255.255.255.255 for IPv4 or
            ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff for IPv6

        Since
        - 10.0
        """
        ...


    class TeredoInfo:
        """
        A simple immutable data class to encapsulate the information to be found in a Teredo address.
        
        All of the fields in this class are encoded in various portions of the IPv6 address as part
        of the protocol. More protocols details can be found at: <a target="_parent"
        href="http://en.wikipedia.org/wiki/Teredo_tunneling">http://en.wikipedia.
        org/wiki/Teredo_tunneling</a>.
        
        The RFC can be found here: <a target="_parent" href="http://tools.ietf.org/html/rfc4380">RFC
        4380</a>.

        Since
        - 5.0
        """

        def __init__(self, server: "Inet4Address", client: "Inet4Address", port: int, flags: int):
            ...


        def getServer(self) -> "Inet4Address":
            ...


        def getClient(self) -> "Inet4Address":
            ...


        def getPort(self) -> int:
            ...


        def getFlags(self) -> int:
            ...
