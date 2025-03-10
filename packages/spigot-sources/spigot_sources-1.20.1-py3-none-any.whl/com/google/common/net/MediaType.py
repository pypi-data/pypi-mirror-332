"""
Python module generated from Java source file com.google.common.net.MediaType

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.base import Ascii
from com.google.common.base import CharMatcher
from com.google.common.base import Joiner
from com.google.common.base.Joiner import MapJoiner
from com.google.common.base import MoreObjects
from com.google.common.base import Objects
from com.google.common.base import Optional
from com.google.common.collect import ImmutableListMultimap
from com.google.common.collect import ImmutableMultiset
from com.google.common.collect import ImmutableSet
from com.google.common.collect import Maps
from com.google.common.collect import Multimap
from com.google.common.collect import Multimaps
from com.google.common.net import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from com.google.errorprone.annotations import Immutable
from com.google.errorprone.annotations.concurrent import LazyInit
from java.nio.charset import Charset
from java.nio.charset import IllegalCharsetNameException
from java.nio.charset import UnsupportedCharsetException
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class MediaType:
    """
    Represents an <a href="http://en.wikipedia.org/wiki/Internet_media_type">Internet Media Type</a>
    (also known as a MIME Type or Content Type). This class also supports the concept of media ranges
    <a href="http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.1">defined by HTTP/1.1</a>.
    As such, the `*` character is treated as a wildcard and is used to represent any acceptable
    type or subtype value. A media type may not have wildcard type with a declared subtype. The
    `*` character has no special meaning as part of a parameter. All values for type, subtype,
    parameter attributes or parameter values must be valid according to RFCs <a
    href="https://tools.ietf.org/html/rfc2045">2045</a> and <a
    href="https://tools.ietf.org/html/rfc2046">2046</a>.
    
    All portions of the media type that are case-insensitive (type, subtype, parameter attributes)
    are normalized to lowercase. The value of the `charset` parameter is normalized to
    lowercase, but all others are left as-is.
    
    Note that this specifically does <strong>not</strong> represent the value of the MIME `Content-Type` header and as such has no support for header-specific considerations such as line
    folding and comments.
    
    For media types that take a charset the predefined constants default to UTF-8 and have a
    "_UTF_8" suffix. To get a version without a character set, use .withoutParameters.

    Author(s)
    - Gregory Kick

    Since
    - 12.0
    """

    ANY_TYPE = createConstant(WILDCARD, WILDCARD)
    ANY_TEXT_TYPE = createConstant(TEXT_TYPE, WILDCARD)
    ANY_IMAGE_TYPE = createConstant(IMAGE_TYPE, WILDCARD)
    ANY_AUDIO_TYPE = createConstant(AUDIO_TYPE, WILDCARD)
    ANY_VIDEO_TYPE = createConstant(VIDEO_TYPE, WILDCARD)
    ANY_APPLICATION_TYPE = createConstant(APPLICATION_TYPE, WILDCARD)
    ANY_FONT_TYPE = createConstant(FONT_TYPE, WILDCARD)
    """
    Wildcard matching any "font" top-level media type.

    Since
    - 30.0
    """
    CACHE_MANIFEST_UTF_8 = createConstantUtf8(TEXT_TYPE, "cache-manifest")
    CSS_UTF_8 = createConstantUtf8(TEXT_TYPE, "css")
    CSV_UTF_8 = createConstantUtf8(TEXT_TYPE, "csv")
    HTML_UTF_8 = createConstantUtf8(TEXT_TYPE, "html")
    I_CALENDAR_UTF_8 = createConstantUtf8(TEXT_TYPE, "calendar")
    PLAIN_TEXT_UTF_8 = createConstantUtf8(TEXT_TYPE, "plain")
    TEXT_JAVASCRIPT_UTF_8 = createConstantUtf8(TEXT_TYPE, "javascript")
    """
    <a href="http://www.rfc-editor.org/rfc/rfc4329.txt">RFC 4329</a> declares .JAVASCRIPT_UTF_8 application/javascript to be the correct media type for JavaScript, but this
    may be necessary in certain situations for compatibility.
    """
    TSV_UTF_8 = createConstantUtf8(TEXT_TYPE, "tab-separated-values")
    """
    <a href="http://www.iana.org/assignments/media-types/text/tab-separated-values">Tab separated
    values</a>.

    Since
    - 15.0
    """
    VCARD_UTF_8 = createConstantUtf8(TEXT_TYPE, "vcard")
    WML_UTF_8 = createConstantUtf8(TEXT_TYPE, "vnd.wap.wml")
    """
    UTF-8 encoded <a href="https://en.wikipedia.org/wiki/Wireless_Markup_Language">Wireless Markup
    Language</a>.

    Since
    - 13.0
    """
    XML_UTF_8 = createConstantUtf8(TEXT_TYPE, "xml")
    """
    As described in <a href="http://www.ietf.org/rfc/rfc3023.txt">RFC 3023</a>, this constant
    (`text/xml`) is used for XML documents that are "readable by casual users." .APPLICATION_XML_UTF_8 is provided for documents that are intended for applications.
    """
    VTT_UTF_8 = createConstantUtf8(TEXT_TYPE, "vtt")
    """
    As described in <a href="https://w3c.github.io/webvtt/#iana-text-vtt">the VTT spec</a>, this is
    used for Web Video Text Tracks (WebVTT) files, used with the HTML5 track element.

    Since
    - 20.0
    """
    BMP = createConstant(IMAGE_TYPE, "bmp")
    """
    <a href="https://en.wikipedia.org/wiki/BMP_file_format">Bitmap file format</a> (`bmp`
    files).

    Since
    - 13.0
    """
    CRW = createConstant(IMAGE_TYPE, "x-canon-crw")
    """
    The <a href="https://en.wikipedia.org/wiki/Camera_Image_File_Format">Canon Image File
    Format</a> (`crw` files), a widely-used "raw image" format for cameras. It is found in
    `/etc/mime.types`, e.g. in <a href=
    "http://anonscm.debian.org/gitweb/?p=collab-maint/mime-support.git;a=blob;f=mime.types;hb=HEAD"
    >Debian 3.48-1</a>.

    Since
    - 15.0
    """
    GIF = createConstant(IMAGE_TYPE, "gif")
    ICO = createConstant(IMAGE_TYPE, "vnd.microsoft.icon")
    JPEG = createConstant(IMAGE_TYPE, "jpeg")
    PNG = createConstant(IMAGE_TYPE, "png")
    PSD = createConstant(IMAGE_TYPE, "vnd.adobe.photoshop")
    """
    The Photoshop File Format (`psd` files) as defined by <a
    href="http://www.iana.org/assignments/media-types/image/vnd.adobe.photoshop">IANA</a>, and
    found in `/etc/mime.types`, e.g. <a
    href="http://svn.apache.org/repos/asf/httpd/httpd/branches/1.3.x/conf/mime.types"></a> of the
    Apache <a href="http://httpd.apache.org/">HTTPD project</a>; for the specification, see <a
    href="http://www.adobe.com/devnet-apps/photoshop/fileformatashtml/PhotoshopFileFormats.htm">
    Adobe Photoshop Document Format</a> and <a
    href="http://en.wikipedia.org/wiki/Adobe_Photoshop#File_format">Wikipedia</a>; this is the
    regular output/input of Photoshop (which can also export to various image formats; note that
    files with extension "PSB" are in a distinct but related format).
    
    This is a more recent replacement for the older, experimental type `x-photoshop`: <a
    href="http://tools.ietf.org/html/rfc2046#section-6">RFC-2046.6</a>.

    Since
    - 15.0
    """
    SVG_UTF_8 = createConstantUtf8(IMAGE_TYPE, "svg+xml")
    TIFF = createConstant(IMAGE_TYPE, "tiff")
    WEBP = createConstant(IMAGE_TYPE, "webp")
    """
    <a href="https://en.wikipedia.org/wiki/WebP">WebP image format</a>.

    Since
    - 13.0
    """
    HEIF = createConstant(IMAGE_TYPE, "heif")
    """
    <a href="https://www.iana.org/assignments/media-types/image/heif">HEIF image format</a>.

    Since
    - 28.1
    """
    JP2K = createConstant(IMAGE_TYPE, "jp2")
    """
    <a href="https://tools.ietf.org/html/rfc3745">JP2K image format</a>.

    Since
    - 28.1
    """
    MP4_AUDIO = createConstant(AUDIO_TYPE, "mp4")
    MPEG_AUDIO = createConstant(AUDIO_TYPE, "mpeg")
    OGG_AUDIO = createConstant(AUDIO_TYPE, "ogg")
    WEBM_AUDIO = createConstant(AUDIO_TYPE, "webm")
    L16_AUDIO = createConstant(AUDIO_TYPE, "l16")
    """
    L16 audio, as defined by <a href="https://tools.ietf.org/html/rfc2586">RFC 2586</a>.

    Since
    - 24.1
    """
    L24_AUDIO = createConstant(AUDIO_TYPE, "l24")
    """
    L24 audio, as defined by <a href="https://tools.ietf.org/html/rfc3190">RFC 3190</a>.

    Since
    - 20.0
    """
    BASIC_AUDIO = createConstant(AUDIO_TYPE, "basic")
    """
    Basic Audio, as defined by <a href="http://tools.ietf.org/html/rfc2046#section-4.3">RFC
    2046</a>.

    Since
    - 20.0
    """
    AAC_AUDIO = createConstant(AUDIO_TYPE, "aac")
    """
    Advanced Audio Coding. For more information, see <a
    href="https://en.wikipedia.org/wiki/Advanced_Audio_Coding">Advanced Audio Coding</a>.

    Since
    - 20.0
    """
    VORBIS_AUDIO = createConstant(AUDIO_TYPE, "vorbis")
    """
    Vorbis Audio, as defined by <a href="http://tools.ietf.org/html/rfc5215">RFC 5215</a>.

    Since
    - 20.0
    """
    WMA_AUDIO = createConstant(AUDIO_TYPE, "x-ms-wma")
    """
    Windows Media Audio. For more information, see <a
    href="https://msdn.microsoft.com/en-us/library/windows/desktop/dd562994(v=vs.85).aspx">file
    name extensions for Windows Media metafiles</a>.

    Since
    - 20.0
    """
    WAX_AUDIO = createConstant(AUDIO_TYPE, "x-ms-wax")
    """
    Windows Media metafiles. For more information, see <a
    href="https://msdn.microsoft.com/en-us/library/windows/desktop/dd562994(v=vs.85).aspx">file
    name extensions for Windows Media metafiles</a>.

    Since
    - 20.0
    """
    VND_REAL_AUDIO = createConstant(AUDIO_TYPE, "vnd.rn-realaudio")
    """
    Real Audio. For more information, see <a
    href="http://service.real.com/help/faq/rp8/configrp8win.html">this link</a>.

    Since
    - 20.0
    """
    VND_WAVE_AUDIO = createConstant(AUDIO_TYPE, "vnd.wave")
    """
    WAVE format, as defined by <a href="https://tools.ietf.org/html/rfc2361">RFC 2361</a>.

    Since
    - 20.0
    """
    MP4_VIDEO = createConstant(VIDEO_TYPE, "mp4")
    MPEG_VIDEO = createConstant(VIDEO_TYPE, "mpeg")
    OGG_VIDEO = createConstant(VIDEO_TYPE, "ogg")
    QUICKTIME = createConstant(VIDEO_TYPE, "quicktime")
    WEBM_VIDEO = createConstant(VIDEO_TYPE, "webm")
    WMV = createConstant(VIDEO_TYPE, "x-ms-wmv")
    FLV_VIDEO = createConstant(VIDEO_TYPE, "x-flv")
    """
    Flash video. For more information, see <a href=
    "http://help.adobe.com/en_US/ActionScript/3.0_ProgrammingAS3/WS5b3ccc516d4fbf351e63e3d118a9b90204-7d48.html"
    >this link</a>.

    Since
    - 20.0
    """
    THREE_GPP_VIDEO = createConstant(VIDEO_TYPE, "3gpp")
    """
    The 3GP multimedia container format. For more information, see <a
    href="ftp://www.3gpp.org/tsg_sa/TSG_SA/TSGS_23/Docs/PDF/SP-040065.pdf#page=10">3GPP TS
    26.244</a>.

    Since
    - 20.0
    """
    THREE_GPP2_VIDEO = createConstant(VIDEO_TYPE, "3gpp2")
    """
    The 3G2 multimedia container format. For more information, see <a
    href="http://www.3gpp2.org/Public_html/specs/C.S0050-B_v1.0_070521.pdf#page=16">3GPP2
    C.S0050-B</a>.

    Since
    - 20.0
    """
    APPLICATION_XML_UTF_8 = createConstantUtf8(APPLICATION_TYPE, "xml")
    """
    As described in <a href="http://www.ietf.org/rfc/rfc3023.txt">RFC 3023</a>, this constant
    (`application/xml`) is used for XML documents that are "unreadable by casual users."
    .XML_UTF_8 is provided for documents that may be read by users.

    Since
    - 14.0
    """
    ATOM_UTF_8 = createConstantUtf8(APPLICATION_TYPE, "atom+xml")
    BZIP2 = createConstant(APPLICATION_TYPE, "x-bzip2")
    DART_UTF_8 = createConstantUtf8(APPLICATION_TYPE, "dart")
    """
    Files in the <a href="https://www.dartlang.org/articles/embedding-in-html/">dart</a>
    programming language.

    Since
    - 19.0
    """
    APPLE_PASSBOOK = createConstant(APPLICATION_TYPE, "vnd.apple.pkpass")
    """
    <a href="https://goo.gl/2QoMvg">Apple Passbook</a>.

    Since
    - 19.0
    """
    EOT = createConstant(APPLICATION_TYPE, "vnd.ms-fontobject")
    """
    <a href="http://en.wikipedia.org/wiki/Embedded_OpenType">Embedded OpenType</a> fonts. This is
    <a href="http://www.iana.org/assignments/media-types/application/vnd.ms-fontobject">registered
    </a> with the IANA.

    Since
    - 17.0
    """
    EPUB = createConstant(APPLICATION_TYPE, "epub+zip")
    """
    As described in the <a href="http://idpf.org/epub">International Digital Publishing Forum</a>
    EPUB is the distribution and interchange format standard for digital publications and
    documents. This media type is defined in the <a
    href="http://www.idpf.org/epub/30/spec/epub30-ocf.html">EPUB Open Container Format</a>
    specification.

    Since
    - 15.0
    """
    FORM_DATA = createConstant(APPLICATION_TYPE, "x-www-form-urlencoded")
    KEY_ARCHIVE = createConstant(APPLICATION_TYPE, "pkcs12")
    """
    As described in <a href="https://www.rsa.com/rsalabs/node.asp?id=2138">PKCS #12: Personal
    Information Exchange Syntax Standard</a>, PKCS #12 defines an archive file format for storing
    many cryptography objects as a single file.

    Since
    - 15.0
    """
    APPLICATION_BINARY = createConstant(APPLICATION_TYPE, "binary")
    """
    This is a non-standard media type, but is commonly used in serving hosted binary files as it is
    <a href="http://code.google.com/p/browsersec/wiki/Part2#Survey_of_content_sniffing_behaviors">
    known not to trigger content sniffing in current browsers</a>. It *should not* be used in
    other situations as it is not specified by any RFC and does not appear in the <a
    href="http://www.iana.org/assignments/media-types">/IANA MIME Media Types</a> list. Consider
    .OCTET_STREAM for binary data that is not being served to a browser.

    Since
    - 14.0
    """
    GEO_JSON = createConstant(APPLICATION_TYPE, "geo+json")
    """
    Media type for the <a href="https://tools.ietf.org/html/rfc7946">GeoJSON Format</a>, a
    geospatial data interchange format based on JSON.

    Since
    - 28.0
    """
    GZIP = createConstant(APPLICATION_TYPE, "x-gzip")
    HAL_JSON = createConstant(APPLICATION_TYPE, "hal+json")
    """
    <a href="https://tools.ietf.org/html/draft-kelly-json-hal-08#section-3">JSON Hypertext
    Application Language (HAL) documents</a>.

    Since
    - 26.0
    """
    JAVASCRIPT_UTF_8 = createConstantUtf8(APPLICATION_TYPE, "javascript")
    """
    <a href="http://www.rfc-editor.org/rfc/rfc4329.txt">RFC 4329</a> declares this to be the
    correct media type for JavaScript, but .TEXT_JAVASCRIPT_UTF_8 text/javascript may be
    necessary in certain situations for compatibility.
    """
    JOSE = createConstant(APPLICATION_TYPE, "jose")
    """
    For <a href="https://tools.ietf.org/html/rfc7515">JWS or JWE objects using the Compact
    Serialization</a>.

    Since
    - 27.1
    """
    JOSE_JSON = createConstant(APPLICATION_TYPE, "jose+json")
    """
    For <a href="https://tools.ietf.org/html/rfc7515">JWS or JWE objects using the JSON
    Serialization</a>.

    Since
    - 27.1
    """
    JSON_UTF_8 = createConstantUtf8(APPLICATION_TYPE, "json")
    MANIFEST_JSON_UTF_8 = createConstantUtf8(APPLICATION_TYPE, "manifest+json")
    """
    The <a href="http://www.w3.org/TR/appmanifest/">Manifest for a web application</a>.

    Since
    - 19.0
    """
    KML = createConstant(APPLICATION_TYPE, "vnd.google-earth.kml+xml")
    """
    <a href="http://www.opengeospatial.org/standards/kml/">OGC KML (Keyhole Markup Language)</a>.
    """
    KMZ = createConstant(APPLICATION_TYPE, "vnd.google-earth.kmz")
    """
    <a href="http://www.opengeospatial.org/standards/kml/">OGC KML (Keyhole Markup Language)</a>,
    compressed using the ZIP format into KMZ archives.
    """
    MBOX = createConstant(APPLICATION_TYPE, "mbox")
    """
    The <a href="https://tools.ietf.org/html/rfc4155">mbox database format</a>.

    Since
    - 13.0
    """
    APPLE_MOBILE_CONFIG = createConstant(APPLICATION_TYPE, "x-apple-aspen-config")
    """
    <a href="http://goo.gl/1pGBFm">Apple over-the-air mobile configuration profiles</a>.

    Since
    - 18.0
    """
    MICROSOFT_EXCEL = createConstant(APPLICATION_TYPE, "vnd.ms-excel")
    """
    <a href="http://goo.gl/XDQ1h2">Microsoft Excel</a> spreadsheets.
    """
    MICROSOFT_OUTLOOK = createConstant(APPLICATION_TYPE, "vnd.ms-outlook")
    """
    <a href="http://goo.gl/XrTEqG">Microsoft Outlook</a> items.

    Since
    - 27.1
    """
    MICROSOFT_POWERPOINT = createConstant(APPLICATION_TYPE, "vnd.ms-powerpoint")
    """
    <a href="http://goo.gl/XDQ1h2">Microsoft Powerpoint</a> presentations.
    """
    MICROSOFT_WORD = createConstant(APPLICATION_TYPE, "msword")
    """
    <a href="http://goo.gl/XDQ1h2">Microsoft Word</a> documents.
    """
    MEDIA_PRESENTATION_DESCRIPTION = createConstant(APPLICATION_TYPE, "dash+xml")
    """
    Media type for <a
    href="https://en.wikipedia.org/wiki/Dynamic_Adaptive_Streaming_over_HTTP">Dynamic Adaptive
    Streaming over HTTP (DASH)</a>. This is <a
    href="https://www.iana.org/assignments/media-types/application/dash+xml">registered</a> with
    the IANA.

    Since
    - 28.2
    """
    WASM_APPLICATION = createConstant(APPLICATION_TYPE, "wasm")
    """
    WASM applications. For more information see <a href="https://webassembly.org/">the Web Assembly
    overview</a>.

    Since
    - 27.0
    """
    NACL_APPLICATION = createConstant(APPLICATION_TYPE, "x-nacl")
    """
    NaCl applications. For more information see <a
    href="https://developer.chrome.com/native-client/devguide/coding/application-structure">the
    Developer Guide for Native Client Application Structure</a>.

    Since
    - 20.0
    """
    NACL_PORTABLE_APPLICATION = createConstant(APPLICATION_TYPE, "x-pnacl")
    """
    NaCl portable applications. For more information see <a
    href="https://developer.chrome.com/native-client/devguide/coding/application-structure">the
    Developer Guide for Native Client Application Structure</a>.

    Since
    - 20.0
    """
    OCTET_STREAM = createConstant(APPLICATION_TYPE, "octet-stream")
    OGG_CONTAINER = createConstant(APPLICATION_TYPE, "ogg")
    OOXML_DOCUMENT = createConstant(APPLICATION_TYPE, "vnd.openxmlformats-officedocument.wordprocessingml.document")
    OOXML_PRESENTATION = createConstant(APPLICATION_TYPE, "vnd.openxmlformats-officedocument.presentationml.presentation")
    OOXML_SHEET = createConstant(APPLICATION_TYPE, "vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    OPENDOCUMENT_GRAPHICS = createConstant(APPLICATION_TYPE, "vnd.oasis.opendocument.graphics")
    OPENDOCUMENT_PRESENTATION = createConstant(APPLICATION_TYPE, "vnd.oasis.opendocument.presentation")
    OPENDOCUMENT_SPREADSHEET = createConstant(APPLICATION_TYPE, "vnd.oasis.opendocument.spreadsheet")
    OPENDOCUMENT_TEXT = createConstant(APPLICATION_TYPE, "vnd.oasis.opendocument.text")
    OPENSEARCH_DESCRIPTION_UTF_8 = createConstantUtf8(APPLICATION_TYPE, "opensearchdescription+xml")
    """
    <a href="https://tools.ietf.org/id/draft-ellermann-opensearch-01.html">OpenSearch</a>
    Description files are XML files that describe how a website can be used as a search engine by
    consumers (e.g. web browsers).

    Since
    - 28.2
    """
    PDF = createConstant(APPLICATION_TYPE, "pdf")
    POSTSCRIPT = createConstant(APPLICATION_TYPE, "postscript")
    PROTOBUF = createConstant(APPLICATION_TYPE, "protobuf")
    """
    <a href="http://tools.ietf.org/html/draft-rfernando-protocol-buffers-00">Protocol buffers</a>

    Since
    - 15.0
    """
    RDF_XML_UTF_8 = createConstantUtf8(APPLICATION_TYPE, "rdf+xml")
    """
    <a href="https://en.wikipedia.org/wiki/RDF/XML">RDF/XML</a> documents, which are XML
    serializations of <a
    href="https://en.wikipedia.org/wiki/Resource_Description_Framework">Resource Description
    Framework</a> graphs.

    Since
    - 14.0
    """
    RTF_UTF_8 = createConstantUtf8(APPLICATION_TYPE, "rtf")
    SFNT = createConstant(APPLICATION_TYPE, "font-sfnt")
    """
    <a href="https://tools.ietf.org/html/rfc8081">RFC 8081</a> declares .FONT_SFNT
    font/sfnt to be the correct media type for SFNT, but this may be necessary in certain
    situations for compatibility.

    Since
    - 17.0
    """
    SHOCKWAVE_FLASH = createConstant(APPLICATION_TYPE, "x-shockwave-flash")
    SKETCHUP = createConstant(APPLICATION_TYPE, "vnd.sketchup.skp")
    """
    `skp` files produced by the 3D Modeling software <a
    href="https://www.sketchup.com/">SketchUp</a>

    Since
    - 13.0
    """
    SOAP_XML_UTF_8 = createConstantUtf8(APPLICATION_TYPE, "soap+xml")
    """
    As described in <a href="http://www.ietf.org/rfc/rfc3902.txt">RFC 3902</a>, this constant
    (`application/soap+xml`) is used to identify SOAP 1.2 message envelopes that have been
    serialized with XML 1.0.
    
    For SOAP 1.1 messages, see `XML_UTF_8` per <a
    href="http://www.w3.org/TR/2000/NOTE-SOAP-20000508/">W3C Note on Simple Object Access Protocol
    (SOAP) 1.1</a>

    Since
    - 20.0
    """
    TAR = createConstant(APPLICATION_TYPE, "x-tar")
    WOFF = createConstant(APPLICATION_TYPE, "font-woff")
    """
    <a href="https://tools.ietf.org/html/rfc8081">RFC 8081</a> declares .FONT_WOFF
    font/woff to be the correct media type for WOFF, but this may be necessary in certain
    situations for compatibility.

    Since
    - 17.0
    """
    WOFF2 = createConstant(APPLICATION_TYPE, "font-woff2")
    """
    <a href="https://tools.ietf.org/html/rfc8081">RFC 8081</a> declares .FONT_WOFF2
    font/woff2 to be the correct media type for WOFF2, but this may be necessary in certain
    situations for compatibility.

    Since
    - 20.0
    """
    XHTML_UTF_8 = createConstantUtf8(APPLICATION_TYPE, "xhtml+xml")
    XRD_UTF_8 = createConstantUtf8(APPLICATION_TYPE, "xrd+xml")
    """
    Extensible Resource Descriptors. This is not yet registered with the IANA, but it is specified
    by OASIS in the <a href="http://docs.oasis-open.org/xri/xrd/v1.0/cd02/xrd-1.0-cd02.html">XRD
    definition</a> and implemented in projects such as <a
    href="http://code.google.com/p/webfinger/">WebFinger</a>.

    Since
    - 14.0
    """
    ZIP = createConstant(APPLICATION_TYPE, "zip")
    FONT_COLLECTION = createConstant(FONT_TYPE, "collection")
    """
    A collection of font outlines as defined by <a href="https://tools.ietf.org/html/rfc8081">RFC
    8081</a>.

    Since
    - 30.0
    """
    FONT_OTF = createConstant(FONT_TYPE, "otf")
    """
    <a href="https://en.wikipedia.org/wiki/OpenType">Open Type Font Format</a> (OTF) as defined by
    <a href="https://tools.ietf.org/html/rfc8081">RFC 8081</a>.

    Since
    - 30.0
    """
    FONT_SFNT = createConstant(FONT_TYPE, "sfnt")
    """
    <a href="https://en.wikipedia.org/wiki/SFNT">Spline or Scalable Font Format</a> (SFNT). <a
    href="https://tools.ietf.org/html/rfc8081">RFC 8081</a> declares this to be the correct media
    type for SFNT, but .SFNT application/font-sfnt may be necessary in certain situations
    for compatibility.

    Since
    - 30.0
    """
    FONT_TTF = createConstant(FONT_TYPE, "ttf")
    """
    <a href="https://en.wikipedia.org/wiki/TrueType">True Type Font Format</a> (TTF) as defined by
    <a href="https://tools.ietf.org/html/rfc8081">RFC 8081</a>.

    Since
    - 30.0
    """
    FONT_WOFF = createConstant(FONT_TYPE, "woff")
    """
    <a href="http://en.wikipedia.org/wiki/Web_Open_Font_Format">Web Open Font Format</a> (WOFF). <a
    href="https://tools.ietf.org/html/rfc8081">RFC 8081</a> declares this to be the correct media
    type for SFNT, but .WOFF application/font-woff may be necessary in certain situations
    for compatibility.

    Since
    - 30.0
    """
    FONT_WOFF2 = createConstant(FONT_TYPE, "woff2")
    """
    <a href="http://en.wikipedia.org/wiki/Web_Open_Font_Format">Web Open Font Format</a> (WOFF2).
    <a href="https://tools.ietf.org/html/rfc8081">RFC 8081</a> declares this to be the correct
    media type for SFNT, but .WOFF2 application/font-woff2 may be necessary in certain
    situations for compatibility.

    Since
    - 30.0
    """


    def type(self) -> str:
        """
        Returns the top-level media type. For example, `"text"` in `"text/plain"`.
        """
        ...


    def subtype(self) -> str:
        """
        Returns the media subtype. For example, `"plain"` in `"text/plain"`.
        """
        ...


    def parameters(self) -> "ImmutableListMultimap"[str, str]:
        """
        Returns a multimap containing the parameters of this media type.
        """
        ...


    def charset(self) -> "Optional"["Charset"]:
        """
        Returns an optional charset for the value of the charset parameter if it is specified.

        Raises
        - IllegalStateException: if multiple charset values have been set for this media type
        - IllegalCharsetNameException: if a charset value is present, but illegal
        - UnsupportedCharsetException: if a charset value is present, but no support is available
            in this instance of the Java virtual machine
        """
        ...


    def withoutParameters(self) -> "MediaType":
        """
        Returns a new instance with the same type and subtype as this instance, but without any
        parameters.
        """
        ...


    def withParameters(self, parameters: "Multimap"[str, str]) -> "MediaType":
        """
        *Replaces* all parameters with the given parameters.

        Raises
        - IllegalArgumentException: if any parameter or value is invalid
        """
        ...


    def withParameters(self, attribute: str, values: Iterable[str]) -> "MediaType":
        """
        *Replaces* all parameters with the given attribute with parameters using the given
        values. If there are no values, any existing parameters with the given attribute are removed.

        Raises
        - IllegalArgumentException: if either `attribute` or `values` is invalid

        Since
        - 24.0
        """
        ...


    def withParameter(self, attribute: str, value: str) -> "MediaType":
        """
        *Replaces* all parameters with the given attribute with a single parameter with the
        given value. If multiple parameters with the same attributes are necessary use .withParameters(String, Iterable). Prefer .withCharset for setting the `charset`
        parameter when using a Charset object.

        Raises
        - IllegalArgumentException: if either `attribute` or `value` is invalid
        """
        ...


    def withCharset(self, charset: "Charset") -> "MediaType":
        """
        Returns a new instance with the same type and subtype as this instance, with the `charset` parameter set to the Charset.name name of the given charset. Only one `charset` parameter will be present on the new instance regardless of the number set on this
        one.
        
        If a charset must be specified that is not supported on this JVM (and thus is not
        representable as a Charset instance, use .withParameter.
        """
        ...


    def hasWildcard(self) -> bool:
        """
        Returns True if either the type or subtype is the wildcard.
        """
        ...


    def is(self, mediaTypeRange: "MediaType") -> bool:
        """
        Returns `True` if this instance falls within the range (as defined by <a
        href="http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html">the HTTP Accept header</a>) given
        by the argument according to three criteria:
        
        <ol>
          - The type of the argument is the wildcard or equal to the type of this instance.
          - The subtype of the argument is the wildcard or equal to the subtype of this instance.
          - All of the parameters present in the argument are present in this instance.
        </ol>
        
        For example:
        
        ````PLAIN_TEXT_UTF_8.is(PLAIN_TEXT_UTF_8) // True
        PLAIN_TEXT_UTF_8.is(HTML_UTF_8) // False
        PLAIN_TEXT_UTF_8.is(ANY_TYPE) // True
        PLAIN_TEXT_UTF_8.is(ANY_TEXT_TYPE) // True
        PLAIN_TEXT_UTF_8.is(ANY_IMAGE_TYPE) // False
        PLAIN_TEXT_UTF_8.is(ANY_TEXT_TYPE.withCharset(UTF_8)) // True
        PLAIN_TEXT_UTF_8.withoutParameters().is(ANY_TEXT_TYPE.withCharset(UTF_8)) // False
        PLAIN_TEXT_UTF_8.is(ANY_TEXT_TYPE.withCharset(UTF_16)) // False````
        
        Note that while it is possible to have the same parameter declared multiple times within a
        media type this method does not consider the number of occurrences of a parameter. For example,
        `"text/plain; charset=UTF-8"` satisfies `"text/plain; charset=UTF-8;
        charset=UTF-8"`.
        """
        ...


    @staticmethod
    def create(type: str, subtype: str) -> "MediaType":
        """
        Creates a new media type with the given type and subtype.

        Raises
        - IllegalArgumentException: if type or subtype is invalid or if a wildcard is used for the
            type, but not the subtype.
        """
        ...


    @staticmethod
    def parse(input: str) -> "MediaType":
        """
        Parses a media type from its string representation.

        Raises
        - IllegalArgumentException: if the input is not parsable
        """
        ...


    def equals(self, obj: "Object") -> bool:
        ...


    def hashCode(self) -> int:
        ...


    def toString(self) -> str:
        """
        Returns the string representation of this media type in the format described in <a
        href="http://www.ietf.org/rfc/rfc2045.txt">RFC 2045</a>.
        """
        ...
