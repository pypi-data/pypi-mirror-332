"""
Python module generated from Java source file java.net.URLConnection

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import IOException
from java.io import InputStream
from java.io import OutputStream
from java.net import *
from java.security import AccessController
from java.security import Permission
from java.security import PrivilegedAction
from java.util import Collections
from java.util import Date
from java.util import Hashtable
from java.util import Iterator
from java.util import Locale
from java.util import Objects
from java.util import ServiceConfigurationError
from java.util import ServiceLoader
from java.util import StringTokenizer
from java.util.concurrent import ConcurrentHashMap
from sun.net.www import MessageHeader
from sun.security.action import GetPropertyAction
from sun.security.util import SecurityConstants
from typing import Any, Callable, Iterable, Tuple


class URLConnection:
    """
    The abstract class `URLConnection` is the superclass
    of all classes that represent a communications link between the
    application and a URL. Instances of this class can be used both to
    read from and to write to the resource referenced by the URL.
    
    
    In general, creating a connection to a URL is a multistep process:
    <ol>
    - The connection object is created by invoking the
        URL.openConnection() openConnection method on a URL.
    - The setup parameters and general request properties are manipulated.
    - The actual connection to the remote object is made, using the
       .connect() connect method.
    - The remote object becomes available. The header fields and the contents
        of the remote object can be accessed.
    </ol>
    
    The setup parameters are modified using the following methods:
    
      - `setAllowUserInteraction`
      - `setDoInput`
      - `setDoOutput`
      - `setIfModifiedSince`
      - `setUseCaches`
    
    
    and the general request properties are modified using the method:
    
      - `setRequestProperty`
    
    
    Default values for the `AllowUserInteraction` and
    `UseCaches` parameters can be set using the methods
    `setDefaultAllowUserInteraction` and
    `setDefaultUseCaches`.
    
    Each of the above `set` methods has a corresponding
    `get` method to retrieve the value of the parameter or
    general request property. The specific parameters and general
    request properties that are applicable are protocol specific.
    
    The following methods are used to access the header fields and
    the contents after the connection is made to the remote object:
    
      - `getContent`
      - `getHeaderField`
      - `getInputStream`
      - `getOutputStream`
    
    
    Certain header fields are accessed frequently. The methods:
    
      - `getContentEncoding`
      - `getContentLength`
      - `getContentType`
      - `getDate`
      - `getExpiration`
      - `getLastModified`
    
    
    provide convenient access to these fields. The
    `getContentType` method is used by the
    `getContent` method to determine the type of the remote
    object; subclasses may find it convenient to override the
    `getContentType` method.
    
    In the common case, all of the pre-connection parameters and
    general request properties can be ignored: the pre-connection
    parameters and request properties default to sensible values. For
    most clients of this interface, there are only two interesting
    methods: `getInputStream` and `getContent`,
    which are mirrored in the `URL` class by convenience methods.
    
    More information on the request properties and header fields of
    an `http` connection can be found at:
    <blockquote>```
    <a href="http://www.ietf.org/rfc/rfc2616.txt">http://www.ietf.org/rfc/rfc2616.txt</a>
    ```</blockquote>
    
    Invoking the `close()` methods on the `InputStream` or `OutputStream` of an
    `URLConnection` after a request may free network resources associated with this
    instance, unless particular protocol specifications specify different behaviours
    for it.

    Author(s)
    - James Gosling

    See
    - java.net.URLConnection.setUseCaches(boolean)

    Since
    - 1.0
    """

    @staticmethod
    def getFileNameMap() -> "FileNameMap":
        """
        Loads filename map (a mimetable) from a data file. It will
        first try to load the user-specific table, defined
        by &quot;content.types.user.table&quot; property. If that fails,
        it tries to load the default built-in table.

        Returns
        - the FileNameMap

        See
        - .setFileNameMap(java.net.FileNameMap)

        Since
        - 1.2
        """
        ...


    @staticmethod
    def setFileNameMap(map: "FileNameMap") -> None:
        """
        Sets the FileNameMap.
        
        If there is a security manager, this method first calls
        the security manager's `checkSetFactory` method
        to ensure the operation is allowed.
        This could result in a SecurityException.

        Arguments
        - map: the FileNameMap to be set

        Raises
        - SecurityException: if a security manager exists and its
                    `checkSetFactory` method doesn't allow the operation.

        See
        - .getFileNameMap()

        Since
        - 1.2
        """
        ...


    def connect(self) -> None:
        """
        Opens a communications link to the resource referenced by this
        URL, if such a connection has not already been established.
        
        If the `connect` method is called when the connection
        has already been opened (indicated by the `connected`
        field having the value `True`), the call is ignored.
        
        URLConnection objects go through two phases: first they are
        created, then they are connected.  After being created, and
        before being connected, various options can be specified
        (e.g., doInput and UseCaches).  After connecting, it is an
        error to try to set them.  Operations that depend on being
        connected, like getContentLength, will implicitly perform the
        connection, if necessary.

        Raises
        - SocketTimeoutException: if the timeout expires before
                      the connection can be established
        - IOException: if an I/O error occurs while opening the
                      connection.

        See
        - .setConnectTimeout(int)
        """
        ...


    def setConnectTimeout(self, timeout: int) -> None:
        """
        Sets a specified timeout value, in milliseconds, to be used
        when opening a communications link to the resource referenced
        by this URLConnection.  If the timeout expires before the
        connection can be established, a
        java.net.SocketTimeoutException is raised. A timeout of zero is
        interpreted as an infinite timeout.
        
         Some non-standard implementation of this method may ignore
        the specified timeout. To see the connect timeout set, please
        call getConnectTimeout().

        Arguments
        - timeout: an `int` that specifies the connect
                      timeout value in milliseconds

        Raises
        - IllegalArgumentException: if the timeout parameter is negative

        See
        - .connect()

        Since
        - 1.5
        """
        ...


    def getConnectTimeout(self) -> int:
        """
        Returns setting for connect timeout.
        
        0 return implies that the option is disabled
        (i.e., timeout of infinity).

        Returns
        - an `int` that indicates the connect timeout
                value in milliseconds

        See
        - .connect()

        Since
        - 1.5
        """
        ...


    def setReadTimeout(self, timeout: int) -> None:
        """
        Sets the read timeout to a specified timeout, in
        milliseconds. A non-zero value specifies the timeout when
        reading from Input stream when a connection is established to a
        resource. If the timeout expires before there is data available
        for read, a java.net.SocketTimeoutException is raised. A
        timeout of zero is interpreted as an infinite timeout.
        
         Some non-standard implementation of this method ignores the
        specified timeout. To see the read timeout set, please call
        getReadTimeout().

        Arguments
        - timeout: an `int` that specifies the timeout
        value to be used in milliseconds

        Raises
        - IllegalArgumentException: if the timeout parameter is negative

        See
        - InputStream.read()

        Since
        - 1.5
        """
        ...


    def getReadTimeout(self) -> int:
        """
        Returns setting for read timeout. 0 return implies that the
        option is disabled (i.e., timeout of infinity).

        Returns
        - an `int` that indicates the read timeout
                value in milliseconds

        See
        - InputStream.read()

        Since
        - 1.5
        """
        ...


    def getURL(self) -> "URL":
        """
        Returns the value of this `URLConnection`'s `URL`
        field.

        Returns
        - the value of this `URLConnection`'s `URL`
                 field.

        See
        - java.net.URLConnection.url
        """
        ...


    def getContentLength(self) -> int:
        """
        Returns the value of the `content-length` header field.
        <P>
        <B>Note</B>: .getContentLengthLong() getContentLengthLong()
        should be preferred over this method, since it returns a `long`
        instead and is therefore more portable.</P>

        Returns
        - the content length of the resource that this connection's URL
                 references, `-1` if the content length is not known,
                 or if the content length is greater than Integer.MAX_VALUE.
        """
        ...


    def getContentLengthLong(self) -> int:
        """
        Returns the value of the `content-length` header field as a
        long.

        Returns
        - the content length of the resource that this connection's URL
                 references, or `-1` if the content length is
                 not known.

        Since
        - 1.7
        """
        ...


    def getContentType(self) -> str:
        """
        Returns the value of the `content-type` header field.

        Returns
        - the content type of the resource that the URL references,
                 or `null` if not known.

        See
        - java.net.URLConnection.getHeaderField(java.lang.String)
        """
        ...


    def getContentEncoding(self) -> str:
        """
        Returns the value of the `content-encoding` header field.

        Returns
        - the content encoding of the resource that the URL references,
                 or `null` if not known.

        See
        - java.net.URLConnection.getHeaderField(java.lang.String)
        """
        ...


    def getExpiration(self) -> int:
        """
        Returns the value of the `expires` header field.

        Returns
        - the expiration date of the resource that this URL references,
                 or 0 if not known. The value is the number of milliseconds since
                 January 1, 1970 GMT.

        See
        - java.net.URLConnection.getHeaderField(java.lang.String)
        """
        ...


    def getDate(self) -> int:
        """
        Returns the value of the `date` header field.

        Returns
        - the sending date of the resource that the URL references,
                 or `0` if not known. The value returned is the
                 number of milliseconds since January 1, 1970 GMT.

        See
        - java.net.URLConnection.getHeaderField(java.lang.String)
        """
        ...


    def getLastModified(self) -> int:
        """
        Returns the value of the `last-modified` header field.
        The result is the number of milliseconds since January 1, 1970 GMT.

        Returns
        - the date the resource referenced by this
                 `URLConnection` was last modified, or 0 if not known.

        See
        - java.net.URLConnection.getHeaderField(java.lang.String)
        """
        ...


    def getHeaderField(self, name: str) -> str:
        """
        Returns the value of the named header field.
        
        If called on a connection that sets the same header multiple times
        with possibly different values, only the last value is returned.

        Arguments
        - name: the name of a header field.

        Returns
        - the value of the named header field, or `null`
                 if there is no such field in the header.
        """
        ...


    def getHeaderFields(self) -> dict[str, list[str]]:
        """
        Returns an unmodifiable Map of the header fields.
        The Map keys are Strings that represent the
        response-header field names. Each Map value is an
        unmodifiable List of Strings that represents
        the corresponding field values.

        Returns
        - a Map of header fields

        Since
        - 1.4
        """
        ...


    def getHeaderFieldInt(self, name: str, Default: int) -> int:
        """
        Returns the value of the named field parsed as a number.
        
        This form of `getHeaderField` exists because some
        connection types (e.g., `http-ng`) have pre-parsed
        headers. Classes for that connection type can override this method
        and short-circuit the parsing.

        Arguments
        - name: the name of the header field.
        - Default: the default value.

        Returns
        - the value of the named field, parsed as an integer. The
                 `Default` value is returned if the field is
                 missing or malformed.
        """
        ...


    def getHeaderFieldLong(self, name: str, Default: int) -> int:
        """
        Returns the value of the named field parsed as a number.
        
        This form of `getHeaderField` exists because some
        connection types (e.g., `http-ng`) have pre-parsed
        headers. Classes for that connection type can override this method
        and short-circuit the parsing.

        Arguments
        - name: the name of the header field.
        - Default: the default value.

        Returns
        - the value of the named field, parsed as a long. The
                 `Default` value is returned if the field is
                 missing or malformed.

        Since
        - 1.7
        """
        ...


    def getHeaderFieldDate(self, name: str, Default: int) -> int:
        """
        Returns the value of the named field parsed as date.
        The result is the number of milliseconds since January 1, 1970 GMT
        represented by the named field.
        
        This form of `getHeaderField` exists because some
        connection types (e.g., `http-ng`) have pre-parsed
        headers. Classes for that connection type can override this method
        and short-circuit the parsing.

        Arguments
        - name: the name of the header field.
        - Default: a default value.

        Returns
        - the value of the field, parsed as a date. The value of the
                 `Default` argument is returned if the field is
                 missing or malformed.
        """
        ...


    def getHeaderFieldKey(self, n: int) -> str:
        """
        Returns the key for the `n`<sup>th</sup> header field.
        Some implementations may treat the `0`<sup>th</sup>
        header field as special, in which case, .getHeaderField(int) getHeaderField(0)
        may return some value, but `getHeaderFieldKey(0)` returns `null`.
        For `n > 0` it returns `null` if there are fewer than `n+1` fields.

        Arguments
        - n: an index, where `n>=0`

        Returns
        - the key for the `n`<sup>th</sup> header field,
                 or `null` if there are fewer than `n+1`
                 fields when `n > 0`.
        """
        ...


    def getHeaderField(self, n: int) -> str:
        """
        Returns the value for the `n`<sup>th</sup> header field.
        It returns `null` if there are fewer than
        `n+1` fields.
        
        This method can be used in conjunction with the
        .getHeaderFieldKey(int) getHeaderFieldKey method to iterate through all
        the headers in the message.

        Arguments
        - n: an index, where `n>=0`

        Returns
        - the value of the `n`<sup>th</sup> header field
                 or `null` if there are fewer than `n+1` fields

        See
        - java.net.URLConnection.getHeaderFieldKey(int)
        """
        ...


    def getContent(self) -> "Object":
        """
        Retrieves the contents of this URL connection.
        
        This method first determines the content type of the object by
        calling the `getContentType` method. If this is
        the first time that the application has seen that specific content
        type, a content handler for that content type is created.
         This is done as follows:
        <ol>
        - If the application has set up a content handler factory instance
            using the `setContentHandlerFactory` method, the
            `createContentHandler` method of that instance is called
            with the content type as an argument; the result is a content
            handler for that content type.
        - If no `ContentHandlerFactory` has yet been set up,
            or if the factory's `createContentHandler` method
            returns `null`, then the java.util.ServiceLoader
            ServiceLoader mechanism is used to locate java.net.ContentHandlerFactory ContentHandlerFactory
            implementations using the system class
            loader. The order that factories are located is implementation
            specific, and an implementation is free to cache the located
            factories. A java.util.ServiceConfigurationError
            ServiceConfigurationError, `Error` or `RuntimeException`
            thrown from the `createContentHandler`, if encountered, will
            be propagated to the calling thread. The `createContentHandler` method of each factory, if instantiated, is
            invoked, with the content type, until a factory returns non-null,
            or all factories have been exhausted.
        - Failing that, this method tries to load a content handler
            class as defined by java.net.ContentHandler ContentHandler.
            If the class does not exist, or is not a subclass of `ContentHandler`, then an `UnknownServiceException` is thrown.
        </ol>

        Returns
        - the object fetched. The `instanceof` operator
                      should be used to determine the specific kind of object
                      returned.

        Raises
        - IOException: if an I/O error occurs while
                      getting the content.
        - UnknownServiceException: if the protocol does not support
                      the content type.

        See
        - java.net.URLConnection.setContentHandlerFactory(java.net.ContentHandlerFactory)
        """
        ...


    def getContent(self, classes: list[type[Any]]) -> "Object":
        """
        Retrieves the contents of this URL connection.

        Arguments
        - classes: the `Class` array
        indicating the requested types

        Returns
        - the object fetched that is the first match of the type
                      specified in the classes array. null if none of
                      the requested types are supported.
                      The `instanceof` operator should be used to
                      determine the specific kind of object returned.

        Raises
        - IOException: if an I/O error occurs while
                      getting the content.
        - UnknownServiceException: if the protocol does not support
                      the content type.

        See
        - java.net.URLConnection.setContentHandlerFactory(java.net.ContentHandlerFactory)

        Since
        - 1.3
        """
        ...


    def getPermission(self) -> "Permission":
        """
        Returns a permission object representing the permission
        necessary to make the connection represented by this
        object. This method returns null if no permission is
        required to make the connection. By default, this method
        returns `java.security.AllPermission`. Subclasses
        should override this method and return the permission
        that best represents the permission required to make
        a connection to the URL. For example, a `URLConnection`
        representing a `file:` URL would return a
        `java.io.FilePermission` object.
        
        The permission returned may dependent upon the state of the
        connection. For example, the permission before connecting may be
        different from that after connecting. For example, an HTTP
        sever, say foo.com, may redirect the connection to a different
        host, say bar.com. Before connecting the permission returned by
        the connection will represent the permission needed to connect
        to foo.com, while the permission returned after connecting will
        be to bar.com.
        
        Permissions are generally used for two purposes: to protect
        caches of objects obtained through URLConnections, and to check
        the right of a recipient to learn about a particular URL. In
        the first case, the permission should be obtained
        *after* the object has been obtained. For example, in an
        HTTP connection, this will represent the permission to connect
        to the host from which the data was ultimately fetched. In the
        second case, the permission should be obtained and tested
        *before* connecting.

        Returns
        - the permission object representing the permission
        necessary to make the connection represented by this
        URLConnection.

        Raises
        - IOException: if the computation of the permission
        requires network or file I/O and an exception occurs while
        computing it.
        """
        ...


    def getInputStream(self) -> "InputStream":
        """
        Returns an input stream that reads from this open connection.
        
        A SocketTimeoutException can be thrown when reading from the
        returned input stream if the read timeout expires before data
        is available for read.

        Returns
        - an input stream that reads from this open connection.

        Raises
        - IOException: if an I/O error occurs while
                      creating the input stream.
        - UnknownServiceException: if the protocol does not support
                      input.

        See
        - .getReadTimeout()
        """
        ...


    def getOutputStream(self) -> "OutputStream":
        """
        Returns an output stream that writes to this connection.

        Returns
        - an output stream that writes to this connection.

        Raises
        - IOException: if an I/O error occurs while
                      creating the output stream.
        - UnknownServiceException: if the protocol does not support
                      output.
        """
        ...


    def toString(self) -> str:
        """
        Returns a `String` representation of this URL connection.

        Returns
        - a string representation of this `URLConnection`.
        """
        ...


    def setDoInput(self, doinput: bool) -> None:
        """
        Sets the value of the `doInput` field for this
        `URLConnection` to the specified value.
        
        A URL connection can be used for input and/or output.  Set the doInput
        flag to True if you intend to use the URL connection for input,
        False if not.  The default is True.

        Arguments
        - doinput: the new value.

        Raises
        - IllegalStateException: if already connected

        See
        - .getDoInput()
        """
        ...


    def getDoInput(self) -> bool:
        """
        Returns the value of this `URLConnection`'s
        `doInput` flag.

        Returns
        - the value of this `URLConnection`'s
                 `doInput` flag.

        See
        - .setDoInput(boolean)
        """
        ...


    def setDoOutput(self, dooutput: bool) -> None:
        """
        Sets the value of the `doOutput` field for this
        `URLConnection` to the specified value.
        
        A URL connection can be used for input and/or output.  Set the doOutput
        flag to True if you intend to use the URL connection for output,
        False if not.  The default is False.

        Arguments
        - dooutput: the new value.

        Raises
        - IllegalStateException: if already connected

        See
        - .getDoOutput()
        """
        ...


    def getDoOutput(self) -> bool:
        """
        Returns the value of this `URLConnection`'s
        `doOutput` flag.

        Returns
        - the value of this `URLConnection`'s
                 `doOutput` flag.

        See
        - .setDoOutput(boolean)
        """
        ...


    def setAllowUserInteraction(self, allowuserinteraction: bool) -> None:
        """
        Set the value of the `allowUserInteraction` field of
        this `URLConnection`.

        Arguments
        - allowuserinteraction: the new value.

        Raises
        - IllegalStateException: if already connected

        See
        - .getAllowUserInteraction()
        """
        ...


    def getAllowUserInteraction(self) -> bool:
        """
        Returns the value of the `allowUserInteraction` field for
        this object.

        Returns
        - the value of the `allowUserInteraction` field for
                 this object.

        See
        - .setAllowUserInteraction(boolean)
        """
        ...


    @staticmethod
    def setDefaultAllowUserInteraction(defaultallowuserinteraction: bool) -> None:
        """
        Sets the default value of the
        `allowUserInteraction` field for all future
        `URLConnection` objects to the specified value.

        Arguments
        - defaultallowuserinteraction: the new value.

        See
        - .getDefaultAllowUserInteraction()
        """
        ...


    @staticmethod
    def getDefaultAllowUserInteraction() -> bool:
        """
        Returns the default value of the `allowUserInteraction`
        field.
        
        This default is "sticky", being a part of the static state of all
        URLConnections.  This flag applies to the next, and all following
        URLConnections that are created.

        Returns
        - the default value of the `allowUserInteraction`
                 field.

        See
        - .setDefaultAllowUserInteraction(boolean)
        """
        ...


    def setUseCaches(self, usecaches: bool) -> None:
        """
        Sets the value of the `useCaches` field of this
        `URLConnection` to the specified value.
        
        Some protocols do caching of documents.  Occasionally, it is important
        to be able to "tunnel through" and ignore the caches (e.g., the
        "reload" button in a browser).  If the UseCaches flag on a connection
        is True, the connection is allowed to use whatever caches it can.
         If False, caches are to be ignored.
         The default value comes from defaultUseCaches, which defaults to
        True. A default value can also be set per-protocol using
        .setDefaultUseCaches(String,boolean).

        Arguments
        - usecaches: a `boolean` indicating whether
        or not to allow caching

        Raises
        - IllegalStateException: if already connected

        See
        - .getUseCaches()
        """
        ...


    def getUseCaches(self) -> bool:
        """
        Returns the value of this `URLConnection`'s
        `useCaches` field.

        Returns
        - the value of this `URLConnection`'s
                 `useCaches` field.

        See
        - .setUseCaches(boolean)
        """
        ...


    def setIfModifiedSince(self, ifmodifiedsince: int) -> None:
        """
        Sets the value of the `ifModifiedSince` field of
        this `URLConnection` to the specified value.

        Arguments
        - ifmodifiedsince: the new value.

        Raises
        - IllegalStateException: if already connected

        See
        - .getIfModifiedSince()
        """
        ...


    def getIfModifiedSince(self) -> int:
        """
        Returns the value of this object's `ifModifiedSince` field.

        Returns
        - the value of this object's `ifModifiedSince` field.

        See
        - .setIfModifiedSince(long)
        """
        ...


    def getDefaultUseCaches(self) -> bool:
        """
        Returns the default value of a `URLConnection`'s
        `useCaches` flag.
        
        This default is "sticky", being a part of the static state of all
        URLConnections.  This flag applies to the next, and all following
        URLConnections that are created. This default value can be over-ridden
        per protocol using .setDefaultUseCaches(String,boolean)

        Returns
        - the default value of a `URLConnection`'s
                 `useCaches` flag.

        See
        - .setDefaultUseCaches(boolean)
        """
        ...


    def setDefaultUseCaches(self, defaultusecaches: bool) -> None:
        """
        Sets the default value of the `useCaches` field to the
        specified value. This default value can be over-ridden
        per protocol using .setDefaultUseCaches(String,boolean)

        Arguments
        - defaultusecaches: the new value.

        See
        - .getDefaultUseCaches()
        """
        ...


    @staticmethod
    def setDefaultUseCaches(protocol: str, defaultVal: bool) -> None:
        """
        Sets the default value of the `useCaches` field for the named
        protocol to the given value. This value overrides any default setting
        set by .setDefaultUseCaches(boolean) for the given protocol.
        Successive calls to this method change the setting and affect the
        default value for all future connections of that protocol. The protocol
        name is case insensitive.

        Arguments
        - protocol: the protocol to set the default for
        - defaultVal: whether caching is enabled by default for the given protocol

        Since
        - 9
        """
        ...


    @staticmethod
    def getDefaultUseCaches(protocol: str) -> bool:
        """
        Returns the default value of the `useCaches` flag for the given protocol. If
        .setDefaultUseCaches(String,boolean) was called for the given protocol,
        then that value is returned. Otherwise, if .setDefaultUseCaches(boolean)
        was called, then that value is returned. If neither method was called,
        the return value is `True`. The protocol name is case insensitive.

        Arguments
        - protocol: the protocol whose defaultUseCaches setting is required

        Returns
        - the default value of the `useCaches` flag for the given protocol.

        Since
        - 9
        """
        ...


    def setRequestProperty(self, key: str, value: str) -> None:
        """
        Sets the general request property. If a property with the key already
        exists, overwrite its value with the new value.
        
         NOTE: HTTP requires all request properties which can
        legally have multiple instances with the same key
        to use a comma-separated list syntax which enables multiple
        properties to be appended into a single property.

        Arguments
        - key: the keyword by which the request is known
                         (e.g., "`Accept`").
        - value: the value associated with it.

        Raises
        - IllegalStateException: if already connected
        - NullPointerException: if key is `null`

        See
        - .getRequestProperty(java.lang.String)
        """
        ...


    def addRequestProperty(self, key: str, value: str) -> None:
        """
        Adds a general request property specified by a
        key-value pair.  This method will not overwrite
        existing values associated with the same key.

        Arguments
        - key: the keyword by which the request is known
                         (e.g., "`Accept`").
        - value: the value associated with it.

        Raises
        - IllegalStateException: if already connected
        - NullPointerException: if key is null

        See
        - .getRequestProperties()

        Since
        - 1.4
        """
        ...


    def getRequestProperty(self, key: str) -> str:
        """
        Returns the value of the named general request property for this
        connection.

        Arguments
        - key: the keyword by which the request is known (e.g., "Accept").

        Returns
        - the value of the named general request property for this
                  connection. If key is null, then null is returned.

        Raises
        - IllegalStateException: if already connected

        See
        - .setRequestProperty(java.lang.String, java.lang.String)
        """
        ...


    def getRequestProperties(self) -> dict[str, list[str]]:
        """
        Returns an unmodifiable Map of general request
        properties for this connection. The Map keys
        are Strings that represent the request-header
        field names. Each Map value is a unmodifiable List
        of Strings that represents the corresponding
        field values.

        Returns
        - a Map of the general request properties for this connection.

        Raises
        - IllegalStateException: if already connected

        Since
        - 1.4
        """
        ...


    @staticmethod
    def setDefaultRequestProperty(key: str, value: str) -> None:
        """
        Sets the default value of a general request property. When a
        `URLConnection` is created, it is initialized with
        these properties.

        Arguments
        - key: the keyword by which the request is known
                         (e.g., "`Accept`").
        - value: the value associated with the key.

        See
        - .getDefaultRequestProperty(java.lang.String)

        Deprecated
        - The instance specific setRequestProperty method
        should be used after an appropriate instance of URLConnection
        is obtained. Invoking this method will have no effect.
        """
        ...


    @staticmethod
    def getDefaultRequestProperty(key: str) -> str:
        """
        Returns the value of the default request property. Default request
        properties are set for every connection.

        Arguments
        - key: the keyword by which the request is known (e.g., "Accept").

        Returns
        - the value of the default request property
        for the specified key.

        See
        - .setDefaultRequestProperty(java.lang.String, java.lang.String)

        Deprecated
        - The instance specific getRequestProperty method
        should be used after an appropriate instance of URLConnection
        is obtained.
        """
        ...


    @staticmethod
    def setContentHandlerFactory(fac: "ContentHandlerFactory") -> None:
        """
        Sets the `ContentHandlerFactory` of an
        application. It can be called at most once by an application.
        
        The `ContentHandlerFactory` instance is used to
        construct a content handler from a content type.
        
        If there is a security manager, this method first calls
        the security manager's `checkSetFactory` method
        to ensure the operation is allowed.
        This could result in a SecurityException.

        Arguments
        - fac: the desired factory.

        Raises
        - Error: if the factory has already been defined.
        - SecurityException: if a security manager exists and its
                    `checkSetFactory` method doesn't allow the operation.

        See
        - SecurityManager.checkSetFactory
        """
        ...


    @staticmethod
    def guessContentTypeFromName(fname: str) -> str:
        """
        Tries to determine the content type of an object, based
        on the specified "file" component of a URL.
        This is a convenience method that can be used by
        subclasses that override the `getContentType` method.

        Arguments
        - fname: a filename.

        Returns
        - a guess as to what the content type of the object is,
                 based upon its file name.

        See
        - java.net.URLConnection.getContentType()
        """
        ...


    @staticmethod
    def guessContentTypeFromStream(is: "InputStream") -> str:
        """
        Tries to determine the type of an input stream based on the
        characters at the beginning of the input stream. This method can
        be used by subclasses that override the
        `getContentType` method.
        
        Ideally, this routine would not be needed. But many
        `http` servers return the incorrect content type; in
        addition, there are many nonstandard extensions. Direct inspection
        of the bytes to determine the content type is often more accurate
        than believing the content type claimed by the `http` server.

        Arguments
        - is: an input stream that supports marks.

        Returns
        - a guess at the content type, or `null` if none
                    can be determined.

        Raises
        - IOException: if an I/O error occurs while reading the
                      input stream.

        See
        - java.net.URLConnection.getContentType()
        """
        ...
