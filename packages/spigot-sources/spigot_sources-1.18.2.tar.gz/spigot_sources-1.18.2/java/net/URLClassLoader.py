"""
Python module generated from Java source file java.net.URLClassLoader

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import Closeable
from java.io import File
from java.io import FilePermission
from java.io import IOException
from java.io import InputStream
from java.net import *
from java.security import AccessControlContext
from java.security import AccessController
from java.security import CodeSigner
from java.security import CodeSource
from java.security import Permission
from java.security import PermissionCollection
from java.security import PrivilegedAction
from java.security import PrivilegedExceptionAction
from java.security import SecureClassLoader
from java.util import Enumeration
from java.util import NoSuchElementException
from java.util import Objects
from java.util import WeakHashMap
from java.util.jar import Attributes
from java.util.jar.Attributes import Name
from java.util.jar import JarFile
from java.util.jar import Manifest
from jdk.internal.access import SharedSecrets
from jdk.internal.loader import Resource
from jdk.internal.loader import URLClassPath
from jdk.internal.perf import PerfCounter
from sun.net.www import ParseUtil
from sun.security.util import SecurityConstants
from typing import Any, Callable, Iterable, Tuple


class URLClassLoader(SecureClassLoader, Closeable):
    """
    This class loader is used to load classes and resources from a search
    path of URLs referring to both JAR files and directories. Any `jar:`
    scheme URL (see java.net.JarURLConnection) is assumed to refer to a
    JAR file.  Any `file:` scheme URL that ends with a '/' is assumed to
    refer to a directory. Otherwise, the URL is assumed to refer to a JAR file
    which will be opened as needed.
    
    This class loader supports the loading of classes and resources from the
    contents of a <a href="../util/jar/JarFile.html#multirelease">multi-release</a>
    JAR file that is referred to by a given URL.
    
    The AccessControlContext of the thread that created the instance of
    URLClassLoader will be used when subsequently loading classes and
    resources.
    
    The classes that are loaded are by default granted permission only to
    access the URLs specified when the URLClassLoader was created.

    Author(s)
    - David Connelly

    Since
    - 1.2
    """

    def __init__(self, urls: list["URL"], parent: "ClassLoader"):
        """
        Constructs a new URLClassLoader for the given URLs. The URLs will be
        searched in the order specified for classes and resources after first
        searching in the specified parent class loader.  Any `jar:`
        scheme URL is assumed to refer to a JAR file.  Any `file:` scheme
        URL that ends with a '/' is assumed to refer to a directory.  Otherwise,
        the URL is assumed to refer to a JAR file which will be downloaded and
        opened as needed.
        
        If there is a security manager, this method first
        calls the security manager's `checkCreateClassLoader` method
        to ensure creation of a class loader is allowed.

        Arguments
        - urls: the URLs from which to load classes and resources
        - parent: the parent class loader for delegation

        Raises
        - SecurityException: if a security manager exists and its
                    `checkCreateClassLoader` method doesn't allow
                    creation of a class loader.
        - NullPointerException: if `urls` or any of its
                    elements is `null`.

        See
        - SecurityManager.checkCreateClassLoader
        """
        ...


    def __init__(self, urls: list["URL"]):
        """
        Constructs a new URLClassLoader for the specified URLs using the
        default delegation parent `ClassLoader`. The URLs will
        be searched in the order specified for classes and resources after
        first searching in the parent class loader. Any URL that ends with
        a '/' is assumed to refer to a directory. Otherwise, the URL is
        assumed to refer to a JAR file which will be downloaded and opened
        as needed.
        
        If there is a security manager, this method first
        calls the security manager's `checkCreateClassLoader` method
        to ensure creation of a class loader is allowed.

        Arguments
        - urls: the URLs from which to load classes and resources

        Raises
        - SecurityException: if a security manager exists and its
                    `checkCreateClassLoader` method doesn't allow
                    creation of a class loader.
        - NullPointerException: if `urls` or any of its
                    elements is `null`.

        See
        - SecurityManager.checkCreateClassLoader
        """
        ...


    def __init__(self, urls: list["URL"], parent: "ClassLoader", factory: "URLStreamHandlerFactory"):
        """
        Constructs a new URLClassLoader for the specified URLs, parent
        class loader, and URLStreamHandlerFactory. The parent argument
        will be used as the parent class loader for delegation. The
        factory argument will be used as the stream handler factory to
        obtain protocol handlers when creating new jar URLs.
        
        If there is a security manager, this method first
        calls the security manager's `checkCreateClassLoader` method
        to ensure creation of a class loader is allowed.

        Arguments
        - urls: the URLs from which to load classes and resources
        - parent: the parent class loader for delegation
        - factory: the URLStreamHandlerFactory to use when creating URLs

        Raises
        - SecurityException: if a security manager exists and its
                `checkCreateClassLoader` method doesn't allow
                creation of a class loader.
        - NullPointerException: if `urls` or any of its
                elements is `null`.

        See
        - SecurityManager.checkCreateClassLoader
        """
        ...


    def __init__(self, name: str, urls: list["URL"], parent: "ClassLoader"):
        """
        Constructs a new named `URLClassLoader` for the specified URLs.
        The URLs will be searched in the order specified for classes
        and resources after first searching in the specified parent class loader.
        Any URL that ends with a '/' is assumed to refer to a directory.
        Otherwise, the URL is assumed to refer to a JAR file which will be
        downloaded and opened as needed.

        Arguments
        - name: class loader name; or `null` if not named
        - urls: the URLs from which to load classes and resources
        - parent: the parent class loader for delegation

        Raises
        - IllegalArgumentException: if the given name is empty.
        - NullPointerException: if `urls` or any of its
                elements is `null`.
        - SecurityException: if a security manager exists and its
                SecurityManager.checkCreateClassLoader() method doesn't
                allow creation of a class loader.

        Since
        - 9
        """
        ...


    def __init__(self, name: str, urls: list["URL"], parent: "ClassLoader", factory: "URLStreamHandlerFactory"):
        """
        Constructs a new named `URLClassLoader` for the specified URLs,
        parent class loader, and URLStreamHandlerFactory.
        The parent argument will be used as the parent class loader for delegation.
        The factory argument will be used as the stream handler factory to
        obtain protocol handlers when creating new jar URLs.

        Arguments
        - name: class loader name; or `null` if not named
        - urls: the URLs from which to load classes and resources
        - parent: the parent class loader for delegation
        - factory: the URLStreamHandlerFactory to use when creating URLs

        Raises
        - IllegalArgumentException: if the given name is empty.
        - NullPointerException: if `urls` or any of its
                elements is `null`.
        - SecurityException: if a security manager exists and its
                `checkCreateClassLoader` method doesn't allow
                creation of a class loader.

        Since
        - 9
        """
        ...


    def getResourceAsStream(self, name: str) -> "InputStream":
        """
        Returns an input stream for reading the specified resource.
        If this loader is closed, then any resources opened by this method
        will be closed.
        
         The search order is described in the documentation for .getResource(String).  

        Arguments
        - name: The resource name

        Returns
        - An input stream for reading the resource, or `null`
                 if the resource could not be found

        Raises
        - NullPointerException: If `name` is `null`

        Since
        - 1.7
        """
        ...


    def close(self) -> None:
        """
        Closes this URLClassLoader, so that it can no longer be used to load
        new classes or resources that are defined by this loader.
        Classes and resources defined by any of this loader's parents in the
        delegation hierarchy are still accessible. Also, any classes or resources
        that are already loaded, are still accessible.
        
        In the case of jar: and file: URLs, it also closes any files
        that were opened by it. If another thread is loading a
        class when the `close` method is invoked, then the result of
        that load is undefined.
        
        The method makes a best effort attempt to close all opened files,
        by catching IOExceptions internally. Unchecked exceptions
        and errors are not caught. Calling close on an already closed
        loader has no effect.

        Raises
        - IOException: if closing any file opened by this class loader
        resulted in an IOException. Any such exceptions are caught internally.
        If only one is caught, then it is re-thrown. If more than one exception
        is caught, then the second and following exceptions are added
        as suppressed exceptions of the first one caught, which is then re-thrown.
        - SecurityException: if a security manager is set, and it denies
          RuntimePermission`("closeClassLoader")`

        Since
        - 1.7
        """
        ...


    def getURLs(self) -> list["URL"]:
        """
        Returns the search path of URLs for loading classes and resources.
        This includes the original list of URLs specified to the constructor,
        along with any URLs subsequently appended by the addURL() method.

        Returns
        - the search path of URLs for loading classes and resources.
        """
        ...


    def findResource(self, name: str) -> "URL":
        """
        Finds the resource with the specified name on the URL search path.

        Arguments
        - name: the name of the resource

        Returns
        - a `URL` for the resource, or `null`
        if the resource could not be found, or if the loader is closed.
        """
        ...


    def findResources(self, name: str) -> "Enumeration"["URL"]:
        """
        Returns an Enumeration of URLs representing all of the resources
        on the URL search path having the specified name.

        Arguments
        - name: the resource name

        Returns
        - An `Enumeration` of `URL`s.
                If the loader is closed, the Enumeration contains no elements.

        Raises
        - IOException: if an I/O exception occurs
        """
        ...


    @staticmethod
    def newInstance(urls: list["URL"], parent: "ClassLoader") -> "URLClassLoader":
        """
        Creates a new instance of URLClassLoader for the specified
        URLs and parent class loader. If a security manager is
        installed, the `loadClass` method of the URLClassLoader
        returned by this method will invoke the
        `SecurityManager.checkPackageAccess` method before
        loading the class.

        Arguments
        - urls: the URLs to search for classes and resources
        - parent: the parent class loader for delegation

        Returns
        - the resulting class loader

        Raises
        - NullPointerException: if `urls` or any of its
                    elements is `null`.
        """
        ...


    @staticmethod
    def newInstance(urls: list["URL"]) -> "URLClassLoader":
        """
        Creates a new instance of URLClassLoader for the specified
        URLs and default parent class loader. If a security manager is
        installed, the `loadClass` method of the URLClassLoader
        returned by this method will invoke the
        `SecurityManager.checkPackageAccess` before
        loading the class.

        Arguments
        - urls: the URLs to search for classes and resources

        Returns
        - the resulting class loader

        Raises
        - NullPointerException: if `urls` or any of its
                    elements is `null`.
        """
        ...
