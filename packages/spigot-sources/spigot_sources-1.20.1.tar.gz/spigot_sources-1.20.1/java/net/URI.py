"""
Python module generated from Java source file java.net.URI

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import File
from java.io import IOException
from java.io import InvalidObjectException
from java.io import ObjectInputStream
from java.io import ObjectOutputStream
from java.io import Serializable
from java.net import *
from java.nio.charset import CharacterCodingException
from java.nio.charset import CharsetDecoder
from java.nio.charset import CharsetEncoder
from java.nio.charset import CoderResult
from java.nio.charset import CodingErrorAction
from java.nio.file import Path
from java.text import Normalizer
from jdk.internal.access import JavaNetUriAccess
from jdk.internal.access import SharedSecrets
from sun.nio.cs import UTF_8
from typing import Any, Callable, Iterable, Tuple


class URI(Comparable, Serializable):

    def __init__(self, str: str):
        """
        Constructs a URI by parsing the given string.
        
         This constructor parses the given string exactly as specified by the
        grammar in <a
        href="http://www.ietf.org/rfc/rfc2396.txt">RFC&nbsp;2396</a>,
        Appendix&nbsp;A, ***except for the following deviations:*** 
        
        
        
          -  An empty authority component is permitted as long as it is
          followed by a non-empty path, a query component, or a fragment
          component.  This allows the parsing of URIs such as
          `"file:///foo/bar"`, which seems to be the intent of
          RFC&nbsp;2396 although the grammar does not permit it.  If the
          authority component is empty then the user-information, host, and port
          components are undefined. 
        
          -  Empty relative paths are permitted; this seems to be the
          intent of RFC&nbsp;2396 although the grammar does not permit it.  The
          primary consequence of this deviation is that a standalone fragment
          such as `".foo"` parses as a relative URI with an empty path
          and the given fragment, and can be usefully <a
          href="#resolve-frag">resolved</a> against a base URI.
        
          -  IPv4 addresses in host components are parsed rigorously, as
          specified by <a
          href="http://www.ietf.org/rfc/rfc2732.txt">RFC&nbsp;2732</a>: Each
          element of a dotted-quad address must contain no more than three
          decimal digits.  Each element is further constrained to have a value
          no greater than 255. 
        
          -   Hostnames in host components that comprise only a single
          domain label are permitted to start with an *alphanum*
          character. This seems to be the intent of <a
          href="http://www.ietf.org/rfc/rfc2396.txt">RFC&nbsp;2396</a>
          section&nbsp;3.2.2 although the grammar does not permit it. The
          consequence of this deviation is that the authority component of a
          hierarchical URI such as `s://123`, will parse as a server-based
          authority. 
        
          -  IPv6 addresses are permitted for the host component.  An IPv6
          address must be enclosed in square brackets (`'['` and
          `']'`) as specified by <a
          href="http://www.ietf.org/rfc/rfc2732.txt">RFC&nbsp;2732</a>.  The
          IPv6 address itself must parse according to <a
          href="http://www.ietf.org/rfc/rfc2373.txt">RFC&nbsp;2373</a>.  IPv6
          addresses are further constrained to describe no more than sixteen
          bytes of address information, a constraint implicit in RFC&nbsp;2373
          but not expressible in the grammar. 
        
          -  Characters in the *other* category are permitted wherever
          RFC&nbsp;2396 permits *escaped* octets, that is, in the
          user-information, path, query, and fragment components, as well as in
          the authority component if the authority is registry-based.  This
          allows URIs to contain Unicode characters beyond those in the US-ASCII
          character set. 
        

        Arguments
        - str: The string to be parsed into a URI

        Raises
        - NullPointerException: If `str` is `null`
        - URISyntaxException: If the given string violates RFC&nbsp;2396, as augmented
                 by the above deviations
        """
        ...


    def __init__(self, scheme: str, userInfo: str, host: str, port: int, path: str, query: str, fragment: str):
        """
        Constructs a hierarchical URI from the given components.
        
         If a scheme is given then the path, if also given, must either be
        empty or begin with a slash character (`'/'`).  Otherwise a
        component of the new URI may be left undefined by passing `null`
        for the corresponding parameter or, in the case of the `port`
        parameter, by passing `-1`.
        
         This constructor first builds a URI string from the given components
        according to the rules specified in <a
        href="http://www.ietf.org/rfc/rfc2396.txt">RFC&nbsp;2396</a>,
        section&nbsp;5.2, step&nbsp;7: 
        
        <ol>
        
          -  Initially, the result string is empty. 
        
          -  If a scheme is given then it is appended to the result,
          followed by a colon character (`':'`).  
        
          -  If user information, a host, or a port are given then the
          string `"//"` is appended.  
        
          -  If user information is given then it is appended, followed by
          a commercial-at character (`'@'`).  Any character not in the
          *unreserved*, *punct*, *escaped*, or *other*
          categories is <a href="#quote">quoted</a>.  
        
          -  If a host is given then it is appended.  If the host is a
          literal IPv6 address but is not enclosed in square brackets
          (`'['` and `']'`) then the square brackets are added.
          
        
          -  If a port number is given then a colon character
          (`':'`) is appended, followed by the port number in decimal.
          
        
          -  If a path is given then it is appended.  Any character not in
          the *unreserved*, *punct*, *escaped*, or *other*
          categories, and not equal to the slash character (`'/'`) or the
          commercial-at character (`'@'`), is quoted.  
        
          -  If a query is given then a question-mark character
          (`'?'`) is appended, followed by the query.  Any character that
          is not a <a href="#legal-chars">legal URI character</a> is quoted.
          
        
          -  Finally, if a fragment is given then a hash character
          (`'.'`) is appended, followed by the fragment.  Any character
          that is not a legal URI character is quoted.  
        
        </ol>
        
         The resulting URI string is then parsed as if by invoking the .URI(String) constructor and then invoking the .parseServerAuthority() method upon the result; this may cause a URISyntaxException to be thrown.  

        Arguments
        - scheme: Scheme name
        - userInfo: User name and authorization information
        - host: Host name
        - port: Port number
        - path: Path
        - query: Query
        - fragment: Fragment

        Raises
        - URISyntaxException: If both a scheme and a path are given but the path is relative,
                if the URI string constructed from the given components violates
                RFC&nbsp;2396, or if the authority component of the string is
                present but cannot be parsed as a server-based authority
        """
        ...


    def __init__(self, scheme: str, authority: str, path: str, query: str, fragment: str):
        """
        Constructs a hierarchical URI from the given components.
        
         If a scheme is given then the path, if also given, must either be
        empty or begin with a slash character (`'/'`).  Otherwise a
        component of the new URI may be left undefined by passing `null`
        for the corresponding parameter.
        
         This constructor first builds a URI string from the given components
        according to the rules specified in <a
        href="http://www.ietf.org/rfc/rfc2396.txt">RFC&nbsp;2396</a>,
        section&nbsp;5.2, step&nbsp;7: 
        
        <ol>
        
          -  Initially, the result string is empty.  
        
          -  If a scheme is given then it is appended to the result,
          followed by a colon character (`':'`).  
        
          -  If an authority is given then the string `"//"` is
          appended, followed by the authority.  If the authority contains a
          literal IPv6 address then the address must be enclosed in square
          brackets (`'['` and `']'`).  Any character not in the
          *unreserved*, *punct*, *escaped*, or *other*
          categories, and not equal to the commercial-at character
          (`'@'`), is <a href="#quote">quoted</a>.  
        
          -  If a path is given then it is appended.  Any character not in
          the *unreserved*, *punct*, *escaped*, or *other*
          categories, and not equal to the slash character (`'/'`) or the
          commercial-at character (`'@'`), is quoted.  
        
          -  If a query is given then a question-mark character
          (`'?'`) is appended, followed by the query.  Any character that
          is not a <a href="#legal-chars">legal URI character</a> is quoted.
          
        
          -  Finally, if a fragment is given then a hash character
          (`'.'`) is appended, followed by the fragment.  Any character
          that is not a legal URI character is quoted.  
        
        </ol>
        
         The resulting URI string is then parsed as if by invoking the .URI(String) constructor and then invoking the .parseServerAuthority() method upon the result; this may cause a URISyntaxException to be thrown.  

        Arguments
        - scheme: Scheme name
        - authority: Authority
        - path: Path
        - query: Query
        - fragment: Fragment

        Raises
        - URISyntaxException: If both a scheme and a path are given but the path is relative,
                if the URI string constructed from the given components violates
                RFC&nbsp;2396, or if the authority component of the string is
                present but cannot be parsed as a server-based authority
        """
        ...


    def __init__(self, scheme: str, host: str, path: str, fragment: str):
        """
        Constructs a hierarchical URI from the given components.
        
         A component may be left undefined by passing `null`.
        
         This convenience constructor works as if by invoking the
        seven-argument constructor as follows:
        
        <blockquote>
        `new` .URI(String, String, String, int, String, String, String)
        URI`(scheme, null, host, -1, path, null, fragment);`
        </blockquote>

        Arguments
        - scheme: Scheme name
        - host: Host name
        - path: Path
        - fragment: Fragment

        Raises
        - URISyntaxException: If the URI string constructed from the given components
                 violates RFC&nbsp;2396
        """
        ...


    def __init__(self, scheme: str, ssp: str, fragment: str):
        """
        Constructs a URI from the given components.
        
         A component may be left undefined by passing `null`.
        
         This constructor first builds a URI in string form using the given
        components as follows:  
        
        <ol>
        
          -  Initially, the result string is empty.  
        
          -  If a scheme is given then it is appended to the result,
          followed by a colon character (`':'`).  
        
          -  If a scheme-specific part is given then it is appended.  Any
          character that is not a <a href="#legal-chars">legal URI character</a>
          is <a href="#quote">quoted</a>.  
        
          -  Finally, if a fragment is given then a hash character
          (`'.'`) is appended to the string, followed by the fragment.
          Any character that is not a legal URI character is quoted.  
        
        </ol>
        
         The resulting URI string is then parsed in order to create the new
        URI instance as if by invoking the .URI(String) constructor;
        this may cause a URISyntaxException to be thrown.  

        Arguments
        - scheme: Scheme name
        - ssp: Scheme-specific part
        - fragment: Fragment

        Raises
        - URISyntaxException: If the URI string constructed from the given components
                 violates RFC&nbsp;2396
        """
        ...


    @staticmethod
    def create(str: str) -> "URI":
        """
        Creates a URI by parsing the given string.
        
         This convenience factory method works as if by invoking the .URI(String) constructor; any URISyntaxException thrown by the
        constructor is caught and wrapped in a new IllegalArgumentException object, which is then thrown.
        
         This method is provided for use in situations where it is known that
        the given string is a legal URI, for example for URI constants declared
        within a program, and so it would be considered a programming error
        for the string not to parse as such.  The constructors, which throw
        URISyntaxException directly, should be used in situations where a
        URI is being constructed from user input or from some other source that
        may be prone to errors.  

        Arguments
        - str: The string to be parsed into a URI

        Returns
        - The new URI

        Raises
        - NullPointerException: If `str` is `null`
        - IllegalArgumentException: If the given string violates RFC&nbsp;2396
        """
        ...


    def parseServerAuthority(self) -> "URI":
        """
        Attempts to parse this URI's authority component, if defined, into
        user-information, host, and port components.
        
         If this URI's authority component has already been recognized as
        being server-based then it will already have been parsed into
        user-information, host, and port components.  In this case, or if this
        URI has no authority component, this method simply returns this URI.
        
         Otherwise this method attempts once more to parse the authority
        component into user-information, host, and port components, and throws
        an exception describing why the authority component could not be parsed
        in that way.
        
         This method is provided because the generic URI syntax specified in
        <a href="http://www.ietf.org/rfc/rfc2396.txt">RFC&nbsp;2396</a>
        cannot always distinguish a malformed server-based authority from a
        legitimate registry-based authority.  It must therefore treat some
        instances of the former as instances of the latter.  The authority
        component in the URI string `"//foo:bar"`, for example, is not a
        legal server-based authority but it is legal as a registry-based
        authority.
        
         In many common situations, for example when working URIs that are
        known to be either URNs or URLs, the hierarchical URIs being used will
        always be server-based.  They therefore must either be parsed as such or
        treated as an error.  In these cases a statement such as
        
        <blockquote>
        `URI`*u*`= new URI(str).parseServerAuthority();`
        </blockquote>
        
         can be used to ensure that *u* always refers to a URI that, if
        it has an authority component, has a server-based authority with proper
        user-information, host, and port components.  Invoking this method also
        ensures that if the authority could not be parsed in that way then an
        appropriate diagnostic message can be issued based upon the exception
        that is thrown. 

        Returns
        - A URI whose authority field has been parsed
                 as a server-based authority

        Raises
        - URISyntaxException: If the authority component of this URI is defined
                 but cannot be parsed as a server-based authority
                 according to RFC&nbsp;2396
        """
        ...


    def normalize(self) -> "URI":
        """
        Normalizes this URI's path.
        
         If this URI is opaque, or if its path is already in normal form,
        then this URI is returned.  Otherwise a new URI is constructed that is
        identical to this URI except that its path is computed by normalizing
        this URI's path in a manner consistent with <a
        href="http://www.ietf.org/rfc/rfc2396.txt">RFC&nbsp;2396</a>,
        section&nbsp;5.2, step&nbsp;6, sub-steps&nbsp;c through&nbsp;f; that is:
        
        
        <ol>
        
          -  All `"."` segments are removed. 
        
          -  If a `".."` segment is preceded by a non-`".."`
          segment then both of these segments are removed.  This step is
          repeated until it is no longer applicable. 
        
          -  If the path is relative, and if its first segment contains a
          colon character (`':'`), then a `"."` segment is
          prepended.  This prevents a relative URI with a path such as
          `"a:b/c/d"` from later being re-parsed as an opaque URI with a
          scheme of `"a"` and a scheme-specific part of `"b/c/d"`.
          ***(Deviation from RFC&nbsp;2396)*** 
        
        </ol>
        
         A normalized path will begin with one or more `".."` segments
        if there were insufficient non-`".."` segments preceding them to
        allow their removal.  A normalized path will begin with a `"."`
        segment if one was inserted by step 3 above.  Otherwise, a normalized
        path will not contain any `"."` or `".."` segments. 

        Returns
        - A URI equivalent to this URI,
                 but whose path is in normal form
        """
        ...


    def resolve(self, uri: "URI") -> "URI":
        """
        Resolves the given URI against this URI.
        
         If the given URI is already absolute, or if this URI is opaque, then
        the given URI is returned.
        
        <a id="resolve-frag"></a> If the given URI's fragment component is
        defined, its path component is empty, and its scheme, authority, and
        query components are undefined, then a URI with the given fragment but
        with all other components equal to those of this URI is returned.  This
        allows a URI representing a standalone fragment reference, such as
        `".foo"`, to be usefully resolved against a base URI.
        
         Otherwise this method constructs a new hierarchical URI in a manner
        consistent with <a
        href="http://www.ietf.org/rfc/rfc2396.txt">RFC&nbsp;2396</a>,
        section&nbsp;5.2; that is: 
        
        <ol>
        
          -  A new URI is constructed with this URI's scheme and the given
          URI's query and fragment components. 
        
          -  If the given URI has an authority component then the new URI's
          authority and path are taken from the given URI. 
        
          -  Otherwise the new URI's authority component is copied from
          this URI, and its path is computed as follows: 
        
          <ol>
        
            -  If the given URI's path is absolute then the new URI's path
            is taken from the given URI. 
        
            -  Otherwise the given URI's path is relative, and so the new
            URI's path is computed by resolving the path of the given URI
            against the path of this URI.  This is done by concatenating all but
            the last segment of this URI's path, if any, with the given URI's
            path and then normalizing the result as if by invoking the .normalize() normalize method. 
        
          </ol>
        
        </ol>
        
         The result of this method is absolute if, and only if, either this
        URI is absolute or the given URI is absolute.  

        Arguments
        - uri: The URI to be resolved against this URI

        Returns
        - The resulting URI

        Raises
        - NullPointerException: If `uri` is `null`
        """
        ...


    def resolve(self, str: str) -> "URI":
        """
        Constructs a new URI by parsing the given string and then resolving it
        against this URI.
        
         This convenience method works as if invoking it were equivalent to
        evaluating the expression .resolve(java.net.URI)
        resolve`(URI.`.create(String) create`(str))`. 

        Arguments
        - str: The string to be parsed into a URI

        Returns
        - The resulting URI

        Raises
        - NullPointerException: If `str` is `null`
        - IllegalArgumentException: If the given string violates RFC&nbsp;2396
        """
        ...


    def relativize(self, uri: "URI") -> "URI":
        """
        Relativizes the given URI against this URI.
        
         The relativization of the given URI against this URI is computed as
        follows: 
        
        <ol>
        
          -  If either this URI or the given URI are opaque, or if the
          scheme and authority components of the two URIs are not identical, or
          if the path of this URI is not a prefix of the path of the given URI,
          then the given URI is returned. 
        
          -  Otherwise a new relative hierarchical URI is constructed with
          query and fragment components taken from the given URI and with a path
          component computed by removing this URI's path from the beginning of
          the given URI's path. 
        
        </ol>

        Arguments
        - uri: The URI to be relativized against this URI

        Returns
        - The resulting URI

        Raises
        - NullPointerException: If `uri` is `null`
        """
        ...


    def toURL(self) -> "URL":
        """
        Constructs a URL from this URI.
        
         This convenience method works as if invoking it were equivalent to
        evaluating the expression `new URL(this.toString())` after
        first checking that this URI is absolute. 

        Returns
        - A URL constructed from this URI

        Raises
        - IllegalArgumentException: If this URL is not absolute
        - MalformedURLException: If a protocol handler for the URL could not be found,
                 or if some other error occurred while constructing the URL
        """
        ...


    def getScheme(self) -> str:
        """
        Returns the scheme component of this URI.
        
         The scheme component of a URI, if defined, only contains characters
        in the *alphanum* category and in the string `"-.+"`.  A
        scheme always starts with an *alpha* character. 
        
        The scheme component of a URI cannot contain escaped octets, hence this
        method does not perform any decoding.

        Returns
        - The scheme component of this URI,
                 or `null` if the scheme is undefined
        """
        ...


    def isAbsolute(self) -> bool:
        """
        Tells whether or not this URI is absolute.
        
         A URI is absolute if, and only if, it has a scheme component. 

        Returns
        - `True` if, and only if, this URI is absolute
        """
        ...


    def isOpaque(self) -> bool:
        """
        Tells whether or not this URI is opaque.
        
         A URI is opaque if, and only if, it is absolute and its
        scheme-specific part does not begin with a slash character ('/').
        An opaque URI has a scheme, a scheme-specific part, and possibly
        a fragment; all other components are undefined. 

        Returns
        - `True` if, and only if, this URI is opaque
        """
        ...


    def getRawSchemeSpecificPart(self) -> str:
        """
        Returns the raw scheme-specific part of this URI.  The scheme-specific
        part is never undefined, though it may be empty.
        
         The scheme-specific part of a URI only contains legal URI
        characters. 

        Returns
        - The raw scheme-specific part of this URI
                 (never `null`)
        """
        ...


    def getSchemeSpecificPart(self) -> str:
        """
        Returns the decoded scheme-specific part of this URI.
        
         The string returned by this method is equal to that returned by the
        .getRawSchemeSpecificPart() getRawSchemeSpecificPart method
        except that all sequences of escaped octets are <a
        href="#decode">decoded</a>.  

        Returns
        - The decoded scheme-specific part of this URI
                 (never `null`)
        """
        ...


    def getRawAuthority(self) -> str:
        """
        Returns the raw authority component of this URI.
        
         The authority component of a URI, if defined, only contains the
        commercial-at character (`'@'`) and characters in the
        *unreserved*, *punct*, *escaped*, and *other*
        categories.  If the authority is server-based then it is further
        constrained to have valid user-information, host, and port
        components. 

        Returns
        - The raw authority component of this URI,
                 or `null` if the authority is undefined
        """
        ...


    def getAuthority(self) -> str:
        """
        Returns the decoded authority component of this URI.
        
         The string returned by this method is equal to that returned by the
        .getRawAuthority() getRawAuthority method except that all
        sequences of escaped octets are <a href="#decode">decoded</a>.  

        Returns
        - The decoded authority component of this URI,
                 or `null` if the authority is undefined
        """
        ...


    def getRawUserInfo(self) -> str:
        """
        Returns the raw user-information component of this URI.
        
         The user-information component of a URI, if defined, only contains
        characters in the *unreserved*, *punct*, *escaped*, and
        *other* categories. 

        Returns
        - The raw user-information component of this URI,
                 or `null` if the user information is undefined
        """
        ...


    def getUserInfo(self) -> str:
        """
        Returns the decoded user-information component of this URI.
        
         The string returned by this method is equal to that returned by the
        .getRawUserInfo() getRawUserInfo method except that all
        sequences of escaped octets are <a href="#decode">decoded</a>.  

        Returns
        - The decoded user-information component of this URI,
                 or `null` if the user information is undefined
        """
        ...


    def getHost(self) -> str:
        """
        Returns the host component of this URI.
        
         The host component of a URI, if defined, will have one of the
        following forms: 
        
        
        
          -  A domain name consisting of one or more *labels*
          separated by period characters (`'.'`), optionally followed by
          a period character.  Each label consists of *alphanum* characters
          as well as hyphen characters (`'-'`), though hyphens never
          occur as the first or last characters in a label. The rightmost
          label of a domain name consisting of two or more labels, begins
          with an *alpha* character. 
        
          -  A dotted-quad IPv4 address of the form
          *digit*`+.`*digit*`+.`*digit*`+.`*digit*`+`,
          where no *digit* sequence is longer than three characters and no
          sequence has a value larger than 255. 
        
          -  An IPv6 address enclosed in square brackets (`'['` and
          `']'`) and consisting of hexadecimal digits, colon characters
          (`':'`), and possibly an embedded IPv4 address.  The full
          syntax of IPv6 addresses is specified in <a
          href="http://www.ietf.org/rfc/rfc2373.txt">*RFC&nbsp;2373: IPv6
          Addressing Architecture*</a>.  
        
        
        
        The host component of a URI cannot contain escaped octets, hence this
        method does not perform any decoding.

        Returns
        - The host component of this URI,
                 or `null` if the host is undefined
        """
        ...


    def getPort(self) -> int:
        """
        Returns the port number of this URI.
        
         The port component of a URI, if defined, is a non-negative
        integer. 

        Returns
        - The port component of this URI,
                 or `-1` if the port is undefined
        """
        ...


    def getRawPath(self) -> str:
        """
        Returns the raw path component of this URI.
        
         The path component of a URI, if defined, only contains the slash
        character (`'/'`), the commercial-at character (`'@'`),
        and characters in the *unreserved*, *punct*, *escaped*,
        and *other* categories. 

        Returns
        - The path component of this URI,
                 or `null` if the path is undefined
        """
        ...


    def getPath(self) -> str:
        """
        Returns the decoded path component of this URI.
        
         The string returned by this method is equal to that returned by the
        .getRawPath() getRawPath method except that all sequences of
        escaped octets are <a href="#decode">decoded</a>.  

        Returns
        - The decoded path component of this URI,
                 or `null` if the path is undefined
        """
        ...


    def getRawQuery(self) -> str:
        """
        Returns the raw query component of this URI.
        
         The query component of a URI, if defined, only contains legal URI
        characters. 

        Returns
        - The raw query component of this URI,
                 or `null` if the query is undefined
        """
        ...


    def getQuery(self) -> str:
        """
        Returns the decoded query component of this URI.
        
         The string returned by this method is equal to that returned by the
        .getRawQuery() getRawQuery method except that all sequences of
        escaped octets are <a href="#decode">decoded</a>.  

        Returns
        - The decoded query component of this URI,
                 or `null` if the query is undefined
        """
        ...


    def getRawFragment(self) -> str:
        """
        Returns the raw fragment component of this URI.
        
         The fragment component of a URI, if defined, only contains legal URI
        characters. 

        Returns
        - The raw fragment component of this URI,
                 or `null` if the fragment is undefined
        """
        ...


    def getFragment(self) -> str:
        """
        Returns the decoded fragment component of this URI.
        
         The string returned by this method is equal to that returned by the
        .getRawFragment() getRawFragment method except that all
        sequences of escaped octets are <a href="#decode">decoded</a>.  

        Returns
        - The decoded fragment component of this URI,
                 or `null` if the fragment is undefined
        """
        ...


    def equals(self, ob: "Object") -> bool:
        """
        Tests this URI for equality with another object.
        
         If the given object is not a URI then this method immediately
        returns `False`.
        
         For two URIs to be considered equal requires that either both are
        opaque or both are hierarchical.  Their schemes must either both be
        undefined or else be equal without regard to case. Their fragments
        must either both be undefined or else be equal.
        
         For two opaque URIs to be considered equal, their scheme-specific
        parts must be equal.
        
         For two hierarchical URIs to be considered equal, their paths must
        be equal and their queries must either both be undefined or else be
        equal.  Their authorities must either both be undefined, or both be
        registry-based, or both be server-based.  If their authorities are
        defined and are registry-based, then they must be equal.  If their
        authorities are defined and are server-based, then their hosts must be
        equal without regard to case, their port numbers must be equal, and
        their user-information components must be equal.
        
         When testing the user-information, path, query, fragment, authority,
        or scheme-specific parts of two URIs for equality, the raw forms rather
        than the encoded forms of these components are compared and the
        hexadecimal digits of escaped octets are compared without regard to
        case.
        
         This method satisfies the general contract of the java.lang.Object.equals(Object) Object.equals method. 

        Arguments
        - ob: The object to which this object is to be compared

        Returns
        - `True` if, and only if, the given object is a URI that
                 is identical to this URI
        """
        ...


    def hashCode(self) -> int:
        """
        Returns a hash-code value for this URI.  The hash code is based upon all
        of the URI's components, and satisfies the general contract of the
        java.lang.Object.hashCode() Object.hashCode method.

        Returns
        - A hash-code value for this URI
        """
        ...


    def compareTo(self, that: "URI") -> int:
        """
        Compares this URI to another object, which must be a URI.
        
         When comparing corresponding components of two URIs, if one
        component is undefined but the other is defined then the first is
        considered to be less than the second.  Unless otherwise noted, string
        components are ordered according to their natural, case-sensitive
        ordering as defined by the java.lang.String.compareTo(String)
        String.compareTo method.  String components that are subject to
        encoding are compared by comparing their raw forms rather than their
        encoded forms and the hexadecimal digits of escaped octets are compared
        without regard to case.
        
         The ordering of URIs is defined as follows: 
        
        
        
          -  Two URIs with different schemes are ordered according the
          ordering of their schemes, without regard to case. 
        
          -  A hierarchical URI is considered to be less than an opaque URI
          with an identical scheme. 
        
          -  Two opaque URIs with identical schemes are ordered according
          to the ordering of their scheme-specific parts. 
        
          -  Two opaque URIs with identical schemes and scheme-specific
          parts are ordered according to the ordering of their
          fragments. 
        
          -  Two hierarchical URIs with identical schemes are ordered
          according to the ordering of their authority components: 
        
          
        
            -  If both authority components are server-based then the URIs
            are ordered according to their user-information components; if these
            components are identical then the URIs are ordered according to the
            ordering of their hosts, without regard to case; if the hosts are
            identical then the URIs are ordered according to the ordering of
            their ports. 
        
            -  If one or both authority components are registry-based then
            the URIs are ordered according to the ordering of their authority
            components. 
        
          
        
          -  Finally, two hierarchical URIs with identical schemes and
          authority components are ordered according to the ordering of their
          paths; if their paths are identical then they are ordered according to
          the ordering of their queries; if the queries are identical then they
          are ordered according to the order of their fragments. 
        
        
        
         This method satisfies the general contract of the java.lang.Comparable.compareTo(Object) Comparable.compareTo
        method. 

        Arguments
        - that: The object to which this URI is to be compared

        Returns
        - A negative integer, zero, or a positive integer as this URI is
                 less than, equal to, or greater than the given URI

        Raises
        - ClassCastException: If the given object is not a URI
        """
        ...


    def toString(self) -> str:
        """
        Returns the content of this URI as a string.
        
         If this URI was created by invoking one of the constructors in this
        class then a string equivalent to the original input string, or to the
        string computed from the originally-given components, as appropriate, is
        returned.  Otherwise this URI was created by normalization, resolution,
        or relativization, and so a string is constructed from this URI's
        components according to the rules specified in <a
        href="http://www.ietf.org/rfc/rfc2396.txt">RFC&nbsp;2396</a>,
        section&nbsp;5.2, step&nbsp;7. 

        Returns
        - The string form of this URI
        """
        ...


    def toASCIIString(self) -> str:
        """
        Returns the content of this URI as a US-ASCII string.
        
         If this URI does not contain any characters in the *other*
        category then an invocation of this method will return the same value as
        an invocation of the .toString() toString method.  Otherwise
        this method works as if by invoking that method and then <a
        href="#encode">encoding</a> the result.  

        Returns
        - The string form of this URI, encoded as needed
                 so that it only contains characters in the US-ASCII
                 charset
        """
        ...
