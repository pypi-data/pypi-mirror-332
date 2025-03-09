"""
Python module generated from Java source file java.nio.file.FileSystems

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import IOException
from java.lang.reflect import Constructor
from java.net import URI
from java.nio.file import *
from java.nio.file.spi import FileSystemProvider
from java.security import AccessController
from java.security import PrivilegedAction
from java.util import Collections
from java.util import ServiceConfigurationError
from java.util import ServiceLoader
from jdk.internal.misc import VM
from sun.nio.fs import DefaultFileSystemProvider
from typing import Any, Callable, Iterable, Tuple


class FileSystems:

    @staticmethod
    def getDefault() -> "FileSystem":
        """
        Returns the default `FileSystem`. The default file system creates
        objects that provide access to the file systems accessible to the Java
        virtual machine. The *working directory* of the file system is
        the current user directory, named by the system property `user.dir`.
        This allows for interoperability with the java.io.File java.io.File
        class.
        
         The first invocation of any of the methods defined by this class
        locates the default FileSystemProvider provider object. Where the
        system property `java.nio.file.spi.DefaultFileSystemProvider` is
        not defined then the default provider is a system-default provider that
        is invoked to create the default file system.
        
         If the system property `java.nio.file.spi.DefaultFileSystemProvider`
        is defined then it is taken to be a list of one or more fully-qualified
        names of concrete provider classes identified by the URI scheme
        `"file"`. Where the property is a list of more than one name then
        the names are separated by a comma. Each class is loaded, using the system
        class loader, and instantiated by invoking a one argument constructor
        whose formal parameter type is `FileSystemProvider`. The providers
        are loaded and instantiated in the order they are listed in the property.
        If this process fails or a provider's scheme is not equal to `"file"`
        then an unspecified error is thrown. URI schemes are normally compared
        without regard to case but for the default provider, the scheme is
        required to be `"file"`. The first provider class is instantiated
        by invoking it with a reference to the system-default provider.
        The second provider class is instantiated by invoking it with a reference
        to the first provider instance. The third provider class is instantiated
        by invoking it with a reference to the second instance, and so on. The
        last provider to be instantiated becomes the default provider; its `getFileSystem` method is invoked with the URI `"file:///"` to
        get a reference to the default file system.
        
         Subsequent invocations of this method return the file system that was
        returned by the first invocation.

        Returns
        - the default file system
        """
        ...


    @staticmethod
    def getFileSystem(uri: "URI") -> "FileSystem":
        """
        Returns a reference to an existing `FileSystem`.
        
         This method iterates over the FileSystemProvider.installedProviders()
        installed providers to locate the provider that is identified by the URI
        URI.getScheme scheme of the given URI. URI schemes are compared
        without regard to case. The exact form of the URI is highly provider
        dependent. If found, the provider's FileSystemProvider.getFileSystem
        getFileSystem method is invoked to obtain a reference to the `FileSystem`.
        
         Once a file system created by this provider is FileSystem.close
        closed it is provider-dependent if this method returns a reference to
        the closed file system or throws FileSystemNotFoundException.
        If the provider allows a new file system to be created with the same URI
        as a file system it previously created then this method throws the
        exception if invoked after the file system is closed (and before a new
        instance is created by the .newFileSystem newFileSystem method).
        
         If a security manager is installed then a provider implementation
        may require to check a permission before returning a reference to an
        existing file system. In the case of the FileSystems.getDefault
        default file system, no permission check is required.

        Arguments
        - uri: the URI to locate the file system

        Returns
        - the reference to the file system

        Raises
        - IllegalArgumentException: if the pre-conditions for the `uri` parameter are not met
        - FileSystemNotFoundException: if the file system, identified by the URI, does not exist
        - ProviderNotFoundException: if a provider supporting the URI scheme is not installed
        - SecurityException: if a security manager is installed and it denies an unspecified
                 permission
        """
        ...


    @staticmethod
    def newFileSystem(uri: "URI", env: dict[str, Any]) -> "FileSystem":
        """
        Constructs a new file system that is identified by a URI
        
         This method iterates over the FileSystemProvider.installedProviders()
        installed providers to locate the provider that is identified by the URI
        URI.getScheme scheme of the given URI. URI schemes are compared
        without regard to case. The exact form of the URI is highly provider
        dependent. If found, the provider's FileSystemProvider.newFileSystem(URI,Map)
        newFileSystem(URI,Map) method is invoked to construct the new file system.
        
         Once a file system is FileSystem.close closed it is
        provider-dependent if the provider allows a new file system to be created
        with the same URI as a file system it previously created.
        
         **Usage Example:**
        Suppose there is a provider identified by the scheme `"memory"`
        installed:
        ```
         FileSystem fs = FileSystems.newFileSystem(URI.create("memory:///?name=logfs"),
                                                   Map.of("capacity", "16G", "blockSize", "4k"));
        ```

        Arguments
        - uri: the URI identifying the file system
        - env: a map of provider specific properties to configure the file system;
                 may be empty

        Returns
        - a new file system

        Raises
        - IllegalArgumentException: if the pre-conditions for the `uri` parameter are not met,
                 or the `env` parameter does not contain properties required
                 by the provider, or a property value is invalid
        - FileSystemAlreadyExistsException: if the file system has already been created
        - ProviderNotFoundException: if a provider supporting the URI scheme is not installed
        - IOException: if an I/O error occurs creating the file system
        - SecurityException: if a security manager is installed and it denies an unspecified
                 permission required by the file system provider implementation
        """
        ...


    @staticmethod
    def newFileSystem(uri: "URI", env: dict[str, Any], loader: "ClassLoader") -> "FileSystem":
        """
        Constructs a new file system that is identified by a URI
        
         This method first attempts to locate an installed provider in exactly
        the same manner as the .newFileSystem(URI,Map) newFileSystem(URI,Map)
        method. If none of the installed providers support the URI scheme then an
        attempt is made to locate the provider using the given class loader. If a
        provider supporting the URI scheme is located then its FileSystemProvider.newFileSystem(URI,Map) newFileSystem(URI,Map) is
        invoked to construct the new file system.

        Arguments
        - uri: the URI identifying the file system
        - env: a map of provider specific properties to configure the file system;
                 may be empty
        - loader: the class loader to locate the provider or `null` to only
                 attempt to locate an installed provider

        Returns
        - a new file system

        Raises
        - IllegalArgumentException: if the pre-conditions for the `uri` parameter are not met,
                 or the `env` parameter does not contain properties required
                 by the provider, or a property value is invalid
        - FileSystemAlreadyExistsException: if the URI scheme identifies an installed provider and the file
                 system has already been created
        - ProviderNotFoundException: if a provider supporting the URI scheme is not found
        - ServiceConfigurationError: when an error occurs while loading a service provider
        - IOException: an I/O error occurs creating the file system
        - SecurityException: if a security manager is installed and it denies an unspecified
                 permission required by the file system provider implementation
        """
        ...


    @staticmethod
    def newFileSystem(path: "Path", loader: "ClassLoader") -> "FileSystem":
        """
        Constructs a new `FileSystem` to access the contents of a file as a
        file system.
        
         This method makes use of specialized providers that create pseudo file
        systems where the contents of one or more files is treated as a file
        system.
        
         This method first attempts to locate an installed provider in exactly
        the same manner as the .newFileSystem(Path, Map, ClassLoader)
        newFileSystem(Path, Map, ClassLoader) method with an empty map. If none
        of the installed providers return a `FileSystem` then an attempt is
        made to locate the provider using the given class loader. If a provider
        returns a file system then the lookup terminates and the file system is
        returned.

        Arguments
        - path: the path to the file
        - loader: the class loader to locate the provider or `null` to only
                 attempt to locate an installed provider

        Returns
        - a new file system

        Raises
        - ProviderNotFoundException: if a provider supporting this file type cannot be located
        - ServiceConfigurationError: when an error occurs while loading a service provider
        - IOException: if an I/O error occurs
        - SecurityException: if a security manager is installed and it denies an unspecified
                 permission
        """
        ...


    @staticmethod
    def newFileSystem(path: "Path", env: dict[str, Any]) -> "FileSystem":
        """
        Constructs a new `FileSystem` to access the contents of a file as a
        file system.
        
         This method makes use of specialized providers that create pseudo file
        systems where the contents of one or more files is treated as a file
        system.
        
         This method first attempts to locate an installed provider in exactly
        the same manner as the .newFileSystem(Path,Map,ClassLoader)
        newFileSystem(Path, Map, ClassLoader) method. If found, the provider's
        FileSystemProvider.newFileSystem(Path, Map) newFileSystem(Path, Map)
        method is invoked to construct the new file system.

        Arguments
        - path: the path to the file
        - env: a map of provider specific properties to configure the file system;
                 may be empty

        Returns
        - a new file system

        Raises
        - ProviderNotFoundException: if a provider supporting this file type cannot be located
        - ServiceConfigurationError: when an error occurs while loading a service provider
        - IOException: if an I/O error occurs
        - SecurityException: if a security manager is installed and it denies an unspecified
                 permission

        Since
        - 13
        """
        ...


    @staticmethod
    def newFileSystem(path: "Path") -> "FileSystem":
        """
        Constructs a new `FileSystem` to access the contents of a file as a
        file system.
        
         This method makes use of specialized providers that create pseudo file
        systems where the contents of one or more files is treated as a file
        system.
        
         This method first attempts to locate an installed provider in exactly
        the same manner as the .newFileSystem(Path,Map,ClassLoader)
        newFileSystem(Path, Map, ClassLoader) method. If found, the provider's
        FileSystemProvider.newFileSystem(Path, Map) newFileSystem(Path, Map)
        method is invoked with an empty map to construct the new file system.

        Arguments
        - path: the path to the file

        Returns
        - a new file system

        Raises
        - ProviderNotFoundException: if a provider supporting this file type cannot be located
        - ServiceConfigurationError: when an error occurs while loading a service provider
        - IOException: if an I/O error occurs
        - SecurityException: if a security manager is installed and it denies an unspecified
                 permission

        Since
        - 13
        """
        ...


    @staticmethod
    def newFileSystem(path: "Path", env: dict[str, Any], loader: "ClassLoader") -> "FileSystem":
        """
        Constructs a new `FileSystem` to access the contents of a file as a
        file system.
        
         This method makes use of specialized providers that create pseudo file
        systems where the contents of one or more files is treated as a file
        system.
        
         This method iterates over the FileSystemProvider.installedProviders()
        installed providers. It invokes, in turn, each provider's FileSystemProvider.newFileSystem(Path,Map) newFileSystem(Path,Map)
        method. If a provider returns a file system then the iteration
        terminates and the file system is returned.
        If none of the installed providers return a `FileSystem` then
        an attempt is made to locate the provider using the given class loader.
        If a provider returns a file
        system, then the lookup terminates and the file system is returned.

        Arguments
        - path: the path to the file
        - env: a map of provider specific properties to configure the file system;
                 may be empty
        - loader: the class loader to locate the provider or `null` to only
                 attempt to locate an installed provider

        Returns
        - a new file system

        Raises
        - ProviderNotFoundException: if a provider supporting this file type cannot be located
        - ServiceConfigurationError: when an error occurs while loading a service provider
        - IOException: if an I/O error occurs
        - SecurityException: if a security manager is installed and it denies an unspecified
                 permission

        Since
        - 13
        """
        ...
