"""
Python module generated from Java source file java.util.ServiceLoader

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import BufferedReader
from java.io import IOException
from java.io import InputStream
from java.io import InputStreamReader
from java.lang.reflect import Constructor
from java.lang.reflect import InvocationTargetException
from java.lang.reflect import Method
from java.lang.reflect import Modifier
from java.net import URL
from java.net import URLConnection
from java.security import AccessControlContext
from java.security import AccessController
from java.security import PrivilegedAction
from java.security import PrivilegedActionException
from java.security import PrivilegedExceptionAction
from java.util import *
from java.util.function import Consumer
from java.util.function import Supplier
from java.util.stream import Stream
from java.util.stream import StreamSupport
from jdk.internal.access import JavaLangAccess
from jdk.internal.access import SharedSecrets
from jdk.internal.loader import BootLoader
from jdk.internal.loader import ClassLoaders
from jdk.internal.misc import VM
from jdk.internal.module import ServicesCatalog
from jdk.internal.module.ServicesCatalog import ServiceProvider
from jdk.internal.reflect import CallerSensitive
from jdk.internal.reflect import Reflection
from sun.nio.cs import UTF_8
from typing import Any, Callable, Iterable, Tuple


class ServiceLoader(Iterable):

    def iterator(self) -> Iterator["S"]:
        """
        Returns an iterator to lazily load and instantiate the available
        providers of this loader's service.
        
         To achieve laziness the actual work of locating and instantiating
        providers is done by the iterator itself. Its Iterator.hasNext
        hasNext and Iterator.next next methods can therefore throw a
        ServiceConfigurationError for any of the reasons specified in
        the <a href="#errors">Errors</a> section above. To write robust code it
        is only necessary to catch `ServiceConfigurationError` when using
        the iterator. If an error is thrown then subsequent invocations of the
        iterator will make a best effort to locate and instantiate the next
        available provider, but in general such recovery cannot be guaranteed.
        
         Caching: The iterator returned by this method first yields all of
        the elements of the provider cache, in the order that they were loaded.
        It then lazily loads and instantiates any remaining service providers,
        adding each one to the cache in turn. If this loader's provider caches are
        cleared by invoking the .reload() reload method then existing
        iterators for this service loader should be discarded.
        The `hasNext` and `next` methods of the iterator throw java.util.ConcurrentModificationException ConcurrentModificationException
        if used after the provider cache has been cleared.
        
         The iterator returned by this method does not support removal.
        Invoking its java.util.Iterator.remove() remove method will
        cause an UnsupportedOperationException to be thrown.

        Returns
        - An iterator that lazily loads providers for this loader's
                 service

        Unknown Tags
        - Throwing an error in these cases may seem extreme.  The rationale
        for this behavior is that a malformed provider-configuration file, like a
        malformed class file, indicates a serious problem with the way the Java
        virtual machine is configured or is being used.  As such it is preferable
        to throw an error rather than try to recover or, even worse, fail silently.
        - 9
        """
        ...


    def stream(self) -> "Stream"["Provider"["S"]]:
        """
        Returns a stream to lazily load available providers of this loader's
        service. The stream elements are of type Provider Provider, the
        `Provider`'s Provider.get() get method must be invoked to
        get or instantiate the provider.
        
         To achieve laziness the actual work of locating providers is done
        when processing the stream. If a service provider cannot be loaded for any
        of the reasons specified in the <a href="#errors">Errors</a> section
        above then ServiceConfigurationError is thrown by whatever method
        caused the service provider to be loaded. 
        
         Caching: When processing the stream then providers that were previously
        loaded by stream operations are processed first, in load order. It then
        lazily loads any remaining service providers. If this loader's provider
        caches are cleared by invoking the .reload() reload method then
        existing streams for this service loader should be discarded. The returned
        stream's source Spliterator spliterator is *fail-fast* and
        will throw ConcurrentModificationException if the provider cache
        has been cleared. 
        
         The following examples demonstrate usage. The first example creates
        a stream of `CodecFactory` objects, the second example is the same
        except that it sorts the providers by provider class name (and so locate
        all providers).
        ````Stream<CodecFactory> providers = ServiceLoader.load(CodecFactory.class)
                   .stream()
                   .map(Provider::get);
        
           Stream<CodecFactory> providers = ServiceLoader.load(CodecFactory.class)
                   .stream()
                   .sorted(Comparator.comparing(p -> p.type().getName()))
                   .map(Provider::get);````

        Returns
        - A stream that lazily loads providers for this loader's service

        Since
        - 9
        """
        ...


    @staticmethod
    def load(service: type["S"], loader: "ClassLoader") -> "ServiceLoader"["S"]:
        """
        Creates a new service loader for the given service. The service loader
        uses the given class loader as the starting point to locate service
        providers for the service. The service loader's .iterator()
        iterator and .stream() stream locate providers in both named
        and unnamed modules, as follows:
        
        
          -   Step 1: Locate providers in named modules. 
        
           Service providers are located in all named modules of the class
          loader or to any class loader reachable via parent delegation. 
        
           In addition, if the class loader is not the bootstrap or ClassLoader.getPlatformClassLoader() platform class loader, then service
          providers may be located in the named modules of other class loaders.
          Specifically, if the class loader, or any class loader reachable via
          parent delegation, has a module in a ModuleLayer module
          layer, then service providers in all modules in the module layer are
          located.  
        
           For example, suppose there is a module layer where each module is
          in its own class loader (see ModuleLayer.defineModulesWithManyLoaders
          defineModulesWithManyLoaders). If this `ServiceLoader.load` method
          is invoked to locate providers using any of the class loaders created for
          the module layer, then it will locate all of the providers in the module
          layer, irrespective of their defining class loader. 
        
           Ordering: The service loader will first locate any service providers
          in modules defined to the class loader, then its parent class loader,
          its parent parent, and so on to the bootstrap class loader. If a class
          loader has modules in a module layer then all providers in that module
          layer are located (irrespective of their class loader) before the
          providers in the parent class loader are located. The ordering of
          modules in same class loader, or the ordering of modules in a module
          layer, is not defined. 
        
           If a module declares more than one provider then the providers
          are located in the order that its module descriptor java.lang.module.ModuleDescriptor.Provides.providers() lists the
          providers. Providers added dynamically by instrumentation agents (see
          java.lang.instrument.Instrumentation.redefineModule redefineModule)
          are always located after providers declared by the module.  
        
          -   Step 2: Locate providers in unnamed modules. 
        
           Service providers in unnamed modules are located if their class names
          are listed in provider-configuration files located by the class loader's
          ClassLoader.getResources(String) getResources method. 
        
           The ordering is based on the order that the class loader's `getResources` method finds the service configuration files and within
          that, the order that the class names are listed in the file. 
        
           In a provider-configuration file, any mention of a service provider
          that is deployed in a named module is ignored. This is to avoid
          duplicates that would otherwise arise when a named module has both a
          *provides* directive and a provider-configuration file that mention
          the same service provider. 
        
           The provider class must be visible to the class loader.  
        
        
        
        Type `<S>`: the class of the service type

        Arguments
        - service: The interface or abstract class representing the service
        - loader: The class loader to be used to load provider-configuration files
                and provider classes, or `null` if the system class
                loader (or, failing that, the bootstrap class loader) is to be
                used

        Returns
        - A new service loader

        Raises
        - ServiceConfigurationError: if the service type is not accessible to the caller or the
                caller is in an explicit module and its module descriptor does
                not declare that it uses `service`

        Unknown Tags
        - If the class path of the class loader includes remote network
        URLs then those URLs may be dereferenced in the process of searching for
        provider-configuration files.
        
         This activity is normal, although it may cause puzzling entries to be
        created in web-server logs.  If a web server is not configured correctly,
        however, then this activity may cause the provider-loading algorithm to fail
        spuriously.
        
         A web server should return an HTTP 404 (Not Found) response when a
        requested resource does not exist.  Sometimes, however, web servers are
        erroneously configured to return an HTTP 200 (OK) response along with a
        helpful HTML error page in such cases.  This will cause a ServiceConfigurationError to be thrown when this class attempts to parse
        the HTML page as a provider-configuration file.  The best solution to this
        problem is to fix the misconfigured web server to return the correct
        response code (HTTP 404) along with the HTML error page.
        - 9
        """
        ...


    @staticmethod
    def load(service: type["S"]) -> "ServiceLoader"["S"]:
        """
        Creates a new service loader for the given service type, using the
        current thread's java.lang.Thread.getContextClassLoader
        context class loader.
        
         An invocation of this convenience method of the form
        ````ServiceLoader.load(service)````
        
        is equivalent to
        
        ````ServiceLoader.load(service, Thread.currentThread().getContextClassLoader())````
        
        Type `<S>`: the class of the service type

        Arguments
        - service: The interface or abstract class representing the service

        Returns
        - A new service loader

        Raises
        - ServiceConfigurationError: if the service type is not accessible to the caller or the
                caller is in an explicit module and its module descriptor does
                not declare that it uses `service`

        Unknown Tags
        - Service loader objects obtained with this method should not be
        cached VM-wide. For example, different applications in the same VM may
        have different thread context class loaders. A lookup by one application
        may locate a service provider that is only visible via its thread
        context class loader and so is not suitable to be located by the other
        application. Memory leaks can also arise. A thread local may be suited
        to some applications.
        - 9
        """
        ...


    @staticmethod
    def loadInstalled(service: type["S"]) -> "ServiceLoader"["S"]:
        """
        Creates a new service loader for the given service type, using the
        ClassLoader.getPlatformClassLoader() platform class loader.
        
         This convenience method is equivalent to: 
        
        ````ServiceLoader.load(service, ClassLoader.getPlatformClassLoader())````
        
         This method is intended for use when only installed providers are
        desired.  The resulting service will only find and load providers that
        have been installed into the current Java virtual machine; providers on
        the application's module path or class path will be ignored.
        
        Type `<S>`: the class of the service type

        Arguments
        - service: The interface or abstract class representing the service

        Returns
        - A new service loader

        Raises
        - ServiceConfigurationError: if the service type is not accessible to the caller or the
                caller is in an explicit module and its module descriptor does
                not declare that it uses `service`

        Unknown Tags
        - 9
        """
        ...


    @staticmethod
    def load(layer: "ModuleLayer", service: type["S"]) -> "ServiceLoader"["S"]:
        """
        Creates a new service loader for the given service type to load service
        providers from modules in the given module layer and its ancestors. It
        does not locate providers in unnamed modules. The ordering that the service
        loader's .iterator() iterator and .stream() stream locate
        providers and yield elements is as follows:
        
        
          -  Providers are located in a module layer before locating providers
          in parent layers. Traversal of parent layers is depth-first with each
          layer visited at most once. For example, suppose L0 is the boot layer, L1
          and L2 are modules layers with L0 as their parent. Now suppose that L3 is
          created with L1 and L2 as the parents (in that order). Using a service
          loader to locate providers with L3 as the context will locate providers
          in the following order: L3, L1, L0, L2. 
        
          -  If a module declares more than one provider then the providers
          are located in the order that its module descriptor
          java.lang.module.ModuleDescriptor.Provides.providers()
          lists the providers. Providers added dynamically by instrumentation
          agents are always located after providers declared by the module. 
        
          -  The ordering of modules in a module layer is not defined. 
        
        
        Type `<S>`: the class of the service type

        Arguments
        - layer: The module layer
        - service: The interface or abstract class representing the service

        Returns
        - A new service loader

        Raises
        - ServiceConfigurationError: if the service type is not accessible to the caller or the
                caller is in an explicit module and its module descriptor does
                not declare that it uses `service`

        Since
        - 9

        Unknown Tags
        - Unlike the other load methods defined here, the service type
        is the second parameter. The reason for this is to avoid source
        compatibility issues for code that uses `load(S, null)`.
        """
        ...


    def findFirst(self) -> "Optional"["S"]:
        """
        Load the first available service provider of this loader's service. This
        convenience method is equivalent to invoking the .iterator()
        iterator() method and obtaining the first element. It therefore
        returns the first element from the provider cache if possible, it
        otherwise attempts to load and instantiate the first provider.
        
         The following example loads the first available service provider. If
        no service providers are located then it uses a default implementation.
        ````CodecFactory factory = ServiceLoader.load(CodecFactory.class)
                                               .findFirst()
                                               .orElse(DEFAULT_CODECSET_FACTORY);````

        Returns
        - The first service provider or empty `Optional` if no
                service providers are located

        Raises
        - ServiceConfigurationError: If a provider class cannot be loaded for any of the reasons
                specified in the <a href="#errors">Errors</a> section above.

        Since
        - 9
        """
        ...


    def reload(self) -> None:
        """
        Clear this loader's provider cache so that all providers will be
        reloaded.
        
         After invoking this method, subsequent invocations of the .iterator() iterator or .stream() stream methods will lazily
        locate providers (and instantiate in the case of `iterator`)
        from scratch, just as is done by a newly-created service loader.
        
         This method is intended for use in situations in which new service
        providers can be installed into a running Java virtual machine.
        """
        ...


    def toString(self) -> str:
        """
        Returns a string describing this service.

        Returns
        - A descriptive string
        """
        ...


    class Provider(Supplier):
        """
        Represents a service provider located by `ServiceLoader`.
        
         When using a loader's ServiceLoader.stream() stream() method
        then the elements are of type `Provider`. This allows processing
        to select or filter on the provider class without instantiating the
        provider. 
        
        Type `<S>`: The service type

        Since
        - 9
        """

        def type(self) -> type["S"]:
            """
            Returns the provider type. There is no guarantee that this type is
            accessible or that it has a public no-args constructor. The .get() get() method should be used to obtain the provider instance.
            
             When a module declares that the provider class is created by a
            provider factory then this method returns the return type of its
            public static "`provider()`" method.

            Returns
            - The provider type
            """
            ...


        def get(self) -> "S":
            """
            Returns an instance of the provider.

            Returns
            - An instance of the provider.

            Raises
            - ServiceConfigurationError: If the service provider cannot be instantiated, or in the
                    case of a provider factory, the public static
                    "`provider()`" method returns `null` or throws
                    an error or exception. The `ServiceConfigurationError`
                    will carry an appropriate cause where possible.
            """
            ...
