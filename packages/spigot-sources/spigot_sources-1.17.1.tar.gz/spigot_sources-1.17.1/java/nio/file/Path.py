"""
Python module generated from Java source file java.nio.file.Path

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import File
from java.io import IOException
from java.net import URI
from java.nio.file import *
from java.nio.file.spi import FileSystemProvider
from java.util import Iterator
from java.util import NoSuchElementException
from typing import Any, Callable, Iterable, Tuple


class Path(Comparable, Iterable, Watchable):

    @staticmethod
    def of(first: str, *more: Tuple[str, ...]) -> "Path":
        """
        Returns a `Path` by converting a path string, or a sequence of
        strings that when joined form a path string. If `more` does not
        specify any elements then the value of the `first` parameter is
        the path string to convert. If `more` specifies one or more
        elements then each non-empty string, including `first`, is
        considered to be a sequence of name elements and is joined to form a
        path string. The details as to how the Strings are joined is provider
        specific but typically they will be joined using the
        FileSystem.getSeparator name-separator as the separator.
        For example, if the name separator is "`/`" and
        `getPath("/foo","bar","gus")` is invoked, then the path string
        `"/foo/bar/gus"` is converted to a `Path`. A `Path`
        representing an empty path is returned if `first` is the empty
        string and `more` does not contain any non-empty strings.
        
         The `Path` is obtained by invoking the FileSystem.getPath
        getPath method of the FileSystems.getDefault default FileSystem.
        
         Note that while this method is very convenient, using it will imply
        an assumed reference to the default `FileSystem` and limit the
        utility of the calling code. Hence it should not be used in library code
        intended for flexible reuse. A more flexible alternative is to use an
        existing `Path` instance as an anchor, such as:
        ````Path dir = ...
            Path path = dir.resolve("file");````

        Arguments
        - first: the path string or initial part of the path string
        - more: additional strings to be joined to form the path string

        Returns
        - the resulting `Path`

        Raises
        - InvalidPathException: if the path string cannot be converted to a `Path`

        See
        - FileSystem.getPath

        Since
        - 11
        """
        ...


    @staticmethod
    def of(uri: "URI") -> "Path":
        """
        Returns a `Path` by converting a URI.
        
         This method iterates over the FileSystemProvider.installedProviders()
        installed providers to locate the provider that is identified by the
        URI URI.getScheme scheme of the given URI. URI schemes are
        compared without regard to case. If the provider is found then its FileSystemProvider.getPath getPath method is invoked to convert the
        URI.
        
         In the case of the default provider, identified by the URI scheme
        "file", the given URI has a non-empty path component, and undefined query
        and fragment components. Whether the authority component may be present
        is platform specific. The returned `Path` is associated with the
        FileSystems.getDefault default file system.
        
         The default provider provides a similar *round-trip* guarantee
        to the java.io.File class. For a given `Path` *p* it
        is guaranteed that
        <blockquote>`Path.of(`*p*`.`Path.toUri() toUri`()).equals(`
        *p*`.`Path.toAbsolutePath() toAbsolutePath`())`
        </blockquote>
        so long as the original `Path`, the `URI`, and the new `Path` are all created in (possibly different invocations of) the same
        Java virtual machine. Whether other providers make any guarantees is
        provider specific and therefore unspecified.

        Arguments
        - uri: the URI to convert

        Returns
        - the resulting `Path`

        Raises
        - IllegalArgumentException: if preconditions on the `uri` parameter do not hold. The
                 format of the URI is provider specific.
        - FileSystemNotFoundException: The file system, identified by the URI, does not exist and
                 cannot be created automatically, or the provider identified by
                 the URI's scheme component is not installed
        - SecurityException: if a security manager is installed and it denies an unspecified
                 permission to access the file system

        Since
        - 11
        """
        ...


    def getFileSystem(self) -> "FileSystem":
        """
        Returns the file system that created this object.

        Returns
        - the file system that created this object
        """
        ...


    def isAbsolute(self) -> bool:
        """
        Tells whether or not this path is absolute.
        
         An absolute path is complete in that it doesn't need to be combined
        with other path information in order to locate a file.

        Returns
        - `True` if, and only if, this path is absolute
        """
        ...


    def getRoot(self) -> "Path":
        """
        Returns the root component of this path as a `Path` object,
        or `null` if this path does not have a root component.

        Returns
        - a path representing the root component of this path,
                 or `null`
        """
        ...


    def getFileName(self) -> "Path":
        """
        Returns the name of the file or directory denoted by this path as a
        `Path` object. The file name is the *farthest* element from
        the root in the directory hierarchy.

        Returns
        - a path representing the name of the file or directory, or
                 `null` if this path has zero elements
        """
        ...


    def getParent(self) -> "Path":
        """
        Returns the *parent path*, or `null` if this path does not
        have a parent.
        
         The parent of this path object consists of this path's root
        component, if any, and each element in the path except for the
        *farthest* from the root in the directory hierarchy. This method
        does not access the file system; the path or its parent may not exist.
        Furthermore, this method does not eliminate special names such as "."
        and ".." that may be used in some implementations. On UNIX for example,
        the parent of "`/a/b/c`" is "`/a/b`", and the parent of
        `"x/y/.`" is "`x/y`". This method may be used with the .normalize normalize method, to eliminate redundant names, for cases where
        *shell-like* navigation is required.
        
         If this path has more than one element, and no root component, then
        this method is equivalent to evaluating the expression:
        <blockquote>```
        subpath(0,&nbsp;getNameCount()-1);
        ```</blockquote>

        Returns
        - a path representing the path's parent
        """
        ...


    def getNameCount(self) -> int:
        """
        Returns the number of name elements in the path.

        Returns
        - the number of elements in the path, or `0` if this path
                 only represents a root component
        """
        ...


    def getName(self, index: int) -> "Path":
        """
        Returns a name element of this path as a `Path` object.
        
         The `index` parameter is the index of the name element to return.
        The element that is *closest* to the root in the directory hierarchy
        has index `0`. The element that is *farthest* from the root
        has index .getNameCount count`-1`.

        Arguments
        - index: the index of the element

        Returns
        - the name element

        Raises
        - IllegalArgumentException: if `index` is negative, `index` is greater than or
                 equal to the number of elements, or this path has zero name
                 elements
        """
        ...


    def subpath(self, beginIndex: int, endIndex: int) -> "Path":
        """
        Returns a relative `Path` that is a subsequence of the name
        elements of this path.
        
         The `beginIndex` and `endIndex` parameters specify the
        subsequence of name elements. The name that is *closest* to the root
        in the directory hierarchy has index `0`. The name that is
        *farthest* from the root has index .getNameCount
        count`-1`. The returned `Path` object has the name elements
        that begin at `beginIndex` and extend to the element at index `endIndex-1`.

        Arguments
        - beginIndex: the index of the first element, inclusive
        - endIndex: the index of the last element, exclusive

        Returns
        - a new `Path` object that is a subsequence of the name
                 elements in this `Path`

        Raises
        - IllegalArgumentException: if `beginIndex` is negative, or greater than or equal to
                 the number of elements. If `endIndex` is less than or
                 equal to `beginIndex`, or larger than the number of elements.
        """
        ...


    def startsWith(self, other: "Path") -> bool:
        """
        Tests if this path starts with the given path.
        
         This path *starts* with the given path if this path's root
        component *starts* with the root component of the given path,
        and this path starts with the same name elements as the given path.
        If the given path has more name elements than this path then `False`
        is returned.
        
         Whether or not the root component of this path starts with the root
        component of the given path is file system specific. If this path does
        not have a root component and the given path has a root component then
        this path does not start with the given path.
        
         If the given path is associated with a different `FileSystem`
        to this path then `False` is returned.

        Arguments
        - other: the given path

        Returns
        - `True` if this path starts with the given path; otherwise
                 `False`
        """
        ...


    def startsWith(self, other: str) -> bool:
        """
        Tests if this path starts with a `Path`, constructed by converting
        the given path string, in exactly the manner specified by the .startsWith(Path) startsWith(Path) method. On UNIX for example, the path
        "`foo/bar`" starts with "`foo`" and "`foo/bar`". It
        does not start with "`f`" or "`fo`".

        Arguments
        - other: the given path string

        Returns
        - `True` if this path starts with the given path; otherwise
                 `False`

        Raises
        - InvalidPathException: If the path string cannot be converted to a Path.

        Unknown Tags
        - The default implementation is equivalent for this path to:
        ````startsWith(getFileSystem().getPath(other));````
        """
        ...


    def endsWith(self, other: "Path") -> bool:
        """
        Tests if this path ends with the given path.
        
         If the given path has *N* elements, and no root component,
        and this path has *N* or more elements, then this path ends with
        the given path if the last *N* elements of each path, starting at
        the element farthest from the root, are equal.
        
         If the given path has a root component then this path ends with the
        given path if the root component of this path *ends with* the root
        component of the given path, and the corresponding elements of both paths
        are equal. Whether or not the root component of this path ends with the
        root component of the given path is file system specific. If this path
        does not have a root component and the given path has a root component
        then this path does not end with the given path.
        
         If the given path is associated with a different `FileSystem`
        to this path then `False` is returned.

        Arguments
        - other: the given path

        Returns
        - `True` if this path ends with the given path; otherwise
                 `False`
        """
        ...


    def endsWith(self, other: str) -> bool:
        """
        Tests if this path ends with a `Path`, constructed by converting
        the given path string, in exactly the manner specified by the .endsWith(Path) endsWith(Path) method. On UNIX for example, the path
        "`foo/bar`" ends with "`foo/bar`" and "`bar`". It does
        not end with "`r`" or "`/bar`". Note that trailing separators
        are not taken into account, and so invoking this method on the `Path`"`foo/bar`" with the `String` "`bar/`" returns
        `True`.

        Arguments
        - other: the given path string

        Returns
        - `True` if this path ends with the given path; otherwise
                 `False`

        Raises
        - InvalidPathException: If the path string cannot be converted to a Path.

        Unknown Tags
        - The default implementation is equivalent for this path to:
        ````endsWith(getFileSystem().getPath(other));````
        """
        ...


    def normalize(self) -> "Path":
        """
        Returns a path that is this path with redundant name elements eliminated.
        
         The precise definition of this method is implementation dependent but
        in general it derives from this path, a path that does not contain
        *redundant* name elements. In many file systems, the "`.`"
        and "`..`" are special names used to indicate the current directory
        and parent directory. In such file systems all occurrences of "`.`"
        are considered redundant. If a "`..`" is preceded by a
        non-"`..`" name then both names are considered redundant (the
        process to identify such names is repeated until it is no longer
        applicable).
        
         This method does not access the file system; the path may not locate
        a file that exists. Eliminating "`..`" and a preceding name from a
        path may result in the path that locates a different file than the original
        path. This can arise when the preceding name is a symbolic link.

        Returns
        - the resulting path or this path if it does not contain
                 redundant name elements; an empty path is returned if this path
                 does not have a root component and all name elements are redundant

        See
        - .toRealPath
        """
        ...


    def resolve(self, other: "Path") -> "Path":
        """
        Resolve the given path against this path.
        
         If the `other` parameter is an .isAbsolute() absolute
        path then this method trivially returns `other`. If `other`
        is an *empty path* then this method trivially returns this path.
        Otherwise this method considers this path to be a directory and resolves
        the given path against this path. In the simplest case, the given path
        does not have a .getRoot root component, in which case this method
        *joins* the given path to this path and returns a resulting path
        that .endsWith ends with the given path. Where the given path has
        a root component then resolution is highly implementation dependent and
        therefore unspecified.

        Arguments
        - other: the path to resolve against this path

        Returns
        - the resulting path

        See
        - .relativize
        """
        ...


    def resolve(self, other: str) -> "Path":
        """
        Converts a given path string to a `Path` and resolves it against
        this `Path` in exactly the manner specified by the .resolve(Path) resolve method. For example, suppose that the name
        separator is "`/`" and a path represents "`foo/bar`", then
        invoking this method with the path string "`gus`" will result in
        the `Path` "`foo/bar/gus`".

        Arguments
        - other: the path string to resolve against this path

        Returns
        - the resulting path

        Raises
        - InvalidPathException: if the path string cannot be converted to a Path.

        See
        - FileSystem.getPath

        Unknown Tags
        - The default implementation is equivalent for this path to:
        ````resolve(getFileSystem().getPath(other));````
        """
        ...


    def resolveSibling(self, other: "Path") -> "Path":
        """
        Resolves the given path against this path's .getParent parent
        path. This is useful where a file name needs to be *replaced* with
        another file name. For example, suppose that the name separator is
        "`/`" and a path represents "`dir1/dir2/foo`", then invoking
        this method with the `Path` "`bar`" will result in the `Path` "`dir1/dir2/bar`". If this path does not have a parent path,
        or `other` is .isAbsolute() absolute, then this method
        returns `other`. If `other` is an empty path then this method
        returns this path's parent, or where this path doesn't have a parent, the
        empty path.

        Arguments
        - other: the path to resolve against this path's parent

        Returns
        - the resulting path

        See
        - .resolve(Path)

        Unknown Tags
        - The default implementation is equivalent for this path to:
        ````(getParent() == null) ? other : getParent().resolve(other);````
        unless `other == null`, in which case a
        `NullPointerException` is thrown.
        """
        ...


    def resolveSibling(self, other: str) -> "Path":
        """
        Converts a given path string to a `Path` and resolves it against
        this path's .getParent parent path in exactly the manner
        specified by the .resolveSibling(Path) resolveSibling method.

        Arguments
        - other: the path string to resolve against this path's parent

        Returns
        - the resulting path

        Raises
        - InvalidPathException: if the path string cannot be converted to a Path.

        See
        - FileSystem.getPath

        Unknown Tags
        - The default implementation is equivalent for this path to:
        ````resolveSibling(getFileSystem().getPath(other));````
        """
        ...


    def relativize(self, other: "Path") -> "Path":
        """
        Constructs a relative path between this path and a given path.
        
         Relativization is the inverse of .resolve(Path) resolution.
        This method attempts to construct a .isAbsolute relative path
        that when .resolve(Path) resolved against this path, yields a
        path that locates the same file as the given path. For example, on UNIX,
        if this path is `"/a/b"` and the given path is `"/a/b/c/d"`
        then the resulting relative path would be `"c/d"`. Where this
        path and the given path do not have a .getRoot root component,
        then a relative path can be constructed. A relative path cannot be
        constructed if only one of the paths have a root component. Where both
        paths have a root component then it is implementation dependent if a
        relative path can be constructed. If this path and the given path are
        .equals equal then an *empty path* is returned.
        
         For any two .normalize normalized paths *p* and
        *q*, where *q* does not have a root component,
        <blockquote>
          *p*`.relativize(`*p*
          `.resolve(`*q*`)).equals(`*q*`)`
        </blockquote>
        
         When symbolic links are supported, then whether the resulting path,
        when resolved against this path, yields a path that can be used to locate
        the Files.isSameFile same file as `other` is implementation
        dependent. For example, if this path is  `"/a/b"` and the given
        path is `"/a/x"` then the resulting relative path may be `"../x"`. If `"b"` is a symbolic link then is implementation
        dependent if `"a/b/../x"` would locate the same file as `"/a/x"`.

        Arguments
        - other: the path to relativize against this path

        Returns
        - the resulting relative path, or an empty path if both paths are
                 equal

        Raises
        - IllegalArgumentException: if `other` is not a `Path` that can be relativized
                 against this path
        """
        ...


    def toUri(self) -> "URI":
        """
        Returns a URI to represent this path.
        
         This method constructs an absolute URI with a URI.getScheme() scheme equal to the URI scheme that identifies the
        provider. The exact form of the scheme specific part is highly provider
        dependent.
        
         In the case of the default provider, the URI is hierarchical with
        a URI.getPath() path component that is absolute. The query and
        fragment components are undefined. Whether the authority component is
        defined or not is implementation dependent. There is no guarantee that
        the `URI` may be used to construct a java.io.File java.io.File.
        In particular, if this path represents a Universal Naming Convention (UNC)
        path, then the UNC server name may be encoded in the authority component
        of the resulting URI. In the case of the default provider, and the file
        exists, and it can be determined that the file is a directory, then the
        resulting `URI` will end with a slash.
        
         The default provider provides a similar *round-trip* guarantee
        to the java.io.File class. For a given `Path` *p* it
        is guaranteed that
        <blockquote>
        Path.of(URI) Path.of`(`*p*`.toUri()).equals(`*p*
        `.`.toAbsolutePath() toAbsolutePath`())`
        </blockquote>
        so long as the original `Path`, the `URI`, and the new `Path` are all created in (possibly different invocations of) the same
        Java virtual machine. Whether other providers make any guarantees is
        provider specific and therefore unspecified.
        
         When a file system is constructed to access the contents of a file
        as a file system then it is highly implementation specific if the returned
        URI represents the given path in the file system or it represents a
        *compound* URI that encodes the URI of the enclosing file system.
        A format for compound URIs is not defined in this release; such a scheme
        may be added in a future release.

        Returns
        - the URI representing this path

        Raises
        - java.io.IOError: if an I/O error occurs obtaining the absolute path, or where a
                 file system is constructed to access the contents of a file as
                 a file system, and the URI of the enclosing file system cannot be
                 obtained
        - SecurityException: In the case of the default provider, and a security manager
                 is installed, the .toAbsolutePath toAbsolutePath method
                 throws a security exception.
        """
        ...


    def toAbsolutePath(self) -> "Path":
        """
        Returns a `Path` object representing the absolute path of this
        path.
        
         If this path is already Path.isAbsolute absolute then this
        method simply returns this path. Otherwise, this method resolves the path
        in an implementation dependent manner, typically by resolving the path
        against a file system default directory. Depending on the implementation,
        this method may throw an I/O error if the file system is not accessible.

        Returns
        - a `Path` object representing the absolute path

        Raises
        - java.io.IOError: if an I/O error occurs
        - SecurityException: In the case of the default provider, a security manager
                 is installed, and this path is not absolute, then the security
                 manager's SecurityManager.checkPropertyAccess(String)
                 checkPropertyAccess method is invoked to check access to the
                 system property `user.dir`
        """
        ...


    def toRealPath(self, *options: Tuple["LinkOption", ...]) -> "Path":
        """
        Returns the *real* path of an existing file.
        
         The precise definition of this method is implementation dependent but
        in general it derives from this path, an .isAbsolute absolute
        path that locates the Files.isSameFile same file as this path, but
        with name elements that represent the actual name of the directories
        and the file. For example, where filename comparisons on a file system
        are case insensitive then the name elements represent the names in their
        actual case. Additionally, the resulting path has redundant name
        elements removed.
        
         If this path is relative then its absolute path is first obtained,
        as if by invoking the .toAbsolutePath toAbsolutePath method.
        
         The `options` array may be used to indicate how symbolic links
        are handled. By default, symbolic links are resolved to their final
        target. If the option LinkOption.NOFOLLOW_LINKS NOFOLLOW_LINKS is
        present then this method does not resolve symbolic links.
        
        Some implementations allow special names such as "`..`" to refer to
        the parent directory. When deriving the *real path*, and a
        "`..`" (or equivalent) is preceded by a non-"`..`" name then
        an implementation will typically cause both names to be removed. When
        not resolving symbolic links and the preceding name is a symbolic link
        then the names are only removed if it guaranteed that the resulting path
        will locate the same file as this path.

        Arguments
        - options: options indicating how symbolic links are handled

        Returns
        - an absolute path represent the *real* path of the file
                 located by this object

        Raises
        - IOException: if the file does not exist or an I/O error occurs
        - SecurityException: In the case of the default provider, and a security manager
                 is installed, its SecurityManager.checkRead(String) checkRead
                 method is invoked to check read access to the file, and where
                 this path is not absolute, its SecurityManager.checkPropertyAccess(String)
                 checkPropertyAccess method is invoked to check access to the
                 system property `user.dir`
        """
        ...


    def toFile(self) -> "File":
        """
        Returns a File object representing this path. Where this `Path` is associated with the default provider, then this method is
        equivalent to returning a `File` object constructed with the
        `String` representation of this path.
        
         If this path was created by invoking the `File` File.toPath toPath method then there is no guarantee that the `File` object returned by this method is .equals equal to the
        original `File`.

        Returns
        - a `File` object representing this path

        Raises
        - UnsupportedOperationException: if this `Path` is not associated with the default provider

        Unknown Tags
        - The default implementation is equivalent for this path to:
        ````new File(toString());````
        if the `FileSystem` which created this `Path` is the default
        file system; otherwise an `UnsupportedOperationException` is
        thrown.
        """
        ...


    def register(self, watcher: "WatchService", events: list["WatchEvent.Kind"[Any]], *modifiers: Tuple["WatchEvent.Modifier", ...]) -> "WatchKey":
        """
        Registers the file located by this path with a watch service.
        
         In this release, this path locates a directory that exists. The
        directory is registered with the watch service so that entries in the
        directory can be watched. The `events` parameter is the events to
        register and may contain the following events:
        
          - StandardWatchEventKinds.ENTRY_CREATE ENTRY_CREATE -
              entry created or moved into the directory
          - StandardWatchEventKinds.ENTRY_DELETE ENTRY_DELETE -
               entry deleted or moved out of the directory
          - StandardWatchEventKinds.ENTRY_MODIFY ENTRY_MODIFY -
               entry in directory was modified
        
        
         The WatchEvent.context context for these events is the
        relative path between the directory located by this path, and the path
        that locates the directory entry that is created, deleted, or modified.
        
         The set of events may include additional implementation specific
        event that are not defined by the enum StandardWatchEventKinds
        
         The `modifiers` parameter specifies *modifiers* that
        qualify how the directory is registered. This release does not define any
        *standard* modifiers. It may contain implementation specific
        modifiers.
        
         Where a file is registered with a watch service by means of a symbolic
        link then it is implementation specific if the watch continues to depend
        on the existence of the symbolic link after it is registered.

        Arguments
        - watcher: the watch service to which this object is to be registered
        - events: the events for which this object should be registered
        - modifiers: the modifiers, if any, that modify how the object is registered

        Returns
        - a key representing the registration of this object with the
                 given watch service

        Raises
        - UnsupportedOperationException: if unsupported events or modifiers are specified
        - IllegalArgumentException: if an invalid combination of events or modifiers is specified
        - ClosedWatchServiceException: if the watch service is closed
        - NotDirectoryException: if the file is registered to watch the entries in a directory
                 and the file is not a directory  *(optional specific exception)*
        - IOException: if an I/O error occurs
        - SecurityException: In the case of the default provider, and a security manager is
                 installed, the SecurityManager.checkRead(String) checkRead
                 method is invoked to check read access to the file.
        """
        ...


    def register(self, watcher: "WatchService", *events: Tuple["WatchEvent.Kind"[Any], ...]) -> "WatchKey":
        """
        Registers the file located by this path with a watch service.
        
         An invocation of this method behaves in exactly the same way as the
        invocation
        ```
            watchable..register(WatchService,WatchEvent.Kind[],WatchEvent.Modifier[]) register(watcher, events, new WatchEvent.Modifier[0]);
        ```
        
         **Usage Example:**
        Suppose we wish to register a directory for entry create, delete, and modify
        events:
        ```
            Path dir = ...
            WatchService watcher = ...
        
            WatchKey key = dir.register(watcher, ENTRY_CREATE, ENTRY_DELETE, ENTRY_MODIFY);
        ```

        Arguments
        - watcher: The watch service to which this object is to be registered
        - events: The events for which this object should be registered

        Returns
        - A key representing the registration of this object with the
                 given watch service

        Raises
        - UnsupportedOperationException: If unsupported events are specified
        - IllegalArgumentException: If an invalid combination of events is specified
        - ClosedWatchServiceException: If the watch service is closed
        - NotDirectoryException: If the file is registered to watch the entries in a directory
                 and the file is not a directory  *(optional specific exception)*
        - IOException: If an I/O error occurs
        - SecurityException: In the case of the default provider, and a security manager is
                 installed, the SecurityManager.checkRead(String) checkRead
                 method is invoked to check read access to the file.

        Unknown Tags
        - The default implementation is equivalent for this path to:
        ````register(watcher, events, new WatchEvent.Modifier[0]);````
        """
        ...


    def iterator(self) -> Iterator["Path"]:
        """
        Returns an iterator over the name elements of this path.
        
         The first element returned by the iterator represents the name
        element that is closest to the root in the directory hierarchy, the
        second element is the next closest, and so on. The last element returned
        is the name of the file or directory denoted by this path. The .getRoot root component, if present, is not returned by the iterator.

        Returns
        - an iterator over the name elements of this path.

        Unknown Tags
        - The default implementation returns an `Iterator<Path>` which, for
        this path, traverses the `Path`s returned by
        `getName(index)`, where `index` ranges from zero to
        `getNameCount() - 1`, inclusive.
        """
        ...


    def compareTo(self, other: "Path") -> int:
        """
        Compares two abstract paths lexicographically. The ordering defined by
        this method is provider specific, and in the case of the default
        provider, platform specific. This method does not access the file system
        and neither file is required to exist.
        
         This method may not be used to compare paths that are associated
        with different file system providers.

        Arguments
        - other: the path compared to this path.

        Returns
        - zero if the argument is .equals equal to this path, a
                 value less than zero if this path is lexicographically less than
                 the argument, or a value greater than zero if this path is
                 lexicographically greater than the argument

        Raises
        - ClassCastException: if the paths are associated with different providers
        """
        ...


    def equals(self, other: "Object") -> bool:
        """
        Tests this path for equality with the given object.
        
         If the given object is not a Path, or is a Path associated with a
        different `FileSystem`, then this method returns `False`.
        
         Whether or not two path are equal depends on the file system
        implementation. In some cases the paths are compared without regard
        to case, and others are case sensitive. This method does not access the
        file system and the file is not required to exist. Where required, the
        Files.isSameFile isSameFile method may be used to check if two
        paths locate the same file.
        
         This method satisfies the general contract of the java.lang.Object.equals(Object) Object.equals method. 

        Arguments
        - other: the object to which this object is to be compared

        Returns
        - `True` if, and only if, the given object is a `Path`
                 that is identical to this `Path`
        """
        ...


    def hashCode(self) -> int:
        """
        Computes a hash code for this path.
        
         The hash code is based upon the components of the path, and
        satisfies the general contract of the Object.hashCode
        Object.hashCode method.

        Returns
        - the hash-code value for this path
        """
        ...


    def toString(self) -> str:
        """
        Returns the string representation of this path.
        
         If this path was created by converting a path string using the
        FileSystem.getPath getPath method then the path string returned
        by this method may differ from the original String used to create the path.
        
         The returned path string uses the default name FileSystem.getSeparator separator to separate names in the path.

        Returns
        - the string representation of this path
        """
        ...
