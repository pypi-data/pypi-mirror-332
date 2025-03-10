"""
Python module generated from Java source file com.google.common.net.HttpHeaders

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtCompatible
from com.google.common.net import *
from typing import Any, Callable, Iterable, Tuple


class HttpHeaders:
    """
    Contains constant definitions for the HTTP header field names. See:
    
    - <a href="http://www.ietf.org/rfc/rfc2109.txt">RFC 2109</a>
    - <a href="http://www.ietf.org/rfc/rfc2183.txt">RFC 2183</a>
    - <a href="http://www.ietf.org/rfc/rfc2616.txt">RFC 2616</a>
    - <a href="http://www.ietf.org/rfc/rfc2965.txt">RFC 2965</a>
    - <a href="http://www.ietf.org/rfc/rfc5988.txt">RFC 5988</a>

    Author(s)
    - Kurt Alfred Kluever

    Since
    - 11.0
    """

    CACHE_CONTROL = "Cache-Control"
    """
    The HTTP `Cache-Control` header field name.
    """
    CONTENT_LENGTH = "Content-Length"
    """
    The HTTP `Content-Length` header field name.
    """
    CONTENT_TYPE = "Content-Type"
    """
    The HTTP `Content-Type` header field name.
    """
    DATE = "Date"
    """
    The HTTP `Date` header field name.
    """
    PRAGMA = "Pragma"
    """
    The HTTP `Pragma` header field name.
    """
    VIA = "Via"
    """
    The HTTP `Via` header field name.
    """
    WARNING = "Warning"
    """
    The HTTP `Warning` header field name.
    """
    ACCEPT = "Accept"
    """
    The HTTP `Accept` header field name.
    """
    ACCEPT_CHARSET = "Accept-Charset"
    """
    The HTTP `Accept-Charset` header field name.
    """
    ACCEPT_ENCODING = "Accept-Encoding"
    """
    The HTTP `Accept-Encoding` header field name.
    """
    ACCEPT_LANGUAGE = "Accept-Language"
    """
    The HTTP `Accept-Language` header field name.
    """
    ACCESS_CONTROL_REQUEST_HEADERS = "Access-Control-Request-Headers"
    """
    The HTTP `Access-Control-Request-Headers` header field name.
    """
    ACCESS_CONTROL_REQUEST_METHOD = "Access-Control-Request-Method"
    """
    The HTTP `Access-Control-Request-Method` header field name.
    """
    AUTHORIZATION = "Authorization"
    """
    The HTTP `Authorization` header field name.
    """
    CONNECTION = "Connection"
    """
    The HTTP `Connection` header field name.
    """
    COOKIE = "Cookie"
    """
    The HTTP `Cookie` header field name.
    """
    EXPECT = "Expect"
    """
    The HTTP `Expect` header field name.
    """
    FROM = "From"
    """
    The HTTP `From` header field name.
    """
    FORWARDED = "Forwarded"
    """
    The HTTP <a href="https://tools.ietf.org/html/rfc7239">`Forwarded`</a> header field name.

    Since
    - 20.0
    """
    FOLLOW_ONLY_WHEN_PRERENDER_SHOWN = "Follow-Only-When-Prerender-Shown"
    """
    The HTTP `Follow-Only-When-Prerender-Shown` header field name.

    Since
    - 17.0
    """
    HOST = "Host"
    """
    The HTTP `Host` header field name.
    """
    IF_MATCH = "If-Match"
    """
    The HTTP `If-Match` header field name.
    """
    IF_MODIFIED_SINCE = "If-Modified-Since"
    """
    The HTTP `If-Modified-Since` header field name.
    """
    IF_NONE_MATCH = "If-None-Match"
    """
    The HTTP `If-None-Match` header field name.
    """
    IF_RANGE = "If-Range"
    """
    The HTTP `If-Range` header field name.
    """
    IF_UNMODIFIED_SINCE = "If-Unmodified-Since"
    """
    The HTTP `If-Unmodified-Since` header field name.
    """
    LAST_EVENT_ID = "Last-Event-ID"
    """
    The HTTP `Last-Event-ID` header field name.
    """
    MAX_FORWARDS = "Max-Forwards"
    """
    The HTTP `Max-Forwards` header field name.
    """
    ORIGIN = "Origin"
    """
    The HTTP `Origin` header field name.
    """
    PROXY_AUTHORIZATION = "Proxy-Authorization"
    """
    The HTTP `Proxy-Authorization` header field name.
    """
    RANGE = "Range"
    """
    The HTTP `Range` header field name.
    """
    REFERER = "Referer"
    """
    The HTTP `Referer` header field name.
    """
    SERVICE_WORKER = "Service-Worker"
    """
    The HTTP <a href="https://www.w3.org/TR/service-workers/#update-algorithm">
    `Service-Worker`</a> header field name.
    """
    TE = "TE"
    """
    The HTTP `TE` header field name.
    """
    UPGRADE = "Upgrade"
    """
    The HTTP `Upgrade` header field name.
    """
    USER_AGENT = "User-Agent"
    """
    The HTTP `User-Agent` header field name.
    """
    ACCEPT_RANGES = "Accept-Ranges"
    """
    The HTTP `Accept-Ranges` header field name.
    """
    ACCESS_CONTROL_ALLOW_HEADERS = "Access-Control-Allow-Headers"
    """
    The HTTP `Access-Control-Allow-Headers` header field name.
    """
    ACCESS_CONTROL_ALLOW_METHODS = "Access-Control-Allow-Methods"
    """
    The HTTP `Access-Control-Allow-Methods` header field name.
    """
    ACCESS_CONTROL_ALLOW_ORIGIN = "Access-Control-Allow-Origin"
    """
    The HTTP `Access-Control-Allow-Origin` header field name.
    """
    ACCESS_CONTROL_ALLOW_CREDENTIALS = "Access-Control-Allow-Credentials"
    """
    The HTTP `Access-Control-Allow-Credentials` header field name.
    """
    ACCESS_CONTROL_EXPOSE_HEADERS = "Access-Control-Expose-Headers"
    """
    The HTTP `Access-Control-Expose-Headers` header field name.
    """
    ACCESS_CONTROL_MAX_AGE = "Access-Control-Max-Age"
    """
    The HTTP `Access-Control-Max-Age` header field name.
    """
    AGE = "Age"
    """
    The HTTP `Age` header field name.
    """
    ALLOW = "Allow"
    """
    The HTTP `Allow` header field name.
    """
    CONTENT_DISPOSITION = "Content-Disposition"
    """
    The HTTP `Content-Disposition` header field name.
    """
    CONTENT_ENCODING = "Content-Encoding"
    """
    The HTTP `Content-Encoding` header field name.
    """
    CONTENT_LANGUAGE = "Content-Language"
    """
    The HTTP `Content-Language` header field name.
    """
    CONTENT_LOCATION = "Content-Location"
    """
    The HTTP `Content-Location` header field name.
    """
    CONTENT_MD5 = "Content-MD5"
    """
    The HTTP `Content-MD5` header field name.
    """
    CONTENT_RANGE = "Content-Range"
    """
    The HTTP `Content-Range` header field name.
    """
    CONTENT_SECURITY_POLICY = "Content-Security-Policy"
    """
    The HTTP <a href="http://w3.org/TR/CSP/#content-security-policy-header-field">
    `Content-Security-Policy`</a> header field name.

    Since
    - 15.0
    """
    CONTENT_SECURITY_POLICY_REPORT_ONLY = "Content-Security-Policy-Report-Only"
    """
    The HTTP <a href="http://w3.org/TR/CSP/#content-security-policy-report-only-header-field">
    `Content-Security-Policy-Report-Only`</a> header field name.

    Since
    - 15.0
    """
    X_CONTENT_SECURITY_POLICY = "X-Content-Security-Policy"
    """
    The HTTP nonstandard `X-Content-Security-Policy` header field name. It was introduced in
    <a href="https://www.w3.org/TR/2011/WD-CSP-20111129/">CSP v.1</a> and used by the Firefox
    until version 23 and the Internet Explorer version 10.
    Please, use .CONTENT_SECURITY_POLICY to pass the CSP.

    Since
    - 20.0
    """
    X_CONTENT_SECURITY_POLICY_REPORT_ONLY = "X-Content-Security-Policy-Report-Only"
    """
    The HTTP nonstandard `X-Content-Security-Policy-Report-Only` header field name.
    It was introduced in <a href="https://www.w3.org/TR/2011/WD-CSP-20111129/">CSP v.1</a> and
    used by the Firefox until version 23 and the Internet Explorer version 10.
    Please, use .CONTENT_SECURITY_POLICY_REPORT_ONLY to pass the CSP.

    Since
    - 20.0
    """
    X_WEBKIT_CSP = "X-WebKit-CSP"
    """
    The HTTP nonstandard `X-WebKit-CSP` header field name. It was introduced in
    <a href="https://www.w3.org/TR/2011/WD-CSP-20111129/">CSP v.1</a> and used by the Chrome until
    version 25. Please, use .CONTENT_SECURITY_POLICY to pass the CSP.

    Since
    - 20.0
    """
    X_WEBKIT_CSP_REPORT_ONLY = "X-WebKit-CSP-Report-Only"
    """
    The HTTP nonstandard `X-WebKit-CSP-Report-Only` header field name. It was introduced in
    <a href="https://www.w3.org/TR/2011/WD-CSP-20111129/">CSP v.1</a> and used by the Chrome until
    version 25. Please, use .CONTENT_SECURITY_POLICY_REPORT_ONLY to pass the CSP.

    Since
    - 20.0
    """
    ETAG = "ETag"
    """
    The HTTP `ETag` header field name.
    """
    EXPIRES = "Expires"
    """
    The HTTP `Expires` header field name.
    """
    LAST_MODIFIED = "Last-Modified"
    """
    The HTTP `Last-Modified` header field name.
    """
    LINK = "Link"
    """
    The HTTP `Link` header field name.
    """
    LOCATION = "Location"
    """
    The HTTP `Location` header field name.
    """
    P3P = "P3P"
    """
    The HTTP `P3P` header field name. Limited browser support.
    """
    PROXY_AUTHENTICATE = "Proxy-Authenticate"
    """
    The HTTP `Proxy-Authenticate` header field name.
    """
    REFRESH = "Refresh"
    """
    The HTTP `Refresh` header field name. Non-standard header supported by most browsers.
    """
    RETRY_AFTER = "Retry-After"
    """
    The HTTP `Retry-After` header field name.
    """
    SERVER = "Server"
    """
    The HTTP `Server` header field name.
    """
    SERVICE_WORKER_ALLOWED = "Service-Worker-Allowed"
    """
    The HTTP <a href="https://www.w3.org/TR/service-workers/#update-algorithm">
    `Service-Worker-Allowed`</a> header field name.

    Since
    - 20.0
    """
    SET_COOKIE = "Set-Cookie"
    """
    The HTTP `Set-Cookie` header field name.
    """
    SET_COOKIE2 = "Set-Cookie2"
    """
    The HTTP `Set-Cookie2` header field name.
    """
    STRICT_TRANSPORT_SECURITY = "Strict-Transport-Security"
    """
    The HTTP
    <a href="http://tools.ietf.org/html/rfc6797#section-6.1">`Strict-Transport-Security`</a>
    header field name.

    Since
    - 15.0
    """
    TIMING_ALLOW_ORIGIN = "Timing-Allow-Origin"
    """
    The HTTP <a href="http://www.w3.org/TR/resource-timing/#cross-origin-resources">
    `Timing-Allow-Origin`</a> header field name.

    Since
    - 15.0
    """
    TRAILER = "Trailer"
    """
    The HTTP `Trailer` header field name.
    """
    TRANSFER_ENCODING = "Transfer-Encoding"
    """
    The HTTP `Transfer-Encoding` header field name.
    """
    VARY = "Vary"
    """
    The HTTP `Vary` header field name.
    """
    WWW_AUTHENTICATE = "WWW-Authenticate"
    """
    The HTTP `WWW-Authenticate` header field name.
    """
    DNT = "DNT"
    """
    The HTTP `DNT` header field name.
    """
    X_CONTENT_TYPE_OPTIONS = "X-Content-Type-Options"
    """
    The HTTP `X-Content-Type-Options` header field name.
    """
    X_DO_NOT_TRACK = "X-Do-Not-Track"
    """
    The HTTP `X-Do-Not-Track` header field name.
    """
    X_FORWARDED_FOR = "X-Forwarded-For"
    """
    The HTTP `X-Forwarded-For` header field name (superseded by `Forwarded`).
    """
    X_FORWARDED_PROTO = "X-Forwarded-Proto"
    """
    The HTTP `X-Forwarded-Proto` header field name.
    """
    X_FORWARDED_HOST = "X-Forwarded-Host"
    """
    The HTTP <a href="http://goo.gl/lQirAH">`X-Forwarded-Host`</a> header field name.

    Since
    - 20.0
    """
    X_FORWARDED_PORT = "X-Forwarded-Port"
    """
    The HTTP <a href="http://goo.gl/YtV2at">`X-Forwarded-Port`</a> header field name.

    Since
    - 20.0
    """
    X_FRAME_OPTIONS = "X-Frame-Options"
    """
    The HTTP `X-Frame-Options` header field name.
    """
    X_POWERED_BY = "X-Powered-By"
    """
    The HTTP `X-Powered-By` header field name.
    """
    PUBLIC_KEY_PINS = "Public-Key-Pins"
    """
    The HTTP
    <a href="http://tools.ietf.org/html/draft-evans-palmer-key-pinning">`Public-Key-Pins`</a>
    header field name.

    Since
    - 15.0
    """
    PUBLIC_KEY_PINS_REPORT_ONLY = "Public-Key-Pins-Report-Only"
    """
    The HTTP <a href="http://tools.ietf.org/html/draft-evans-palmer-key-pinning">
    `Public-Key-Pins-Report-Only`</a> header field name.

    Since
    - 15.0
    """
    X_REQUESTED_WITH = "X-Requested-With"
    """
    The HTTP `X-Requested-With` header field name.
    """
    X_USER_IP = "X-User-IP"
    """
    The HTTP `X-User-IP` header field name.
    """
    X_XSS_PROTECTION = "X-XSS-Protection"
    """
    The HTTP `X-XSS-Protection` header field name.
    """
    PING_FROM = "Ping-From"
    """
    The HTTP <a href="http://html.spec.whatwg.org/multipage/semantics.html#hyperlink-auditing">
    `Ping-From`</a> header field name.

    Since
    - 19.0
    """
    PING_TO = "Ping-To"
    """
    The HTTP <a href="http://html.spec.whatwg.org/multipage/semantics.html#hyperlink-auditing">
    `Ping-To`</a> header field name.

    Since
    - 19.0
    """
