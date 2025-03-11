"""
Python module generated from Java source file java.util.jar.JarFile

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import ByteArrayInputStream
from java.io import EOFException
from java.io import File
from java.io import IOException
from java.io import InputStream
from java.lang.ref import SoftReference
from java.net import URL
from java.security import CodeSigner
from java.security import CodeSource
from java.security.cert import Certificate
from java.util import Collections
from java.util import Enumeration
from java.util import Locale
from java.util import NoSuchElementException
from java.util import Objects
from java.util.function import Function
from java.util.jar import *
from java.util.stream import Stream
from java.util.zip import ZipEntry
from java.util.zip import ZipException
from java.util.zip import ZipFile
from jdk.internal.access import JavaUtilZipFileAccess
from jdk.internal.access import SharedSecrets
from sun.security.action import GetPropertyAction
from sun.security.util import ManifestEntryVerifier
from typing import Any, Callable, Iterable, Tuple


class JarFile(ZipFile):
    """
    The `JarFile` class is used to read the contents of a jar file
    from any file that can be opened with `java.io.RandomAccessFile`.
    It extends the class `java.util.zip.ZipFile` with support
    for reading an optional `Manifest` entry, and support for
    processing multi-release jar files.  The `Manifest` can be used
    to specify meta-information about the jar file and its entries.
    
    <a id="multirelease">A multi-release jar file</a> is a jar file that
    contains a manifest with a main attribute named "Multi-Release",
    a set of "base" entries, some of which are public classes with public
    or protected methods that comprise the public interface of the jar file,
    and a set of "versioned" entries contained in subdirectories of the
    "META-INF/versions" directory.  The versioned entries are partitioned by the
    major version of the Java platform.  A versioned entry, with a version
    `n`, `8 < n`, in the "META-INF/versions/{n}" directory overrides
    the base entry as well as any entry with a version number `i` where
    `8 < i < n`.
    
    By default, a `JarFile` for a multi-release jar file is configured
    to process the multi-release jar file as if it were a plain (unversioned) jar
    file, and as such an entry name is associated with at most one base entry.
    The `JarFile` may be configured to process a multi-release jar file by
    creating the `JarFile` with the
    JarFile.JarFile(File, boolean, int, Runtime.Version) constructor.  The
    `Runtime.Version` object sets a maximum version used when searching for
    versioned entries.  When so configured, an entry name
    can correspond with at most one base entry and zero or more versioned
    entries. A search is required to associate the entry name with the latest
    versioned entry whose version is less than or equal to the maximum version
    (see .getEntry(String)).
    
    Class loaders that utilize `JarFile` to load classes from the
    contents of `JarFile` entries should construct the `JarFile`
    by invoking the JarFile.JarFile(File, boolean, int, Runtime.Version)
    constructor with the value `Runtime.version()` assigned to the last
    argument.  This assures that classes compatible with the major
    version of the running JVM are loaded from multi-release jar files.
    
     If the `verify` flag is on when opening a signed jar file, the content
    of the jar entry is verified against the signature embedded inside the manifest
    that is associated with its JarEntry.getRealName() path name. For a
    multi-release jar file, the content of a versioned entry is verfieid against
    its own signature and JarEntry.getCodeSigners() returns its own signers.
    
    Please note that the verification process does not include validating the
    signer's certificate. A caller should inspect the return value of
    JarEntry.getCodeSigners() to further determine if the signature
    can be trusted.
    
     Unless otherwise noted, passing a `null` argument to a constructor
    or method in this class will cause a NullPointerException to be
    thrown.

    Author(s)
    - David Connelly

    See
    - java.util.jar.JarEntry

    Since
    - 1.2

    Unknown Tags
    - <div class="block">
    If the API can not be used to configure a `JarFile` (e.g. to override
    the configuration of a compiled application or library), two `System`
    properties are available.
    
    - 
    `jdk.util.jar.version` can be assigned a value that is the
    `String` representation of a non-negative integer
    `<= Runtime.version().feature()`.  The value is used to set the effective
    runtime version to something other than the default value obtained by
    evaluating `Runtime.version().feature()`. The effective runtime version
    is the version that the JarFile.JarFile(File, boolean, int, Runtime.Version)
    constructor uses when the value of the last argument is
    `JarFile.runtimeVersion()`.
    
    - 
    `jdk.util.jar.enableMultiRelease` can be assigned one of the three
    `String` values *True*, *False*, or *force*.  The
    value *True*, the default value, enables multi-release jar file
    processing.  The value *False* disables multi-release jar processing,
    ignoring the "Multi-Release" manifest attribute, and the versioned
    directories in a multi-release jar file if they exist.  Furthermore,
    the method JarFile.isMultiRelease() returns *False*. The value
    *force* causes the `JarFile` to be initialized to runtime
    versioning after construction.  It effectively does the same as this code:
    `(new JarFile(File, boolean, int, JarFile.runtimeVersion())`.
    
    
    </div>
    """

    MANIFEST_NAME = META_INF + "MANIFEST.MF"
    """
    The JAR manifest file name.
    """


    def __init__(self, name: str):
        """
        Creates a new `JarFile` to read from the specified
        file `name`. The `JarFile` will be verified if
        it is signed.

        Arguments
        - name: the name of the jar file to be opened for reading

        Raises
        - IOException: if an I/O error has occurred
        - SecurityException: if access to the file is denied
                by the SecurityManager
        """
        ...


    def __init__(self, name: str, verify: bool):
        """
        Creates a new `JarFile` to read from the specified
        file `name`.

        Arguments
        - name: the name of the jar file to be opened for reading
        - verify: whether or not to verify the jar file if
        it is signed.

        Raises
        - IOException: if an I/O error has occurred
        - SecurityException: if access to the file is denied
                by the SecurityManager
        """
        ...


    def __init__(self, file: "File"):
        """
        Creates a new `JarFile` to read from the specified
        `File` object. The `JarFile` will be verified if
        it is signed.

        Arguments
        - file: the jar file to be opened for reading

        Raises
        - IOException: if an I/O error has occurred
        - SecurityException: if access to the file is denied
                by the SecurityManager
        """
        ...


    def __init__(self, file: "File", verify: bool):
        """
        Creates a new `JarFile` to read from the specified
        `File` object.

        Arguments
        - file: the jar file to be opened for reading
        - verify: whether or not to verify the jar file if
        it is signed.

        Raises
        - IOException: if an I/O error has occurred
        - SecurityException: if access to the file is denied
                by the SecurityManager.
        """
        ...


    def __init__(self, file: "File", verify: bool, mode: int):
        """
        Creates a new `JarFile` to read from the specified
        `File` object in the specified mode.  The mode argument
        must be either `OPEN_READ` or `OPEN_READ | OPEN_DELETE`.

        Arguments
        - file: the jar file to be opened for reading
        - verify: whether or not to verify the jar file if
        it is signed.
        - mode: the mode in which the file is to be opened

        Raises
        - IOException: if an I/O error has occurred
        - IllegalArgumentException: if the `mode` argument is invalid
        - SecurityException: if access to the file is denied
                by the SecurityManager

        Since
        - 1.3
        """
        ...


    def __init__(self, file: "File", verify: bool, mode: int, version: "Runtime.Version"):
        """
        Creates a new `JarFile` to read from the specified
        `File` object in the specified mode.  The mode argument
        must be either `OPEN_READ` or `OPEN_READ | OPEN_DELETE`.
        The version argument, after being converted to a canonical form, is
        used to configure the `JarFile` for processing
        multi-release jar files.
        
        The canonical form derived from the version parameter is
        `Runtime.Version.parse(Integer.toString(n))` where `n` is
        `Math.max(version.feature(), JarFile.baseVersion().feature())`.

        Arguments
        - file: the jar file to be opened for reading
        - verify: whether or not to verify the jar file if
        it is signed.
        - mode: the mode in which the file is to be opened
        - version: specifies the release version for a multi-release jar file

        Raises
        - IOException: if an I/O error has occurred
        - IllegalArgumentException: if the `mode` argument is invalid
        - SecurityException: if access to the file is denied
                by the SecurityManager
        - NullPointerException: if `version` is `null`

        Since
        - 9
        """
        ...


    @staticmethod
    def baseVersion() -> "Runtime.Version":
        """
        Returns the version that represents the unversioned configuration of a
        multi-release jar file.

        Returns
        - the version that represents the unversioned configuration

        Since
        - 9
        """
        ...


    @staticmethod
    def runtimeVersion() -> "Runtime.Version":
        """
        Returns the version that represents the effective runtime versioned
        configuration of a multi-release jar file.
        
        By default the feature version number of the returned `Version` will
        be equal to the feature version number of `Runtime.version()`.
        However, if the `jdk.util.jar.version` property is set, the
        returned `Version` is derived from that property and feature version
        numbers may not be equal.

        Returns
        - the version that represents the runtime versioned configuration

        Since
        - 9
        """
        ...


    def getVersion(self) -> "Runtime.Version":
        """
        Returns the maximum version used when searching for versioned entries.
        
        If this `JarFile` is not a multi-release jar file or is not
        configured to be processed as such, then the version returned will be the
        same as that returned from .baseVersion().

        Returns
        - the maximum version

        Since
        - 9
        """
        ...


    def isMultiRelease(self) -> bool:
        """
        Indicates whether or not this jar file is a multi-release jar file.

        Returns
        - True if this JarFile is a multi-release jar file

        Since
        - 9
        """
        ...


    def getManifest(self) -> "Manifest":
        """
        Returns the jar file manifest, or `null` if none.

        Returns
        - the jar file manifest, or `null` if none

        Raises
        - IllegalStateException: may be thrown if the jar file has been closed
        - IOException: if an I/O error has occurred
        """
        ...


    def getJarEntry(self, name: str) -> "JarEntry":
        """
        Returns the `JarEntry` for the given base entry name or
        `null` if not found.
        
        If this `JarFile` is a multi-release jar file and is configured
        to be processed as such, then a search is performed to find and return
        a `JarEntry` that is the latest versioned entry associated with the
        given entry name.  The returned `JarEntry` is the versioned entry
        corresponding to the given base entry name prefixed with the string
        `"META-INF/versions/{n`/"}, for the largest value of `n` for
        which an entry exists.  If such a versioned entry does not exist, then
        the `JarEntry` for the base entry is returned, otherwise
        `null` is returned if no entries are found.  The initial value for
        the version `n` is the maximum version as returned by the method
        JarFile.getVersion().

        Arguments
        - name: the jar file entry name

        Returns
        - the `JarEntry` for the given entry name, or
                the versioned entry name, or `null` if not found

        Raises
        - IllegalStateException: may be thrown if the jar file has been closed

        See
        - java.util.jar.JarEntry

        Unknown Tags
        - <div class="block">
        This implementation invokes JarFile.getEntry(String).
        </div>
        """
        ...


    def getEntry(self, name: str) -> "ZipEntry":
        """
        Returns the `ZipEntry` for the given base entry name or
        `null` if not found.
        
        If this `JarFile` is a multi-release jar file and is configured
        to be processed as such, then a search is performed to find and return
        a `ZipEntry` that is the latest versioned entry associated with the
        given entry name.  The returned `ZipEntry` is the versioned entry
        corresponding to the given base entry name prefixed with the string
        `"META-INF/versions/{n`/"}, for the largest value of `n` for
        which an entry exists.  If such a versioned entry does not exist, then
        the `ZipEntry` for the base entry is returned, otherwise
        `null` is returned if no entries are found.  The initial value for
        the version `n` is the maximum version as returned by the method
        JarFile.getVersion().

        Arguments
        - name: the jar file entry name

        Returns
        - the `ZipEntry` for the given entry name or
                the versioned entry name or `null` if not found

        Raises
        - IllegalStateException: may be thrown if the jar file has been closed

        See
        - java.util.zip.ZipEntry

        Unknown Tags
        - <div class="block">
        This implementation may return a versioned entry for the requested name
        even if there is not a corresponding base entry.  This can occur
        if there is a private or package-private versioned entry that matches.
        If a subclass overrides this method, assure that the override method
        invokes `super.getEntry(name)` to obtain all versioned entries.
        </div>
        """
        ...


    def entries(self) -> "Enumeration"["JarEntry"]:
        """
        Returns an enumeration of the jar file entries.

        Returns
        - an enumeration of the jar file entries

        Raises
        - IllegalStateException: may be thrown if the jar file has been closed
        """
        ...


    def stream(self) -> "Stream"["JarEntry"]:
        """
        Returns an ordered `Stream` over the jar file entries.
        Entries appear in the `Stream` in the order they appear in
        the central directory of the jar file.

        Returns
        - an ordered `Stream` of entries in this jar file

        Raises
        - IllegalStateException: if the jar file has been closed

        Since
        - 1.8
        """
        ...


    def versionedStream(self) -> "Stream"["JarEntry"]:
        """
        Returns a `Stream` of the versioned jar file entries.
        
        If this `JarFile` is a multi-release jar file and is configured to
        be processed as such, then an entry in the stream is the latest versioned entry
        associated with the corresponding base entry name. The maximum version of the
        latest versioned entry is the version returned by .getVersion().
        The returned stream may include an entry that only exists as a versioned entry.
        
        If the jar file is not a multi-release jar file or the `JarFile` is not
        configured for processing a multi-release jar file, this method returns the
        same stream that .stream() returns.

        Returns
        - stream of versioned entries

        Since
        - 10
        """
        ...


    def getInputStream(self, ze: "ZipEntry") -> "InputStream":
        """
        Returns an input stream for reading the contents of the specified
        zip file entry.

        Arguments
        - ze: the zip file entry

        Returns
        - an input stream for reading the contents of the specified
                zip file entry

        Raises
        - ZipException: if a zip file format error has occurred
        - IOException: if an I/O error has occurred
        - SecurityException: if any of the jar file entries
                are incorrectly signed.
        - IllegalStateException: may be thrown if the jar file has been closed
        """
        ...
