"""
Python module generated from Java source file com.google.common.io.Files

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtIncompatible
from com.google.common.base import Joiner
from com.google.common.base import Optional
from com.google.common.base import Predicate
from com.google.common.base import Splitter
from com.google.common.collect import ImmutableList
from com.google.common.collect import ImmutableSet
from com.google.common.collect import Lists
from com.google.common.graph import SuccessorsFunction
from com.google.common.graph import Traverser
from com.google.common.hash import HashCode
from com.google.common.hash import HashFunction
from com.google.common.io import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from com.google.errorprone.annotations import InlineMe
from java.io import BufferedReader
from java.io import BufferedWriter
from java.io import File
from java.io import FileInputStream
from java.io import FileNotFoundException
from java.io import FileOutputStream
from java.io import IOException
from java.io import InputStreamReader
from java.io import OutputStream
from java.io import OutputStreamWriter
from java.io import RandomAccessFile
from java.nio.charset import Charset
from java.nio.charset import StandardCharsets
from java.util import Arrays
from java.util import Collections
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class Files:
    """
    Provides utility methods for working with File files.
    
    java.nio.file.Path users will find similar utilities in MoreFiles and the
    JDK's java.nio.file.Files class.

    Author(s)
    - Colin Decker

    Since
    - 1.0
    """

    @staticmethod
    def newReader(file: "File", charset: "Charset") -> "BufferedReader":
        """
        Returns a buffered reader that reads from a file using the given character set.
        
        **java.nio.file.Path equivalent:** java.nio.file.Files.newBufferedReader(java.nio.file.Path, Charset).

        Arguments
        - file: the file to read from
        - charset: the charset used to decode the input stream; see StandardCharsets for
            helpful predefined constants

        Returns
        - the buffered reader
        """
        ...


    @staticmethod
    def newWriter(file: "File", charset: "Charset") -> "BufferedWriter":
        """
        Returns a buffered writer that writes to a file using the given character set.
        
        **java.nio.file.Path equivalent:** java.nio.file.Files.newBufferedWriter(java.nio.file.Path, Charset,
        java.nio.file.OpenOption...).

        Arguments
        - file: the file to write to
        - charset: the charset used to encode the output stream; see StandardCharsets for
            helpful predefined constants

        Returns
        - the buffered writer
        """
        ...


    @staticmethod
    def asByteSource(file: "File") -> "ByteSource":
        """
        Returns a new ByteSource for reading bytes from the given file.

        Since
        - 14.0
        """
        ...


    @staticmethod
    def asByteSink(file: "File", *modes: Tuple["FileWriteMode", ...]) -> "ByteSink":
        """
        Returns a new ByteSink for writing bytes to the given file. The given `modes`
        control how the file is opened for writing. When no mode is provided, the file will be
        truncated before writing. When the FileWriteMode.APPEND APPEND mode is provided, writes
        will append to the end of the file without truncating it.

        Since
        - 14.0
        """
        ...


    @staticmethod
    def asCharSource(file: "File", charset: "Charset") -> "CharSource":
        """
        Returns a new CharSource for reading character data from the given file using the given
        character set.

        Since
        - 14.0
        """
        ...


    @staticmethod
    def asCharSink(file: "File", charset: "Charset", *modes: Tuple["FileWriteMode", ...]) -> "CharSink":
        """
        Returns a new CharSink for writing character data to the given file using the given
        character set. The given `modes` control how the file is opened for writing. When no mode
        is provided, the file will be truncated before writing. When the FileWriteMode.APPEND
        APPEND mode is provided, writes will append to the end of the file without truncating it.

        Since
        - 14.0
        """
        ...


    @staticmethod
    def toByteArray(file: "File") -> list[int]:
        """
        Reads all bytes from a file into a byte array.
        
        **java.nio.file.Path equivalent:** java.nio.file.Files.readAllBytes.

        Arguments
        - file: the file to read from

        Returns
        - a byte array containing all the bytes from file

        Raises
        - IllegalArgumentException: if the file is bigger than the largest possible byte array
            (2^31 - 1)
        - IOException: if an I/O error occurs
        """
        ...


    @staticmethod
    def toString(file: "File", charset: "Charset") -> str:
        """
        Reads all characters from a file into a String, using the given character set.

        Arguments
        - file: the file to read from
        - charset: the charset used to decode the input stream; see StandardCharsets for
            helpful predefined constants

        Returns
        - a string containing all the characters from the file

        Raises
        - IOException: if an I/O error occurs

        Deprecated
        - Prefer `asCharSource(file, charset).read()`.
        """
        ...


    @staticmethod
    def write(from: list[int], to: "File") -> None:
        """
        Overwrites a file with the contents of a byte array.
        
        **java.nio.file.Path equivalent:** java.nio.file.Files.write(java.nio.file.Path, byte[], java.nio.file.OpenOption...).

        Arguments
        - from: the bytes to write
        - to: the destination file

        Raises
        - IOException: if an I/O error occurs
        """
        ...


    @staticmethod
    def write(from: "CharSequence", to: "File", charset: "Charset") -> None:
        """
        Writes a character sequence (such as a string) to a file using the given character set.

        Arguments
        - from: the character sequence to write
        - to: the destination file
        - charset: the charset used to encode the output stream; see StandardCharsets for
            helpful predefined constants

        Raises
        - IOException: if an I/O error occurs

        Deprecated
        - Prefer `asCharSink(to, charset).write(from)`.
        """
        ...


    @staticmethod
    def copy(from: "File", to: "OutputStream") -> None:
        """
        Copies all bytes from a file to an output stream.
        
        **java.nio.file.Path equivalent:** java.nio.file.Files.copy(java.nio.file.Path, OutputStream).

        Arguments
        - from: the source file
        - to: the output stream

        Raises
        - IOException: if an I/O error occurs
        """
        ...


    @staticmethod
    def copy(from: "File", to: "File") -> None:
        """
        Copies all the bytes from one file to another.
        
        Copying is not an atomic operation - in the case of an I/O error, power loss, process
        termination, or other problems, `to` may not be a complete copy of `from`. If you
        need to guard against those conditions, you should employ other file-level synchronization.
        
        **Warning:** If `to` represents an existing file, that file will be overwritten
        with the contents of `from`. If `to` and `from` refer to the *same*
        file, the contents of that file will be deleted.
        
        **java.nio.file.Path equivalent:** java.nio.file.Files.copy(java.nio.file.Path, java.nio.file.Path, java.nio.file.CopyOption...).

        Arguments
        - from: the source file
        - to: the destination file

        Raises
        - IOException: if an I/O error occurs
        - IllegalArgumentException: if `from.equals(to)`
        """
        ...


    @staticmethod
    def copy(from: "File", charset: "Charset", to: "Appendable") -> None:
        """
        Copies all characters from a file to an appendable object, using the given character set.

        Arguments
        - from: the source file
        - charset: the charset used to decode the input stream; see StandardCharsets for
            helpful predefined constants
        - to: the appendable object

        Raises
        - IOException: if an I/O error occurs

        Deprecated
        - Prefer `asCharSource(from, charset).copyTo(to)`.
        """
        ...


    @staticmethod
    def append(from: "CharSequence", to: "File", charset: "Charset") -> None:
        """
        Appends a character sequence (such as a string) to a file using the given character set.

        Arguments
        - from: the character sequence to append
        - to: the destination file
        - charset: the charset used to encode the output stream; see StandardCharsets for
            helpful predefined constants

        Raises
        - IOException: if an I/O error occurs

        Deprecated
        - Prefer `asCharSink(to, charset, FileWriteMode.APPEND).write(from)`. This
            method is scheduled to be removed in October 2019.
        """
        ...


    @staticmethod
    def equal(file1: "File", file2: "File") -> bool:
        """
        Returns True if the given files exist, are not directories, and contain the same bytes.

        Raises
        - IOException: if an I/O error occurs
        """
        ...


    @staticmethod
    def createTempDir() -> "File":
        """
        Atomically creates a new directory somewhere beneath the system's temporary directory (as
        defined by the `java.io.tmpdir` system property), and returns its name.
        
        Use this method instead of File.createTempFile(String, String) when you wish to
        create a directory, not a regular file. A common pitfall is to call `createTempFile`,
        delete the file and create a directory in its place, but this leads a race condition which can
        be exploited to create security vulnerabilities, especially when executable files are to be
        written into the directory.
        
        Depending on the environmment that this code is run in, the system temporary directory (and
        thus the directory this method creates) may be more visible that a program would like - files
        written to this directory may be read or overwritten by hostile programs running on the same
        machine.
        
        This method assumes that the temporary volume is writable, has free inodes and free blocks,
        and that it will not be called thousands of times per second.
        
        **java.nio.file.Path equivalent:** java.nio.file.Files.createTempDirectory.

        Returns
        - the newly-created directory

        Raises
        - IllegalStateException: if the directory could not be created

        Deprecated
        - For Android users, see the <a
            href="https://developer.android.com/training/data-storage" target="_blank">Data and File
            Storage overview</a> to select an appropriate temporary directory (perhaps `context.getCacheDir()`). For developers on Java 7 or later, use java.nio.file.Files.createTempDirectory, transforming it to a File using java.nio.file.Path.toFile() toFile() if needed.
        """
        ...


    @staticmethod
    def touch(file: "File") -> None:
        """
        Creates an empty file or updates the last updated timestamp on the same as the unix command of
        the same name.

        Arguments
        - file: the file to create or update

        Raises
        - IOException: if an I/O error occurs
        """
        ...


    @staticmethod
    def createParentDirs(file: "File") -> None:
        """
        Creates any necessary but nonexistent parent directories of the specified file. Note that if
        this operation fails it may have succeeded in creating some (but not all) of the necessary
        parent directories.

        Raises
        - IOException: if an I/O error occurs, or if any necessary but nonexistent parent
            directories of the specified file could not be created.

        Since
        - 4.0
        """
        ...


    @staticmethod
    def move(from: "File", to: "File") -> None:
        """
        Moves a file from one path to another. This method can rename a file and/or move it to a
        different directory. In either case `to` must be the target path for the file itself; not
        just the new name for the file or the path to the new parent directory.
        
        **java.nio.file.Path equivalent:** java.nio.file.Files.move.

        Arguments
        - from: the source file
        - to: the destination file

        Raises
        - IOException: if an I/O error occurs
        - IllegalArgumentException: if `from.equals(to)`
        """
        ...


    @staticmethod
    def readFirstLine(file: "File", charset: "Charset") -> str:
        """
        Reads the first line from a file. The line does not include line-termination characters, but
        does include other leading and trailing whitespace.

        Arguments
        - file: the file to read from
        - charset: the charset used to decode the input stream; see StandardCharsets for
            helpful predefined constants

        Returns
        - the first line, or null if the file is empty

        Raises
        - IOException: if an I/O error occurs

        Deprecated
        - Prefer `asCharSource(file, charset).readFirstLine()`.
        """
        ...


    @staticmethod
    def readLines(file: "File", charset: "Charset") -> list[str]:
        """
        Reads all of the lines from a file. The lines do not include line-termination characters, but
        do include other leading and trailing whitespace.
        
        This method returns a mutable `List`. For an `ImmutableList`, use `Files.asCharSource(file, charset).readLines()`.
        
        **java.nio.file.Path equivalent:** java.nio.file.Files.readAllLines(java.nio.file.Path, Charset).

        Arguments
        - file: the file to read from
        - charset: the charset used to decode the input stream; see StandardCharsets for
            helpful predefined constants

        Returns
        - a mutable List containing all the lines

        Raises
        - IOException: if an I/O error occurs
        """
        ...


    @staticmethod
    def readLines(file: "File", charset: "Charset", callback: "LineProcessor"["T"]) -> "T":
        """
        Streams lines from a File, stopping when our callback returns False, or we have read
        all of the lines.

        Arguments
        - file: the file to read from
        - charset: the charset used to decode the input stream; see StandardCharsets for
            helpful predefined constants
        - callback: the LineProcessor to use to handle the lines

        Returns
        - the output of processing the lines

        Raises
        - IOException: if an I/O error occurs

        Deprecated
        - Prefer `asCharSource(file, charset).readLines(callback)`.
        """
        ...


    @staticmethod
    def readBytes(file: "File", processor: "ByteProcessor"["T"]) -> "T":
        """
        Process the bytes of a file.
        
        (If this seems too complicated, maybe you're looking for .toByteArray.)

        Arguments
        - file: the file to read
        - processor: the object to which the bytes of the file are passed.

        Returns
        - the result of the byte processor

        Raises
        - IOException: if an I/O error occurs

        Deprecated
        - Prefer `asByteSource(file).read(processor)`.
        """
        ...


    @staticmethod
    def hash(file: "File", hashFunction: "HashFunction") -> "HashCode":
        """
        Computes the hash code of the `file` using `hashFunction`.

        Arguments
        - file: the file to read
        - hashFunction: the hash function to use to hash the data

        Returns
        - the HashCode of all of the bytes in the file

        Raises
        - IOException: if an I/O error occurs

        Since
        - 12.0

        Deprecated
        - Prefer `asByteSource(file).hash(hashFunction)`.
        """
        ...


    @staticmethod
    def map(file: "File") -> "MappedByteBuffer":
        """
        Fully maps a file read-only in to memory as per FileChannel.map(java.nio.channels.FileChannel.MapMode, long, long).
        
        Files are mapped from offset 0 to its length.
        
        This only works for files ≤ Integer.MAX_VALUE bytes.

        Arguments
        - file: the file to map

        Returns
        - a read-only buffer reflecting `file`

        Raises
        - FileNotFoundException: if the `file` does not exist
        - IOException: if an I/O error occurs

        See
        - FileChannel.map(MapMode, long, long)

        Since
        - 2.0
        """
        ...


    @staticmethod
    def map(file: "File", mode: "MapMode") -> "MappedByteBuffer":
        """
        Fully maps a file in to memory as per FileChannel.map(java.nio.channels.FileChannel.MapMode, long, long) using the requested MapMode.
        
        Files are mapped from offset 0 to its length.
        
        This only works for files ≤ Integer.MAX_VALUE bytes.

        Arguments
        - file: the file to map
        - mode: the mode to use when mapping `file`

        Returns
        - a buffer reflecting `file`

        Raises
        - FileNotFoundException: if the `file` does not exist
        - IOException: if an I/O error occurs

        See
        - FileChannel.map(MapMode, long, long)

        Since
        - 2.0
        """
        ...


    @staticmethod
    def map(file: "File", mode: "MapMode", size: int) -> "MappedByteBuffer":
        """
        Maps a file in to memory as per FileChannel.map(java.nio.channels.FileChannel.MapMode,
        long, long) using the requested MapMode.
        
        Files are mapped from offset 0 to `size`.
        
        If the mode is MapMode.READ_WRITE and the file does not exist, it will be created
        with the requested `size`. Thus this method is useful for creating memory mapped files
        which do not yet exist.
        
        This only works for files ≤ Integer.MAX_VALUE bytes.

        Arguments
        - file: the file to map
        - mode: the mode to use when mapping `file`

        Returns
        - a buffer reflecting `file`

        Raises
        - IOException: if an I/O error occurs

        See
        - FileChannel.map(MapMode, long, long)

        Since
        - 2.0
        """
        ...


    @staticmethod
    def simplifyPath(pathname: str) -> str:
        """
        Returns the lexically cleaned form of the path name, *usually* (but not always) equivalent
        to the original. The following heuristics are used:
        
        
          - empty string becomes .
          - . stays as .
          - fold out ./
          - fold out ../ when possible
          - collapse multiple slashes
          - delete trailing slashes (unless the path is just "/")
        
        
        These heuristics do not always match the behavior of the filesystem. In particular, consider
        the path `a/../b`, which `simplifyPath` will change to `b`. If `a` is a
        symlink to `x`, `a/../b` may refer to a sibling of `x`, rather than the
        sibling of `a` referred to by `b`.

        Since
        - 11.0
        """
        ...


    @staticmethod
    def getFileExtension(fullName: str) -> str:
        """
        Returns the <a href="http://en.wikipedia.org/wiki/Filename_extension">file extension</a> for
        the given file name, or the empty string if the file has no extension. The result does not
        include the '`.`'.
        
        **Note:** This method simply returns everything after the last '`.`' in the file's
        name as determined by File.getName. It does not account for any filesystem-specific
        behavior that the File API does not already account for. For example, on NTFS it will
        report `"txt"` as the extension for the filename `"foo.exe:.txt"` even though NTFS
        will drop the `":.txt"` part of the name when the file is actually created on the
        filesystem due to NTFS's <a href="https://goo.gl/vTpJi4">Alternate Data Streams</a>.

        Since
        - 11.0
        """
        ...


    @staticmethod
    def getNameWithoutExtension(file: str) -> str:
        """
        Returns the file name without its <a
        href="http://en.wikipedia.org/wiki/Filename_extension">file extension</a> or path. This is
        similar to the `basename` unix command. The result does not include the '`.`'.

        Arguments
        - file: The name of the file to trim the extension from. This can be either a fully
            qualified file name (including a path) or just a file name.

        Returns
        - The file name without its path or extension.

        Since
        - 14.0
        """
        ...


    @staticmethod
    def fileTraverser() -> "Traverser"["File"]:
        """
        Returns a Traverser instance for the file and directory tree. The returned traverser
        starts from a File and will return all files and directories it encounters.
        
        **Warning:** `File` provides no support for symbolic links, and as such there is no
        way to ensure that a symbolic link to a directory is not followed when traversing the tree. In
        this case, iterables created by this traverser could contain files that are outside of the
        given directory or even be infinite if there is a symbolic link loop.
        
        If available, consider using MoreFiles.fileTraverser() instead. It behaves the same
        except that it doesn't follow symbolic links and returns `Path` instances.
        
        If the File passed to one of the Traverser methods does not exist or is not
        a directory, no exception will be thrown and the returned Iterable will contain a
        single element: that file.
        
        Example: `Files.fileTraverser().depthFirstPreOrder(new File("/"))` may return files
        with the following paths: `["/", "/etc", "/etc/config.txt", "/etc/fonts", "/home",
        "/home/alice", ...]`

        Since
        - 23.5
        """
        ...


    @staticmethod
    def isDirectory() -> "Predicate"["File"]:
        """
        Returns a predicate that returns the result of File.isDirectory on input files.

        Since
        - 15.0
        """
        ...


    @staticmethod
    def isFile() -> "Predicate"["File"]:
        """
        Returns a predicate that returns the result of File.isFile on input files.

        Since
        - 15.0
        """
        ...
