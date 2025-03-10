"""
Python module generated from Java source file com.google.common.reflect.ClassPath

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import VisibleForTesting
from com.google.common.base import CharMatcher
from com.google.common.base import Predicate
from com.google.common.base import Splitter
from com.google.common.collect import FluentIterable
from com.google.common.collect import ImmutableMap
from com.google.common.collect import ImmutableSet
from com.google.common.collect import Maps
from com.google.common.collect import MultimapBuilder
from com.google.common.collect import SetMultimap
from com.google.common.collect import Sets
from com.google.common.io import ByteSource
from com.google.common.io import CharSource
from com.google.common.io import Resources
from com.google.common.reflect import *
from java.io import File
from java.io import IOException
from java.net import MalformedURLException
from java.net import URL
from java.net import URLClassLoader
from java.nio.charset import Charset
from java.util import Enumeration
from java.util import NoSuchElementException
from java.util.jar import Attributes
from java.util.jar import JarEntry
from java.util.jar import JarFile
from java.util.jar import Manifest
from javax.annotation import Nullable
from typing import Any, Callable, Iterable, Tuple


class ClassPath:
    """
    Scans the source of a ClassLoader and finds all loadable classes and resources.
    
    **Warning:** Currently only URLClassLoader and only `file://` urls are
    supported.

    Author(s)
    - Ben Yu

    Since
    - 14.0
    """

    @staticmethod
    def from(classloader: "ClassLoader") -> "ClassPath":
        """
        Returns a `ClassPath` representing all classes and resources loadable from `classloader` and its parent class loaders.
        
        **Warning:** Currently only URLClassLoader and only `file://` urls are
        supported.

        Raises
        - IOException: if the attempt to read class path resources (jar files or directories)
            failed.
        """
        ...


    def getResources(self) -> "ImmutableSet"["ResourceInfo"]:
        """
        Returns all resources loadable from the current class path, including the class files of all
        loadable classes but excluding the "META-INF/MANIFEST.MF" file.
        """
        ...


    def getAllClasses(self) -> "ImmutableSet"["ClassInfo"]:
        """
        Returns all classes loadable from the current class path.

        Since
        - 16.0
        """
        ...


    def getTopLevelClasses(self) -> "ImmutableSet"["ClassInfo"]:
        """
        Returns all top level classes loadable from the current class path.
        """
        ...


    def getTopLevelClasses(self, packageName: str) -> "ImmutableSet"["ClassInfo"]:
        """
        Returns all top level classes whose package name is `packageName`.
        """
        ...


    def getTopLevelClassesRecursive(self, packageName: str) -> "ImmutableSet"["ClassInfo"]:
        """
        Returns all top level classes whose package name is `packageName` or starts with
        `packageName` followed by a '.'.
        """
        ...


    class ResourceInfo:
        """
        Represents a class path resource that can be either a class file or any other resource file
        loadable from the class path.

        Since
        - 14.0
        """

        def url(self) -> "URL":
            """
            Returns the url identifying the resource.
            
            See ClassLoader.getResource

            Raises
            - NoSuchElementException: if the resource cannot be loaded through the class loader,
                despite physically existing in the class path.
            """
            ...


        def asByteSource(self) -> "ByteSource":
            """
            Returns a ByteSource view of the resource from which its bytes can be read.

            Raises
            - NoSuchElementException: if the resource cannot be loaded through the class loader,
                despite physically existing in the class path.

            Since
            - 20.0
            """
            ...


        def asCharSource(self, charset: "Charset") -> "CharSource":
            """
            Returns a CharSource view of the resource from which its bytes can be read as
            characters decoded with the given `charset`.

            Raises
            - NoSuchElementException: if the resource cannot be loaded through the class loader,
                despite physically existing in the class path.

            Since
            - 20.0
            """
            ...


        def getResourceName(self) -> str:
            """
            Returns the fully qualified name of the resource. Such as "com/mycomp/foo/bar.txt".
            """
            ...


        def hashCode(self) -> int:
            ...


        def equals(self, obj: "Object") -> bool:
            ...


        def toString(self) -> str:
            ...


    class ClassInfo(ResourceInfo):
        """
        Represents a class that can be loaded through .load.

        Since
        - 14.0
        """

        def getPackageName(self) -> str:
            """
            Returns the package name of the class, without attempting to load the class.
            
            Behaves identically to Package.getName() but does not require the class (or
            package) to be loaded.
            """
            ...


        def getSimpleName(self) -> str:
            """
            Returns the simple name of the underlying class as given in the source code.
            
            Behaves identically to Class.getSimpleName() but does not require the class to be
            loaded.
            """
            ...


        def getName(self) -> str:
            """
            Returns the fully qualified name of the class.
            
            Behaves identically to Class.getName() but does not require the class to be
            loaded.
            """
            ...


        def load(self) -> type[Any]:
            """
            Loads (but doesn't link or initialize) the class.

            Raises
            - LinkageError: when there were errors in loading classes that this class depends on.
                For example, NoClassDefFoundError.
            """
            ...


        def toString(self) -> str:
            ...
