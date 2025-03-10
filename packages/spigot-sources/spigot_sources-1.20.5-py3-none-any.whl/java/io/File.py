"""
Python module generated from Java source file java.io.File

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import *
from java.net import MalformedURLException
from java.net import URI
from java.net import URISyntaxException
from java.net import URL
from java.nio.file import FileStore
from java.nio.file import FileSystems
from java.nio.file import Path
from java.security import SecureRandom
from sun.security.action import GetPropertyAction
from typing import Any, Callable, Iterable, Tuple


class File(Serializable, Comparable):

    separatorChar = fs.getSeparator()
    """
    The system-dependent default name-separator character.  This field is
    initialized to contain the first character of the value of the system
    property `file.separator`.  On UNIX systems the value of this
    field is `'/'`; on Microsoft Windows systems it is `'\\'`.

    See
    - java.lang.System.getProperty(java.lang.String)
    """
    separator = "" + separatorChar
    """
    The system-dependent default name-separator character, represented as a
    string for convenience.  This string contains a single character, namely
    .separatorChar.
    """
    pathSeparatorChar = fs.getPathSeparator()
    """
    The system-dependent path-separator character.  This field is
    initialized to contain the first character of the value of the system
    property `path.separator`.  This character is used to
    separate filenames in a sequence of files given as a *path list*.
    On UNIX systems, this character is `':'`; on Microsoft Windows systems it
    is `';'`.

    See
    - java.lang.System.getProperty(java.lang.String)
    """
    pathSeparator = "" + pathSeparatorChar
    """
    The system-dependent path-separator character, represented as a string
    for convenience.  This string contains a single character, namely
    .pathSeparatorChar.
    """


    def __init__(self, pathname: str):
        """
        Creates a new `File` instance by converting the given
        pathname string into an abstract pathname.  If the given string is
        the empty string, then the result is the empty abstract pathname.

        Arguments
        - pathname: A pathname string

        Raises
        - NullPointerException: If the `pathname` argument is `null`
        """
        ...


    def __init__(self, parent: str, child: str):
        """
        Creates a new `File` instance from a parent pathname string
        and a child pathname string.
        
         If `parent` is `null` then the new
        `File` instance is created as if by invoking the
        single-argument `File` constructor on the given
        `child` pathname string.
        
         Otherwise the `parent` pathname string is taken to denote
        a directory, and the `child` pathname string is taken to
        denote either a directory or a file.  If the `child` pathname
        string is absolute then it is converted into a relative pathname in a
        system-dependent way.  If `parent` is the empty string then
        the new `File` instance is created by converting
        `child` into an abstract pathname and resolving the result
        against a system-dependent default directory.  Otherwise each pathname
        string is converted into an abstract pathname and the child abstract
        pathname is resolved against the parent.

        Arguments
        - parent: The parent pathname string
        - child: The child pathname string

        Raises
        - NullPointerException: If `child` is `null`
        """
        ...


    def __init__(self, parent: "File", child: str):
        """
        Creates a new `File` instance from a parent abstract
        pathname and a child pathname string.
        
         If `parent` is `null` then the new
        `File` instance is created as if by invoking the
        single-argument `File` constructor on the given
        `child` pathname string.
        
         Otherwise the `parent` abstract pathname is taken to
        denote a directory, and the `child` pathname string is taken
        to denote either a directory or a file.  If the `child`
        pathname string is absolute then it is converted into a relative
        pathname in a system-dependent way.  If `parent` is the empty
        abstract pathname then the new `File` instance is created by
        converting `child` into an abstract pathname and resolving
        the result against a system-dependent default directory.  Otherwise each
        pathname string is converted into an abstract pathname and the child
        abstract pathname is resolved against the parent.

        Arguments
        - parent: The parent abstract pathname
        - child: The child pathname string

        Raises
        - NullPointerException: If `child` is `null`
        """
        ...


    def __init__(self, uri: "URI"):
        """
        Creates a new `File` instance by converting the given
        `file:` URI into an abstract pathname.
        
         The exact form of a `file:` URI is system-dependent, hence
        the transformation performed by this constructor is also
        system-dependent.
        
         For a given abstract pathname *f* it is guaranteed that
        
        <blockquote>`
        new File(`*&nbsp;f*`..toURI()
        toURI()).equals(`*&nbsp;f*`..getAbsoluteFile() getAbsoluteFile())
        `</blockquote>
        
        so long as the original abstract pathname, the URI, and the new abstract
        pathname are all created in (possibly different invocations of) the same
        Java virtual machine.  This relationship typically does not hold,
        however, when a `file:` URI that is created in a virtual machine
        on one operating system is converted into an abstract pathname in a
        virtual machine on a different operating system.

        Arguments
        - uri: An absolute, hierarchical URI with a scheme equal to
                `"file"`, a non-empty path component, and undefined
                authority, query, and fragment components

        Raises
        - NullPointerException: If `uri` is `null`
        - IllegalArgumentException: If the preconditions on the parameter do not hold

        See
        - java.net.URI

        Since
        - 1.4
        """
        ...


    def getName(self) -> str:
        """
        Returns the name of the file or directory denoted by this abstract
        pathname.  This is just the last name in the pathname's name
        sequence.  If the pathname's name sequence is empty, then the empty
        string is returned.

        Returns
        - The name of the file or directory denoted by this abstract
                 pathname, or the empty string if this pathname's name sequence
                 is empty
        """
        ...


    def getParent(self) -> str:
        """
        Returns the pathname string of this abstract pathname's parent, or
        `null` if this pathname does not name a parent directory.
        
         The *parent* of an abstract pathname consists of the
        pathname's prefix, if any, and each name in the pathname's name
        sequence except for the last.  If the name sequence is empty then
        the pathname does not name a parent directory.

        Returns
        - The pathname string of the parent directory named by this
                 abstract pathname, or `null` if this pathname
                 does not name a parent
        """
        ...


    def getParentFile(self) -> "File":
        """
        Returns the abstract pathname of this abstract pathname's parent,
        or `null` if this pathname does not name a parent
        directory.
        
         The *parent* of an abstract pathname consists of the
        pathname's prefix, if any, and each name in the pathname's name
        sequence except for the last.  If the name sequence is empty then
        the pathname does not name a parent directory.

        Returns
        - The abstract pathname of the parent directory named by this
                 abstract pathname, or `null` if this pathname
                 does not name a parent

        Since
        - 1.2
        """
        ...


    def getPath(self) -> str:
        """
        Converts this abstract pathname into a pathname string.  The resulting
        string uses the .separator default name-separator character to
        separate the names in the name sequence.

        Returns
        - The string form of this abstract pathname
        """
        ...


    def isAbsolute(self) -> bool:
        """
        Tests whether this abstract pathname is absolute.  The definition of
        absolute pathname is system dependent.  On UNIX systems, a pathname is
        absolute if its prefix is `"/"`.  On Microsoft Windows systems, a
        pathname is absolute if its prefix is a drive specifier followed by
        `"\\"`, or if its prefix is `"\\\\"`.

        Returns
        - `True` if this abstract pathname is absolute,
                 `False` otherwise
        """
        ...


    def getAbsolutePath(self) -> str:
        """
        Returns the absolute pathname string of this abstract pathname.
        
         If this abstract pathname is already absolute, then the pathname
        string is simply returned as if by the .getPath
        method.  If this abstract pathname is the empty abstract pathname then
        the pathname string of the current user directory, which is named by the
        system property `user.dir`, is returned.  Otherwise this
        pathname is resolved in a system-dependent way.  On UNIX systems, a
        relative pathname is made absolute by resolving it against the current
        user directory.  On Microsoft Windows systems, a relative pathname is made absolute
        by resolving it against the current directory of the drive named by the
        pathname, if any; if not, it is resolved against the current user
        directory.

        Returns
        - The absolute pathname string denoting the same file or
                 directory as this abstract pathname

        Raises
        - SecurityException: If a required system property value cannot be accessed.

        See
        - java.io.File.isAbsolute()
        """
        ...


    def getAbsoluteFile(self) -> "File":
        """
        Returns the absolute form of this abstract pathname.  Equivalent to
        `new&nbsp;File(this..getAbsolutePath)`.

        Returns
        - The absolute abstract pathname denoting the same file or
                 directory as this abstract pathname

        Raises
        - SecurityException: If a required system property value cannot be accessed.

        Since
        - 1.2
        """
        ...


    def getCanonicalPath(self) -> str:
        """
        Returns the canonical pathname string of this abstract pathname.
        
         A canonical pathname is both absolute and unique.  The precise
        definition of canonical form is system-dependent.  This method first
        converts this pathname to absolute form if necessary, as if by invoking the
        .getAbsolutePath method, and then maps it to its unique form in a
        system-dependent way.  This typically involves removing redundant names
        such as `"."` and `".."` from the pathname, resolving
        symbolic links (on UNIX platforms), and converting drive letters to a
        standard case (on Microsoft Windows platforms).
        
         Every pathname that denotes an existing file or directory has a
        unique canonical form.  Every pathname that denotes a nonexistent file
        or directory also has a unique canonical form.  The canonical form of
        the pathname of a nonexistent file or directory may be different from
        the canonical form of the same pathname after the file or directory is
        created.  Similarly, the canonical form of the pathname of an existing
        file or directory may be different from the canonical form of the same
        pathname after the file or directory is deleted.

        Returns
        - The canonical pathname string denoting the same file or
                 directory as this abstract pathname

        Raises
        - IOException: If an I/O error occurs, which is possible because the
                 construction of the canonical pathname may require
                 filesystem queries
        - SecurityException: If a required system property value cannot be accessed, or
                 if a security manager exists and its java.lang.SecurityManager.checkRead method denies
                 read access to the file

        See
        - Path.toRealPath

        Since
        - 1.1
        """
        ...


    def getCanonicalFile(self) -> "File":
        """
        Returns the canonical form of this abstract pathname.  Equivalent to
        `new&nbsp;File(this..getCanonicalPath)`.

        Returns
        - The canonical pathname string denoting the same file or
                 directory as this abstract pathname

        Raises
        - IOException: If an I/O error occurs, which is possible because the
                 construction of the canonical pathname may require
                 filesystem queries
        - SecurityException: If a required system property value cannot be accessed, or
                 if a security manager exists and its java.lang.SecurityManager.checkRead method denies
                 read access to the file

        See
        - Path.toRealPath

        Since
        - 1.2
        """
        ...


    def toURL(self) -> "URL":
        """
        Converts this abstract pathname into a `file:` URL.  The
        exact form of the URL is system-dependent.  If it can be determined that
        the file denoted by this abstract pathname is a directory, then the
        resulting URL will end with a slash.

        Returns
        - A URL object representing the equivalent file URL

        Raises
        - MalformedURLException: If the path cannot be parsed as a URL

        See
        - java.net.URL

        Since
        - 1.2

        Deprecated
        - This method does not automatically escape characters that
        are illegal in URLs.  It is recommended that new code convert an
        abstract pathname into a URL by first converting it into a URI, via the
        .toURI() toURI method, and then converting the URI into a URL
        via the java.net.URI.toURL() URI.toURL method.
        """
        ...


    def toURI(self) -> "URI":
        """
        Constructs a `file:` URI that represents this abstract pathname.
        
         The exact form of the URI is system-dependent.  If it can be
        determined that the file denoted by this abstract pathname is a
        directory, then the resulting URI will end with a slash.
        
         For a given abstract pathname *f*, it is guaranteed that
        
        <blockquote>`
        new .File(java.net.URI) File(`*&nbsp;f*`.toURI()).equals(
        `*&nbsp;f*`..getAbsoluteFile() getAbsoluteFile())
        `</blockquote>
        
        so long as the original abstract pathname, the URI, and the new abstract
        pathname are all created in (possibly different invocations of) the same
        Java virtual machine.  Due to the system-dependent nature of abstract
        pathnames, however, this relationship typically does not hold when a
        `file:` URI that is created in a virtual machine on one operating
        system is converted into an abstract pathname in a virtual machine on a
        different operating system.
        
         Note that when this abstract pathname represents a UNC pathname then
        all components of the UNC (including the server name component) are encoded
        in the `URI` path. The authority component is undefined, meaning
        that it is represented as `null`. The Path class defines the
        Path.toUri toUri method to encode the server name in the authority
        component of the resulting `URI`. The .toPath toPath method
        may be used to obtain a `Path` representing this abstract pathname.

        Returns
        - An absolute, hierarchical URI with a scheme equal to
                 `"file"`, a path representing this abstract pathname,
                 and undefined authority, query, and fragment components

        Raises
        - SecurityException: If a required system property value cannot
        be accessed.

        See
        - java.net.URI.toURL()

        Since
        - 1.4
        """
        ...


    def canRead(self) -> bool:
        """
        Tests whether the application can read the file denoted by this
        abstract pathname. On some platforms it may be possible to start the
        Java virtual machine with special privileges that allow it to read
        files that are marked as unreadable. Consequently this method may return
        `True` even though the file does not have read permissions.

        Returns
        - `True` if and only if the file specified by this
                 abstract pathname exists *and* can be read by the
                 application; `False` otherwise

        Raises
        - SecurityException: If a security manager exists and its java.lang.SecurityManager.checkRead(java.lang.String)
                 method denies read access to the file
        """
        ...


    def canWrite(self) -> bool:
        """
        Tests whether the application can modify the file denoted by this
        abstract pathname. On some platforms it may be possible to start the
        Java virtual machine with special privileges that allow it to modify
        files that are marked read-only. Consequently this method may return
        `True` even though the file is marked read-only.

        Returns
        - `True` if and only if the file system actually
                 contains a file denoted by this abstract pathname *and*
                 the application is allowed to write to the file;
                 `False` otherwise.

        Raises
        - SecurityException: If a security manager exists and its java.lang.SecurityManager.checkWrite(java.lang.String)
                 method denies write access to the file
        """
        ...


    def exists(self) -> bool:
        """
        Tests whether the file or directory denoted by this abstract pathname
        exists.

        Returns
        - `True` if and only if the file or directory denoted
                 by this abstract pathname exists; `False` otherwise

        Raises
        - SecurityException: If a security manager exists and its java.lang.SecurityManager.checkRead(java.lang.String)
                 method denies read access to the file or directory
        """
        ...


    def isDirectory(self) -> bool:
        """
        Tests whether the file denoted by this abstract pathname is a
        directory.
        
         Where it is required to distinguish an I/O exception from the case
        that the file is not a directory, or where several attributes of the
        same file are required at the same time, then the java.nio.file.Files.readAttributes(Path,Class,LinkOption[])
        Files.readAttributes method may be used.

        Returns
        - `True` if and only if the file denoted by this
                 abstract pathname exists *and* is a directory;
                 `False` otherwise

        Raises
        - SecurityException: If a security manager exists and its java.lang.SecurityManager.checkRead(java.lang.String)
                 method denies read access to the file
        """
        ...


    def isFile(self) -> bool:
        """
        Tests whether the file denoted by this abstract pathname is a normal
        file.  A file is *normal* if it is not a directory and, in
        addition, satisfies other system-dependent criteria.  Any non-directory
        file created by a Java application is guaranteed to be a normal file.
        
         Where it is required to distinguish an I/O exception from the case
        that the file is not a normal file, or where several attributes of the
        same file are required at the same time, then the java.nio.file.Files.readAttributes(Path,Class,LinkOption[])
        Files.readAttributes method may be used.

        Returns
        - `True` if and only if the file denoted by this
                 abstract pathname exists *and* is a normal file;
                 `False` otherwise

        Raises
        - SecurityException: If a security manager exists and its java.lang.SecurityManager.checkRead(java.lang.String)
                 method denies read access to the file
        """
        ...


    def isHidden(self) -> bool:
        """
        Tests whether the file named by this abstract pathname is a hidden
        file.  The exact definition of *hidden* is system-dependent.  On
        UNIX systems, a file is considered to be hidden if its name begins with
        a period character (`'.'`).  On Microsoft Windows systems, a file is
        considered to be hidden if it has been marked as such in the filesystem.

        Returns
        - `True` if and only if the file denoted by this
                 abstract pathname is hidden according to the conventions of the
                 underlying platform

        Raises
        - SecurityException: If a security manager exists and its java.lang.SecurityManager.checkRead(java.lang.String)
                 method denies read access to the file

        Since
        - 1.2
        """
        ...


    def lastModified(self) -> int:
        """
        Returns the time that the file denoted by this abstract pathname was
        last modified.

        Returns
        - A `long` value representing the time the file was
                 last modified, measured in milliseconds since the epoch
                 (00:00:00 GMT, January 1, 1970), or `0L` if the
                 file does not exist or if an I/O error occurs.  The value may
                 be negative indicating the number of milliseconds before the
                 epoch

        Raises
        - SecurityException: If a security manager exists and its java.lang.SecurityManager.checkRead(java.lang.String)
                 method denies read access to the file

        Unknown Tags
        - While the unit of time of the return value is milliseconds, the
        granularity of the value depends on the underlying file system and may
        be larger.  For example, some file systems use time stamps in units of
        seconds.
        
         Where it is required to distinguish an I/O exception from the case
        where `0L` is returned, or where several attributes of the
        same file are required at the same time, or where the time of last
        access or the creation time are required, then the java.nio.file.Files.readAttributes(Path,Class,LinkOption[])
        Files.readAttributes method may be used.  If however only the
        time of last modification is required, then the
        java.nio.file.Files.getLastModifiedTime(Path,LinkOption[])
        Files.getLastModifiedTime method may be used instead.
        """
        ...


    def length(self) -> int:
        """
        Returns the length of the file denoted by this abstract pathname.
        The return value is unspecified if this pathname denotes a directory.
        
         Where it is required to distinguish an I/O exception from the case
        that `0L` is returned, or where several attributes of the same file
        are required at the same time, then the java.nio.file.Files.readAttributes(Path,Class,LinkOption[])
        Files.readAttributes method may be used.

        Returns
        - The length, in bytes, of the file denoted by this abstract
                 pathname, or `0L` if the file does not exist.  Some
                 operating systems may return `0L` for pathnames
                 denoting system-dependent entities such as devices or pipes.

        Raises
        - SecurityException: If a security manager exists and its java.lang.SecurityManager.checkRead(java.lang.String)
                 method denies read access to the file
        """
        ...


    def createNewFile(self) -> bool:
        """
        Atomically creates a new, empty file named by this abstract pathname if
        and only if a file with this name does not yet exist.  The check for the
        existence of the file and the creation of the file if it does not exist
        are a single operation that is atomic with respect to all other
        filesystem activities that might affect the file.
        <P>
        Note: this method should *not* be used for file-locking, as
        the resulting protocol cannot be made to work reliably. The
        java.nio.channels.FileLock FileLock
        facility should be used instead.

        Returns
        - `True` if the named file does not exist and was
                 successfully created; `False` if the named file
                 already exists

        Raises
        - IOException: If an I/O error occurred
        - SecurityException: If a security manager exists and its java.lang.SecurityManager.checkWrite(java.lang.String)
                 method denies write access to the file

        Since
        - 1.2
        """
        ...


    def delete(self) -> bool:
        """
        Deletes the file or directory denoted by this abstract pathname.  If
        this pathname denotes a directory, then the directory must be empty in
        order to be deleted.
        
         Note that the java.nio.file.Files class defines the java.nio.file.Files.delete(Path) delete method to throw an IOException
        when a file cannot be deleted. This is useful for error reporting and to
        diagnose why a file cannot be deleted.

        Returns
        - `True` if and only if the file or directory is
                 successfully deleted; `False` otherwise

        Raises
        - SecurityException: If a security manager exists and its java.lang.SecurityManager.checkDelete method denies
                 delete access to the file
        """
        ...


    def deleteOnExit(self) -> None:
        """
        Requests that the file or directory denoted by this abstract
        pathname be deleted when the virtual machine terminates.
        Files (or directories) are deleted in the reverse order that
        they are registered. Invoking this method to delete a file or
        directory that is already registered for deletion has no effect.
        Deletion will be attempted only for normal termination of the
        virtual machine, as defined by the Java Language Specification.
        
         Once deletion has been requested, it is not possible to cancel the
        request.  This method should therefore be used with care.
        
        <P>
        Note: this method should *not* be used for file-locking, as
        the resulting protocol cannot be made to work reliably. The
        java.nio.channels.FileLock FileLock
        facility should be used instead.

        Raises
        - SecurityException: If a security manager exists and its java.lang.SecurityManager.checkDelete method denies
                 delete access to the file

        See
        - .delete

        Since
        - 1.2
        """
        ...


    def list(self) -> list[str]:
        """
        Returns an array of strings naming the files and directories in the
        directory denoted by this abstract pathname.
        
         If this abstract pathname does not denote a directory, then this
        method returns `null`.  Otherwise an array of strings is
        returned, one for each file or directory in the directory.  Names
        denoting the directory itself and the directory's parent directory are
        not included in the result.  Each string is a file name rather than a
        complete path.
        
         There is no guarantee that the name strings in the resulting array
        will appear in any specific order; they are not, in particular,
        guaranteed to appear in alphabetical order.
        
         Note that the java.nio.file.Files class defines the java.nio.file.Files.newDirectoryStream(Path) newDirectoryStream method to
        open a directory and iterate over the names of the files in the directory.
        This may use less resources when working with very large directories, and
        may be more responsive when working with remote directories.

        Returns
        - An array of strings naming the files and directories in the
                 directory denoted by this abstract pathname.  The array will be
                 empty if the directory is empty.  Returns `null` if
                 this abstract pathname does not denote a directory, or if an
                 I/O error occurs.

        Raises
        - SecurityException: If a security manager exists and its SecurityManager.checkRead(String) method denies read access to
                 the directory
        """
        ...


    def list(self, filter: "FilenameFilter") -> list[str]:
        """
        Returns an array of strings naming the files and directories in the
        directory denoted by this abstract pathname that satisfy the specified
        filter.  The behavior of this method is the same as that of the
        .list() method, except that the strings in the returned array
        must satisfy the filter.  If the given `filter` is `null`
        then all names are accepted.  Otherwise, a name satisfies the filter if
        and only if the value `True` results when the FilenameFilter.accept FilenameFilter.accept(File,&nbsp;String) method
        of the filter is invoked on this abstract pathname and the name of a
        file or directory in the directory that it denotes.

        Arguments
        - filter: A filename filter

        Returns
        - An array of strings naming the files and directories in the
                 directory denoted by this abstract pathname that were accepted
                 by the given `filter`.  The array will be empty if the
                 directory is empty or if no names were accepted by the filter.
                 Returns `null` if this abstract pathname does not denote
                 a directory, or if an I/O error occurs.

        Raises
        - SecurityException: If a security manager exists and its SecurityManager.checkRead(String) method denies read access to
                 the directory

        See
        - java.nio.file.Files.newDirectoryStream(Path,String)
        """
        ...


    def listFiles(self) -> list["File"]:
        """
        Returns an array of abstract pathnames denoting the files in the
        directory denoted by this abstract pathname.
        
         If this abstract pathname does not denote a directory, then this
        method returns `null`.  Otherwise an array of `File` objects
        is returned, one for each file or directory in the directory.  Pathnames
        denoting the directory itself and the directory's parent directory are
        not included in the result.  Each resulting abstract pathname is
        constructed from this abstract pathname using the .File(File,
        String) File(File,&nbsp;String) constructor.  Therefore if this
        pathname is absolute then each resulting pathname is absolute; if this
        pathname is relative then each resulting pathname will be relative to
        the same directory.
        
         There is no guarantee that the name strings in the resulting array
        will appear in any specific order; they are not, in particular,
        guaranteed to appear in alphabetical order.
        
         Note that the java.nio.file.Files class defines the java.nio.file.Files.newDirectoryStream(Path) newDirectoryStream method
        to open a directory and iterate over the names of the files in the
        directory. This may use less resources when working with very large
        directories.

        Returns
        - An array of abstract pathnames denoting the files and
                 directories in the directory denoted by this abstract pathname.
                 The array will be empty if the directory is empty.  Returns
                 `null` if this abstract pathname does not denote a
                 directory, or if an I/O error occurs.

        Raises
        - SecurityException: If a security manager exists and its SecurityManager.checkRead(String) method denies read access to
                 the directory

        Since
        - 1.2
        """
        ...


    def listFiles(self, filter: "FilenameFilter") -> list["File"]:
        """
        Returns an array of abstract pathnames denoting the files and
        directories in the directory denoted by this abstract pathname that
        satisfy the specified filter.  The behavior of this method is the same
        as that of the .listFiles() method, except that the pathnames in
        the returned array must satisfy the filter.  If the given `filter`
        is `null` then all pathnames are accepted.  Otherwise, a pathname
        satisfies the filter if and only if the value `True` results when
        the FilenameFilter.accept
        FilenameFilter.accept(File,&nbsp;String) method of the filter is
        invoked on this abstract pathname and the name of a file or directory in
        the directory that it denotes.

        Arguments
        - filter: A filename filter

        Returns
        - An array of abstract pathnames denoting the files and
                 directories in the directory denoted by this abstract pathname.
                 The array will be empty if the directory is empty.  Returns
                 `null` if this abstract pathname does not denote a
                 directory, or if an I/O error occurs.

        Raises
        - SecurityException: If a security manager exists and its SecurityManager.checkRead(String) method denies read access to
                 the directory

        See
        - java.nio.file.Files.newDirectoryStream(Path,String)

        Since
        - 1.2
        """
        ...


    def listFiles(self, filter: "FileFilter") -> list["File"]:
        """
        Returns an array of abstract pathnames denoting the files and
        directories in the directory denoted by this abstract pathname that
        satisfy the specified filter.  The behavior of this method is the same
        as that of the .listFiles() method, except that the pathnames in
        the returned array must satisfy the filter.  If the given `filter`
        is `null` then all pathnames are accepted.  Otherwise, a pathname
        satisfies the filter if and only if the value `True` results when
        the FileFilter.accept FileFilter.accept(File) method of the
        filter is invoked on the pathname.

        Arguments
        - filter: A file filter

        Returns
        - An array of abstract pathnames denoting the files and
                 directories in the directory denoted by this abstract pathname.
                 The array will be empty if the directory is empty.  Returns
                 `null` if this abstract pathname does not denote a
                 directory, or if an I/O error occurs.

        Raises
        - SecurityException: If a security manager exists and its SecurityManager.checkRead(String) method denies read access to
                 the directory

        See
        - java.nio.file.Files.newDirectoryStream(Path,java.nio.file.DirectoryStream.Filter)

        Since
        - 1.2
        """
        ...


    def mkdir(self) -> bool:
        """
        Creates the directory named by this abstract pathname.

        Returns
        - `True` if and only if the directory was
                 created; `False` otherwise

        Raises
        - SecurityException: If a security manager exists and its java.lang.SecurityManager.checkWrite(java.lang.String)
                 method does not permit the named directory to be created
        """
        ...


    def mkdirs(self) -> bool:
        """
        Creates the directory named by this abstract pathname, including any
        necessary but nonexistent parent directories.  Note that if this
        operation fails it may have succeeded in creating some of the necessary
        parent directories.

        Returns
        - `True` if and only if the directory was created,
                 along with all necessary parent directories; `False`
                 otherwise

        Raises
        - SecurityException: If a security manager exists and its java.lang.SecurityManager.checkRead(java.lang.String)
                 method does not permit verification of the existence of the
                 named directory and all necessary parent directories; or if
                 the java.lang.SecurityManager.checkWrite(java.lang.String)
                 method does not permit the named directory and all necessary
                 parent directories to be created
        """
        ...


    def renameTo(self, dest: "File") -> bool:
        """
        Renames the file denoted by this abstract pathname.
        
         Many aspects of the behavior of this method are inherently
        platform-dependent: The rename operation might not be able to move a
        file from one filesystem to another, it might not be atomic, and it
        might not succeed if a file with the destination abstract pathname
        already exists.  The return value should always be checked to make sure
        that the rename operation was successful.  As instances of `File`
        are immutable, this File object is not changed to name the destination
        file or directory.
        
         Note that the java.nio.file.Files class defines the java.nio.file.Files.move move method to move or rename a file in a
        platform independent manner.

        Arguments
        - dest: The new abstract pathname for the named file

        Returns
        - `True` if and only if the renaming succeeded;
                 `False` otherwise

        Raises
        - SecurityException: If a security manager exists and its java.lang.SecurityManager.checkWrite(java.lang.String)
                 method denies write access to either the old or new pathnames
        - NullPointerException: If parameter `dest` is `null`
        """
        ...


    def setLastModified(self, time: int) -> bool:
        """
        Sets the last-modified time of the file or directory named by this
        abstract pathname.
        
         All platforms support file-modification times to the nearest second,
        but some provide more precision.  The argument will be truncated to fit
        the supported precision.  If the operation succeeds and no intervening
        operations on the file take place, then the next invocation of the
        .lastModified method will return the (possibly
        truncated) `time` argument that was passed to this method.

        Arguments
        - time: The new last-modified time, measured in milliseconds since
                      the epoch (00:00:00 GMT, January 1, 1970)

        Returns
        - `True` if and only if the operation succeeded;
                 `False` otherwise

        Raises
        - IllegalArgumentException: If the argument is negative
        - SecurityException: If a security manager exists and its java.lang.SecurityManager.checkWrite(java.lang.String)
                 method denies write access to the named file

        Since
        - 1.2
        """
        ...


    def setReadOnly(self) -> bool:
        """
        Marks the file or directory named by this abstract pathname so that
        only read operations are allowed. After invoking this method the file
        or directory will not change until it is either deleted or marked
        to allow write access. On some platforms it may be possible to start the
        Java virtual machine with special privileges that allow it to modify
        files that are marked read-only. Whether or not a read-only file or
        directory may be deleted depends upon the underlying system.

        Returns
        - `True` if and only if the operation succeeded;
                 `False` otherwise

        Raises
        - SecurityException: If a security manager exists and its java.lang.SecurityManager.checkWrite(java.lang.String)
                 method denies write access to the named file

        Since
        - 1.2
        """
        ...


    def setWritable(self, writable: bool, ownerOnly: bool) -> bool:
        """
        Sets the owner's or everybody's write permission for this abstract
        pathname. On some platforms it may be possible to start the Java virtual
        machine with special privileges that allow it to modify files that
        disallow write operations.
        
         The java.nio.file.Files class defines methods that operate on
        file attributes including file permissions. This may be used when finer
        manipulation of file permissions is required.

        Arguments
        - writable: If `True`, sets the access permission to allow write
                 operations; if `False` to disallow write operations
        - ownerOnly: If `True`, the write permission applies only to the
                 owner's write permission; otherwise, it applies to everybody.  If
                 the underlying file system can not distinguish the owner's write
                 permission from that of others, then the permission will apply to
                 everybody, regardless of this value.

        Returns
        - `True` if and only if the operation succeeded. The
                 operation will fail if the user does not have permission to change
                 the access permissions of this abstract pathname.

        Raises
        - SecurityException: If a security manager exists and its java.lang.SecurityManager.checkWrite(java.lang.String)
                 method denies write access to the named file

        Since
        - 1.6
        """
        ...


    def setWritable(self, writable: bool) -> bool:
        """
        A convenience method to set the owner's write permission for this abstract
        pathname. On some platforms it may be possible to start the Java virtual
        machine with special privileges that allow it to modify files that
        disallow write operations.
        
         An invocation of this method of the form `file.setWritable(arg)`
        behaves in exactly the same way as the invocation
        
        ````file.setWritable(arg, True)````

        Arguments
        - writable: If `True`, sets the access permission to allow write
                 operations; if `False` to disallow write operations

        Returns
        - `True` if and only if the operation succeeded.  The
                 operation will fail if the user does not have permission to
                 change the access permissions of this abstract pathname.

        Raises
        - SecurityException: If a security manager exists and its java.lang.SecurityManager.checkWrite(java.lang.String)
                 method denies write access to the file

        Since
        - 1.6
        """
        ...


    def setReadable(self, readable: bool, ownerOnly: bool) -> bool:
        """
        Sets the owner's or everybody's read permission for this abstract
        pathname. On some platforms it may be possible to start the Java virtual
        machine with special privileges that allow it to read files that are
        marked as unreadable.
        
         The java.nio.file.Files class defines methods that operate on
        file attributes including file permissions. This may be used when finer
        manipulation of file permissions is required.

        Arguments
        - readable: If `True`, sets the access permission to allow read
                 operations; if `False` to disallow read operations
        - ownerOnly: If `True`, the read permission applies only to the
                 owner's read permission; otherwise, it applies to everybody.  If
                 the underlying file system can not distinguish the owner's read
                 permission from that of others, then the permission will apply to
                 everybody, regardless of this value.

        Returns
        - `True` if and only if the operation succeeded.  The
                 operation will fail if the user does not have permission to
                 change the access permissions of this abstract pathname.  If
                 `readable` is `False` and the underlying
                 file system does not implement a read permission, then the
                 operation will fail.

        Raises
        - SecurityException: If a security manager exists and its java.lang.SecurityManager.checkWrite(java.lang.String)
                 method denies write access to the file

        Since
        - 1.6
        """
        ...


    def setReadable(self, readable: bool) -> bool:
        """
        A convenience method to set the owner's read permission for this abstract
        pathname. On some platforms it may be possible to start the Java virtual
        machine with special privileges that allow it to read files that are
        marked as unreadable.
        
        An invocation of this method of the form `file.setReadable(arg)`
        behaves in exactly the same way as the invocation
        
        ````file.setReadable(arg, True)````

        Arguments
        - readable: If `True`, sets the access permission to allow read
                 operations; if `False` to disallow read operations

        Returns
        - `True` if and only if the operation succeeded.  The
                 operation will fail if the user does not have permission to
                 change the access permissions of this abstract pathname.  If
                 `readable` is `False` and the underlying
                 file system does not implement a read permission, then the
                 operation will fail.

        Raises
        - SecurityException: If a security manager exists and its java.lang.SecurityManager.checkWrite(java.lang.String)
                 method denies write access to the file

        Since
        - 1.6
        """
        ...


    def setExecutable(self, executable: bool, ownerOnly: bool) -> bool:
        """
        Sets the owner's or everybody's execute permission for this abstract
        pathname. On some platforms it may be possible to start the Java virtual
        machine with special privileges that allow it to execute files that are
        not marked executable.
        
         The java.nio.file.Files class defines methods that operate on
        file attributes including file permissions. This may be used when finer
        manipulation of file permissions is required.

        Arguments
        - executable: If `True`, sets the access permission to allow execute
                 operations; if `False` to disallow execute operations
        - ownerOnly: If `True`, the execute permission applies only to the
                 owner's execute permission; otherwise, it applies to everybody.
                 If the underlying file system can not distinguish the owner's
                 execute permission from that of others, then the permission will
                 apply to everybody, regardless of this value.

        Returns
        - `True` if and only if the operation succeeded.  The
                 operation will fail if the user does not have permission to
                 change the access permissions of this abstract pathname.  If
                 `executable` is `False` and the underlying
                 file system does not implement an execute permission, then the
                 operation will fail.

        Raises
        - SecurityException: If a security manager exists and its java.lang.SecurityManager.checkWrite(java.lang.String)
                 method denies write access to the file

        Since
        - 1.6
        """
        ...


    def setExecutable(self, executable: bool) -> bool:
        """
        A convenience method to set the owner's execute permission for this
        abstract pathname. On some platforms it may be possible to start the Java
        virtual machine with special privileges that allow it to execute files
        that are not marked executable.
        
        An invocation of this method of the form `file.setExcutable(arg)`
        behaves in exactly the same way as the invocation
        
        ````file.setExecutable(arg, True)````

        Arguments
        - executable: If `True`, sets the access permission to allow execute
                 operations; if `False` to disallow execute operations

        Returns
        - `True` if and only if the operation succeeded.  The
                  operation will fail if the user does not have permission to
                  change the access permissions of this abstract pathname.  If
                  `executable` is `False` and the underlying
                  file system does not implement an execute permission, then the
                  operation will fail.

        Raises
        - SecurityException: If a security manager exists and its java.lang.SecurityManager.checkWrite(java.lang.String)
                 method denies write access to the file

        Since
        - 1.6
        """
        ...


    def canExecute(self) -> bool:
        """
        Tests whether the application can execute the file denoted by this
        abstract pathname. On some platforms it may be possible to start the
        Java virtual machine with special privileges that allow it to execute
        files that are not marked executable. Consequently this method may return
        `True` even though the file does not have execute permissions.

        Returns
        - `True` if and only if the abstract pathname exists
                 *and* the application is allowed to execute the file

        Raises
        - SecurityException: If a security manager exists and its java.lang.SecurityManager.checkExec(java.lang.String)
                 method denies execute access to the file

        Since
        - 1.6
        """
        ...


    @staticmethod
    def listRoots() -> list["File"]:
        """
        List the available filesystem roots.
        
         A particular Java platform may support zero or more
        hierarchically-organized file systems.  Each file system has a
        `root` directory from which all other files in that file system
        can be reached.  Windows platforms, for example, have a root directory
        for each active drive; UNIX platforms have a single root directory,
        namely `"/"`.  The set of available filesystem roots is affected
        by various system-level operations such as the insertion or ejection of
        removable media and the disconnecting or unmounting of physical or
        virtual disk drives.
        
         This method returns an array of `File` objects that denote the
        root directories of the available filesystem roots.  It is guaranteed
        that the canonical pathname of any file physically present on the local
        machine will begin with one of the roots returned by this method.
        
         The canonical pathname of a file that resides on some other machine
        and is accessed via a remote-filesystem protocol such as SMB or NFS may
        or may not begin with one of the roots returned by this method.  If the
        pathname of a remote file is syntactically indistinguishable from the
        pathname of a local file then it will begin with one of the roots
        returned by this method.  Thus, for example, `File` objects
        denoting the root directories of the mapped network drives of a Windows
        platform will be returned by this method, while `File` objects
        containing UNC pathnames will not be returned by this method.
        
         Unlike most methods in this class, this method does not throw
        security exceptions.  If a security manager exists and its SecurityManager.checkRead(String) method denies read access to a
        particular root directory, then that directory will not appear in the
        result.

        Returns
        - An array of `File` objects denoting the available
                 filesystem roots, or `null` if the set of roots could not
                 be determined.  The array will be empty if there are no
                 filesystem roots.

        See
        - java.nio.file.FileStore

        Since
        - 1.2
        """
        ...


    def getTotalSpace(self) -> int:
        """
        Returns the size of the partition <a href="#partName">named</a> by this
        abstract pathname. If the total number of bytes in the partition is
        greater than Long.MAX_VALUE, then `Long.MAX_VALUE` will be
        returned.

        Returns
        - The size, in bytes, of the partition or `0L` if this
                 abstract pathname does not name a partition or if the size
                 cannot be obtained

        Raises
        - SecurityException: If a security manager has been installed and it denies
                 RuntimePermission`("getFileSystemAttributes")`
                 or its SecurityManager.checkRead(String) method denies
                 read access to the file named by this abstract pathname

        See
        - FileStore.getTotalSpace

        Since
        - 1.6
        """
        ...


    def getFreeSpace(self) -> int:
        """
        Returns the number of unallocated bytes in the partition <a
        href="#partName">named</a> by this abstract path name.  If the
        number of unallocated bytes in the partition is greater than
        Long.MAX_VALUE, then `Long.MAX_VALUE` will be returned.
        
         The returned number of unallocated bytes is a hint, but not
        a guarantee, that it is possible to use most or any of these
        bytes.  The number of unallocated bytes is most likely to be
        accurate immediately after this call.  It is likely to be made
        inaccurate by any external I/O operations including those made
        on the system outside of this virtual machine.  This method
        makes no guarantee that write operations to this file system
        will succeed.

        Returns
        - The number of unallocated bytes on the partition or `0L`
                 if the abstract pathname does not name a partition or if this
                 number cannot be obtained.  This value will be less than or
                 equal to the total file system size returned by
                 .getTotalSpace.

        Raises
        - SecurityException: If a security manager has been installed and it denies
                 RuntimePermission`("getFileSystemAttributes")`
                 or its SecurityManager.checkRead(String) method denies
                 read access to the file named by this abstract pathname

        See
        - FileStore.getUnallocatedSpace

        Since
        - 1.6
        """
        ...


    def getUsableSpace(self) -> int:
        """
        Returns the number of bytes available to this virtual machine on the
        partition <a href="#partName">named</a> by this abstract pathname.  If
        the number of available bytes in the partition is greater than
        Long.MAX_VALUE, then `Long.MAX_VALUE` will be returned.
        When possible, this method checks for write permissions and other
        operating system restrictions and will therefore usually provide a more
        accurate estimate of how much new data can actually be written than
        .getFreeSpace.
        
         The returned number of available bytes is a hint, but not a
        guarantee, that it is possible to use most or any of these bytes.  The
        number of available bytes is most likely to be accurate immediately
        after this call.  It is likely to be made inaccurate by any external
        I/O operations including those made on the system outside of this
        virtual machine.  This method makes no guarantee that write operations
        to this file system will succeed.

        Returns
        - The number of available bytes on the partition or `0L`
                 if the abstract pathname does not name a partition or if this
                 number cannot be obtained.  On systems where this information
                 is not available, this method will be equivalent to a call to
                 .getFreeSpace.

        Raises
        - SecurityException: If a security manager has been installed and it denies
                 RuntimePermission`("getFileSystemAttributes")`
                 or its SecurityManager.checkRead(String) method denies
                 read access to the file named by this abstract pathname

        See
        - FileStore.getUsableSpace

        Since
        - 1.6
        """
        ...


    @staticmethod
    def createTempFile(prefix: str, suffix: str, directory: "File") -> "File":
        """
         Creates a new empty file in the specified directory, using the
        given prefix and suffix strings to generate its name.  If this method
        returns successfully then it is guaranteed that:
        
        <ol>
        -  The file denoted by the returned abstract pathname did not exist
             before this method was invoked, and
        -  Neither this method nor any of its variants will return the same
             abstract pathname again in the current invocation of the virtual
             machine.
        </ol>
        
        This method provides only part of a temporary-file facility.  To arrange
        for a file created by this method to be deleted automatically, use the
        .deleteOnExit method.
        
         The `prefix` argument must be at least three characters
        long.  It is recommended that the prefix be a short, meaningful string
        such as `"hjb"` or `"mail"`.  The
        `suffix` argument may be `null`, in which case the
        suffix `".tmp"` will be used.
        
         To create the new file, the prefix and the suffix may first be
        adjusted to fit the limitations of the underlying platform.  If the
        prefix is too long then it will be truncated, but its first three
        characters will always be preserved.  If the suffix is too long then it
        too will be truncated, but if it begins with a period character
        (`'.'`) then the period and the first three characters
        following it will always be preserved.  Once these adjustments have been
        made the name of the new file will be generated by concatenating the
        prefix, five or more internally-generated characters, and the suffix.
        
         If the `directory` argument is `null` then the
        system-dependent default temporary-file directory will be used.  The
        default temporary-file directory is specified by the system property
        `java.io.tmpdir`.  On UNIX systems the default value of this
        property is typically `"/tmp"` or `"/var/tmp"`; on
        Microsoft Windows systems it is typically `"C:\\WINNT\\TEMP"`.  A different
        value may be given to this system property when the Java virtual machine
        is invoked, but programmatic changes to this property are not guaranteed
        to have any effect upon the temporary directory used by this method.

        Arguments
        - prefix: The prefix string to be used in generating the file's
                           name; must be at least three characters long
        - suffix: The suffix string to be used in generating the file's
                           name; may be `null`, in which case the
                           suffix `".tmp"` will be used
        - directory: The directory in which the file is to be created, or
                           `null` if the default temporary-file
                           directory is to be used

        Returns
        - An abstract pathname denoting a newly-created empty file

        Raises
        - IllegalArgumentException: If the `prefix` argument contains fewer than three
                 characters
        - IOException: If a file could not be created
        - SecurityException: If a security manager exists and its java.lang.SecurityManager.checkWrite(java.lang.String)
                 method does not allow a file to be created

        Since
        - 1.2
        """
        ...


    @staticmethod
    def createTempFile(prefix: str, suffix: str) -> "File":
        """
        Creates an empty file in the default temporary-file directory, using
        the given prefix and suffix to generate its name. Invoking this method
        is equivalent to invoking .createTempFile(java.lang.String,
        java.lang.String, java.io.File)
        createTempFile(prefix,&nbsp;suffix,&nbsp;null).
        
         The java.nio.file.Files.createTempFile(String,String,java.nio.file.attribute.FileAttribute[])
        Files.createTempFile method provides an alternative method to create an
        empty file in the temporary-file directory. Files created by that method
        may have more restrictive access permissions to files created by this
        method and so may be more suited to security-sensitive applications.

        Arguments
        - prefix: The prefix string to be used in generating the file's
                           name; must be at least three characters long
        - suffix: The suffix string to be used in generating the file's
                           name; may be `null`, in which case the
                           suffix `".tmp"` will be used

        Returns
        - An abstract pathname denoting a newly-created empty file

        Raises
        - IllegalArgumentException: If the `prefix` argument contains fewer than three
                 characters
        - IOException: If a file could not be created
        - SecurityException: If a security manager exists and its java.lang.SecurityManager.checkWrite(java.lang.String)
                 method does not allow a file to be created

        See
        - java.nio.file.Files.createTempDirectory(String,FileAttribute[])

        Since
        - 1.2
        """
        ...


    def compareTo(self, pathname: "File") -> int:
        """
        Compares two abstract pathnames lexicographically.  The ordering
        defined by this method depends upon the underlying system.  On UNIX
        systems, alphabetic case is significant in comparing pathnames; on
        Microsoft Windows systems it is not.

        Arguments
        - pathname: The abstract pathname to be compared to this abstract
                           pathname

        Returns
        - Zero if the argument is equal to this abstract pathname, a
                 value less than zero if this abstract pathname is
                 lexicographically less than the argument, or a value greater
                 than zero if this abstract pathname is lexicographically
                 greater than the argument

        Since
        - 1.2
        """
        ...


    def equals(self, obj: "Object") -> bool:
        """
        Tests this abstract pathname for equality with the given object.
        Returns `True` if and only if the argument is not
        `null` and is an abstract pathname that is the same as this
        abstract pathname.  Whether or not two abstract
        pathnames are equal depends upon the underlying operating system.
        On UNIX systems, alphabetic case is significant in comparing pathnames;
        on Microsoft Windows systems it is not.

        Arguments
        - obj: The object to be compared with this abstract pathname

        Returns
        - `True` if and only if the objects are the same;
                 `False` otherwise

        See
        - java.nio.file.Files.isSameFile(Path,Path)

        Unknown Tags
        - This method only tests whether the abstract pathnames are equal;
                 it does not access the file system and the file is not required
                 to exist.
        """
        ...


    def hashCode(self) -> int:
        """
        Computes a hash code for this abstract pathname.  Because equality of
        abstract pathnames is inherently system-dependent, so is the computation
        of their hash codes.  On UNIX systems, the hash code of an abstract
        pathname is equal to the exclusive *or* of the hash code
        of its pathname string and the decimal value
        `1234321`.  On Microsoft Windows systems, the hash
        code is equal to the exclusive *or* of the hash code of
        its pathname string converted to lower case and the decimal
        value `1234321`.  Locale is not taken into account on
        lowercasing the pathname string.

        Returns
        - A hash code for this abstract pathname
        """
        ...


    def toString(self) -> str:
        """
        Returns the pathname string of this abstract pathname.  This is just the
        string returned by the .getPath method.

        Returns
        - The string form of this abstract pathname
        """
        ...


    def toPath(self) -> "Path":
        """
        Returns a Path java.nio.file.Path object constructed from
        this abstract path. The resulting `Path` is associated with the
        java.nio.file.FileSystems.getDefault default-filesystem.
        
         The first invocation of this method works as if invoking it were
        equivalent to evaluating the expression:
        <blockquote>```
        java.nio.file.FileSystems.getDefault FileSystems.getDefault().java.nio.file.FileSystem.getPath getPath(this..getPath getPath());
        ```</blockquote>
        Subsequent invocations of this method return the same `Path`.
        
         If this abstract pathname is the empty abstract pathname then this
        method returns a `Path` that may be used to access the current
        user directory.

        Returns
        - a `Path` constructed from this abstract path

        Raises
        - java.nio.file.InvalidPathException: if a `Path` object cannot be constructed from the abstract
                 path (see java.nio.file.FileSystem.getPath FileSystem.getPath)

        See
        - Path.toFile

        Since
        - 1.7
        """
        ...
