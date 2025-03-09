"""
Python module generated from Java source file java.util.jar.JarEntry

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import IOException
from java.security import CodeSigner
from java.security.cert import Certificate
from java.util.jar import *
from java.util.zip import ZipEntry
from typing import Any, Callable, Iterable, Tuple


class JarEntry(ZipEntry):
    """
    This class is used to represent a JAR file entry.

    Since
    - 1.2
    """

    def __init__(self, name: str):
        """
        Creates a new `JarEntry` for the specified JAR file
        entry name.

        Arguments
        - name: the JAR file entry name

        Raises
        - NullPointerException: if the entry name is `null`
        - IllegalArgumentException: if the entry name is longer than
                   0xFFFF bytes.
        """
        ...


    def __init__(self, ze: "ZipEntry"):
        """
        Creates a new `JarEntry` with fields taken from the
        specified `ZipEntry` object.

        Arguments
        - ze: the `ZipEntry` object to create the
                  `JarEntry` from
        """
        ...


    def __init__(self, je: "JarEntry"):
        """
        Creates a new `JarEntry` with fields taken from the
        specified `JarEntry` object.

        Arguments
        - je: the `JarEntry` to copy
        """
        ...


    def getAttributes(self) -> "Attributes":
        """
        Returns the `Manifest` `Attributes` for this
        entry, or `null` if none.

        Returns
        - the `Manifest` `Attributes` for this
        entry, or `null` if none

        Raises
        - IOException: if an I/O error has occurred
        """
        ...


    def getCertificates(self) -> list["Certificate"]:
        """
        Returns the `Certificate` objects for this entry, or
        `null` if none. This method can only be called once
        the `JarEntry` has been completely verified by reading
        from the entry input stream until the end of the stream has been
        reached. Otherwise, this method will return `null`.
        
        The returned certificate array comprises all the signer certificates
        that were used to verify this entry. Each signer certificate is
        followed by its supporting certificate chain (which may be empty).
        Each signer certificate and its supporting certificate chain are ordered
        bottom-to-top (i.e., with the signer certificate first and the (root)
        certificate authority last).

        Returns
        - the `Certificate` objects for this entry, or
        `null` if none.
        """
        ...


    def getCodeSigners(self) -> list["CodeSigner"]:
        """
        Returns the `CodeSigner` objects for this entry, or
        `null` if none. This method can only be called once
        the `JarEntry` has been completely verified by reading
        from the entry input stream until the end of the stream has been
        reached. Otherwise, this method will return `null`.
        
        The returned array comprises all the code signers that have signed
        this entry.

        Returns
        - the `CodeSigner` objects for this entry, or
        `null` if none.

        Since
        - 1.5
        """
        ...


    def getRealName(self) -> str:
        """
        Returns the real name of this `JarEntry`.
        
        If this `JarEntry` is an entry of a
        <a href="JarFile.html#multirelease">multi-release jar file</a> and the
        `JarFile` is configured to be processed as such, the name returned
        by this method is the path name of the versioned entry that the
        `JarEntry` represents, rather than the path name of the base entry
        that .getName() returns. If the `JarEntry` does not represent
        a versioned entry of a multi-release `JarFile` or the `JarFile`
        is not configured for processing a multi-release jar file, this method
        returns the same name that .getName() returns.

        Returns
        - the real name of the JarEntry

        Since
        - 10
        """
        ...
