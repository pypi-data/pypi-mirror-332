"""
Python module generated from Java source file java.security.MessageDigest

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import ByteArrayOutputStream
from java.io import PrintStream
from java.security import *
from java.util import *
from javax.crypto import SecretKey
from sun.security.jca import GetInstance
from sun.security.util import Debug
from sun.security.util import MessageDigestSpi2
from typing import Any, Callable, Iterable, Tuple


class MessageDigest(MessageDigestSpi):

    @staticmethod
    def getInstance(algorithm: str) -> "MessageDigest":
        """
        Returns a MessageDigest object that implements the specified digest
        algorithm.
        
         This method traverses the list of registered security Providers,
        starting with the most preferred Provider.
        A new MessageDigest object encapsulating the
        MessageDigestSpi implementation from the first
        Provider that supports the specified algorithm is returned.
        
         Note that the list of registered providers may be retrieved via
        the Security.getProviders() Security.getProviders() method.

        Arguments
        - algorithm: the name of the algorithm requested.
        See the MessageDigest section in the <a href=
        "/../specs/security/standard-names.html#messagedigest-algorithms">
        Java Security Standard Algorithm Names Specification</a>
        for information about standard algorithm names.

        Returns
        - a `MessageDigest` object that implements the
                specified algorithm

        Raises
        - NoSuchAlgorithmException: if no `Provider` supports a
                `MessageDigestSpi` implementation for the
                specified algorithm
        - NullPointerException: if `algorithm` is `null`

        See
        - Provider

        Unknown Tags
        - The JDK Reference Implementation additionally uses the
        `jdk.security.provider.preferred`
        Security.getProperty(String) Security property to determine
        the preferred provider order for the specified algorithm. This
        may be different than the order of providers returned by
        Security.getProviders() Security.getProviders().
        """
        ...


    @staticmethod
    def getInstance(algorithm: str, provider: str) -> "MessageDigest":
        """
        Returns a MessageDigest object that implements the specified digest
        algorithm.
        
         A new MessageDigest object encapsulating the
        MessageDigestSpi implementation from the specified provider
        is returned.  The specified provider must be registered
        in the security provider list.
        
         Note that the list of registered providers may be retrieved via
        the Security.getProviders() Security.getProviders() method.

        Arguments
        - algorithm: the name of the algorithm requested.
        See the MessageDigest section in the <a href=
        "/../specs/security/standard-names.html#messagedigest-algorithms">
        Java Security Standard Algorithm Names Specification</a>
        for information about standard algorithm names.
        - provider: the name of the provider.

        Returns
        - a `MessageDigest` object that implements the
                specified algorithm

        Raises
        - IllegalArgumentException: if the provider name is `null`
                or empty
        - NoSuchAlgorithmException: if a `MessageDigestSpi`
                implementation for the specified algorithm is not
                available from the specified provider
        - NoSuchProviderException: if the specified provider is not
                registered in the security provider list
        - NullPointerException: if `algorithm` is `null`

        See
        - Provider
        """
        ...


    @staticmethod
    def getInstance(algorithm: str, provider: "Provider") -> "MessageDigest":
        """
        Returns a MessageDigest object that implements the specified digest
        algorithm.
        
         A new MessageDigest object encapsulating the
        MessageDigestSpi implementation from the specified Provider
        object is returned.  Note that the specified Provider object
        does not have to be registered in the provider list.

        Arguments
        - algorithm: the name of the algorithm requested.
        See the MessageDigest section in the <a href=
        "/../specs/security/standard-names.html#messagedigest-algorithms">
        Java Security Standard Algorithm Names Specification</a>
        for information about standard algorithm names.
        - provider: the provider.

        Returns
        - a `MessageDigest` object that implements the
                specified algorithm

        Raises
        - IllegalArgumentException: if the specified provider is
                `null`
        - NoSuchAlgorithmException: if a `MessageDigestSpi`
                implementation for the specified algorithm is not available
                from the specified `Provider` object
        - NullPointerException: if `algorithm` is `null`

        See
        - Provider

        Since
        - 1.4
        """
        ...


    def getProvider(self) -> "Provider":
        """
        Returns the provider of this message digest object.

        Returns
        - the provider of this message digest object
        """
        ...


    def update(self, input: int) -> None:
        """
        Updates the digest using the specified byte.

        Arguments
        - input: the byte with which to update the digest.
        """
        ...


    def update(self, input: list[int], offset: int, len: int) -> None:
        """
        Updates the digest using the specified array of bytes, starting
        at the specified offset.

        Arguments
        - input: the array of bytes.
        - offset: the offset to start from in the array of bytes.
        - len: the number of bytes to use, starting at
        `offset`.
        """
        ...


    def update(self, input: list[int]) -> None:
        """
        Updates the digest using the specified array of bytes.

        Arguments
        - input: the array of bytes.
        """
        ...


    def update(self, input: "ByteBuffer") -> None:
        """
        Update the digest using the specified ByteBuffer. The digest is
        updated using the `input.remaining()` bytes starting
        at `input.position()`.
        Upon return, the buffer's position will be equal to its limit;
        its limit will not have changed.

        Arguments
        - input: the ByteBuffer

        Since
        - 1.5
        """
        ...


    def digest(self) -> list[int]:
        """
        Completes the hash computation by performing final operations
        such as padding. The digest is reset after this call is made.

        Returns
        - the array of bytes for the resulting hash value.
        """
        ...


    def digest(self, buf: list[int], offset: int, len: int) -> int:
        """
        Completes the hash computation by performing final operations
        such as padding. The digest is reset after this call is made.

        Arguments
        - buf: output buffer for the computed digest
        - offset: offset into the output buffer to begin storing the digest
        - len: number of bytes within buf allotted for the digest

        Returns
        - the number of bytes placed into `buf`

        Raises
        - DigestException: if an error occurs.
        """
        ...


    def digest(self, input: list[int]) -> list[int]:
        """
        Performs a final update on the digest using the specified array
        of bytes, then completes the digest computation. That is, this
        method first calls .update(byte[]) update(input),
        passing the *input* array to the `update` method,
        then calls .digest() digest().

        Arguments
        - input: the input to be updated before the digest is
        completed.

        Returns
        - the array of bytes for the resulting hash value.
        """
        ...


    def toString(self) -> str:
        """
        Returns a string representation of this message digest object.
        """
        ...


    @staticmethod
    def isEqual(digesta: list[int], digestb: list[int]) -> bool:
        """
        Compares two digests for equality. Two digests are equal if they have
        the same length and all bytes at corresponding positions are equal.

        Arguments
        - digesta: one of the digests to compare.
        - digestb: the other digest to compare.

        Returns
        - True if the digests are equal, False otherwise.

        Unknown Tags
        - All bytes in `digesta` are examined to determine equality.
        The calculation time depends only on the length of `digesta`.
        It does not depend on the length of `digestb` or the contents
        of `digesta` and `digestb`.
        """
        ...


    def reset(self) -> None:
        """
        Resets the digest for further use.
        """
        ...


    def getAlgorithm(self) -> str:
        """
        Returns a string that identifies the algorithm, independent of
        implementation details. The name should be a standard
        Java Security name (such as "SHA-256").
        See the MessageDigest section in the <a href=
        "/../specs/security/standard-names.html#messagedigest-algorithms">
        Java Security Standard Algorithm Names Specification</a>
        for information about standard algorithm names.

        Returns
        - the name of the algorithm
        """
        ...


    def getDigestLength(self) -> int:
        """
        Returns the length of the digest in bytes, or 0 if this operation is
        not supported by the provider and the implementation is not cloneable.

        Returns
        - the digest length in bytes, or 0 if this operation is not
        supported by the provider and the implementation is not cloneable.

        Since
        - 1.2
        """
        ...


    def clone(self) -> "Object":
        """
        Returns a clone if the implementation is cloneable.

        Returns
        - a clone if the implementation is cloneable.

        Raises
        - CloneNotSupportedException: if this is called on an
        implementation that does not support `Cloneable`.
        """
        ...
