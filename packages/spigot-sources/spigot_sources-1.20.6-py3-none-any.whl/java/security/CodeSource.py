"""
Python module generated from Java source file java.security.CodeSource

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import ByteArrayInputStream
from java.io import IOException
from java.net import SocketPermission
from java.net import URL
from java.security import *
from java.security.cert import *
from java.util import Hashtable
from java.util import Objects
from sun.net.util import URLUtil
from sun.security.util import IOUtils
from typing import Any, Callable, Iterable, Tuple


class CodeSource(Serializable):

    def __init__(self, url: "URL", certs: list["java.security.cert.Certificate"]):
        """
        Constructs a CodeSource and associates it with the specified
        location and set of certificates.

        Arguments
        - url: the location (URL).  It may be `null`.
        - certs: the certificate(s). It may be `null`. The contents
        of the array are copied to protect against subsequent modification.
        """
        ...


    def __init__(self, url: "URL", signers: list["CodeSigner"]):
        """
        Constructs a CodeSource and associates it with the specified
        location and set of code signers.

        Arguments
        - url: the location (URL).  It may be `null`.
        - signers: the code signers. It may be `null`. The contents
        of the array are copied to protect against subsequent modification.

        Since
        - 1.5
        """
        ...


    def hashCode(self) -> int:
        """
        Returns the hash code value for this object.

        Returns
        - a hash code value for this object.
        """
        ...


    def equals(self, obj: "Object") -> bool:
        """
        Tests for equality between the specified object and this
        object. Two CodeSource objects are considered equal if their
        locations are of identical value and if their signer certificate
        chains are of identical value. It is not required that
        the certificate chains be in the same order.

        Arguments
        - obj: the object to test for equality with this object.

        Returns
        - True if the objects are considered equal, False otherwise.
        """
        ...


    def getLocation(self) -> "URL":
        """
        Returns the location associated with this CodeSource.

        Returns
        - the location (URL), or `null` if no URL was supplied
        during construction.
        """
        ...


    def getCertificates(self) -> list["java.security.cert.Certificate"]:
        """
        Returns the certificates associated with this CodeSource.
        
        If this CodeSource object was created using the
        .CodeSource(URL url, CodeSigner[] signers)
        constructor then its certificate chains are extracted and used to
        create an array of Certificate objects. Each signer certificate is
        followed by its supporting certificate chain (which may be empty).
        Each signer certificate and its supporting certificate chain is ordered
        bottom-to-top (i.e., with the signer certificate first and the (root)
        certificate authority last).

        Returns
        - a copy of the certificate array, or `null` if there
        is none.
        """
        ...


    def getCodeSigners(self) -> list["CodeSigner"]:
        """
        Returns the code signers associated with this CodeSource.
        
        If this CodeSource object was created using the
        .CodeSource(URL url, java.security.cert.Certificate[] certs)
        constructor then its certificate chains are extracted and used to
        create an array of CodeSigner objects. Note that only X.509 certificates
        are examined - all other certificate types are ignored.

        Returns
        - a copy of the code signer array, or `null` if there
        is none.

        Since
        - 1.5
        """
        ...


    def implies(self, codesource: "CodeSource") -> bool:
        """
        Returns True if this CodeSource object "implies" the specified CodeSource.
        
        More specifically, this method makes the following checks.
        If any fail, it returns False. If they all succeed, it returns True.
        
        -  *codesource* must not be null.
        -  If this object's certificates are not null, then all
        of this object's certificates must be present in *codesource*'s
        certificates.
        -  If this object's location (getLocation()) is not null, then the
        following checks are made against this object's location and
        *codesource*'s:
          
            -   *codesource*'s location must not be null.
        
            -   If this object's location
                  equals *codesource*'s location, then return True.
        
            -   This object's protocol (getLocation().getProtocol()) must be
                  equal to *codesource*'s protocol, ignoring case.
        
            -   If this object's host (getLocation().getHost()) is not null,
                  then the SocketPermission
                  constructed with this object's host must imply the
                  SocketPermission constructed with *codesource*'s host.
        
            -   If this object's port (getLocation().getPort()) is not
                  equal to -1 (that is, if a port is specified), it must equal
                  *codesource*'s port or default port
                  (codesource.getLocation().getDefaultPort()).
        
            -   If this object's file (getLocation().getFile()) doesn't equal
                  *codesource*'s file, then the following checks are made:
                  If this object's file ends with "/-",
                  then *codesource*'s file must start with this object's
                  file (exclusive the trailing "-").
                  If this object's file ends with a "/*",
                  then *codesource*'s file must start with this object's
                  file and must not have any further "/" separators.
                  If this object's file doesn't end with a "/",
                  then *codesource*'s file must match this object's
                  file with a '/' appended.
        
            -   If this object's reference (getLocation().getRef()) is
                  not null, it must equal *codesource*'s reference.
        
          
        
        
        For example, the codesource objects with the following locations
        and null certificates all imply
        the codesource with the location "http://www.example.com/classes/foo.jar"
        and null certificates:
        ```
            http:
            http://*.example.com/classes/*
            http://www.example.com/classes/-
            http://www.example.com/classes/foo.jar
        ```
        
        Note that if this CodeSource has a null location and a null
        certificate chain, then it implies every other CodeSource.

        Arguments
        - codesource: CodeSource to compare against.

        Returns
        - True if the specified codesource is implied by this codesource,
        False if not.
        """
        ...


    def toString(self) -> str:
        """
        Returns a string describing this CodeSource, telling its
        URL and certificates.

        Returns
        - information about this CodeSource.
        """
        ...
