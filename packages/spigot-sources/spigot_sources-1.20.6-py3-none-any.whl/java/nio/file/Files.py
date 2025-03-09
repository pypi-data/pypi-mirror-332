"""
Python module generated from Java source file java.nio.file.Files

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import BufferedReader
from java.io import BufferedWriter
from java.io import Closeable
from java.io import File
from java.io import IOException
from java.io import InputStream
from java.io import InputStreamReader
from java.io import OutputStream
from java.io import OutputStreamWriter
from java.io import Reader
from java.io import UncheckedIOException
from java.io import Writer
from java.nio.charset import Charset
from java.nio.charset import CharsetDecoder
from java.nio.charset import CharsetEncoder
from java.nio.charset import StandardCharsets
from java.nio.file import *
from java.nio.file.attribute import BasicFileAttributeView
from java.nio.file.attribute import BasicFileAttributes
from java.nio.file.attribute import DosFileAttributes
from java.nio.file.attribute import FileAttribute
from java.nio.file.attribute import FileAttributeView
from java.nio.file.attribute import FileOwnerAttributeView
from java.nio.file.attribute import FileStoreAttributeView
from java.nio.file.attribute import FileTime
from java.nio.file.attribute import PosixFileAttributeView
from java.nio.file.attribute import PosixFileAttributes
from java.nio.file.attribute import PosixFilePermission
from java.nio.file.attribute import UserPrincipal
from java.nio.file.spi import FileSystemProvider
from java.nio.file.spi import FileTypeDetector
from java.security import AccessController
from java.security import PrivilegedAction
from java.util import Arrays
from java.util import Collections
from java.util import EnumSet
from java.util import Iterator
from java.util import Objects
from java.util import ServiceLoader
from java.util import Spliterator
from java.util.function import BiPredicate
from java.util.stream import Stream
from java.util.stream import StreamSupport
from jdk.internal.util import ArraysSupport
from sun.nio.ch import FileChannelImpl
from sun.nio.cs import UTF_8
from sun.nio.fs import ExtendedFileSystemProvider
from typing import Any, Callable, Iterable, Tuple


class Files:

    @staticmethod
    def newInputStream(path: "Path", *options: Tuple["OpenOption", ...]) -> "InputStream":
        ...


    @staticmethod
    def newOutputStream(path: "Path", *options: Tuple["OpenOption", ...]) -> "OutputStream":
        ...


    @staticmethod
    def newByteChannel(path: "Path", options: set["OpenOption"], *attrs: Tuple["FileAttribute"[Any], ...]) -> "SeekableByteChannel":
        ...


    @staticmethod
    def newByteChannel(path: "Path", *options: Tuple["OpenOption", ...]) -> "SeekableByteChannel":
        ...


    @staticmethod
    def newDirectoryStream(dir: "Path") -> "DirectoryStream"["Path"]:
        ...


    @staticmethod
    def newDirectoryStream(dir: "Path", glob: str) -> "DirectoryStream"["Path"]:
        ...


    @staticmethod
    def newDirectoryStream(dir: "Path", filter: "DirectoryStream.Filter"["Path"]) -> "DirectoryStream"["Path"]:
        ...


    @staticmethod
    def createFile(path: "Path", *attrs: Tuple["FileAttribute"[Any], ...]) -> "Path":
        ...


    @staticmethod
    def createDirectory(dir: "Path", *attrs: Tuple["FileAttribute"[Any], ...]) -> "Path":
        ...


    @staticmethod
    def createDirectories(dir: "Path", *attrs: Tuple["FileAttribute"[Any], ...]) -> "Path":
        ...


    @staticmethod
    def createTempFile(dir: "Path", prefix: str, suffix: str, *attrs: Tuple["FileAttribute"[Any], ...]) -> "Path":
        ...


    @staticmethod
    def createTempFile(prefix: str, suffix: str, *attrs: Tuple["FileAttribute"[Any], ...]) -> "Path":
        ...


    @staticmethod
    def createTempDirectory(dir: "Path", prefix: str, *attrs: Tuple["FileAttribute"[Any], ...]) -> "Path":
        ...


    @staticmethod
    def createTempDirectory(prefix: str, *attrs: Tuple["FileAttribute"[Any], ...]) -> "Path":
        ...


    @staticmethod
    def createSymbolicLink(link: "Path", target: "Path", *attrs: Tuple["FileAttribute"[Any], ...]) -> "Path":
        ...


    @staticmethod
    def createLink(link: "Path", existing: "Path") -> "Path":
        ...


    @staticmethod
    def delete(path: "Path") -> None:
        ...


    @staticmethod
    def deleteIfExists(path: "Path") -> bool:
        ...


    @staticmethod
    def copy(source: "Path", target: "Path", *options: Tuple["CopyOption", ...]) -> "Path":
        ...


    @staticmethod
    def move(source: "Path", target: "Path", *options: Tuple["CopyOption", ...]) -> "Path":
        ...


    @staticmethod
    def readSymbolicLink(link: "Path") -> "Path":
        ...


    @staticmethod
    def getFileStore(path: "Path") -> "FileStore":
        ...


    @staticmethod
    def isSameFile(path: "Path", path2: "Path") -> bool:
        ...


    @staticmethod
    def mismatch(path: "Path", path2: "Path") -> int:
        ...


    @staticmethod
    def isHidden(path: "Path") -> bool:
        ...


    @staticmethod
    def probeContentType(path: "Path") -> str:
        ...


    @staticmethod
    def getFileAttributeView(path: "Path", type: type["V"], *options: Tuple["LinkOption", ...]) -> "V":
        ...


    @staticmethod
    def readAttributes(path: "Path", type: type["A"], *options: Tuple["LinkOption", ...]) -> "A":
        ...


    @staticmethod
    def setAttribute(path: "Path", attribute: str, value: "Object", *options: Tuple["LinkOption", ...]) -> "Path":
        ...


    @staticmethod
    def getAttribute(path: "Path", attribute: str, *options: Tuple["LinkOption", ...]) -> "Object":
        ...


    @staticmethod
    def readAttributes(path: "Path", attributes: str, *options: Tuple["LinkOption", ...]) -> dict[str, "Object"]:
        ...


    @staticmethod
    def getPosixFilePermissions(path: "Path", *options: Tuple["LinkOption", ...]) -> set["PosixFilePermission"]:
        ...


    @staticmethod
    def setPosixFilePermissions(path: "Path", perms: set["PosixFilePermission"]) -> "Path":
        ...


    @staticmethod
    def getOwner(path: "Path", *options: Tuple["LinkOption", ...]) -> "UserPrincipal":
        ...


    @staticmethod
    def setOwner(path: "Path", owner: "UserPrincipal") -> "Path":
        ...


    @staticmethod
    def isSymbolicLink(path: "Path") -> bool:
        ...


    @staticmethod
    def isDirectory(path: "Path", *options: Tuple["LinkOption", ...]) -> bool:
        ...


    @staticmethod
    def isRegularFile(path: "Path", *options: Tuple["LinkOption", ...]) -> bool:
        ...


    @staticmethod
    def getLastModifiedTime(path: "Path", *options: Tuple["LinkOption", ...]) -> "FileTime":
        ...


    @staticmethod
    def setLastModifiedTime(path: "Path", time: "FileTime") -> "Path":
        ...


    @staticmethod
    def size(path: "Path") -> int:
        ...


    @staticmethod
    def exists(path: "Path", *options: Tuple["LinkOption", ...]) -> bool:
        ...


    @staticmethod
    def notExists(path: "Path", *options: Tuple["LinkOption", ...]) -> bool:
        ...


    @staticmethod
    def isReadable(path: "Path") -> bool:
        ...


    @staticmethod
    def isWritable(path: "Path") -> bool:
        ...


    @staticmethod
    def isExecutable(path: "Path") -> bool:
        ...


    @staticmethod
    def walkFileTree(start: "Path", options: set["FileVisitOption"], maxDepth: int, visitor: "FileVisitor"["Path"]) -> "Path":
        ...


    @staticmethod
    def walkFileTree(start: "Path", visitor: "FileVisitor"["Path"]) -> "Path":
        ...


    @staticmethod
    def newBufferedReader(path: "Path", cs: "Charset") -> "BufferedReader":
        ...


    @staticmethod
    def newBufferedReader(path: "Path") -> "BufferedReader":
        ...


    @staticmethod
    def newBufferedWriter(path: "Path", cs: "Charset", *options: Tuple["OpenOption", ...]) -> "BufferedWriter":
        ...


    @staticmethod
    def newBufferedWriter(path: "Path", *options: Tuple["OpenOption", ...]) -> "BufferedWriter":
        ...


    @staticmethod
    def copy(in: "InputStream", target: "Path", *options: Tuple["CopyOption", ...]) -> int:
        ...


    @staticmethod
    def copy(source: "Path", out: "OutputStream") -> int:
        ...


    @staticmethod
    def readAllBytes(path: "Path") -> list[int]:
        ...


    @staticmethod
    def readString(path: "Path") -> str:
        ...


    @staticmethod
    def readString(path: "Path", cs: "Charset") -> str:
        ...


    @staticmethod
    def readAllLines(path: "Path", cs: "Charset") -> list[str]:
        ...


    @staticmethod
    def readAllLines(path: "Path") -> list[str]:
        ...


    @staticmethod
    def write(path: "Path", bytes: list[int], *options: Tuple["OpenOption", ...]) -> "Path":
        ...


    @staticmethod
    def write(path: "Path", lines: Iterable["CharSequence"], cs: "Charset", *options: Tuple["OpenOption", ...]) -> "Path":
        ...


    @staticmethod
    def write(path: "Path", lines: Iterable["CharSequence"], *options: Tuple["OpenOption", ...]) -> "Path":
        ...


    @staticmethod
    def writeString(path: "Path", csq: "CharSequence", *options: Tuple["OpenOption", ...]) -> "Path":
        ...


    @staticmethod
    def writeString(path: "Path", csq: "CharSequence", cs: "Charset", *options: Tuple["OpenOption", ...]) -> "Path":
        ...


    @staticmethod
    def list(dir: "Path") -> "Stream"["Path"]:
        ...


    @staticmethod
    def walk(start: "Path", maxDepth: int, *options: Tuple["FileVisitOption", ...]) -> "Stream"["Path"]:
        ...


    @staticmethod
    def walk(start: "Path", *options: Tuple["FileVisitOption", ...]) -> "Stream"["Path"]:
        ...


    @staticmethod
    def find(start: "Path", maxDepth: int, matcher: "BiPredicate"["Path", "BasicFileAttributes"], *options: Tuple["FileVisitOption", ...]) -> "Stream"["Path"]:
        ...


    @staticmethod
    def lines(path: "Path", cs: "Charset") -> "Stream"[str]:
        ...


    @staticmethod
    def lines(path: "Path") -> "Stream"[str]:
        ...
