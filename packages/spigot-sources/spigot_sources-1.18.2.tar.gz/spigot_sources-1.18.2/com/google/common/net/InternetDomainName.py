"""
Python module generated from Java source file com.google.common.net.InternetDomainName

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtCompatible
from com.google.common.base import Ascii
from com.google.common.base import CharMatcher
from com.google.common.base import Joiner
from com.google.common.base import Optional
from com.google.common.base import Splitter
from com.google.common.collect import ImmutableList
from com.google.common.net import *
from com.google.errorprone.annotations import Immutable
from com.google.thirdparty.publicsuffix import PublicSuffixPatterns
from com.google.thirdparty.publicsuffix import PublicSuffixType
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class InternetDomainName:
    """
    An immutable well-formed internet domain name, such as `com` or `foo.co.uk`. Only
    syntactic analysis is performed; no DNS lookups or other network interactions take place. Thus
    there is no guarantee that the domain actually exists on the internet.
    
    One common use of this class is to determine whether a given string is likely to represent an
    addressable domain on the web -- that is, for a candidate string `"xxx"`, might browsing to
    `"http://xxx/"` result in a webpage being displayed? In the past, this test was frequently
    done by determining whether the domain ended with a .isPublicSuffix() public suffix
    but was not itself a public suffix. However, this test is no longer accurate. There are many
    domains which are both public suffixes and addressable as hosts; `"uk.com"` is one example.
    Using the subset of public suffixes that are .isRegistrySuffix() registry suffixes,
    one can get a better result, as only a few registry suffixes are addressable. However, the most
    useful test to determine if a domain is a plausible web host is .hasPublicSuffix(). This
    will return `True` for many domains which (currently) are not hosts, such as `"com"`,
    but given that any public suffix may become a host without warning, it is better to err on the
    side of permissiveness and thus avoid spurious rejection of valid sites. Of course, to actually
    determine addressability of any host, clients of this class will need to perform their own DNS
    lookups.
    
    During construction, names are normalized in two ways:
    
    <ol>
      - ASCII uppercase characters are converted to lowercase.
      - Unicode dot separators other than the ASCII period (`'.'`) are converted to the ASCII
          period.
    </ol>
    
    The normalized values will be returned from .toString() and .parts(), and will
    be reflected in the result of .equals(Object).
    
    <a href="http://en.wikipedia.org/wiki/Internationalized_domain_name">Internationalized domain
    names</a> such as `网络.cn` are supported, as are the equivalent <a
    href="http://en.wikipedia.org/wiki/Internationalized_domain_name">IDNA Punycode-encoded</a>
    versions.

    Author(s)
    - Catherine Berry

    Since
    - 5.0
    """

    @staticmethod
    def from(domain: str) -> "InternetDomainName":
        """
        Returns an instance of InternetDomainName after lenient validation. Specifically,
        validation against <a href="http://www.ietf.org/rfc/rfc3490.txt">RFC 3490</a>
        ("Internationalizing Domain Names in Applications") is skipped, while validation against <a
        href="http://www.ietf.org/rfc/rfc1035.txt">RFC 1035</a> is relaxed in the following ways:
        
        
          - Any part containing non-ASCII characters is considered valid.
          - Underscores ('_') are permitted wherever dashes ('-') are permitted.
          - Parts other than the final part may start with a digit, as mandated by <a
              href="https://tools.ietf.org/html/rfc1123#section-2">RFC 1123</a>.

        Arguments
        - domain: A domain name (not IP address)

        Raises
        - IllegalArgumentException: if `domain` is not syntactically valid according to
            .isValid

        Since
        - 10.0 (previously named `fromLenient`)
        """
        ...


    def parts(self) -> "ImmutableList"[str]:
        """
        Returns the individual components of this domain name, normalized to all lower case. For
        example, for the domain name `mail.google.com`, this method returns the list `["mail", "google", "com"]`.
        """
        ...


    def isPublicSuffix(self) -> bool:
        """
        Indicates whether this domain name represents a *public suffix*, as defined by the Mozilla
        Foundation's <a href="http://publicsuffix.org/">Public Suffix List</a> (PSL). A public suffix
        is one under which Internet users can directly register names, such as `com`, `co.uk` or `pvt.k12.wy.us`. Examples of domain names that are *not* public suffixes
        include `google.com`, `foo.co.uk`, and `myblog.blogspot.com`.
        
        Public suffixes are a proper superset of .isRegistrySuffix() registry suffixes.
        The list of public suffixes additionally contains privately owned domain names under which
        Internet users can register subdomains. An example of a public suffix that is not a registry
        suffix is `blogspot.com`. Note that it is True that all public suffixes *have*
        registry suffixes, since domain name registries collectively control all internet domain names.
        
        For considerations on whether the public suffix or registry suffix designation is more
        suitable for your application, see <a
        href="https://github.com/google/guava/wiki/InternetDomainNameExplained">this article</a>.

        Returns
        - `True` if this domain name appears exactly on the public suffix list

        Since
        - 6.0
        """
        ...


    def hasPublicSuffix(self) -> bool:
        """
        Indicates whether this domain name ends in a .isPublicSuffix() public suffix,
        including if it is a public suffix itself. For example, returns `True` for `www.google.com`, `foo.co.uk` and `com`, but not for `invalid` or `google.invalid`. This is the recommended method for determining whether a domain is potentially
        an addressable host.
        
        Note that this method is equivalent to .hasRegistrySuffix() because all registry
        suffixes are public suffixes *and* all public suffixes have registry suffixes.

        Since
        - 6.0
        """
        ...


    def publicSuffix(self) -> "InternetDomainName":
        """
        Returns the .isPublicSuffix() public suffix portion of the domain name, or `null` if no public suffix is present.

        Since
        - 6.0
        """
        ...


    def isUnderPublicSuffix(self) -> bool:
        """
        Indicates whether this domain name ends in a .isPublicSuffix() public suffix,
        while not being a public suffix itself. For example, returns `True` for `www.google.com`, `foo.co.uk` and `myblog.blogspot.com`, but not for `com`,
        `co.uk`, `google.invalid`, or `blogspot.com`.
        
        This method can be used to determine whether it will probably be possible to set cookies on
        the domain, though even that depends on individual browsers' implementations of cookie
        controls. See <a href="http://www.ietf.org/rfc/rfc2109.txt">RFC 2109</a> for details.

        Since
        - 6.0
        """
        ...


    def isTopPrivateDomain(self) -> bool:
        """
        Indicates whether this domain name is composed of exactly one subdomain component followed by a
        .isPublicSuffix() public suffix. For example, returns `True` for `google.com` `foo.co.uk`, and `myblog.blogspot.com`, but not for `www.google.com`, `co.uk`, or `blogspot.com`.
        
        This method can be used to determine whether a domain is probably the highest level for
        which cookies may be set, though even that depends on individual browsers' implementations of
        cookie controls. See <a href="http://www.ietf.org/rfc/rfc2109.txt">RFC 2109</a> for details.

        Since
        - 6.0
        """
        ...


    def topPrivateDomain(self) -> "InternetDomainName":
        """
        Returns the portion of this domain name that is one level beneath the .isPublicSuffix() public suffix. For example, for `x.adwords.google.co.uk` it returns
        `google.co.uk`, since `co.uk` is a public suffix. Similarly, for `myblog.blogspot.com` it returns the same domain, `myblog.blogspot.com`, since `blogspot.com` is a public suffix.
        
        If .isTopPrivateDomain() is True, the current domain name instance is returned.
        
        This method can be used to determine the probable highest level parent domain for which
        cookies may be set, though even that depends on individual browsers' implementations of cookie
        controls.

        Raises
        - IllegalStateException: if this domain does not end with a public suffix

        Since
        - 6.0
        """
        ...


    def isRegistrySuffix(self) -> bool:
        """
        Indicates whether this domain name represents a *registry suffix*, as defined by a subset
        of the Mozilla Foundation's <a href="http://publicsuffix.org/">Public Suffix List</a> (PSL). A
        registry suffix is one under which Internet users can directly register names via a domain name
        registrar, and have such registrations lawfully protected by internet-governing bodies such as
        ICANN. Examples of registry suffixes include `com`, `co.uk`, and `pvt.k12.wy.us`. Examples of domain names that are *not* registry suffixes include `google.com` and `foo.co.uk`.
        
        Registry suffixes are a proper subset of .isPublicSuffix() public suffixes. The
        list of public suffixes additionally contains privately owned domain names under which Internet
        users can register subdomains. An example of a public suffix that is not a registry suffix is
        `blogspot.com`. Note that it is True that all public suffixes *have* registry
        suffixes, since domain name registries collectively control all internet domain names.
        
        For considerations on whether the public suffix or registry suffix designation is more
        suitable for your application, see <a
        href="https://github.com/google/guava/wiki/InternetDomainNameExplained">this article</a>.

        Returns
        - `True` if this domain name appears exactly on the public suffix list as part of
            the registry suffix section (labelled "ICANN").

        Since
        - 23.3
        """
        ...


    def hasRegistrySuffix(self) -> bool:
        """
        Indicates whether this domain name ends in a .isRegistrySuffix() registry suffix,
        including if it is a registry suffix itself. For example, returns `True` for `www.google.com`, `foo.co.uk` and `com`, but not for `invalid` or `google.invalid`.
        
        Note that this method is equivalent to .hasPublicSuffix() because all registry
        suffixes are public suffixes *and* all public suffixes have registry suffixes.

        Since
        - 23.3
        """
        ...


    def registrySuffix(self) -> "InternetDomainName":
        """
        Returns the .isRegistrySuffix() registry suffix portion of the domain name, or
        `null` if no registry suffix is present.

        Since
        - 23.3
        """
        ...


    def isUnderRegistrySuffix(self) -> bool:
        """
        Indicates whether this domain name ends in a .isRegistrySuffix() registry suffix,
        while not being a registry suffix itself. For example, returns `True` for `www.google.com`, `foo.co.uk` and `blogspot.com`, but not for `com`, `co.uk`, or `google.invalid`.

        Since
        - 23.3
        """
        ...


    def isTopDomainUnderRegistrySuffix(self) -> bool:
        """
        Indicates whether this domain name is composed of exactly one subdomain component followed by a
        .isRegistrySuffix() registry suffix. For example, returns `True` for `google.com`, `foo.co.uk`, and `blogspot.com`, but not for `www.google.com`,
        `co.uk`, or `myblog.blogspot.com`.
        
        **Warning:** This method should not be used to determine the probable highest level
        parent domain for which cookies may be set. Use .topPrivateDomain() for that purpose.

        Since
        - 23.3
        """
        ...


    def topDomainUnderRegistrySuffix(self) -> "InternetDomainName":
        """
        Returns the portion of this domain name that is one level beneath the .isRegistrySuffix() registry suffix. For example, for `x.adwords.google.co.uk` it
        returns `google.co.uk`, since `co.uk` is a registry suffix. Similarly, for `myblog.blogspot.com` it returns `blogspot.com`, since `com` is a registry suffix.
        
        If .isTopDomainUnderRegistrySuffix() is True, the current domain name instance is
        returned.
        
        **Warning:** This method should not be used to determine whether a domain is probably the
        highest level for which cookies may be set. Use .isTopPrivateDomain() for that purpose.

        Raises
        - IllegalStateException: if this domain does not end with a registry suffix

        Since
        - 23.3
        """
        ...


    def hasParent(self) -> bool:
        """
        Indicates whether this domain is composed of two or more parts.
        """
        ...


    def parent(self) -> "InternetDomainName":
        """
        Returns an `InternetDomainName` that is the immediate ancestor of this one; that is, the
        current domain with the leftmost part removed. For example, the parent of `www.google.com` is `google.com`.

        Raises
        - IllegalStateException: if the domain has no parent, as determined by .hasParent
        """
        ...


    def child(self, leftParts: str) -> "InternetDomainName":
        """
        Creates and returns a new `InternetDomainName` by prepending the argument and a dot to
        the current name. For example, `InternetDomainName.from("foo.com").child("www.bar")`
        returns a new `InternetDomainName` with the value `www.bar.foo.com`. Only lenient
        validation is performed, as described .from(String) here.

        Raises
        - NullPointerException: if leftParts is null
        - IllegalArgumentException: if the resulting name is not valid
        """
        ...


    @staticmethod
    def isValid(name: str) -> bool:
        """
        Indicates whether the argument is a syntactically valid domain name using lenient validation.
        Specifically, validation against <a href="http://www.ietf.org/rfc/rfc3490.txt">RFC 3490</a>
        ("Internationalizing Domain Names in Applications") is skipped.
        
        The following two code snippets are equivalent:
        
        ````domainName = InternetDomainName.isValid(name)
            ? InternetDomainName.from(name)
            : DEFAULT_DOMAIN;````
        
        ````try {
          domainName = InternetDomainName.from(name);` catch (IllegalArgumentException e) {
          domainName = DEFAULT_DOMAIN;
        }
        }```

        Since
        - 8.0 (previously named `isValidLenient`)
        """
        ...


    def toString(self) -> str:
        """
        Returns the domain name, normalized to all lower case.
        """
        ...


    def equals(self, object: "Object") -> bool:
        """
        Equality testing is based on the text supplied by the caller, after normalization as described
        in the class documentation. For example, a non-ASCII Unicode domain name and the Punycode
        version of the same domain name would not be considered equal.
        """
        ...


    def hashCode(self) -> int:
        ...
