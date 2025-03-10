"""
Python module generated from Java source file java.security.Key

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.security import *
from typing import Any, Callable, Iterable, Tuple


class Key(Serializable):

    serialVersionUID = 6603384152749567654L
    """
    The class fingerprint that is set to indicate
    serialization compatibility with a previous
    version of the class.

    Deprecated
    - A `serialVersionUID` field in an interface is
    ineffectual. Do not use; no replacement.
    """


    def getAlgorithm(self) -> str:
        """
        Returns the standard algorithm name for this key. For
        example, "DSA" would indicate that this key is a DSA key.
        See the key related sections (KeyFactory, KeyGenerator,
        KeyPairGenerator, and SecretKeyFactory) in the <a href=
        "/../specs/security/standard-names.html">
        Java Security Standard Algorithm Names Specification</a>
        for information about standard key algorithm names.

        Returns
        - the name of the algorithm associated with this key.
        """
        ...


    def getFormat(self) -> str:
        """
        Returns the name of the primary encoding format of this key,
        or null if this key does not support encoding.
        The primary encoding format is
        named in terms of the appropriate ASN.1 data format, if an
        ASN.1 specification for this key exists.
        For example, the name of the ASN.1 data format for public
        keys is <I>SubjectPublicKeyInfo</I>, as
        defined by the X.509 standard; in this case, the returned format is
        `"X.509"`. Similarly,
        the name of the ASN.1 data format for private keys is
        <I>PrivateKeyInfo</I>,
        as defined by the PKCS #8 standard; in this case, the returned format is
        `"PKCS.8"`.

        Returns
        - the primary encoding format of the key.
        """
        ...


    def getEncoded(self) -> list[int]:
        """
        Returns the key in its primary encoding format, or null
        if this key does not support encoding.

        Returns
        - the encoded key, or null if the key does not support
        encoding.
        """
        ...
