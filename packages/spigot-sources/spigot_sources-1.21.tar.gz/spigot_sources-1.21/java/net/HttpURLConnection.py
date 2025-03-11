"""
Python module generated from Java source file java.net.HttpURLConnection

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import IOException
from java.io import InputStream
from java.net import *
from java.security import Permission
from java.util import Date
from typing import Any, Callable, Iterable, Tuple


class HttpURLConnection(URLConnection):
    """
    A URLConnection with support for HTTP-specific features. See
    <A HREF="http://www.w3.org/pub/WWW/Protocols/"> the spec </A> for
    details.
    
    
    Each HttpURLConnection instance is used to make a single request
    but the underlying network connection to the HTTP server may be
    transparently shared by other instances. Calling the close() methods
    on the InputStream or OutputStream of an HttpURLConnection
    after a request may free network resources associated with this
    instance but has no effect on any shared persistent connection.
    Calling the disconnect() method may close the underlying socket
    if a persistent connection is otherwise idle at that time.
    
    <P>The HTTP protocol handler has a few settings that can be accessed through
    System Properties. This covers
    <a href="doc-files/net-properties.html#Proxies">Proxy settings</a> as well as
    <a href="doc-files/net-properties.html#MiscHTTP"> various other settings</a>.
    </P>
    
    **Security permissions**
    
    If a security manager is installed, and if a method is called which results in an
    attempt to open a connection, the caller must possess either:
    - a "connect" SocketPermission to the host/port combination of the
    destination URL or
    - a URLPermission that permits this request.
    
    If automatic redirection is enabled, and this request is redirected to another
    destination, then the caller must also have permission to connect to the
    redirected host/URL.

    See
    - java.net.HttpURLConnection.disconnect()

    Since
    - 1.1
    """

    HTTP_OK = 200
    """
    HTTP Status-Code 200: OK.
    """
    HTTP_CREATED = 201
    """
    HTTP Status-Code 201: Created.
    """
    HTTP_ACCEPTED = 202
    """
    HTTP Status-Code 202: Accepted.
    """
    HTTP_NOT_AUTHORITATIVE = 203
    """
    HTTP Status-Code 203: Non-Authoritative Information.
    """
    HTTP_NO_CONTENT = 204
    """
    HTTP Status-Code 204: No Content.
    """
    HTTP_RESET = 205
    """
    HTTP Status-Code 205: Reset Content.
    """
    HTTP_PARTIAL = 206
    """
    HTTP Status-Code 206: Partial Content.
    """
    HTTP_MULT_CHOICE = 300
    """
    HTTP Status-Code 300: Multiple Choices.
    """
    HTTP_MOVED_PERM = 301
    """
    HTTP Status-Code 301: Moved Permanently.
    """
    HTTP_MOVED_TEMP = 302
    """
    HTTP Status-Code 302: Temporary Redirect.
    """
    HTTP_SEE_OTHER = 303
    """
    HTTP Status-Code 303: See Other.
    """
    HTTP_NOT_MODIFIED = 304
    """
    HTTP Status-Code 304: Not Modified.
    """
    HTTP_USE_PROXY = 305
    """
    HTTP Status-Code 305: Use Proxy.
    """
    HTTP_BAD_REQUEST = 400
    """
    HTTP Status-Code 400: Bad Request.
    """
    HTTP_UNAUTHORIZED = 401
    """
    HTTP Status-Code 401: Unauthorized.
    """
    HTTP_PAYMENT_REQUIRED = 402
    """
    HTTP Status-Code 402: Payment Required.
    """
    HTTP_FORBIDDEN = 403
    """
    HTTP Status-Code 403: Forbidden.
    """
    HTTP_NOT_FOUND = 404
    """
    HTTP Status-Code 404: Not Found.
    """
    HTTP_BAD_METHOD = 405
    """
    HTTP Status-Code 405: Method Not Allowed.
    """
    HTTP_NOT_ACCEPTABLE = 406
    """
    HTTP Status-Code 406: Not Acceptable.
    """
    HTTP_PROXY_AUTH = 407
    """
    HTTP Status-Code 407: Proxy Authentication Required.
    """
    HTTP_CLIENT_TIMEOUT = 408
    """
    HTTP Status-Code 408: Request Time-Out.
    """
    HTTP_CONFLICT = 409
    """
    HTTP Status-Code 409: Conflict.
    """
    HTTP_GONE = 410
    """
    HTTP Status-Code 410: Gone.
    """
    HTTP_LENGTH_REQUIRED = 411
    """
    HTTP Status-Code 411: Length Required.
    """
    HTTP_PRECON_FAILED = 412
    """
    HTTP Status-Code 412: Precondition Failed.
    """
    HTTP_ENTITY_TOO_LARGE = 413
    """
    HTTP Status-Code 413: Request Entity Too Large.
    """
    HTTP_REQ_TOO_LONG = 414
    """
    HTTP Status-Code 414: Request-URI Too Large.
    """
    HTTP_UNSUPPORTED_TYPE = 415
    """
    HTTP Status-Code 415: Unsupported Media Type.
    """
    HTTP_SERVER_ERROR = 500
    """
    HTTP Status-Code 500: Internal Server Error.

    Deprecated
    - it is misplaced and shouldn't have existed.
    """
    HTTP_INTERNAL_ERROR = 500
    """
    HTTP Status-Code 500: Internal Server Error.
    """
    HTTP_NOT_IMPLEMENTED = 501
    """
    HTTP Status-Code 501: Not Implemented.
    """
    HTTP_BAD_GATEWAY = 502
    """
    HTTP Status-Code 502: Bad Gateway.
    """
    HTTP_UNAVAILABLE = 503
    """
    HTTP Status-Code 503: Service Unavailable.
    """
    HTTP_GATEWAY_TIMEOUT = 504
    """
    HTTP Status-Code 504: Gateway Timeout.
    """
    HTTP_VERSION = 505
    """
    HTTP Status-Code 505: HTTP Version Not Supported.
    """


    def setAuthenticator(self, auth: "Authenticator") -> None:
        """
        Supplies an java.net.Authenticator Authenticator to be used
        when authentication is requested through the HTTP protocol for
        this `HttpURLConnection`.
        If no authenticator is supplied, the
        Authenticator.setDefault(java.net.Authenticator) default
        authenticator will be used.

        Arguments
        - auth: The `Authenticator` that should be used by this
                  `HttpURLConnection`.

        Raises
        - UnsupportedOperationException: if setting an Authenticator is
                 not supported by the underlying implementation.
        - IllegalStateException: if URLConnection is already connected.
        - NullPointerException: if the supplied `auth` is `null`.

        Since
        - 9

        Unknown Tags
        - The default behavior of this method is to unconditionally
                  throw UnsupportedOperationException. Concrete
                  implementations of `HttpURLConnection`
                  which support supplying an `Authenticator` for a
                  specific `HttpURLConnection` instance should
                  override this method to implement a different behavior.
        - Depending on authentication schemes, an implementation
                  may or may not need to use the provided authenticator
                  to obtain a password. For instance, an implementation that
                  relies on third-party security libraries may still invoke the
                  default authenticator if these libraries are configured
                  to do so.
                  Likewise, an implementation that supports transparent
                  NTLM authentication may let the system attempt
                  to connect using the system user credentials first,
                  before invoking the provided authenticator.
                  
                  However, if an authenticator is specifically provided,
                  then the underlying connection may only be reused for
                  `HttpURLConnection` instances which share the same
                  `Authenticator` instance, and authentication information,
                  if cached, may only be reused for an `HttpURLConnection`
                  sharing that same `Authenticator`.
        """
        ...


    def getHeaderFieldKey(self, n: int) -> str:
        """
        Returns the key for the `n`<sup>th</sup> header field.
        Some implementations may treat the `0`<sup>th</sup>
        header field as special, i.e. as the status line returned by the HTTP
        server. In this case, .getHeaderField(int) getHeaderField(0) returns the status
        line, but `getHeaderFieldKey(0)` returns null.

        Arguments
        - n: an index, where `n >=0`.

        Returns
        - the key for the `n`<sup>th</sup> header field,
                 or `null` if the key does not exist.
        """
        ...


    def setFixedLengthStreamingMode(self, contentLength: int) -> None:
        """
        This method is used to enable streaming of a HTTP request body
        without internal buffering, when the content length is known in
        advance.
        
        An exception will be thrown if the application
        attempts to write more data than the indicated
        content-length, or if the application closes the OutputStream
        before writing the indicated amount.
        
        When output streaming is enabled, authentication
        and redirection cannot be handled automatically.
        A HttpRetryException will be thrown when reading
        the response if authentication or redirection are required.
        This exception can be queried for the details of the error.
        
        This method must be called before the URLConnection is connected.
        
        <B>NOTE:</B> .setFixedLengthStreamingMode(long) is recommended
        instead of this method as it allows larger content lengths to be set.

        Arguments
        - contentLength: The number of bytes which will be written
                 to the OutputStream.

        Raises
        - IllegalStateException: if URLConnection is already connected
                 or if a different streaming mode is already enabled.
        - IllegalArgumentException: if a content length less than
                 zero is specified.

        See
        - .setChunkedStreamingMode(int)

        Since
        - 1.5
        """
        ...


    def setFixedLengthStreamingMode(self, contentLength: int) -> None:
        """
        This method is used to enable streaming of a HTTP request body
        without internal buffering, when the content length is known in
        advance.
        
        <P> An exception will be thrown if the application attempts to write
        more data than the indicated content-length, or if the application
        closes the OutputStream before writing the indicated amount.
        
        <P> When output streaming is enabled, authentication and redirection
        cannot be handled automatically. A HttpRetryException will
        be thrown when reading the response if authentication or redirection
        are required. This exception can be queried for the details of the
        error.
        
        <P> This method must be called before the URLConnection is connected.
        
        <P> The content length set by invoking this method takes precedence
        over any value set by .setFixedLengthStreamingMode(int).

        Arguments
        - contentLength: The number of bytes which will be written to the OutputStream.

        Raises
        - IllegalStateException: if URLConnection is already connected or if a different
                 streaming mode is already enabled.
        - IllegalArgumentException: if a content length less than zero is specified.

        Since
        - 1.7
        """
        ...


    def setChunkedStreamingMode(self, chunklen: int) -> None:
        """
        This method is used to enable streaming of a HTTP request body
        without internal buffering, when the content length is **not**
        known in advance. In this mode, chunked transfer encoding
        is used to send the request body. Note, not all HTTP servers
        support this mode.
        
        When output streaming is enabled, authentication
        and redirection cannot be handled automatically.
        A HttpRetryException will be thrown when reading
        the response if authentication or redirection are required.
        This exception can be queried for the details of the error.
        
        This method must be called before the URLConnection is connected.

        Arguments
        - chunklen: The number of bytes to write in each chunk.
                 If chunklen is less than or equal to zero, a default
                 value will be used.

        Raises
        - IllegalStateException: if URLConnection is already connected
                 or if a different streaming mode is already enabled.

        See
        - .setFixedLengthStreamingMode(int)

        Since
        - 1.5
        """
        ...


    def getHeaderField(self, n: int) -> str:
        """
        Returns the value for the `n`<sup>th</sup> header field.
        Some implementations may treat the `0`<sup>th</sup>
        header field as special, i.e. as the status line returned by the HTTP
        server.
        
        This method can be used in conjunction with the
        .getHeaderFieldKey getHeaderFieldKey method to iterate through all
        the headers in the message.

        Arguments
        - n: an index, where `n>=0`.

        Returns
        - the value of the `n`<sup>th</sup> header field,
                 or `null` if the value does not exist.

        See
        - java.net.HttpURLConnection.getHeaderFieldKey(int)
        """
        ...


    @staticmethod
    def setFollowRedirects(set: bool) -> None:
        """
        Sets whether HTTP redirects  (requests with response code 3xx) should
        be automatically followed by this class.  True by default.  Applets
        cannot change this variable.
        
        If there is a security manager, this method first calls
        the security manager's `checkSetFactory` method
        to ensure the operation is allowed.
        This could result in a SecurityException.

        Arguments
        - set: a `boolean` indicating whether or not
        to follow HTTP redirects.

        Raises
        - SecurityException: if a security manager exists and its
                    `checkSetFactory` method doesn't
                    allow the operation.

        See
        - .getFollowRedirects()
        """
        ...


    @staticmethod
    def getFollowRedirects() -> bool:
        """
        Returns a `boolean` indicating
        whether or not HTTP redirects (3xx) should
        be automatically followed.

        Returns
        - `True` if HTTP redirects should
        be automatically followed, `False` if not.

        See
        - .setFollowRedirects(boolean)
        """
        ...


    def setInstanceFollowRedirects(self, followRedirects: bool) -> None:
        """
        Sets whether HTTP redirects (requests with response code 3xx) should
        be automatically followed by this `HttpURLConnection`
        instance.
        
        The default value comes from followRedirects, which defaults to
        True.

        Arguments
        - followRedirects: a `boolean` indicating
        whether or not to follow HTTP redirects.

        See
        - .getInstanceFollowRedirects

        Since
        - 1.3
        """
        ...


    def getInstanceFollowRedirects(self) -> bool:
        """
        Returns the value of this `HttpURLConnection`'s
        `instanceFollowRedirects` field.

        Returns
        - the value of this `HttpURLConnection`'s
                 `instanceFollowRedirects` field.

        See
        - .setInstanceFollowRedirects(boolean)

        Since
        - 1.3
        """
        ...


    def setRequestMethod(self, method: str) -> None:
        """
        Set the method for the URL request, one of:
        <UL>
         <LI>GET
         <LI>POST
         <LI>HEAD
         <LI>OPTIONS
         <LI>PUT
         <LI>DELETE
         <LI>TRACE
        </UL> are legal, subject to protocol restrictions.  The default
        method is GET.

        Arguments
        - method: the HTTP method

        Raises
        - ProtocolException: if the method cannot be reset or if
                     the requested method isn't valid for HTTP.
        - SecurityException: if a security manager is set and the
                     method is "TRACE", but the "allowHttpTrace"
                     NetPermission is not granted.

        See
        - .getRequestMethod()
        """
        ...


    def getRequestMethod(self) -> str:
        """
        Get the request method.

        Returns
        - the HTTP request method

        See
        - .setRequestMethod(java.lang.String)
        """
        ...


    def getResponseCode(self) -> int:
        """
        Gets the status code from an HTTP response message.
        For example, in the case of the following status lines:
        <PRE>
        HTTP/1.0 200 OK
        HTTP/1.0 401 Unauthorized
        </PRE>
        It will return 200 and 401 respectively.
        Returns -1 if no code can be discerned
        from the response (i.e., the response is not valid HTTP).

        Returns
        - the HTTP Status-Code, or -1

        Raises
        - IOException: if an error occurred connecting to the server.
        """
        ...


    def getResponseMessage(self) -> str:
        """
        Gets the HTTP response message, if any, returned along with the
        response code from a server.  From responses like:
        <PRE>
        HTTP/1.0 200 OK
        HTTP/1.0 404 Not Found
        </PRE>
        Extracts the Strings "OK" and "Not Found" respectively.
        Returns null if none could be discerned from the responses
        (the result was not valid HTTP).

        Returns
        - the HTTP response message, or `null`

        Raises
        - IOException: if an error occurred connecting to the server.
        """
        ...


    def getHeaderFieldDate(self, name: str, Default: int) -> int:
        ...


    def disconnect(self) -> None:
        """
        Indicates that other requests to the server
        are unlikely in the near future. Calling disconnect()
        should not imply that this HttpURLConnection
        instance can be reused for other requests.
        """
        ...


    def usingProxy(self) -> bool:
        """
        Indicates if the connection is going through a proxy.
        
        This method returns `True` if the connection is known
        to be going or has gone through proxies, and returns `False`
        if the connection will never go through a proxy or if
        the use of a proxy cannot be determined.

        Returns
        - a boolean indicating if the connection is using a proxy.
        """
        ...


    def getPermission(self) -> "Permission":
        """
        Returns a SocketPermission object representing the
        permission necessary to connect to the destination host and port.

        Returns
        - a `SocketPermission` object representing the
                permission necessary to connect to the destination
                host and port.

        Raises
        - IOException: if an error occurs while computing
                   the permission.
        """
        ...


    def getErrorStream(self) -> "InputStream":
        """
        Returns the error stream if the connection failed
        but the server sent useful data nonetheless. The
        typical example is when an HTTP server responds
        with a 404, which will cause a FileNotFoundException
        to be thrown in connect, but the server sent an HTML
        help page with suggestions as to what to do.
        
        This method will not cause a connection to be initiated.  If
        the connection was not connected, or if the server did not have
        an error while connecting or if the server had an error but
        no error data was sent, this method will return null. This is
        the default.

        Returns
        - an error stream if any, null if there have been no
        errors, the connection is not connected or the server sent no
        useful data.
        """
        ...
