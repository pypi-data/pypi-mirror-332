"""
Python module generated from Java source file com.google.common.reflect.ClassPath

Java source file obtained from artifact guava version 31.0.1-jre

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
from com.google.common.collect import ImmutableList
from com.google.common.collect import ImmutableMap
from com.google.common.collect import ImmutableSet
from com.google.common.collect import Maps
from com.google.common.io import ByteSource
from com.google.common.io import CharSource
from com.google.common.io import Resources
from com.google.common.reflect import *
from java.io import File
from java.io import IOException
from java.net import MalformedURLException
from java.net import URISyntaxException
from java.net import URL
from java.net import URLClassLoader
from java.nio.charset import Charset
from java.util import Enumeration
from java.util import NoSuchElementException
from java.util.jar import Attributes
from java.util.jar import JarEntry
from java.util.jar import JarFile
from java.util.jar import Manifest
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class ClassPath:
    """
    Scans the source of a ClassLoader and finds all loadable classes and resources.
    
    <h2>Prefer <a href="https://github.com/classgraph/classgraph/wiki">ClassGraph</a> over `ClassPath`</h2>
    
    We recommend using <a href="https://github.com/classgraph/classgraph/wiki">ClassGraph</a>
    instead of `ClassPath`. ClassGraph improves upon `ClassPath` in several ways,
    including addressing many of its limitations. Limitations of `ClassPath` include:
    
    
      - It looks only for files and JARs in URLs available from URLClassLoader instances or
          the ClassLoader.getSystemClassLoader() system class loader. This means it does
          not look for classes in the *module path*.
      - It understands only `file:` URLs. This means that it does not understand <a
          href="https://openjdk.java.net/jeps/220">`jrt:/` URLs</a>, among <a
          href="https://github.com/classgraph/classgraph/wiki/Classpath-specification-mechanisms">others</a>.
      - It does not know how to look for classes when running under an Android VM. (ClassGraph does
          not support this directly, either, but ClassGraph documents how to <a
          href="https://github.com/classgraph/classgraph/wiki/Build-Time-Scanning">perform build-time
          classpath scanning and make the results available to an Android app</a>.)
      - Like all of Guava, it is not tested under Windows. We have gotten <a
          href="https://github.com/google/guava/issues/2130">a report of a specific bug under
          Windows</a>.
      - It <a href="https://github.com/google/guava/issues/2712">returns only one resource for a
          given path</a>, even if resources with that path appear in multiple jars or directories.
      - It assumes that <a href="https://github.com/google/guava/issues/3349">any class with a
          `$` in its name is a nested class</a>.
    
    
    <h2>`ClassPath` and symlinks</h2>
    
    In the case of directory classloaders, symlinks are supported but cycles are not traversed.
    This guarantees discovery of each *unique* loadable resource. However, not all possible
    aliases for resources on cyclic paths will be listed.

    Author(s)
    - Ben Yu

    Since
    - 14.0
    """

    @staticmethod
    def from(classloader: "ClassLoader") -> "ClassPath":
        """
        Returns a `ClassPath` representing all classes and resources loadable from `classloader` and its ancestor class loaders.
        
        **Warning:** `ClassPath` can find classes and resources only from:
        
        
          - URLClassLoader instances' `file:` URLs
          - the ClassLoader.getSystemClassLoader() system class loader. To search the
              system class loader even when it is not a URLClassLoader (as in Java 9), `ClassPath` searches the files from the `java.class.path` system property.

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
        Returns all top level classes loadable from the current class path. Note that "top-level-ness"
        is determined heuristically by class name (see ClassInfo.isTopLevel).
        """
        ...


    def getTopLevelClasses(self, packageName: str) -> "ImmutableSet"["ClassInfo"]:
        """
        Returns all top level classes whose package name is `packageName`.
        """
        ...


    def getTopLevelClassesRecursive(self, packageName: str) -> "ImmutableSet"["ClassInfo"]:
        """
        Returns all top level classes whose package name is `packageName` or starts with `packageName` followed by a '.'.
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
            
            Behaves similarly to `class.getPackage().`Package.getName() getName() but
            does not require the class (or package) to be loaded.
            
            But note that this method may behave differently for a class in the default package: For
            such classes, this method always returns an empty string. But under some version of Java,
            `class.getPackage().getName()` produces a `NullPointerException` because `class.getPackage()` returns `null`.
            """
            ...


        def getSimpleName(self) -> str:
            """
            Returns the simple name of the underlying class as given in the source code.
            
            Behaves similarly to Class.getSimpleName() but does not require the class to be
            loaded.
            
            But note that this class uses heuristics to identify the simple name. See a related
            discussion in <a href="https://github.com/google/guava/issues/3349">issue 3349</a>.
            """
            ...


        def getName(self) -> str:
            """
            Returns the fully qualified name of the class.
            
            Behaves identically to Class.getName() but does not require the class to be
            loaded.
            """
            ...


        def isTopLevel(self) -> bool:
            """
            Returns True if the class name "looks to be" top level (not nested), that is, it includes no
            '$' in the name. This method may return False for a top-level class that's intentionally
            named with the '$' character. If this is a concern, you could use .load and then
            check on the loaded Class object instead.

            Since
            - 30.1
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
