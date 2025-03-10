"""
Python module generated from Java source file com.google.common.net.HttpHeaders

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
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
    CROSS_ORIGIN_RESOURCE_POLICY = "Cross-Origin-Resource-Policy"
    """
    The HTTP <a href="https://fetch.spec.whatwg.org/#cross-origin-resource-policy-header">`Cross-Origin-Resource-Policy`</a> header field name.

    Since
    - 28.0
    """
    EARLY_DATA = "Early-Data"
    """
    The HTTP <a href="https://tools.ietf.org/html/rfc8470">`Early-Data`</a> header field
    name.

    Since
    - 27.0
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
    HTTP2_SETTINGS = "HTTP2-Settings"
    """
    The HTTP <a href="https://tools.ietf.org/html/rfc7540#section-3.2.1">`HTTP2-Settings`
    </a> header field name.

    Since
    - 24.0
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
    ORIGIN_ISOLATION = "Origin-Isolation"
    """
    The HTTP <a href="https://github.com/WICG/origin-isolation">`Origin-Isolation`</a> header
    field name.

    Since
    - 30.1
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
    REFERRER_POLICY = "Referrer-Policy"
    """
    The HTTP <a href="https://www.w3.org/TR/referrer-policy/">`Referrer-Policy`</a> header
    field name.

    Since
    - 23.4
    """
    SERVICE_WORKER = "Service-Worker"
    """
    The HTTP <a href="https://www.w3.org/TR/service-workers/#update-algorithm">`Service-Worker`</a> header field name.

    Since
    - 20.0
    """
    TE = "TE"
    """
    The HTTP `TE` header field name.
    """
    UPGRADE = "Upgrade"
    """
    The HTTP `Upgrade` header field name.
    """
    UPGRADE_INSECURE_REQUESTS = "Upgrade-Insecure-Requests"
    """
    The HTTP <a href="https://w3c.github.io/webappsec-upgrade-insecure-requests/#preference">`Upgrade-Insecure-Requests`</a> header field name.

    Since
    - 28.1
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
    ACCESS_CONTROL_ALLOW_PRIVATE_NETWORK = "Access-Control-Allow-Private-Network"
    """
    The HTTP <a href="https://wicg.github.io/private-network-access/#headers">`Access-Control-Allow-Private-Network`</a> header field name.

    Since
    - 31.1
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
    The HTTP <a href="http://w3.org/TR/CSP/#content-security-policy-header-field">`Content-Security-Policy`</a> header field name.

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
    <a href="https://www.w3.org/TR/2011/WD-CSP-20111129/">CSP v.1</a> and used by the Firefox until
    version 23 and the Internet Explorer version 10. Please, use .CONTENT_SECURITY_POLICY
    to pass the CSP.

    Since
    - 20.0
    """
    X_CONTENT_SECURITY_POLICY_REPORT_ONLY = "X-Content-Security-Policy-Report-Only"
    """
    The HTTP nonstandard `X-Content-Security-Policy-Report-Only` header field name. It was
    introduced in <a href="https://www.w3.org/TR/2011/WD-CSP-20111129/">CSP v.1</a> and used by the
    Firefox until version 23 and the Internet Explorer version 10. Please, use .CONTENT_SECURITY_POLICY_REPORT_ONLY to pass the CSP.

    Since
    - 20.0
    """
    X_WEBKIT_CSP = "X-WebKit-CSP"
    """
    The HTTP nonstandard `X-WebKit-CSP` header field name. It was introduced in <a
    href="https://www.w3.org/TR/2011/WD-CSP-20111129/">CSP v.1</a> and used by the Chrome until
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
    CROSS_ORIGIN_EMBEDDER_POLICY = "Cross-Origin-Embedder-Policy"
    """
    The HTTP <a href="https://wicg.github.io/cross-origin-embedder-policy/#COEP">`Cross-Origin-Embedder-Policy`</a> header field name.

    Since
    - 30.0
    """
    CROSS_ORIGIN_EMBEDDER_POLICY_REPORT_ONLY = "Cross-Origin-Embedder-Policy-Report-Only"
    """
    The HTTP <a href="https://wicg.github.io/cross-origin-embedder-policy/#COEP-RO">`Cross-Origin-Embedder-Policy-Report-Only`</a> header field name.

    Since
    - 30.0
    """
    CROSS_ORIGIN_OPENER_POLICY = "Cross-Origin-Opener-Policy"
    """
    The HTTP Cross-Origin-Opener-Policy header field name.

    Since
    - 28.2
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
    KEEP_ALIVE = "Keep-Alive"
    """
    The HTTP `Keep-Alive` header field name.

    Since
    - 31.0
    """
    NO_VARY_SEARCH = "No-Vary-Search"
    """
    The HTTP <a href="https://github.com/WICG/nav-speculation/blob/main/no-vary-search.md">`No-Vary-Seearch`</a> header field name.

    Since
    - 32.0.0
    """
    ORIGIN_TRIAL = "Origin-Trial"
    """
    The HTTP <a href="https://googlechrome.github.io/OriginTrials/#header">`Origin-Trial`</a>
    header field name.

    Since
    - 27.1
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
    REPORT_TO = "Report-To"
    """
    The HTTP <a href="https://www.w3.org/TR/reporting/">`Report-To`</a> header field name.

    Since
    - 27.1
    """
    RETRY_AFTER = "Retry-After"
    """
    The HTTP `Retry-After` header field name.
    """
    SERVER = "Server"
    """
    The HTTP `Server` header field name.
    """
    SERVER_TIMING = "Server-Timing"
    """
    The HTTP <a href="https://www.w3.org/TR/server-timing/">`Server-Timing`</a> header field
    name.

    Since
    - 23.6
    """
    SERVICE_WORKER_ALLOWED = "Service-Worker-Allowed"
    """
    The HTTP <a href="https://www.w3.org/TR/service-workers/#update-algorithm">`Service-Worker-Allowed`</a> header field name.

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
    SOURCE_MAP = "SourceMap"
    """
    The HTTP <a href="http://goo.gl/Dxx19N">`SourceMap`</a> header field name.

    Since
    - 27.1
    """
    SUPPORTS_LOADING_MODE = "Supports-Loading-Mode"
    """
    The HTTP <a href="https://github.com/WICG/nav-speculation/blob/main/opt-in.md">`Supports-Loading-Mode`</a> header field name. This can be used to specify, for example, <a
    href="https://developer.chrome.com/docs/privacy-sandbox/fenced-frame/#server-opt-in">fenced
    frames</a>.

    Since
    - 32.0.0
    """
    STRICT_TRANSPORT_SECURITY = "Strict-Transport-Security"
    """
    The HTTP <a href="http://tools.ietf.org/html/rfc6797#section-6.1">`Strict-Transport-Security`</a> header field name.

    Since
    - 15.0
    """
    TIMING_ALLOW_ORIGIN = "Timing-Allow-Origin"
    """
    The HTTP <a href="http://www.w3.org/TR/resource-timing/#cross-origin-resources">`Timing-Allow-Origin`</a> header field name.

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
    X_DEVICE_IP = "X-Device-IP"
    """
    The HTTP <a
    href="https://iabtechlab.com/wp-content/uploads/2019/06/VAST_4.2_final_june26.pdf">`X-Device-IP`</a> header field name. Header used for VAST requests to provide the IP address of
    the device on whose behalf the request is being made.

    Since
    - 31.0
    """
    X_DEVICE_REFERER = "X-Device-Referer"
    """
    The HTTP <a
    href="https://iabtechlab.com/wp-content/uploads/2019/06/VAST_4.2_final_june26.pdf">`X-Device-Referer`</a> header field name. Header used for VAST requests to provide the .REFERER header value that the on-behalf-of client would have used when making a request
    itself.

    Since
    - 31.0
    """
    X_DEVICE_ACCEPT_LANGUAGE = "X-Device-Accept-Language"
    """
    The HTTP <a
    href="https://iabtechlab.com/wp-content/uploads/2019/06/VAST_4.2_final_june26.pdf">`X-Device-Accept-Language`</a> header field name. Header used for VAST requests to provide the
    .ACCEPT_LANGUAGE header value that the on-behalf-of client would have used when making
    a request itself.

    Since
    - 31.0
    """
    X_DEVICE_REQUESTED_WITH = "X-Device-Requested-With"
    """
    The HTTP <a
    href="https://iabtechlab.com/wp-content/uploads/2019/06/VAST_4.2_final_june26.pdf">`X-Device-Requested-With`</a> header field name. Header used for VAST requests to provide the
    .X_REQUESTED_WITH header value that the on-behalf-of client would have used when making
    a request itself.

    Since
    - 31.0
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
    The HTTP <a href="http://tools.ietf.org/html/draft-evans-palmer-key-pinning">`Public-Key-Pins`</a> header field name.

    Since
    - 15.0
    """
    PUBLIC_KEY_PINS_REPORT_ONLY = "Public-Key-Pins-Report-Only"
    """
    The HTTP <a href="http://tools.ietf.org/html/draft-evans-palmer-key-pinning">`Public-Key-Pins-Report-Only`</a> header field name.

    Since
    - 15.0
    """
    X_REQUEST_ID = "X-Request-ID"
    """
    The HTTP `X-Request-ID` header field name.

    Since
    - 30.1
    """
    X_REQUESTED_WITH = "X-Requested-With"
    """
    The HTTP `X-Requested-With` header field name.
    """
    X_USER_IP = "X-User-IP"
    """
    The HTTP `X-User-IP` header field name.
    """
    X_DOWNLOAD_OPTIONS = "X-Download-Options"
    """
    The HTTP <a href="https://goo.gl/VKpXxa">`X-Download-Options`</a> header field name.
    
    When the new X-Download-Options header is present with the value `noopen`, the user is
    prevented from opening a file download directly; instead, they must first save the file
    locally.

    Since
    - 24.1
    """
    X_XSS_PROTECTION = "X-XSS-Protection"
    """
    The HTTP `X-XSS-Protection` header field name.
    """
    X_DNS_PREFETCH_CONTROL = "X-DNS-Prefetch-Control"
    """
    The HTTP <a
    href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-DNS-Prefetch-Control">`X-DNS-Prefetch-Control`</a> header controls DNS prefetch behavior. Value can be "on" or "off".
    By default, DNS prefetching is "on" for HTTP pages and "off" for HTTPS pages.
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
    PURPOSE = "Purpose"
    """
    The HTTP <a
    href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Link_prefetching_FAQ#As_a_server_admin.2C_can_I_distinguish_prefetch_requests_from_normal_requests.3F">`Purpose`</a> header field name.

    Since
    - 28.0
    """
    X_PURPOSE = "X-Purpose"
    """
    The HTTP <a
    href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Link_prefetching_FAQ#As_a_server_admin.2C_can_I_distinguish_prefetch_requests_from_normal_requests.3F">`X-Purpose`</a> header field name.

    Since
    - 28.0
    """
    X_MOZ = "X-Moz"
    """
    The HTTP <a
    href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Link_prefetching_FAQ#As_a_server_admin.2C_can_I_distinguish_prefetch_requests_from_normal_requests.3F">`X-Moz`</a> header field name.

    Since
    - 28.0
    """
    DEVICE_MEMORY = "Device-Memory"
    """
    The HTTP <a
    href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Device-Memory">`Device-Memory`</a> header field name.

    Since
    - 31.0
    """
    DOWNLINK = "Downlink"
    """
    The HTTP <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Downlink">`Downlink`</a> header field name.

    Since
    - 31.0
    """
    ECT = "ECT"
    """
    The HTTP <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/ECT">`ECT`</a> header field name.

    Since
    - 31.0
    """
    RTT = "RTT"
    """
    The HTTP <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/RTT">`RTT`</a> header field name.

    Since
    - 31.0
    """
    SAVE_DATA = "Save-Data"
    """
    The HTTP <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Save-Data">`Save-Data`</a> header field name.

    Since
    - 31.0
    """
    VIEWPORT_WIDTH = "Viewport-Width"
    """
    The HTTP <a
    href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Viewport-Width">`Viewport-Width`</a> header field name.

    Since
    - 31.0
    """
    WIDTH = "Width"
    """
    The HTTP <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Width">`Width`</a> header field name.

    Since
    - 31.0
    """
    PERMISSIONS_POLICY = "Permissions-Policy"
    """
    The HTTP <a href="https://www.w3.org/TR/permissions-policy-1/">`Permissions-Policy`</a>
    header field name.

    Since
    - 31.0
    """
    SEC_CH_PREFERS_COLOR_SCHEME = "Sec-CH-Prefers-Color-Scheme"
    """
    The HTTP <a
    href="https://wicg.github.io/user-preference-media-features-headers/#sec-ch-prefers-color-scheme">`Sec-CH-Prefers-Color-Scheme`</a> header field name.
    
    This header is experimental.

    Since
    - 31.0
    """
    ACCEPT_CH = "Accept-CH"
    """
    The HTTP <a
    href="https://www.rfc-editor.org/rfc/rfc8942#name-the-accept-ch-response-head">`Accept-CH`</a> header field name.

    Since
    - 31.0
    """
    CRITICAL_CH = "Critical-CH"
    """
    The HTTP <a
    href="https://datatracker.ietf.org/doc/html/draft-davidben-http-client-hint-reliability-03.txt#section-3">`Critical-CH`</a> header field name.

    Since
    - 31.0
    """
    SEC_CH_UA = "Sec-CH-UA"
    """
    The HTTP <a href="https://wicg.github.io/ua-client-hints/#sec-ch-ua">`Sec-CH-UA`</a>
    header field name.

    Since
    - 30.0
    """
    SEC_CH_UA_ARCH = "Sec-CH-UA-Arch"
    """
    The HTTP <a href="https://wicg.github.io/ua-client-hints/#sec-ch-ua-arch">`Sec-CH-UA-Arch`</a> header field name.

    Since
    - 30.0
    """
    SEC_CH_UA_MODEL = "Sec-CH-UA-Model"
    """
    The HTTP <a href="https://wicg.github.io/ua-client-hints/#sec-ch-ua-model">`Sec-CH-UA-Model`</a> header field name.

    Since
    - 30.0
    """
    SEC_CH_UA_PLATFORM = "Sec-CH-UA-Platform"
    """
    The HTTP <a href="https://wicg.github.io/ua-client-hints/#sec-ch-ua-platform">`Sec-CH-UA-Platform`</a> header field name.

    Since
    - 30.0
    """
    SEC_CH_UA_PLATFORM_VERSION = "Sec-CH-UA-Platform-Version"
    """
    The HTTP <a href="https://wicg.github.io/ua-client-hints/#sec-ch-ua-platform-version">`Sec-CH-UA-Platform-Version`</a> header field name.

    Since
    - 30.0
    """
    SEC_CH_UA_FULL_VERSION = "Sec-CH-UA-Full-Version"
    """
    The HTTP <a href="https://wicg.github.io/ua-client-hints/#sec-ch-ua-full-version">`Sec-CH-UA-Full-Version`</a> header field name.

    Since
    - 30.0

    Deprecated
    - Prefer SEC_CH_UA_FULL_VERSION_LIST.
    """
    SEC_CH_UA_FULL_VERSION_LIST = "Sec-CH-UA-Full-Version-List"
    """
    The HTTP <a href="https://wicg.github.io/ua-client-hints/#sec-ch-ua-full-version-list">`Sec-CH-UA-Full-Version`</a> header field name.

    Since
    - 31.1
    """
    SEC_CH_UA_MOBILE = "Sec-CH-UA-Mobile"
    """
    The HTTP <a href="https://wicg.github.io/ua-client-hints/#sec-ch-ua-mobile">`Sec-CH-UA-Mobile`</a> header field name.

    Since
    - 30.0
    """
    SEC_CH_UA_WOW64 = "Sec-CH-UA-WoW64"
    """
    The HTTP <a href="https://wicg.github.io/ua-client-hints/#sec-ch-ua-wow64">`Sec-CH-UA-WoW64`</a> header field name.

    Since
    - 32.0.0
    """
    SEC_CH_UA_BITNESS = "Sec-CH-UA-Bitness"
    """
    The HTTP <a href="https://wicg.github.io/ua-client-hints/#sec-ch-ua-bitness">`Sec-CH-UA-Bitness`</a> header field name.

    Since
    - 31.0
    """
    SEC_CH_UA_FORM_FACTOR = "Sec-CH-UA-Form-Factor"
    """
    The HTTP <a href="https://wicg.github.io/ua-client-hints/#sec-ch-ua-form-factor">`Sec-CH-UA-Form-Factor`</a> header field name.

    Since
    - 32.0.0
    """
    SEC_CH_VIEWPORT_WIDTH = "Sec-CH-Viewport-Width"
    """
    The HTTP <a
    href="https://wicg.github.io/responsive-image-client-hints/#sec-ch-viewport-width">`Sec-CH-Viewport-Width`</a> header field name.

    Since
    - 32.0.0
    """
    SEC_CH_VIEWPORT_HEIGHT = "Sec-CH-Viewport-Height"
    """
    The HTTP <a
    href="https://wicg.github.io/responsive-image-client-hints/#sec-ch-viewport-height">`Sec-CH-Viewport-Height`</a> header field name.

    Since
    - 32.0.0
    """
    SEC_CH_DPR = "Sec-CH-DPR"
    """
    The HTTP <a href="https://wicg.github.io/responsive-image-client-hints/#sec-ch-dpr">`Sec-CH-DPR`</a> header field name.

    Since
    - 32.0.0
    """
    SEC_FETCH_DEST = "Sec-Fetch-Dest"
    """
    The HTTP <a href="https://w3c.github.io/webappsec-fetch-metadata/">`Sec-Fetch-Dest`</a>
    header field name.

    Since
    - 27.1
    """
    SEC_FETCH_MODE = "Sec-Fetch-Mode"
    """
    The HTTP <a href="https://w3c.github.io/webappsec-fetch-metadata/">`Sec-Fetch-Mode`</a>
    header field name.

    Since
    - 27.1
    """
    SEC_FETCH_SITE = "Sec-Fetch-Site"
    """
    The HTTP <a href="https://w3c.github.io/webappsec-fetch-metadata/">`Sec-Fetch-Site`</a>
    header field name.

    Since
    - 27.1
    """
    SEC_FETCH_USER = "Sec-Fetch-User"
    """
    The HTTP <a href="https://w3c.github.io/webappsec-fetch-metadata/">`Sec-Fetch-User`</a>
    header field name.

    Since
    - 27.1
    """
    SEC_METADATA = "Sec-Metadata"
    """
    The HTTP <a href="https://w3c.github.io/webappsec-fetch-metadata/">`Sec-Metadata`</a>
    header field name.

    Since
    - 26.0
    """
    SEC_TOKEN_BINDING = "Sec-Token-Binding"
    """
    The HTTP <a href="https://tools.ietf.org/html/draft-ietf-tokbind-https">`Sec-Token-Binding`</a> header field name.

    Since
    - 25.1
    """
    SEC_PROVIDED_TOKEN_BINDING_ID = "Sec-Provided-Token-Binding-ID"
    """
    The HTTP <a href="https://tools.ietf.org/html/draft-ietf-tokbind-ttrp">`Sec-Provided-Token-Binding-ID`</a> header field name.

    Since
    - 25.1
    """
    SEC_REFERRED_TOKEN_BINDING_ID = "Sec-Referred-Token-Binding-ID"
    """
    The HTTP <a href="https://tools.ietf.org/html/draft-ietf-tokbind-ttrp">`Sec-Referred-Token-Binding-ID`</a> header field name.

    Since
    - 25.1
    """
    SEC_WEBSOCKET_ACCEPT = "Sec-WebSocket-Accept"
    """
    The HTTP <a href="https://tools.ietf.org/html/rfc6455">`Sec-WebSocket-Accept`</a> header
    field name.

    Since
    - 28.0
    """
    SEC_WEBSOCKET_EXTENSIONS = "Sec-WebSocket-Extensions"
    """
    The HTTP <a href="https://tools.ietf.org/html/rfc6455">`Sec-WebSocket-Extensions`</a>
    header field name.

    Since
    - 28.0
    """
    SEC_WEBSOCKET_KEY = "Sec-WebSocket-Key"
    """
    The HTTP <a href="https://tools.ietf.org/html/rfc6455">`Sec-WebSocket-Key`</a> header
    field name.

    Since
    - 28.0
    """
    SEC_WEBSOCKET_PROTOCOL = "Sec-WebSocket-Protocol"
    """
    The HTTP <a href="https://tools.ietf.org/html/rfc6455">`Sec-WebSocket-Protocol`</a>
    header field name.

    Since
    - 28.0
    """
    SEC_WEBSOCKET_VERSION = "Sec-WebSocket-Version"
    """
    The HTTP <a href="https://tools.ietf.org/html/rfc6455">`Sec-WebSocket-Version`</a> header
    field name.

    Since
    - 28.0
    """
    SEC_BROWSING_TOPICS = "Sec-Browsing-Topics"
    """
    The HTTP <a href="https://patcg-individual-drafts.github.io/topics/">`Sec-Browsing-Topics`</a> header field name.

    Since
    - 32.0.0
    """
    OBSERVE_BROWSING_TOPICS = "Observe-Browsing-Topics"
    """
    The HTTP <a href="https://patcg-individual-drafts.github.io/topics/">`Observe-Browsing-Topics`</a> header field name.

    Since
    - 32.0.0
    """
    CDN_LOOP = "CDN-Loop"
    """
    The HTTP <a href="https://tools.ietf.org/html/rfc8586">`CDN-Loop`</a> header field name.

    Since
    - 28.0
    """


    class ReferrerPolicyValues:
        """
        Values for the <a href="https://www.w3.org/TR/referrer-policy/">`Referrer-Policy`</a>
        header.

        Since
        - 23.4
        """

        NO_REFERRER = "no-referrer"
        NO_REFFERER_WHEN_DOWNGRADE = "no-referrer-when-downgrade"
        SAME_ORIGIN = "same-origin"
        ORIGIN = "origin"
        STRICT_ORIGIN = "strict-origin"
        ORIGIN_WHEN_CROSS_ORIGIN = "origin-when-cross-origin"
        STRICT_ORIGIN_WHEN_CROSS_ORIGIN = "strict-origin-when-cross-origin"
        UNSAFE_URL = "unsafe-url"
