"""
Python module generated from Java source file java.security.CodeSigner

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import *
from java.security import *
from java.security.cert import CertPath
from typing import Any, Callable, Iterable, Tuple


class CodeSigner(Serializable):

    def __init__(self, signerCertPath: "CertPath", timestamp: "Timestamp"):
        """
        Constructs a CodeSigner object.

        Arguments
        - signerCertPath: The signer's certificate path.
                              It must not be `null`.
        - timestamp: A signature timestamp.
                         If `null` then no timestamp was generated
                         for the signature.

        Raises
        - NullPointerException: if `signerCertPath` is
                                     `null`.
        """
        ...


    def getSignerCertPath(self) -> "CertPath":
        """
        Returns the signer's certificate path.

        Returns
        - A certificate path.
        """
        ...


    def getTimestamp(self) -> "Timestamp":
        """
        Returns the signature timestamp.

        Returns
        - The timestamp or `null` if none is present.
        """
        ...


    def hashCode(self) -> int:
        """
        Returns the hash code value for this code signer.
        The hash code is generated using the signer's certificate path and the
        timestamp, if present.

        Returns
        - a hash code value for this code signer.
        """
        ...


    def equals(self, obj: "Object") -> bool:
        """
        Tests for equality between the specified object and this
        code signer. Two code signers are considered equal if their
        signer certificate paths are equal and if their timestamps are equal,
        if present in both.

        Arguments
        - obj: the object to test for equality with this object.

        Returns
        - True if the objects are considered equal, False otherwise.
        """
        ...


    def toString(self) -> str:
        """
        Returns a string describing this code signer.

        Returns
        - A string comprising the signer's certificate and a timestamp,
                if present.
        """
        ...
