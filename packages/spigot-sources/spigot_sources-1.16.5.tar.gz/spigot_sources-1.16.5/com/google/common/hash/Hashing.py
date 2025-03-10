"""
Python module generated from Java source file com.google.common.hash.Hashing

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.base import Supplier
from com.google.common.hash import *
from java.security import Key
from java.security import MessageDigest
from java.util import Arrays
from java.util import Iterator
from java.util.zip import Adler32
from java.util.zip import CRC32
from java.util.zip import Checksum
from javax.annotation import Nullable
from javax.crypto.spec import SecretKeySpec
from typing import Any, Callable, Iterable, Tuple


class Hashing:
    """
    Static methods to obtain HashFunction instances, and other static hashing-related
    utilities.
    
    A comparison of the various hash functions can be found
    <a href="http://goo.gl/jS7HH">here</a>.

    Author(s)
    - Kurt Alfred Kluever

    Since
    - 11.0
    """

    @staticmethod
    def goodFastHash(minimumBits: int) -> "HashFunction":
        """
        Returns a general-purpose, **temporary-use**, non-cryptographic hash function. The algorithm
        the returned function implements is unspecified and subject to change without notice.
        
        **Warning:** a new random seed for these functions is chosen each time the `Hashing` class is loaded. **Do not use this method** if hash codes may escape the current
        process in any way, for example being sent over RPC, or saved to disk.
        
        Repeated calls to this method on the same loaded `Hashing` class, using the same value
        for `minimumBits`, will return identically-behaving HashFunction instances.

        Arguments
        - minimumBits: a positive integer (can be arbitrarily large)

        Returns
        - a hash function, described above, that produces hash codes of length `minimumBits` or greater
        """
        ...


    @staticmethod
    def murmur3_32(seed: int) -> "HashFunction":
        """
        Returns a hash function implementing the
        <a href="https://github.com/aappleby/smhasher/blob/master/src/MurmurHash3.cpp">32-bit murmur3
        algorithm, x86 variant</a> (little-endian variant), using the given seed value.
        
        The exact C++ equivalent is the MurmurHash3_x86_32 function (Murmur3A).
        """
        ...


    @staticmethod
    def murmur3_32() -> "HashFunction":
        """
        Returns a hash function implementing the
        <a href="https://github.com/aappleby/smhasher/blob/master/src/MurmurHash3.cpp">32-bit murmur3
        algorithm, x86 variant</a> (little-endian variant), using a seed value of zero.
        
        The exact C++ equivalent is the MurmurHash3_x86_32 function (Murmur3A).
        """
        ...


    @staticmethod
    def murmur3_128(seed: int) -> "HashFunction":
        """
        Returns a hash function implementing the
        <a href="https://github.com/aappleby/smhasher/blob/master/src/MurmurHash3.cpp">128-bit murmur3
        algorithm, x64 variant</a> (little-endian variant), using the given seed value.
        
        The exact C++ equivalent is the MurmurHash3_x64_128 function (Murmur3F).
        """
        ...


    @staticmethod
    def murmur3_128() -> "HashFunction":
        """
        Returns a hash function implementing the
        <a href="https://github.com/aappleby/smhasher/blob/master/src/MurmurHash3.cpp">128-bit murmur3
        algorithm, x64 variant</a> (little-endian variant), using a seed value of zero.
        
        The exact C++ equivalent is the MurmurHash3_x64_128 function (Murmur3F).
        """
        ...


    @staticmethod
    def sipHash24() -> "HashFunction":
        """
        Returns a hash function implementing the <a href="https://131002.net/siphash/">64-bit
        SipHash-2-4 algorithm</a> using a seed value of `k = 00 01 02 ...`.

        Since
        - 15.0
        """
        ...


    @staticmethod
    def sipHash24(k0: int, k1: int) -> "HashFunction":
        """
        Returns a hash function implementing the <a href="https://131002.net/siphash/">64-bit
        SipHash-2-4 algorithm</a> using the given seed.

        Since
        - 15.0
        """
        ...


    @staticmethod
    def md5() -> "HashFunction":
        """
        Returns a hash function implementing the MD5 hash algorithm (128 hash bits) by delegating to
        the MD5 MessageDigest.
        
        **Warning:** MD5 is not cryptographically secure or collision-resistant and is not
        recommended for use in new code. It should be used for legacy compatibility reasons only.
        Please consider using a hash function in the SHA-2 family of functions (e.g., SHA-256).
        """
        ...


    @staticmethod
    def sha1() -> "HashFunction":
        """
        Returns a hash function implementing the SHA-1 algorithm (160 hash bits) by delegating to the
        SHA-1 MessageDigest.
        
        **Warning:** SHA1 is not cryptographically secure and is not recommended for use in new
        code. It should be used for legacy compatibility reasons only. Please consider using a hash
        function in the SHA-2 family of functions (e.g., SHA-256).
        """
        ...


    @staticmethod
    def sha256() -> "HashFunction":
        """
        Returns a hash function implementing the SHA-256 algorithm (256 hash bits) by delegating to the
        SHA-256 MessageDigest.
        """
        ...


    @staticmethod
    def sha384() -> "HashFunction":
        """
        Returns a hash function implementing the SHA-384 algorithm (384 hash bits) by delegating to the
        SHA-384 MessageDigest.

        Since
        - 19.0
        """
        ...


    @staticmethod
    def sha512() -> "HashFunction":
        """
        Returns a hash function implementing the SHA-512 algorithm (512 hash bits) by delegating to the
        SHA-512 MessageDigest.
        """
        ...


    @staticmethod
    def hmacMd5(key: "Key") -> "HashFunction":
        """
        Returns a hash function implementing the Message Authentication Code (MAC) algorithm, using the
        MD5 (128 hash bits) hash function and the given secret key.

        Arguments
        - key: the secret key

        Raises
        - IllegalArgumentException: if the given key is inappropriate for initializing this MAC

        Since
        - 20.0
        """
        ...


    @staticmethod
    def hmacMd5(key: list[int]) -> "HashFunction":
        """
        Returns a hash function implementing the Message Authentication Code (MAC) algorithm, using the
        MD5 (128 hash bits) hash function and a SecretSpecKey created from the given byte array
        and the MD5 algorithm.

        Arguments
        - key: the key material of the secret key

        Since
        - 20.0
        """
        ...


    @staticmethod
    def hmacSha1(key: "Key") -> "HashFunction":
        """
        Returns a hash function implementing the Message Authentication Code (MAC) algorithm, using the
        SHA-1 (160 hash bits) hash function and the given secret key.

        Arguments
        - key: the secret key

        Raises
        - IllegalArgumentException: if the given key is inappropriate for initializing this MAC

        Since
        - 20.0
        """
        ...


    @staticmethod
    def hmacSha1(key: list[int]) -> "HashFunction":
        """
        Returns a hash function implementing the Message Authentication Code (MAC) algorithm, using the
        SHA-1 (160 hash bits) hash function and a SecretSpecKey created from the given byte
        array and the SHA-1 algorithm.

        Arguments
        - key: the key material of the secret key

        Since
        - 20.0
        """
        ...


    @staticmethod
    def hmacSha256(key: "Key") -> "HashFunction":
        """
        Returns a hash function implementing the Message Authentication Code (MAC) algorithm, using the
        SHA-256 (256 hash bits) hash function and the given secret key.

        Arguments
        - key: the secret key

        Raises
        - IllegalArgumentException: if the given key is inappropriate for initializing this MAC

        Since
        - 20.0
        """
        ...


    @staticmethod
    def hmacSha256(key: list[int]) -> "HashFunction":
        """
        Returns a hash function implementing the Message Authentication Code (MAC) algorithm, using the
        SHA-256 (256 hash bits) hash function and a SecretSpecKey created from the given byte
        array and the SHA-256 algorithm.

        Arguments
        - key: the key material of the secret key

        Since
        - 20.0
        """
        ...


    @staticmethod
    def hmacSha512(key: "Key") -> "HashFunction":
        """
        Returns a hash function implementing the Message Authentication Code (MAC) algorithm, using the
        SHA-512 (512 hash bits) hash function and the given secret key.

        Arguments
        - key: the secret key

        Raises
        - IllegalArgumentException: if the given key is inappropriate for initializing this MAC

        Since
        - 20.0
        """
        ...


    @staticmethod
    def hmacSha512(key: list[int]) -> "HashFunction":
        """
        Returns a hash function implementing the Message Authentication Code (MAC) algorithm, using the
        SHA-512 (512 hash bits) hash function and a SecretSpecKey created from the given byte
        array and the SHA-512 algorithm.

        Arguments
        - key: the key material of the secret key

        Since
        - 20.0
        """
        ...


    @staticmethod
    def crc32c() -> "HashFunction":
        """
        Returns a hash function implementing the CRC32C checksum algorithm (32 hash bits) as described
        by RFC 3720, Section 12.1.

        Since
        - 18.0
        """
        ...


    @staticmethod
    def crc32() -> "HashFunction":
        """
        Returns a hash function implementing the CRC-32 checksum algorithm (32 hash bits) by delegating
        to the CRC32 Checksum.
        
        To get the `long` value equivalent to Checksum.getValue() for a
        `HashCode` produced by this function, use HashCode.padToLong().

        Since
        - 14.0
        """
        ...


    @staticmethod
    def adler32() -> "HashFunction":
        """
        Returns a hash function implementing the Adler-32 checksum algorithm (32 hash bits) by
        delegating to the Adler32 Checksum.
        
        To get the `long` value equivalent to Checksum.getValue() for a
        `HashCode` produced by this function, use HashCode.padToLong().

        Since
        - 14.0
        """
        ...


    @staticmethod
    def farmHashFingerprint64() -> "HashFunction":
        """
        Returns a hash function implementing FarmHash's Fingerprint64, an open-source algorithm.
        
        This is designed for generating persistent fingerprints of strings. It isn't
        cryptographically secure, but it produces a high-quality hash with fewer collisions than some
        alternatives we've used in the past. FarmHashFingerprints generated using this are byte-wise
        identical to those created using the C++ version, but note that this uses unsigned integers
        (see com.google.common.primitives.UnsignedInts). Comparisons between the two should
        take this into account.

        Since
        - 20.0
        """
        ...


    @staticmethod
    def consistentHash(hashCode: "HashCode", buckets: int) -> int:
        """
        Assigns to `hashCode` a "bucket" in the range `[0, buckets)`, in a uniform manner
        that minimizes the need for remapping as `buckets` grows. That is, `consistentHash(h, n)` equals:
        
        
        - `n - 1`, with approximate probability `1/n`
        - `consistentHash(h, n - 1)`, otherwise (probability `1 - 1/n`)
        
        
        This method is suitable for the common use case of dividing work among buckets that meet the
        following conditions:
        
        
        - You want to assign the same fraction of inputs to each bucket.
        - When you reduce the number of buckets, you can accept that the most recently added buckets
        will be removed first. More concretely, if you are dividing traffic among tasks, you can
        decrease the number of tasks from 15 and 10, killing off the final 5 tasks, and `consistentHash` will handle it. If, however, you are dividing traffic among servers `alpha`, `bravo`, and `charlie` and you occasionally need to take each of the
        servers offline, `consistentHash` will be a poor fit: It provides no way for you to
        specify which of the three buckets is disappearing. Thus, if your buckets change from `[alpha, bravo, charlie]` to `[bravo, charlie]`, it will assign all the old `alpha`
        traffic to `bravo` and all the old `bravo` traffic to `charlie`, rather than
        letting `bravo` keep its traffic.
        
        
        
        See the <a href="http://en.wikipedia.org/wiki/Consistent_hashing">Wikipedia article on
        consistent hashing</a> for more information.
        """
        ...


    @staticmethod
    def consistentHash(input: int, buckets: int) -> int:
        """
        Assigns to `input` a "bucket" in the range `[0, buckets)`, in a uniform manner that
        minimizes the need for remapping as `buckets` grows. That is, `consistentHash(h,
        n)` equals:
        
        
        - `n - 1`, with approximate probability `1/n`
        - `consistentHash(h, n - 1)`, otherwise (probability `1 - 1/n`)
        
        
        This method is suitable for the common use case of dividing work among buckets that meet the
        following conditions:
        
        
        - You want to assign the same fraction of inputs to each bucket.
        - When you reduce the number of buckets, you can accept that the most recently added buckets
        will be removed first. More concretely, if you are dividing traffic among tasks, you can
        decrease the number of tasks from 15 and 10, killing off the final 5 tasks, and `consistentHash` will handle it. If, however, you are dividing traffic among servers `alpha`, `bravo`, and `charlie` and you occasionally need to take each of the
        servers offline, `consistentHash` will be a poor fit: It provides no way for you to
        specify which of the three buckets is disappearing. Thus, if your buckets change from `[alpha, bravo, charlie]` to `[bravo, charlie]`, it will assign all the old `alpha`
        traffic to `bravo` and all the old `bravo` traffic to `charlie`, rather than
        letting `bravo` keep its traffic.
        
        
        
        See the <a href="http://en.wikipedia.org/wiki/Consistent_hashing">Wikipedia article on
        consistent hashing</a> for more information.
        """
        ...


    @staticmethod
    def combineOrdered(hashCodes: Iterable["HashCode"]) -> "HashCode":
        """
        Returns a hash code, having the same bit length as each of the input hash codes, that combines
        the information of these hash codes in an ordered fashion. That is, whenever two equal hash
        codes are produced by two calls to this method, it is *as likely as possible* that each
        was computed from the *same* input hash codes in the *same* order.

        Raises
        - IllegalArgumentException: if `hashCodes` is empty, or the hash codes do not all
            have the same bit length
        """
        ...


    @staticmethod
    def combineUnordered(hashCodes: Iterable["HashCode"]) -> "HashCode":
        """
        Returns a hash code, having the same bit length as each of the input hash codes, that combines
        the information of these hash codes in an unordered fashion. That is, whenever two equal hash
        codes are produced by two calls to this method, it is *as likely as possible* that each
        was computed from the *same* input hash codes in *some* order.

        Raises
        - IllegalArgumentException: if `hashCodes` is empty, or the hash codes do not all
            have the same bit length
        """
        ...


    @staticmethod
    def concatenating(first: "HashFunction", second: "HashFunction", *rest: Tuple["HashFunction", ...]) -> "HashFunction":
        """
        Returns a hash function which computes its hash code by concatenating the hash codes of the
        underlying hash functions together. This can be useful if you need to generate hash codes of a
        specific length.
        
        For example, if you need 1024-bit hash codes, you could join two Hashing.sha512 hash
        functions together: `Hashing.concatenating(Hashing.sha512(), Hashing.sha512())`.

        Since
        - 19.0
        """
        ...


    @staticmethod
    def concatenating(hashFunctions: Iterable["HashFunction"]) -> "HashFunction":
        """
        Returns a hash function which computes its hash code by concatenating the hash codes of the
        underlying hash functions together. This can be useful if you need to generate hash codes of a
        specific length.
        
        For example, if you need 1024-bit hash codes, you could join two Hashing.sha512 hash
        functions together: `Hashing.concatenating(Hashing.sha512(), Hashing.sha512())`.

        Since
        - 19.0
        """
        ...
