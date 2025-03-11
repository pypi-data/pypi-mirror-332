"""
Python module generated from Java source file com.google.common.net.HostAndPort

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.base import CharMatcher
from com.google.common.base import Objects
from com.google.common.base import Strings
from com.google.common.net import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from com.google.errorprone.annotations import Immutable
from java.io import Serializable
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class HostAndPort(Serializable):
    """
    An immutable representation of a host and port.
    
    Example usage:
    
    ```
    HostAndPort hp = HostAndPort.fromString("[2001:db8::1]")
        .withDefaultPort(80)
        .requireBracketsForIPv6();
    hp.getHost();   // returns "2001:db8::1"
    hp.getPort();   // returns 80
    hp.toString();  // returns "[2001:db8::1]:80"
    ```
    
    Here are some examples of recognized formats:
    
    
      - example.com
      - example.com:80
      - 192.0.2.1
      - 192.0.2.1:80
      - [2001:db8::1] - .getHost() omits brackets
      - [2001:db8::1]:80 - .getHost() omits brackets
      - 2001:db8::1 - Use .requireBracketsForIPv6() to prohibit this
    
    
    Note that this is not an exhaustive list, because these methods are only concerned with
    brackets, colons, and port numbers. Full validation of the host field (if desired) is the
    caller's responsibility.

    Author(s)
    - Paul Marks

    Since
    - 10.0
    """

    def getHost(self) -> str:
        """
        Returns the portion of this `HostAndPort` instance that should represent the hostname or
        IPv4/IPv6 literal.
        
        A successful parse does not imply any degree of sanity in this field. For additional
        validation, see the HostSpecifier class.

        Since
        - 20.0 (since 10.0 as `getHostText`)
        """
        ...


    def hasPort(self) -> bool:
        """
        Return True if this instance has a defined port.
        """
        ...


    def getPort(self) -> int:
        """
        Get the current port number, failing if no port is defined.

        Returns
        - a validated port number, in the range [0..65535]

        Raises
        - IllegalStateException: if no port is defined. You can use .withDefaultPort(int)
            to prevent this from occurring.
        """
        ...


    def getPortOrDefault(self, defaultPort: int) -> int:
        """
        Returns the current port number, with a default if no port is defined.
        """
        ...


    @staticmethod
    def fromParts(host: str, port: int) -> "HostAndPort":
        """
        Build a HostAndPort instance from separate host and port values.
        
        Note: Non-bracketed IPv6 literals are allowed. Use .requireBracketsForIPv6() to
        prohibit these.

        Arguments
        - host: the host string to parse. Must not contain a port number.
        - port: a port number from [0..65535]

        Returns
        - if parsing was successful, a populated HostAndPort object.

        Raises
        - IllegalArgumentException: if `host` contains a port number, or `port` is out
            of range.
        """
        ...


    @staticmethod
    def fromHost(host: str) -> "HostAndPort":
        """
        Build a HostAndPort instance from a host only.
        
        Note: Non-bracketed IPv6 literals are allowed. Use .requireBracketsForIPv6() to
        prohibit these.

        Arguments
        - host: the host-only string to parse. Must not contain a port number.

        Returns
        - if parsing was successful, a populated HostAndPort object.

        Raises
        - IllegalArgumentException: if `host` contains a port number.

        Since
        - 17.0
        """
        ...


    @staticmethod
    def fromString(hostPortString: str) -> "HostAndPort":
        """
        Split a freeform string into a host and port, without strict validation.
        
        Note that the host-only formats will leave the port field undefined. You can use .withDefaultPort(int) to patch in a default value.

        Arguments
        - hostPortString: the input string to parse.

        Returns
        - if parsing was successful, a populated HostAndPort object.

        Raises
        - IllegalArgumentException: if nothing meaningful could be parsed.
        """
        ...


    def withDefaultPort(self, defaultPort: int) -> "HostAndPort":
        """
        Provide a default port if the parsed string contained only a host.
        
        You can chain this after .fromString(String) to include a port in case the port was
        omitted from the input string. If a port was already provided, then this method is a no-op.

        Arguments
        - defaultPort: a port number, from [0..65535]

        Returns
        - a HostAndPort instance, guaranteed to have a defined port.
        """
        ...


    def requireBracketsForIPv6(self) -> "HostAndPort":
        """
        Generate an error if the host might be a non-bracketed IPv6 literal.
        
        URI formatting requires that IPv6 literals be surrounded by brackets, like "[2001:db8::1]".
        Chain this call after .fromString(String) to increase the strictness of the parser, and
        disallow IPv6 literals that don't contain these brackets.
        
        Note that this parser identifies IPv6 literals solely based on the presence of a colon. To
        perform actual validation of IP addresses, see the InetAddresses.forString(String)
        method.

        Returns
        - `this`, to enable chaining of calls.

        Raises
        - IllegalArgumentException: if bracketless IPv6 is detected.
        """
        ...


    def equals(self, other: "Object") -> bool:
        ...


    def hashCode(self) -> int:
        ...


    def toString(self) -> str:
        """
        Rebuild the host:port string, including brackets if necessary.
        """
        ...
