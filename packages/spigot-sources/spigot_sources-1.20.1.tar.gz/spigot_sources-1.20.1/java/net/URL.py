"""
Python module generated from Java source file java.net.URL

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import File
from java.io import IOException
from java.io import InputStream
from java.io import InvalidObjectException
from java.io.ObjectInputStream import GetField
from java.io import ObjectStreamException
from java.io import ObjectStreamField
from java.net import *
from java.net.spi import URLStreamHandlerProvider
from java.nio.file import Path
from java.security import AccessController
from java.security import PrivilegedAction
from java.util import Hashtable
from java.util import Iterator
from java.util import Locale
from java.util import NoSuchElementException
from java.util import ServiceConfigurationError
from java.util import ServiceLoader
from jdk.internal.access import JavaNetURLAccess
from jdk.internal.access import SharedSecrets
from jdk.internal.misc import VM
from sun.net.util import IPAddressUtil
from sun.security.action import GetPropertyAction
from sun.security.util import SecurityConstants
from typing import Any, Callable, Iterable, Tuple


class URL(Serializable):
    """
    Class `URL` represents a Uniform Resource
    Locator, a pointer to a "resource" on the World
    Wide Web. A resource can be something as simple as a file or a
    directory, or it can be a reference to a more complicated object,
    such as a query to a database or to a search engine. More
    information on the types of URLs and their formats can be found at:
    <a href=
    "http://web.archive.org/web/20051219043731/http://archive.ncsa.uiuc.edu/SDG/Software/Mosaic/Demo/url-primer.html">
    *Types of URL*</a>
    
    In general, a URL can be broken into several parts. Consider the
    following example:
    <blockquote>```
        http://www.example.com/docs/resource1.html
    ```</blockquote>
    
    The URL above indicates that the protocol to use is
    `http` (HyperText Transfer Protocol) and that the
    information resides on a host machine named
    `www.example.com`. The information on that host
    machine is named `/docs/resource1.html`. The exact
    meaning of this name on the host machine is both protocol
    dependent and host dependent. The information normally resides in
    a file, but it could be generated on the fly. This component of
    the URL is called the *path* component.
    
    A URL can optionally specify a "port", which is the
    port number to which the TCP connection is made on the remote host
    machine. If the port is not specified, the default port for
    the protocol is used instead. For example, the default port for
    `http` is `80`. An alternative port could be
    specified as:
    <blockquote>```
        http://www.example.com:1080/docs/resource1.html
    ```</blockquote>
    
    The syntax of `URL` is defined by  <a
    href="http://www.ietf.org/rfc/rfc2396.txt">*RFC&nbsp;2396: Uniform
    Resource Identifiers (URI): Generic Syntax*</a>, amended by <a
    href="http://www.ietf.org/rfc/rfc2732.txt">*RFC&nbsp;2732: Format for
    Literal IPv6 Addresses in URLs*</a>. The Literal IPv6 address format
    also supports scope_ids. The syntax and usage of scope_ids is described
    <a href="Inet6Address.html#scoped">here</a>.
    
    A URL may have appended to it a "fragment", also known
    as a "ref" or a "reference". The fragment is indicated by the sharp
    sign character "#" followed by more characters. For example,
    <blockquote>```
        http://www.example.com/index.html#chapter1
    ```</blockquote>
    
    This fragment is not technically part of the URL. Rather, it
    indicates that after the specified resource is retrieved, the
    application is specifically interested in that part of the
    document that has the tag `chapter1` attached to it. The
    meaning of a tag is resource specific.
    
    An application can also specify a "relative URL",
    which contains only enough information to reach the resource
    relative to another URL. Relative URLs are frequently used within
    HTML pages. For example, if the contents of the URL:
    <blockquote>```
        http://www.example.com/index.html
    ```</blockquote>
    contained within it the relative URL:
    <blockquote>```
        FAQ.html
    ```</blockquote>
    it would be a shorthand for:
    <blockquote>```
        http://www.example.com/FAQ.html
    ```</blockquote>
    
    The relative URL need not specify all the components of a URL. If
    the protocol, host name, or port number is missing, the value is
    inherited from the fully specified URL. The file component must be
    specified. The optional fragment is not inherited.
    
    The URL class does not itself encode or decode any URL components
    according to the escaping mechanism defined in RFC2396. It is the
    responsibility of the caller to encode any fields, which need to be
    escaped prior to calling URL, and also to decode any escaped fields,
    that are returned from URL. Furthermore, because URL has no knowledge
    of URL escaping, it does not recognise equivalence between the encoded
    or decoded form of the same URL. For example, the two URLs:
    ```    http://foo.com/hello world/ and http://foo.com/hello%20world```
    would be considered not equal to each other.
    
    Note, the java.net.URI class does perform escaping of its
    component fields in certain circumstances. The recommended way
    to manage the encoding and decoding of URLs is to use java.net.URI,
    and to convert between these two classes using .toURI() and
    URI.toURL().
    
    The URLEncoder and URLDecoder classes can also be
    used, but only for HTML form encoding, which is not the same
    as the encoding scheme defined in RFC2396.

    Author(s)
    - James Gosling

    Since
    - 1.0

    Unknown Tags
    - Applications working with file paths and file URIs should take great
    care to use the appropriate methods to convert between the two.
    The Path.of(URI) factory method and the File.File(URI)
    constructor can be used to create Path or File
    objects from a file URI. Path.toUri() and File.toURI()
    can be used to create a URI from a file path, which can be
    converted to URL using URI.toURL().
    Applications should never try to .URL(String, String, String)
    construct or .URL(String) parse a `URL`
    from the direct string representation of a `File` or `Path`
    instance.
    
    Some components of a URL or URI, such as *userinfo*, may
    be abused to construct misleading URLs or URIs. Applications
    that deal with URLs or URIs should take into account
    the recommendations advised in <a
    href="https://tools.ietf.org/html/rfc3986#section-7">RFC3986,
    Section 7, Security Considerations</a>.
    """

    def __init__(self, protocol: str, host: str, port: int, file: str):
        """
        Creates a `URL` object from the specified
        `protocol`, `host`, `port`
        number, and `file`.
        
        `host` can be expressed as a host name or a literal
        IP address. If IPv6 literal address is used, it should be
        enclosed in square brackets (`'['` and `']'`), as
        specified by <a
        href="http://www.ietf.org/rfc/rfc2732.txt">RFC&nbsp;2732</a>;
        However, the literal IPv6 address format defined in <a
        href="http://www.ietf.org/rfc/rfc2373.txt">*RFC&nbsp;2373: IP
        Version 6 Addressing Architecture*</a> is also accepted.
        
        Specifying a `port` number of `-1`
        indicates that the URL should use the default port for the
        protocol.
        
        If this is the first URL object being created with the specified
        protocol, a *stream protocol handler* object, an instance of
        class `URLStreamHandler`, is created for that protocol:
        <ol>
        - If the application has previously set up an instance of
            `URLStreamHandlerFactory` as the stream handler factory,
            then the `createURLStreamHandler` method of that instance
            is called with the protocol string as an argument to create the
            stream protocol handler.
        - If no `URLStreamHandlerFactory` has yet been set up,
            or if the factory's `createURLStreamHandler` method
            returns `null`, then the java.util.ServiceLoader
            ServiceLoader mechanism is used to locate java.net.spi.URLStreamHandlerProvider URLStreamHandlerProvider
            implementations using the system class
            loader. The order that providers are located is implementation
            specific, and an implementation is free to cache the located
            providers. A java.util.ServiceConfigurationError
            ServiceConfigurationError, `Error` or `RuntimeException`
            thrown from the `createURLStreamHandler`, if encountered, will
            be propagated to the calling thread. The `createURLStreamHandler` method of each provider, if instantiated, is
            invoked, with the protocol string, until a provider returns non-null,
            or all providers have been exhausted.
        - If the previous step fails to find a protocol handler, the
            constructor reads the value of the system property:
            <blockquote>java.protocol.handler.pkgs</blockquote>
            If the value of that system property is not `null`,
            it is interpreted as a list of packages separated by a vertical
            slash character '`|`'. The constructor tries to load
            the class named:
            <blockquote>`<package>.<protocol>.Handler`</blockquote>
            where `<package>` is replaced by the name of the package
            and `<protocol>` is replaced by the name of the protocol.
            If this class does not exist, or if the class exists but it is not
            a subclass of `URLStreamHandler`, then the next package
            in the list is tried.
        - If the previous step fails to find a protocol handler, then the
            constructor tries to load a built-in protocol handler.
            If this class does not exist, or if the class exists but it is not a
            subclass of `URLStreamHandler`, then a
            `MalformedURLException` is thrown.
        </ol>
        
        Protocol handlers for the following protocols are guaranteed
        to exist on the search path:
        
        - `http`
        - `https`
        - `file`
        - `jar`
        
        Protocol handlers for additional protocols may also be  available.
        Some protocol handlers, for example those used for loading platform
        classes or classes on the class path, may not be overridden. The details
        of such restrictions, and when those restrictions apply (during
        initialization of the runtime for example), are implementation specific
        and therefore not specified
        
        No validation of the inputs is performed by this constructor.

        Arguments
        - protocol: the name of the protocol to use.
        - host: the name of the host.
        - port: the port number on the host.
        - file: the file on the host

        Raises
        - MalformedURLException: if an unknown protocol or the port
                         is a negative number other than -1

        See
        - java.net.URLStreamHandlerFactory.createURLStreamHandler(
                         java.lang.String)
        """
        ...


    def __init__(self, protocol: str, host: str, file: str):
        """
        Creates a URL from the specified `protocol`
        name, `host` name, and `file` name. The
        default port for the specified protocol is used.
        
        This constructor is equivalent to the four-argument
        constructor with the only difference of using the
        default port for the specified protocol.
        
        No validation of the inputs is performed by this constructor.

        Arguments
        - protocol: the name of the protocol to use.
        - host: the name of the host.
        - file: the file on the host.

        Raises
        - MalformedURLException: if an unknown protocol is specified.

        See
        - java.net.URL.URL(java.lang.String, java.lang.String,
                         int, java.lang.String)
        """
        ...


    def __init__(self, protocol: str, host: str, port: int, file: str, handler: "URLStreamHandler"):
        """
        Creates a `URL` object from the specified
        `protocol`, `host`, `port`
        number, `file`, and `handler`. Specifying
        a `port` number of `-1` indicates that
        the URL should use the default port for the protocol. Specifying
        a `handler` of `null` indicates that the URL
        should use a default stream handler for the protocol, as outlined
        for:
            java.net.URL.URL(java.lang.String, java.lang.String, int,
                             java.lang.String)
        
        If the handler is not null and there is a security manager,
        the security manager's `checkPermission`
        method is called with a
        `NetPermission("specifyStreamHandler")` permission.
        This may result in a SecurityException.
        
        No validation of the inputs is performed by this constructor.

        Arguments
        - protocol: the name of the protocol to use.
        - host: the name of the host.
        - port: the port number on the host.
        - file: the file on the host
        - handler: the stream handler for the URL.

        Raises
        - MalformedURLException: if an unknown protocol or the port
                           is a negative number other than -1
        - SecurityException: if a security manager exists and its
               `checkPermission` method doesn't allow
               specifying a stream handler explicitly.

        See
        - java.net.NetPermission
        """
        ...


    def __init__(self, spec: str):
        """
        Creates a `URL` object from the `String`
        representation.
        
        This constructor is equivalent to a call to the two-argument
        constructor with a `null` first argument.

        Arguments
        - spec: the `String` to parse as a URL.

        Raises
        - MalformedURLException: if no protocol is specified, or an
                      unknown protocol is found, or `spec` is `null`,
                      or the parsed URL fails to comply with the specific syntax
                      of the associated protocol.

        See
        - java.net.URL.URL(java.net.URL, java.lang.String)
        """
        ...


    def __init__(self, context: "URL", spec: str):
        """
        Creates a URL by parsing the given spec within a specified context.
        
        The new URL is created from the given context URL and the spec
        argument as described in
        RFC2396 &quot;Uniform Resource Identifiers : Generic * Syntax&quot; :
        <blockquote>```
                 &lt;scheme&gt;://&lt;authority&gt;&lt;path&gt;?&lt;query&gt;#&lt;fragment&gt;
        ```</blockquote>
        The reference is parsed into the scheme, authority, path, query and
        fragment parts. If the path component is empty and the scheme,
        authority, and query components are undefined, then the new URL is a
        reference to the current document. Otherwise, the fragment and query
        parts present in the spec are used in the new URL.
        
        If the scheme component is defined in the given spec and does not match
        the scheme of the context, then the new URL is created as an absolute
        URL based on the spec alone. Otherwise the scheme component is inherited
        from the context URL.
        
        If the authority component is present in the spec then the spec is
        treated as absolute and the spec authority and path will replace the
        context authority and path. If the authority component is absent in the
        spec then the authority of the new URL will be inherited from the
        context.
        
        If the spec's path component begins with a slash character
        &quot;/&quot; then the
        path is treated as absolute and the spec path replaces the context path.
        
        Otherwise, the path is treated as a relative path and is appended to the
        context path, as described in RFC2396. Also, in this case,
        the path is canonicalized through the removal of directory
        changes made by occurrences of &quot;..&quot; and &quot;.&quot;.
        
        For a more detailed description of URL parsing, refer to RFC2396.

        Arguments
        - context: the context in which to parse the specification.
        - spec: the `String` to parse as a URL.

        Raises
        - MalformedURLException: if no protocol is specified, or an
                      unknown protocol is found, or `spec` is `null`,
                      or the parsed URL fails to comply with the specific syntax
                      of the associated protocol.

        See
        - java.net.URLStreamHandler.parseURL(java.net.URL,
                         java.lang.String, int, int)
        """
        ...


    def __init__(self, context: "URL", spec: str, handler: "URLStreamHandler"):
        """
        Creates a URL by parsing the given spec with the specified handler
        within a specified context. If the handler is null, the parsing
        occurs as with the two argument constructor.

        Arguments
        - context: the context in which to parse the specification.
        - spec: the `String` to parse as a URL.
        - handler: the stream handler for the URL.

        Raises
        - MalformedURLException: if no protocol is specified, or an
                      unknown protocol is found, or `spec` is `null`,
                      or the parsed URL fails to comply with the specific syntax
                      of the associated protocol.
        - SecurityException: if a security manager exists and its
               `checkPermission` method doesn't allow
               specifying a stream handler.

        See
        - java.net.URLStreamHandler.parseURL(java.net.URL,
                         java.lang.String, int, int)
        """
        ...


    def getQuery(self) -> str:
        """
        Gets the query part of this `URL`.

        Returns
        - the query part of this `URL`,
        or <CODE>null</CODE> if one does not exist

        Since
        - 1.3
        """
        ...


    def getPath(self) -> str:
        """
        Gets the path part of this `URL`.

        Returns
        - the path part of this `URL`, or an
        empty string if one does not exist

        Since
        - 1.3
        """
        ...


    def getUserInfo(self) -> str:
        """
        Gets the userInfo part of this `URL`.

        Returns
        - the userInfo part of this `URL`, or
        <CODE>null</CODE> if one does not exist

        Since
        - 1.3
        """
        ...


    def getAuthority(self) -> str:
        """
        Gets the authority part of this `URL`.

        Returns
        - the authority part of this `URL`

        Since
        - 1.3
        """
        ...


    def getPort(self) -> int:
        """
        Gets the port number of this `URL`.

        Returns
        - the port number, or -1 if the port is not set
        """
        ...


    def getDefaultPort(self) -> int:
        """
        Gets the default port number of the protocol associated
        with this `URL`. If the URL scheme or the URLStreamHandler
        for the URL do not define a default port number,
        then -1 is returned.

        Returns
        - the port number

        Since
        - 1.4
        """
        ...


    def getProtocol(self) -> str:
        """
        Gets the protocol name of this `URL`.

        Returns
        - the protocol of this `URL`.
        """
        ...


    def getHost(self) -> str:
        """
        Gets the host name of this `URL`, if applicable.
        The format of the host conforms to RFC 2732, i.e. for a
        literal IPv6 address, this method will return the IPv6 address
        enclosed in square brackets (`'['` and `']'`).

        Returns
        - the host name of this `URL`.
        """
        ...


    def getFile(self) -> str:
        """
        Gets the file name of this `URL`.
        The returned file portion will be
        the same as <CODE>getPath()</CODE>, plus the concatenation of
        the value of <CODE>getQuery()</CODE>, if any. If there is
        no query portion, this method and <CODE>getPath()</CODE> will
        return identical results.

        Returns
        - the file name of this `URL`,
        or an empty string if one does not exist
        """
        ...


    def getRef(self) -> str:
        """
        Gets the anchor (also known as the "reference") of this
        `URL`.

        Returns
        - the anchor (also known as the "reference") of this
                 `URL`, or <CODE>null</CODE> if one does not exist
        """
        ...


    def equals(self, obj: "Object") -> bool:
        """
        Compares this URL for equality with another object.
        
        If the given object is not a URL then this method immediately returns
        `False`.
        
        Two URL objects are equal if they have the same protocol, reference
        equivalent hosts, have the same port number on the host, and the same
        file and fragment of the file.
        
        Two hosts are considered equivalent if both host names can be resolved
        into the same IP addresses; else if either host name can't be
        resolved, the host names must be equal without regard to case; or both
        host names equal to null.
        
        Since hosts comparison requires name resolution, this operation is a
        blocking operation. 
        
        Note: The defined behavior for `equals` is known to
        be inconsistent with virtual hosting in HTTP.

        Arguments
        - obj: the URL to compare against.

        Returns
        - `True` if the objects are the same;
                 `False` otherwise.
        """
        ...


    def hashCode(self) -> int:
        """
        Creates an integer suitable for hash table indexing.
        
        The hash code is based upon all the URL components relevant for URL
        comparison. As such, this operation is a blocking operation.

        Returns
        - a hash code for this `URL`.
        """
        ...


    def sameFile(self, other: "URL") -> bool:
        """
        Compares two URLs, excluding the fragment component.
        
        Returns `True` if this `URL` and the
        `other` argument are equal without taking the
        fragment component into consideration.

        Arguments
        - other: the `URL` to compare against.

        Returns
        - `True` if they reference the same remote object;
                 `False` otherwise.
        """
        ...


    def toString(self) -> str:
        """
        Constructs a string representation of this `URL`. The
        string is created by calling the `toExternalForm`
        method of the stream protocol handler for this object.

        Returns
        - a string representation of this object.

        See
        - java.net.URLStreamHandler.toExternalForm(java.net.URL)
        """
        ...


    def toExternalForm(self) -> str:
        """
        Constructs a string representation of this `URL`. The
        string is created by calling the `toExternalForm`
        method of the stream protocol handler for this object.

        Returns
        - a string representation of this object.

        See
        - java.net.URLStreamHandler.toExternalForm(java.net.URL)
        """
        ...


    def toURI(self) -> "URI":
        """
        Returns a java.net.URI equivalent to this URL.
        This method functions in the same way as `new URI (this.toString())`.
        Note, any URL instance that complies with RFC 2396 can be converted
        to a URI. However, some URLs that are not strictly in compliance
        can not be converted to a URI.

        Returns
        - a URI instance equivalent to this URL.

        Raises
        - URISyntaxException: if this URL is not formatted strictly according to
                   RFC2396 and cannot be converted to a URI.

        Since
        - 1.5
        """
        ...


    def openConnection(self) -> "URLConnection":
        """
        Returns a java.net.URLConnection URLConnection instance that
        represents a connection to the remote object referred to by the
        `URL`.
        
        <P>A new instance of java.net.URLConnection URLConnection is
        created every time when invoking the
        java.net.URLStreamHandler.openConnection(URL)
        URLStreamHandler.openConnection(URL) method of the protocol handler for
        this URL.</P>
        
        <P>It should be noted that a URLConnection instance does not establish
        the actual network connection on creation. This will happen only when
        calling java.net.URLConnection.connect() URLConnection.connect().</P>
        
        <P>If for the URL's protocol (such as HTTP or JAR), there
        exists a public, specialized URLConnection subclass belonging
        to one of the following packages or one of their subpackages:
        java.lang, java.io, java.util, java.net, the connection
        returned will be of that subclass. For example, for HTTP an
        HttpURLConnection will be returned, and for JAR a
        JarURLConnection will be returned.</P>

        Returns
        - a java.net.URLConnection URLConnection linking
                    to the URL.

        Raises
        - IOException: if an I/O exception occurs.

        See
        - java.net.URL.URL(java.lang.String, java.lang.String,
                    int, java.lang.String)
        """
        ...


    def openConnection(self, proxy: "Proxy") -> "URLConnection":
        """
        Same as .openConnection(), except that the connection will be
        made through the specified proxy; Protocol handlers that do not
        support proxying will ignore the proxy parameter and make a
        normal connection.
        
        Invoking this method preempts the system's default
        java.net.ProxySelector ProxySelector settings.

        Arguments
        - proxy: the Proxy through which this connection
                    will be made. If direct connection is desired,
                    Proxy.NO_PROXY should be specified.

        Returns
        - a `URLConnection` to the URL.

        Raises
        - IOException: if an I/O exception occurs.
        - SecurityException: if a security manager is present
                    and the caller doesn't have permission to connect
                    to the proxy.
        - IllegalArgumentException: will be thrown if proxy is null,
                    or proxy has the wrong type
        - UnsupportedOperationException: if the subclass that
                    implements the protocol handler doesn't support
                    this method.

        See
        - java.net.URLStreamHandler.openConnection(java.net.URL,
                    java.net.Proxy)

        Since
        - 1.5
        """
        ...


    def openStream(self) -> "InputStream":
        """
        Opens a connection to this `URL` and returns an
        `InputStream` for reading from that connection. This
        method is a shorthand for:
        <blockquote>```
            openConnection().getInputStream()
        ```</blockquote>

        Returns
        - an input stream for reading from the URL connection.

        Raises
        - IOException: if an I/O exception occurs.

        See
        - java.net.URLConnection.getInputStream()
        """
        ...


    def getContent(self) -> "Object":
        """
        Gets the contents of this URL. This method is a shorthand for:
        <blockquote>```
            openConnection().getContent()
        ```</blockquote>

        Returns
        - the contents of this URL.

        Raises
        - IOException: if an I/O exception occurs.

        See
        - java.net.URLConnection.getContent()
        """
        ...


    def getContent(self, classes: list[type[Any]]) -> "Object":
        """
        Gets the contents of this URL. This method is a shorthand for:
        <blockquote>```
            openConnection().getContent(classes)
        ```</blockquote>

        Arguments
        - classes: an array of Java types

        Returns
        - the content object of this URL that is the first match of
                      the types specified in the classes array.
                      null if none of the requested types are supported.

        Raises
        - IOException: if an I/O exception occurs.

        See
        - java.net.URLConnection.getContent(Class[])

        Since
        - 1.3
        """
        ...


    @staticmethod
    def setURLStreamHandlerFactory(fac: "URLStreamHandlerFactory") -> None:
        """
        Sets an application's `URLStreamHandlerFactory`.
        This method can be called at most once in a given Java Virtual
        Machine.
        
         The `URLStreamHandlerFactory` instance is used to
        construct a stream protocol handler from a protocol name.
        
         If there is a security manager, this method first calls
        the security manager's `checkSetFactory` method
        to ensure the operation is allowed.
        This could result in a SecurityException.

        Arguments
        - fac: the desired factory.

        Raises
        - Error: if the application has already set a factory.
        - SecurityException: if a security manager exists and its
                    `checkSetFactory` method doesn't allow
                    the operation.

        See
        - SecurityManager.checkSetFactory
        """
        ...
