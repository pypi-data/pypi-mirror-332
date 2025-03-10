"""
Python module generated from Java source file java.util.ResourceBundle

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import IOException
from java.io import InputStream
from java.io import UncheckedIOException
from java.lang.ref import Reference
from java.lang.ref import ReferenceQueue
from java.lang.ref import SoftReference
from java.lang.ref import WeakReference
from java.lang.reflect import Constructor
from java.lang.reflect import InvocationTargetException
from java.lang.reflect import Modifier
from java.net import JarURLConnection
from java.net import URL
from java.net import URLConnection
from java.security import AccessController
from java.security import PrivilegedAction
from java.security import PrivilegedActionException
from java.security import PrivilegedExceptionAction
from java.util import *
from java.util.concurrent import ConcurrentHashMap
from java.util.concurrent import ConcurrentMap
from java.util.jar import JarEntry
from java.util.spi import ResourceBundleControlProvider
from java.util.spi import ResourceBundleProvider
from java.util.stream import Stream
from jdk.internal.access import JavaUtilResourceBundleAccess
from jdk.internal.access import SharedSecrets
from jdk.internal.loader import BootLoader
from jdk.internal.reflect import CallerSensitive
from jdk.internal.reflect import Reflection
from sun.security.action import GetPropertyAction
from sun.util.locale import BaseLocale
from sun.util.locale import LocaleObjectCache
from sun.util.resources import Bundles
from typing import Any, Callable, Iterable, Tuple


class ResourceBundle:
    """
    Resource bundles contain locale-specific objects.  When your program needs a
    locale-specific resource, a `String` for example, your program can
    load it from the resource bundle that is appropriate for the current user's
    locale. In this way, you can write program code that is largely independent
    of the user's locale isolating most, if not all, of the locale-specific
    information in resource bundles.
    
    
    This allows you to write programs that can:
    <UL>
    <LI> be easily localized, or translated, into different languages
    <LI> handle multiple locales at once
    <LI> be easily modified later to support even more locales
    </UL>
    
    <P>
    Resource bundles belong to families whose members share a common base
    name, but whose names also have additional components that identify
    their locales. For example, the base name of a family of resource
    bundles might be "MyResources". The family should have a default
    resource bundle which simply has the same name as its family -
    "MyResources" - and will be used as the bundle of last resort if a
    specific locale is not supported. The family can then provide as
    many locale-specific members as needed, for example a German one
    named "MyResources_de".
    
    <P>
    Each resource bundle in a family contains the same items, but the items have
    been translated for the locale represented by that resource bundle.
    For example, both "MyResources" and "MyResources_de" may have a
    `String` that's used on a button for canceling operations.
    In "MyResources" the `String` may contain "Cancel" and in
    "MyResources_de" it may contain "Abbrechen".
    
    <P>
    If there are different resources for different countries, you
    can make specializations: for example, "MyResources_de_CH" contains objects for
    the German language (de) in Switzerland (CH). If you want to only
    modify some of the resources
    in the specialization, you can do so.
    
    <P>
    When your program needs a locale-specific object, it loads
    the `ResourceBundle` class using the
    .getBundle(java.lang.String, java.util.Locale) getBundle
    method:
    <blockquote>
    ```
    ResourceBundle myResources =
         ResourceBundle.getBundle("MyResources", currentLocale);
    ```
    </blockquote>
    
    <P>
    Resource bundles contain key/value pairs. The keys uniquely
    identify a locale-specific object in the bundle. Here's an
    example of a `ListResourceBundle` that contains
    two key/value pairs:
    <blockquote>
    ```
    public class MyResources extends ListResourceBundle {
        protected Object[][] getContents() {
            return new Object[][] {
                // LOCALIZE THE SECOND STRING OF EACH ARRAY (e.g., "OK")
                {"OkKey", "OK"},
                {"CancelKey", "Cancel"},
                // END OF MATERIAL TO LOCALIZE
           };
        }
    }
    ```
    </blockquote>
    Keys are always `String`s.
    In this example, the keys are "OkKey" and "CancelKey".
    In the above example, the values
    are also `String`s--"OK" and "Cancel"--but
    they don't have to be. The values can be any type of object.
    
    <P>
    You retrieve an object from resource bundle using the appropriate
    getter method. Because "OkKey" and "CancelKey"
    are both strings, you would use `getString` to retrieve them:
    <blockquote>
    ```
    button1 = new Button(myResources.getString("OkKey"));
    button2 = new Button(myResources.getString("CancelKey"));
    ```
    </blockquote>
    The getter methods all require the key as an argument and return
    the object if found. If the object is not found, the getter method
    throws a `MissingResourceException`.
    
    <P>
    Besides `getString`, `ResourceBundle` also provides
    a method for getting string arrays, `getStringArray`,
    as well as a generic `getObject` method for any other
    type of object. When using `getObject`, you'll
    have to cast the result to the appropriate type. For example:
    <blockquote>
    ```
    int[] myIntegers = (int[]) myResources.getObject("intList");
    ```
    </blockquote>
    
    <P>
    The Java Platform provides two subclasses of `ResourceBundle`,
    `ListResourceBundle` and `PropertyResourceBundle`,
    that provide a fairly simple way to create resources.
    As you saw briefly in a previous example, `ListResourceBundle`
    manages its resource as a list of key/value pairs.
    `PropertyResourceBundle` uses a properties file to manage
    its resources.
    
    
    If `ListResourceBundle` or `PropertyResourceBundle`
    do not suit your needs, you can write your own `ResourceBundle`
    subclass.  Your subclasses must override two methods: `handleGetObject`
    and `getKeys()`.
    
    
    The implementation of a `ResourceBundle` subclass must be thread-safe
    if it's simultaneously used by multiple threads. The default implementations
    of the non-abstract methods in this class, and the methods in the direct
    known concrete subclasses `ListResourceBundle` and
    `PropertyResourceBundle` are thread-safe.
    
    <h2><a id="resource-bundle-modules">Resource Bundles and Named Modules</a></h2>
    
    Resource bundles can be deployed in modules in the following ways:
    
    <h3>Resource bundles together with an application</h3>
    
    Resource bundles can be deployed together with an application in the same
    module.  In that case, the resource bundles are loaded
    by code in the module by calling the .getBundle(String)
    or .getBundle(String, Locale) method.
    
    <h3><a id="service-providers">Resource bundles as service providers</a></h3>
    
    Resource bundles can be deployed in one or more *service provider modules*
    and they can be located using ServiceLoader.
    A ResourceBundleProvider service interface or class must be
    defined. The caller module declares that it uses the service, the service
    provider modules declare that they provide implementations of the service.
    Refer to ResourceBundleProvider for developing resource bundle
    services and deploying resource bundle providers.
    The module obtaining the resource bundle can be a resource bundle
    provider itself; in which case this module only locates the resource bundle
    via service provider mechanism.
    
    A ResourceBundleProvider resource bundle provider can
    provide resource bundles in any format such XML which replaces the need
    of Control ResourceBundle.Control.
    
    <h3><a id="other-modules">Resource bundles in other modules and class path</a></h3>
    
    Resource bundles in a named module may be *encapsulated* so that
    it cannot be located by code in other modules.  Resource bundles
    in unnamed modules and class path are open for any module to access.
    Resource bundle follows the resource encapsulation rules as specified
    in Module.getResourceAsStream(String).
    
    The `getBundle` factory methods with no `Control` parameter
    locate and load resource bundles from
    ResourceBundleProvider service providers.
    It may continue the search as if calling Module.getResourceAsStream(String)
    to find the named resource from a given module and calling
    ClassLoader.getResourceAsStream(String); refer to
    the specification of the `getBundle` method for details.
    Only non-encapsulated resource bundles of "`java.class`"
    or "`java.properties`" format are searched.
    
    If the caller module is a
    <a href="/java.base/java/util/spi/ResourceBundleProvider.html#obtain-resource-bundle">
    resource bundle provider</a>, it does not fall back to the
    class loader search.
    
    <h3>Resource bundles in automatic modules</h3>
    
    A common format of resource bundles is in PropertyResourceBundle
    .properties file format.  Typically `.properties` resource bundles
    are packaged in a JAR file.  Resource bundle only JAR file can be readily
    deployed as an <a href="/java.base/java/lang/module/ModuleFinder.html#automatic-modules">
    automatic module</a>.  For example, if the JAR file contains the
    entry "`p/q/Foo_ja.properties`" and no `.class` entry,
    when resolved and defined as an automatic module, no package is derived
    for this module.  This allows resource bundles in `.properties`
    format packaged in one or more JAR files that may contain entries
    in the same directory and can be resolved successfully as
    automatic modules.
    
    <h3>ResourceBundle.Control</h3>
    
    The ResourceBundle.Control class provides information necessary
    to perform the bundle loading process by the `getBundle`
    factory methods that take a `ResourceBundle.Control`
    instance. You can implement your own subclass in order to enable
    non-standard resource bundle formats, change the search strategy, or
    define caching parameters. Refer to the descriptions of the class and the
    .getBundle(String, Locale, ClassLoader, Control) getBundle
    factory method for details.
    
     ResourceBundle.Control is designed for an application deployed
    in an unnamed module, for example to support resource bundles in
    non-standard formats or package localized resources in a non-traditional
    convention. ResourceBundleProvider is the replacement for
    `ResourceBundle.Control` when migrating to modules.
    `UnsupportedOperationException` will be thrown when a factory
    method that takes the `ResourceBundle.Control` parameter is called.
    
    <a id="modify_default_behavior">For the `getBundle` factory</a>
    methods that take no Control instance, their <a
    href="#default_behavior"> default behavior</a> of resource bundle loading
    can be modified with custom ResourceBundleControlProvider implementations.
    If any of the
    providers provides a Control for the given base name, that Control will be used instead of the default Control. If there is
    more than one service provider for supporting the same base name,
    the first one returned from ServiceLoader will be used.
    A custom Control implementation is ignored by named modules.
    
    <h2>Cache Management</h2>
    
    Resource bundle instances created by the `getBundle` factory
    methods are cached by default, and the factory methods return the same
    resource bundle instance multiple times if it has been
    cached. `getBundle` clients may clear the cache, manage the
    lifetime of cached resource bundle instances using time-to-live values,
    or specify not to cache resource bundle instances. Refer to the
    descriptions of the .getBundle(String, Locale, ClassLoader,
    Control) {@code getBundle factory method}, .clearCache(ClassLoader) clearCache, Control.getTimeToLive(String, Locale)
    ResourceBundle.Control.getTimeToLive, and Control.needsReload(String, Locale, String, ClassLoader, ResourceBundle,
    long) ResourceBundle.Control.needsReload for details.
    
    <h2>Example</h2>
    
    The following is a very simple example of a `ResourceBundle`
    subclass, `MyResources`, that manages two resources (for a larger number of
    resources you would probably use a `Map`).
    Notice that you don't need to supply a value if
    a "parent-level" `ResourceBundle` handles the same
    key with the same value (as for the okKey below).
    <blockquote>
    ```
    // default (English language, United States)
    public class MyResources extends ResourceBundle {
        public Object handleGetObject(String key) {
            if (key.equals("okKey")) return "Ok";
            if (key.equals("cancelKey")) return "Cancel";
            return null;
        }
    
        public Enumeration&lt;String&gt; getKeys() {
            return Collections.enumeration(keySet());
        }
    
        // Overrides handleKeySet() so that the getKeys() implementation
        // can rely on the keySet() value.
        protected Set&lt;String&gt; handleKeySet() {
            return new HashSet&lt;String&gt;(Arrays.asList("okKey", "cancelKey"));
        }
    }
    
    // German language
    public class MyResources_de extends MyResources {
        public Object handleGetObject(String key) {
            // don't need okKey, since parent level handles it.
            if (key.equals("cancelKey")) return "Abbrechen";
            return null;
        }
    
        protected Set&lt;String&gt; handleKeySet() {
            return new HashSet&lt;String&gt;(Arrays.asList("cancelKey"));
        }
    }
    ```
    </blockquote>
    You do not have to restrict yourself to using a single family of
    `ResourceBundle`s. For example, you could have a set of bundles for
    exception messages, `ExceptionResources`
    (`ExceptionResources_fr`, `ExceptionResources_de`, ...),
    and one for widgets, `WidgetResource` (`WidgetResources_fr`,
    `WidgetResources_de`, ...); breaking up the resources however you like.

    See
    - ResourceBundleProvider

    Since
    - 1.1

    Unknown Tags
    - 9
    """

    def __init__(self):
        """
        Sole constructor.  (For invocation by subclass constructors, typically
        implicit.)
        """
        ...


    def getBaseBundleName(self) -> str:
        """
        Returns the base name of this bundle, if known, or `null` if unknown.
        
        If not null, then this is the value of the `baseName` parameter
        that was passed to the `ResourceBundle.getBundle(...)` method
        when the resource bundle was loaded.

        Returns
        - The base name of the resource bundle, as provided to and expected
        by the `ResourceBundle.getBundle(...)` methods.

        See
        - .getBundle(java.lang.String, java.util.Locale, java.lang.ClassLoader)

        Since
        - 1.8
        """
        ...


    def getString(self, key: str) -> str:
        """
        Gets a string for the given key from this resource bundle or one of its parents.
        Calling this method is equivalent to calling
        <blockquote>
        `(String) .getObject(java.lang.String) getObject(key)`.
        </blockquote>

        Arguments
        - key: the key for the desired string

        Returns
        - the string for the given key

        Raises
        - NullPointerException: if `key` is `null`
        - MissingResourceException: if no object for the given key can be found
        - ClassCastException: if the object found for the given key is not a string
        """
        ...


    def getStringArray(self, key: str) -> list[str]:
        """
        Gets a string array for the given key from this resource bundle or one of its parents.
        Calling this method is equivalent to calling
        <blockquote>
        `(String[]) .getObject(java.lang.String) getObject(key)`.
        </blockquote>

        Arguments
        - key: the key for the desired string array

        Returns
        - the string array for the given key

        Raises
        - NullPointerException: if `key` is `null`
        - MissingResourceException: if no object for the given key can be found
        - ClassCastException: if the object found for the given key is not a string array
        """
        ...


    def getObject(self, key: str) -> "Object":
        """
        Gets an object for the given key from this resource bundle or one of its parents.
        This method first tries to obtain the object from this resource bundle using
        .handleGetObject(java.lang.String) handleGetObject.
        If not successful, and the parent resource bundle is not null,
        it calls the parent's `getObject` method.
        If still not successful, it throws a MissingResourceException.

        Arguments
        - key: the key for the desired object

        Returns
        - the object for the given key

        Raises
        - NullPointerException: if `key` is `null`
        - MissingResourceException: if no object for the given key can be found
        """
        ...


    def getLocale(self) -> "Locale":
        """
        Returns the locale of this resource bundle. This method can be used after a
        call to getBundle() to determine whether the resource bundle returned really
        corresponds to the requested locale or is a fallback.

        Returns
        - the locale of this resource bundle
        """
        ...


    @staticmethod
    def getBundle(baseName: str) -> "ResourceBundle":
        """
        Gets a resource bundle using the specified base name, the default locale,
        and the caller module. Calling this method is equivalent to calling
        <blockquote>
        `getBundle(baseName, Locale.getDefault(), callerModule)`,
        </blockquote>

        Arguments
        - baseName: the base name of the resource bundle, a fully qualified class name

        Returns
        - a resource bundle for the given base name and the default locale

        Raises
        - java.lang.NullPointerException: if `baseName` is `null`
        - MissingResourceException: if no resource bundle for the specified base name can be found

        See
        - <a href=".resource-bundle-modules">Resource Bundles and Named Modules</a>
        """
        ...


    @staticmethod
    def getBundle(baseName: str, control: "Control") -> "ResourceBundle":
        """
        Returns a resource bundle using the specified base name, the
        default locale and the specified control. Calling this method
        is equivalent to calling
        ```
        getBundle(baseName, Locale.getDefault(),
                  this.getClass().getClassLoader(), control),
        ```
        except that `getClassLoader()` is run with the security
        privileges of `ResourceBundle`.  See .getBundle(String, Locale, ClassLoader, Control) getBundle for the
        complete description of the resource bundle loading process with a
        `ResourceBundle.Control`.

        Arguments
        - baseName: the base name of the resource bundle, a fully qualified class
               name
        - control: the control which gives information for the resource bundle
               loading process

        Returns
        - a resource bundle for the given base name and the default locale

        Raises
        - NullPointerException: if `baseName` or `control` is
                `null`
        - MissingResourceException: if no resource bundle for the specified base name can be found
        - IllegalArgumentException: if the given `control` doesn't perform properly
                (e.g., `control.getCandidateLocales` returns null.)
                Note that validation of `control` is performed as
                needed.
        - UnsupportedOperationException: if this method is called in a named module

        Since
        - 1.6

        Unknown Tags
        - 9
        """
        ...


    @staticmethod
    def getBundle(baseName: str, locale: "Locale") -> "ResourceBundle":
        """
        Gets a resource bundle using the specified base name and locale,
        and the caller module. Calling this method is equivalent to calling
        <blockquote>
        `getBundle(baseName, locale, callerModule)`,
        </blockquote>

        Arguments
        - baseName: the base name of the resource bundle, a fully qualified class name
        - locale: the locale for which a resource bundle is desired

        Returns
        - a resource bundle for the given base name and locale

        Raises
        - NullPointerException: if `baseName` or `locale` is `null`
        - MissingResourceException: if no resource bundle for the specified base name can be found

        See
        - <a href=".resource-bundle-modules">Resource Bundles and Named Modules</a>
        """
        ...


    @staticmethod
    def getBundle(baseName: str, module: "Module") -> "ResourceBundle":
        """
        Gets a resource bundle using the specified base name and the default locale
        on behalf of the specified module. This method is equivalent to calling
        <blockquote>
        `getBundle(baseName, Locale.getDefault(), module)`
        </blockquote>

        Arguments
        - baseName: the base name of the resource bundle,
                        a fully qualified class name
        - module: the module for which the resource bundle is searched

        Returns
        - a resource bundle for the given base name and the default locale

        Raises
        - NullPointerException: if `baseName` or `module` is `null`
        - SecurityException: if a security manager exists and the caller is not the specified
                module and doesn't have `RuntimePermission("getClassLoader")`
        - MissingResourceException: if no resource bundle for the specified base name can be found in the
                specified module

        See
        - <a href=".resource-bundle-modules">Resource Bundles and Named Modules</a>

        Since
        - 9
        """
        ...


    @staticmethod
    def getBundle(baseName: str, targetLocale: "Locale", module: "Module") -> "ResourceBundle":
        """
        Gets a resource bundle using the specified base name and locale
        on behalf of the specified module.
        
         Resource bundles in named modules may be encapsulated.  When
        the resource bundle is loaded from a
        ResourceBundleProvider service provider, the caller module
        must have an appropriate *uses* clause in its *module descriptor*
        to declare that the module uses of ResourceBundleProvider
        for the named resource bundle.
        Otherwise, it will load the resource bundles that are local in the
        given module as if calling Module.getResourceAsStream(String)
        or that are visible to the class loader of the given module
        as if calling ClassLoader.getResourceAsStream(String).
        When the resource bundle is loaded from the specified module, it is
        subject to the encapsulation rules specified by
        Module.getResourceAsStream Module.getResourceAsStream.
        
        
        If the given `module` is an unnamed module, then this method is
        equivalent to calling .getBundle(String, Locale, ClassLoader)
        getBundle(baseName, targetLocale, module.getClassLoader() to load
        resource bundles that are visible to the class loader of the given
        unnamed module. Custom java.util.spi.ResourceBundleControlProvider
        implementations, if present, will only be invoked if the specified
        module is an unnamed module.

        Arguments
        - baseName: the base name of the resource bundle,
                        a fully qualified class name
        - targetLocale: the locale for which a resource bundle is desired
        - module: the module for which the resource bundle is searched

        Returns
        - a resource bundle for the given base name and locale in the module

        Raises
        - NullPointerException: if `baseName`, `targetLocale`, or `module` is
                `null`
        - SecurityException: if a security manager exists and the caller is not the specified
                module and doesn't have `RuntimePermission("getClassLoader")`
        - MissingResourceException: if no resource bundle for the specified base name and locale can
                be found in the specified `module`

        See
        - <a href=".resource-bundle-modules">Resource Bundles and Named Modules</a>

        Since
        - 9
        """
        ...


    @staticmethod
    def getBundle(baseName: str, targetLocale: "Locale", control: "Control") -> "ResourceBundle":
        """
        Returns a resource bundle using the specified base name, target
        locale and control, and the caller's class loader. Calling this
        method is equivalent to calling
        ```
        getBundle(baseName, targetLocale, this.getClass().getClassLoader(),
                  control),
        ```
        except that `getClassLoader()` is run with the security
        privileges of `ResourceBundle`.  See .getBundle(String, Locale, ClassLoader, Control) getBundle for the
        complete description of the resource bundle loading process with a
        `ResourceBundle.Control`.

        Arguments
        - baseName: the base name of the resource bundle, a fully qualified
               class name
        - targetLocale: the locale for which a resource bundle is desired
        - control: the control which gives information for the resource
               bundle loading process

        Returns
        - a resource bundle for the given base name and a
                `Locale` in `locales`

        Raises
        - NullPointerException: if `baseName`, `locales` or
                `control` is `null`
        - MissingResourceException: if no resource bundle for the specified base name in any
                of the `locales` can be found.
        - IllegalArgumentException: if the given `control` doesn't perform properly
                (e.g., `control.getCandidateLocales` returns null.)
                Note that validation of `control` is performed as
                needed.
        - UnsupportedOperationException: if this method is called in a named module

        Since
        - 1.6

        Unknown Tags
        - 9
        """
        ...


    @staticmethod
    def getBundle(baseName: str, locale: "Locale", loader: "ClassLoader") -> "ResourceBundle":
        """
        Gets a resource bundle using the specified base name, locale, and class
        loader.
        
        When this method is called from a named module and the given
        loader is the class loader of the caller module, this is equivalent
        to calling:
        <blockquote>```
        getBundle(baseName, targetLocale, callerModule)
        ```</blockquote>
        
        otherwise, this is equivalent to calling:
        <blockquote>```
        getBundle(baseName, targetLocale, loader, control)
        ```</blockquote>
        where `control` is the default instance of Control unless
        a `Control` instance is provided by
        ResourceBundleControlProvider SPI.  Refer to the
        description of <a href="#modify_default_behavior">modifying the default
        behavior</a>. The following describes the default behavior.
        
        
        **<a id="default_behavior">Resource Bundle Search and Loading Strategy</a>**
        
        `getBundle` uses the base name, the specified locale, and
        the default locale (obtained from java.util.Locale.getDefault()
        Locale.getDefault) to generate a sequence of <a
        id="candidates">*candidate bundle names*</a>.  If the specified
        locale's language, script, country, and variant are all empty strings,
        then the base name is the only candidate bundle name.  Otherwise, a list
        of candidate locales is generated from the attribute values of the
        specified locale (language, script, country and variant) and appended to
        the base name.  Typically, this will look like the following:
        
        ```
            baseName + "_" + language + "_" + script + "_" + country + "_" + variant
            baseName + "_" + language + "_" + script + "_" + country
            baseName + "_" + language + "_" + script
            baseName + "_" + language + "_" + country + "_" + variant
            baseName + "_" + language + "_" + country
            baseName + "_" + language
        ```
        
        Candidate bundle names where the final component is an empty string
        are omitted, along with the underscore.  For example, if country is an
        empty string, the second and the fifth candidate bundle names above
        would be omitted.  Also, if script is an empty string, the candidate names
        including script are omitted.  For example, a locale with language "de"
        and variant "JAVA" will produce candidate names with base name
        "MyResource" below.
        
        ```
            MyResource_de__JAVA
            MyResource_de
        ```
        
        In the case that the variant contains one or more underscores ('_'), a
        sequence of bundle names generated by truncating the last underscore and
        the part following it is inserted after a candidate bundle name with the
        original variant.  For example, for a locale with language "en", script
        "Latn, country "US" and variant "WINDOWS_VISTA", and bundle base name
        "MyResource", the list of candidate bundle names below is generated:
        
        ```
        MyResource_en_Latn_US_WINDOWS_VISTA
        MyResource_en_Latn_US_WINDOWS
        MyResource_en_Latn_US
        MyResource_en_Latn
        MyResource_en_US_WINDOWS_VISTA
        MyResource_en_US_WINDOWS
        MyResource_en_US
        MyResource_en
        ```
        
        <blockquote>**Note:** For some `Locale`s, the list of
        candidate bundle names contains extra names, or the order of bundle names
        is slightly modified.  See the description of the default implementation
        of Control.getCandidateLocales(String, Locale)
        getCandidateLocales for details.</blockquote>
        
        `getBundle` then iterates over the candidate bundle names
        to find the first one for which it can *instantiate* an actual
        resource bundle. It uses the default controls' Control.getFormats
        getFormats method, which generates two bundle names for each generated
        name, the first a class name and the second a properties file name. For
        each candidate bundle name, it attempts to create a resource bundle:
        
        - First, it attempts to load a class using the generated class name.
        If such a class can be found and loaded using the specified class
        loader, is assignment compatible with ResourceBundle, is accessible from
        ResourceBundle, and can be instantiated, `getBundle` creates a
        new instance of this class and uses it as the *result resource
        bundle*.
        
        - Otherwise, `getBundle` attempts to locate a property
        resource file using the generated properties file name.  It generates a
        path name from the candidate bundle name by replacing all "." characters
        with "/" and appending the string ".properties".  It attempts to find a
        "resource" with this name using java.lang.ClassLoader.getResource(java.lang.String)
        ClassLoader.getResource.  (Note that a "resource" in the sense of
        `getResource` has nothing to do with the contents of a
        resource bundle, it is just a container of data, such as a file.)  If it
        finds a "resource", it attempts to create a new PropertyResourceBundle instance from its contents.  If successful, this
        instance becomes the *result resource bundle*.  
        
        This continues until a result resource bundle is instantiated or the
        list of candidate bundle names is exhausted.  If no matching resource
        bundle is found, the default control's Control.getFallbackLocale
        getFallbackLocale method is called, which returns the current default
        locale.  A new sequence of candidate locale names is generated using this
        locale and searched again, as above.
        
        If still no result bundle is found, the base name alone is looked up. If
        this still fails, a `MissingResourceException` is thrown.
        
        <a id="parent_chain"> Once a result resource bundle has been found,
        its *parent chain* is instantiated</a>.  If the result bundle already
        has a parent (perhaps because it was returned from a cache) the chain is
        complete.
        
        Otherwise, `getBundle` examines the remainder of the
        candidate locale list that was used during the pass that generated the
        result resource bundle.  (As before, candidate bundle names where the
        final component is an empty string are omitted.)  When it comes to the
        end of the candidate list, it tries the plain bundle name.  With each of the
        candidate bundle names it attempts to instantiate a resource bundle (first
        looking for a class and then a properties file, as described above).
        
        Whenever it succeeds, it calls the previously instantiated resource
        bundle's .setParent(java.util.ResourceBundle) setParent method
        with the new resource bundle.  This continues until the list of names
        is exhausted or the current bundle already has a non-null parent.
        
        Once the parent chain is complete, the bundle is returned.
        
        **Note:** `getBundle` caches instantiated resource
        bundles and might return the same resource bundle instance multiple times.
        
        **Note:**The `baseName` argument should be a fully
        qualified class name. However, for compatibility with earlier versions,
        Java SE Runtime Environments do not verify this, and so it is
        possible to access `PropertyResourceBundle`s by specifying a
        path name (using "/") instead of a fully qualified class name (using
        ".").
        
        <a id="default_behavior_example">
        <strong>Example:</strong></a>
        
        The following class and property files are provided:
        
            - MyResources.class
            - MyResources.properties
            - MyResources_fr.properties
            - MyResources_fr_CH.class
            - MyResources_fr_CH.properties
            - MyResources_en.properties
            - MyResources_es_ES.class
        
        
        The contents of all files are valid (that is, public non-abstract
        subclasses of `ResourceBundle` for the ".class" files,
        syntactically correct ".properties" files).  The default locale is
        `Locale("en", "GB")`.
        
        Calling `getBundle` with the locale arguments below will
        instantiate resource bundles as follows:
        
        <table class="striped">
        <caption style="display:none">getBundle() locale to resource bundle mapping</caption>
        <thead>
        <tr><th scope="col">Locale</th><th scope="col">Resource bundle</th></tr>
        </thead>
        <tbody>
        <tr><th scope="row">Locale("fr", "CH")</th><td>MyResources_fr_CH.class, parent MyResources_fr.properties, parent MyResources.class</td></tr>
        <tr><th scope="row">Locale("fr", "FR")</th><td>MyResources_fr.properties, parent MyResources.class</td></tr>
        <tr><th scope="row">Locale("de", "DE")</th><td>MyResources_en.properties, parent MyResources.class</td></tr>
        <tr><th scope="row">Locale("en", "US")</th><td>MyResources_en.properties, parent MyResources.class</td></tr>
        <tr><th scope="row">Locale("es", "ES")</th><td>MyResources_es_ES.class, parent MyResources.class</td></tr>
        </tbody>
        </table>
        
        The file MyResources_fr_CH.properties is never used because it is
        hidden by the MyResources_fr_CH.class. Likewise, MyResources.properties
        is also hidden by MyResources.class.

        Arguments
        - baseName: the base name of the resource bundle, a fully qualified class name
        - locale: the locale for which a resource bundle is desired
        - loader: the class loader from which to load the resource bundle

        Returns
        - a resource bundle for the given base name and locale

        Raises
        - java.lang.NullPointerException: if `baseName`, `locale`, or `loader` is `null`
        - MissingResourceException: if no resource bundle for the specified base name can be found

        See
        - <a href=".resource-bundle-modules">Resource Bundles and Named Modules</a>

        Since
        - 1.2

        Unknown Tags
        - If the caller module is a named module and the given
        `loader` is the caller module's class loader, this method is
        equivalent to `getBundle(baseName, locale)`; otherwise, it may not
        find resource bundles from named modules.
        Use .getBundle(String, Locale, Module) to load resource bundles
        on behalf on a specific module instead.
        - 9
        """
        ...


    @staticmethod
    def getBundle(baseName: str, targetLocale: "Locale", loader: "ClassLoader", control: "Control") -> "ResourceBundle":
        """
        Returns a resource bundle using the specified base name, target
        locale, class loader and control. Unlike the .getBundle(String, Locale, ClassLoader) getBundle
        factory methods with no `control` argument, the given
        `control` specifies how to locate and instantiate resource
        bundles. Conceptually, the bundle loading process with the given
        `control` is performed in the following steps.
        
        <ol>
        - This factory method looks up the resource bundle in the cache for
        the specified `baseName`, `targetLocale` and
        `loader`.  If the requested resource bundle instance is
        found in the cache and the time-to-live periods of the instance and
        all of its parent instances have not expired, the instance is returned
        to the caller. Otherwise, this factory method proceeds with the
        loading process below.
        
        - The ResourceBundle.Control.getFormats(String)
        control.getFormats method is called to get resource bundle formats
        to produce bundle or resource names. The strings
        `"java.class"` and `"java.properties"`
        designate class-based and PropertyResourceBundle
        property-based resource bundles, respectively. Other strings
        starting with `"java."` are reserved for future extensions
        and must not be used for application-defined formats. Other strings
        designate application-defined formats.
        
        - The ResourceBundle.Control.getCandidateLocales(String,
        Locale) control.getCandidateLocales method is called with the target
        locale to get a list of *candidate `Locale`s* for
        which resource bundles are searched.
        
        - The ResourceBundle.Control.newBundle(String, Locale,
        String, ClassLoader, boolean) control.newBundle method is called to
        instantiate a `ResourceBundle` for the base bundle name, a
        candidate locale, and a format. (Refer to the note on the cache
        lookup below.) This step is iterated over all combinations of the
        candidate locales and formats until the `newBundle` method
        returns a `ResourceBundle` instance or the iteration has
        used up all the combinations. For example, if the candidate locales
        are `Locale("de", "DE")`, `Locale("de")` and
        `Locale("")` and the formats are `"java.class"`
        and `"java.properties"`, then the following is the
        sequence of locale-format combinations to be used to call
        `control.newBundle`.
        
        <table class=striped style="width: 50%; text-align: left; margin-left: 40px;">
        <caption style="display:none">locale-format combinations for newBundle</caption>
        <thead>
        <tr>
        <th scope="col">Index</th>
        <th scope="col">`Locale`</th>
        <th scope="col">`format`</th>
        </tr>
        </thead>
        <tbody>
        <tr>
        <th scope="row">1</th>
        <td>`Locale("de", "DE")`</td>
        <td>`java.class`</td>
        </tr>
        <tr>
        <th scope="row">2</th>
        <td>`Locale("de", "DE")`</td>
        <td>`java.properties`</td>
        </tr>
        <tr>
        <th scope="row">3</th>
        <td>`Locale("de")`</td>
        <td>`java.class`</td>
        </tr>
        <tr>
        <th scope="row">4</th>
        <td>`Locale("de")`</td>
        <td>`java.properties`</td>
        </tr>
        <tr>
        <th scope="row">5</th>
        <td>`Locale("")`</td>
        <td>`java.class`</td>
        </tr>
        <tr>
        <th scope="row">6</th>
        <td>`Locale("")`</td>
        <td>`java.properties`</td>
        </tr>
        </tbody>
        </table>
        
        
        - If the previous step has found no resource bundle, proceed to
        Step 6. If a bundle has been found that is a base bundle (a bundle
        for `Locale("")`), and the candidate locale list only contained
        `Locale("")`, return the bundle to the caller. If a bundle
        has been found that is a base bundle, but the candidate locale list
        contained locales other than Locale(""), put the bundle on hold and
        proceed to Step 6. If a bundle has been found that is not a base
        bundle, proceed to Step 7.
        
        - The ResourceBundle.Control.getFallbackLocale(String,
        Locale) control.getFallbackLocale method is called to get a fallback
        locale (alternative to the current target locale) to try further
        finding a resource bundle. If the method returns a non-null locale,
        it becomes the next target locale and the loading process starts over
        from Step 3. Otherwise, if a base bundle was found and put on hold in
        a previous Step 5, it is returned to the caller now. Otherwise, a
        MissingResourceException is thrown.
        
        - At this point, we have found a resource bundle that's not the
        base bundle. If this bundle set its parent during its instantiation,
        it is returned to the caller. Otherwise, its <a
        href="./ResourceBundle.html#parent_chain">parent chain</a> is
        instantiated based on the list of candidate locales from which it was
        found. Finally, the bundle is returned to the caller.
        </ol>
        
        During the resource bundle loading process above, this factory
        method looks up the cache before calling the Control.newBundle(String, Locale, String, ClassLoader, boolean)
        control.newBundle method.  If the time-to-live period of the
        resource bundle found in the cache has expired, the factory method
        calls the ResourceBundle.Control.needsReload(String, Locale,
        String, ClassLoader, ResourceBundle, long) control.needsReload
        method to determine whether the resource bundle needs to be reloaded.
        If reloading is required, the factory method calls
        `control.newBundle` to reload the resource bundle.  If
        `control.newBundle` returns `null`, the factory
        method puts a dummy resource bundle in the cache as a mark of
        nonexistent resource bundles in order to avoid lookup overhead for
        subsequent requests. Such dummy resource bundles are under the same
        expiration control as specified by `control`.
        
        All resource bundles loaded are cached by default. Refer to
        Control.getTimeToLive(String,Locale)
        control.getTimeToLive for details.
        
        The following is an example of the bundle loading process with the
        default `ResourceBundle.Control` implementation.
        
        Conditions:
        
        - Base bundle name: `foo.bar.Messages`
        - Requested `Locale`: Locale.ITALY
        - Default `Locale`: Locale.FRENCH
        - Available resource bundles:
        `foo/bar/Messages_fr.properties` and
        `foo/bar/Messages.properties`
        
        
        First, `getBundle` tries loading a resource bundle in
        the following sequence.
        
        
        - class `foo.bar.Messages_it_IT`
        - file `foo/bar/Messages_it_IT.properties`
        - class `foo.bar.Messages_it`
        - file `foo/bar/Messages_it.properties`
        - class `foo.bar.Messages`
        - file `foo/bar/Messages.properties`
        
        
        At this point, `getBundle` finds
        `foo/bar/Messages.properties`, which is put on hold
        because it's the base bundle.  `getBundle` calls Control.getFallbackLocale(String, Locale)
        control.getFallbackLocale("foo.bar.Messages", Locale.ITALY) which
        returns `Locale.FRENCH`. Next, `getBundle`
        tries loading a bundle in the following sequence.
        
        
        - class `foo.bar.Messages_fr`
        - file `foo/bar/Messages_fr.properties`
        - class `foo.bar.Messages`
        - file `foo/bar/Messages.properties`
        
        
        `getBundle` finds
        `foo/bar/Messages_fr.properties` and creates a
        `ResourceBundle` instance. Then, `getBundle`
        sets up its parent chain from the list of the candidate locales.  Only
        `foo/bar/Messages.properties` is found in the list and
        `getBundle` creates a `ResourceBundle` instance
        that becomes the parent of the instance for
        `foo/bar/Messages_fr.properties`.

        Arguments
        - baseName: the base name of the resource bundle, a fully qualified
               class name
        - targetLocale: the locale for which a resource bundle is desired
        - loader: the class loader from which to load the resource bundle
        - control: the control which gives information for the resource
               bundle loading process

        Returns
        - a resource bundle for the given base name and locale

        Raises
        - NullPointerException: if `baseName`, `targetLocale`,
                `loader`, or `control` is
                `null`
        - MissingResourceException: if no resource bundle for the specified base name can be found
        - IllegalArgumentException: if the given `control` doesn't perform properly
                (e.g., `control.getCandidateLocales` returns null.)
                Note that validation of `control` is performed as
                needed.
        - UnsupportedOperationException: if this method is called in a named module

        Since
        - 1.6

        Unknown Tags
        - 9
        """
        ...


    @staticmethod
    def clearCache() -> None:
        """
        Removes all resource bundles from the cache that have been loaded
        by the caller's module.

        See
        - ResourceBundle.Control.getTimeToLive(String,Locale)

        Since
        - 1.6

        Unknown Tags
        - 9
        """
        ...


    @staticmethod
    def clearCache(loader: "ClassLoader") -> None:
        """
        Removes all resource bundles from the cache that have been loaded
        by the given class loader.

        Arguments
        - loader: the class loader

        Raises
        - NullPointerException: if `loader` is null

        See
        - ResourceBundle.Control.getTimeToLive(String,Locale)

        Since
        - 1.6
        """
        ...


    def getKeys(self) -> "Enumeration"[str]:
        """
        Returns an enumeration of the keys.

        Returns
        - an `Enumeration` of the keys contained in
                this `ResourceBundle` and its parent bundles.
        """
        ...


    def containsKey(self, key: str) -> bool:
        """
        Determines whether the given `key` is contained in
        this `ResourceBundle` or its parent bundles.

        Arguments
        - key: the resource `key`

        Returns
        - `True` if the given `key` is
               contained in this `ResourceBundle` or its
               parent bundles; `False` otherwise.

        Raises
        - NullPointerException: if `key` is `null`

        Since
        - 1.6
        """
        ...


    def keySet(self) -> set[str]:
        """
        Returns a `Set` of all keys contained in this
        `ResourceBundle` and its parent bundles.

        Returns
        - a `Set` of all keys contained in this
                `ResourceBundle` and its parent bundles.

        Since
        - 1.6
        """
        ...


    class Control:
        """
        `ResourceBundle.Control` defines a set of callback methods
        that are invoked by the ResourceBundle.getBundle(String,
        Locale, ClassLoader, Control) ResourceBundle.getBundle factory
        methods during the bundle loading process. In other words, a
        `ResourceBundle.Control` collaborates with the factory
        methods for loading resource bundles. The default implementation of
        the callback methods provides the information necessary for the
        factory methods to perform the <a
        href="./ResourceBundle.html#default_behavior">default behavior</a>.
        
         ResourceBundle.Control is designed for an application deployed
        in an unnamed module, for example to support resource bundles in
        non-standard formats or package localized resources in a non-traditional
        convention. ResourceBundleProvider is the replacement for
        `ResourceBundle.Control` when migrating to modules.
        `UnsupportedOperationException` will be thrown when a factory
        method that takes the `ResourceBundle.Control` parameter is called.
        
        In addition to the callback methods, the .toBundleName(String, Locale) toBundleName and .toResourceName(String, String) toResourceName methods are defined
        primarily for convenience in implementing the callback
        methods. However, the `toBundleName` method could be
        overridden to provide different conventions in the organization and
        packaging of localized resources.  The `toResourceName`
        method is `final` to avoid use of wrong resource and class
        name separators.
        
        Two factory methods, .getControl(List) and .getNoFallbackControl(List), provide
        `ResourceBundle.Control` instances that implement common
        variations of the default bundle loading process.
        
        The formats returned by the Control.getFormats(String)
        getFormats method and candidate locales returned by the ResourceBundle.Control.getCandidateLocales(String, Locale)
        getCandidateLocales method must be consistent in all
        `ResourceBundle.getBundle` invocations for the same base
        bundle. Otherwise, the `ResourceBundle.getBundle` methods
        may return unintended bundles. For example, if only
        `"java.class"` is returned by the `getFormats`
        method for the first call to `ResourceBundle.getBundle`
        and only `"java.properties"` for the second call, then the
        second call will return the class-based one that has been cached
        during the first call.
        
        A `ResourceBundle.Control` instance must be thread-safe
        if it's simultaneously used by multiple threads.
        `ResourceBundle.getBundle` does not synchronize to call
        the `ResourceBundle.Control` methods. The default
        implementations of the methods are thread-safe.
        
        Applications can specify `ResourceBundle.Control`
        instances returned by the `getControl` factory methods or
        created from a subclass of `ResourceBundle.Control` to
        customize the bundle loading process. The following are examples of
        changing the default bundle loading process.
        
        **Example 1**
        
        The following code lets `ResourceBundle.getBundle` look
        up only properties-based resources.
        
        ```
        import java.util.*;
        import static java.util.ResourceBundle.Control.*;
        ...
        ResourceBundle bundle =
          ResourceBundle.getBundle("MyResources", new Locale("fr", "CH"),
                                   ResourceBundle.Control.getControl(FORMAT_PROPERTIES));
        ```
        
        Given the resource bundles in the <a
        href="./ResourceBundle.html#default_behavior_example">example</a> in
        the `ResourceBundle.getBundle` description, this
        `ResourceBundle.getBundle` call loads
        `MyResources_fr_CH.properties` whose parent is
        `MyResources_fr.properties` whose parent is
        `MyResources.properties`. (`MyResources_fr_CH.properties`
        is not hidden, but `MyResources_fr_CH.class` is.)
        
        **Example 2**
        
        The following is an example of loading XML-based bundles
        using Properties.loadFromXML(java.io.InputStream)
        Properties.loadFromXML.
        
        ```
        ResourceBundle rb = ResourceBundle.getBundle("Messages",
            new ResourceBundle.Control() {
                public List&lt;String&gt; getFormats(String baseName) {
                    if (baseName == null)
                        throw new NullPointerException();
                    return Arrays.asList("xml");
                }
                public ResourceBundle newBundle(String baseName,
                                                Locale locale,
                                                String format,
                                                ClassLoader loader,
                                                boolean reload)
                                 throws IllegalAccessException,
                                        InstantiationException,
                                        IOException {
                    if (baseName == null || locale == null
                          || format == null || loader == null)
                        throw new NullPointerException();
                    ResourceBundle bundle = null;
                    if (format.equals("xml")) {
                        String bundleName = toBundleName(baseName, locale);
                        String resourceName = toResourceName(bundleName, format);
                        InputStream stream = null;
                        if (reload) {
                            URL url = loader.getResource(resourceName);
                            if (url != null) {
                                URLConnection connection = url.openConnection();
                                if (connection != null) {
                                    // Disable caches to get fresh data for
                                    // reloading.
                                    connection.setUseCaches(False);
                                    stream = connection.getInputStream();
                                }
                            }
                        } else {
                            stream = loader.getResourceAsStream(resourceName);
                        }
                        if (stream != null) {
                            BufferedInputStream bis = new BufferedInputStream(stream);
                            bundle = new XMLResourceBundle(bis);
                            bis.close();
                        }
                    }
                    return bundle;
                }
            });
        
        ...
        
        private static class XMLResourceBundle extends ResourceBundle {
            private Properties props;
            XMLResourceBundle(InputStream stream) throws IOException {
                props = new Properties();
                props.loadFromXML(stream);
            }
            protected Object handleGetObject(String key) {
                return props.getProperty(key);
            }
            public Enumeration&lt;String&gt; getKeys() {
                ...
            }
        }
        ```

        See
        - java.util.spi.ResourceBundleProvider

        Since
        - 1.6

        Unknown Tags
        - `ResourceBundle.Control` is not supported
        in named modules. If the `ResourceBundle.getBundle` method with
        a `ResourceBundle.Control` is called in a named module, the method
        will throw an UnsupportedOperationException. Any service providers
        of ResourceBundleControlProvider are ignored in named modules.
        - 9
        """

        FORMAT_DEFAULT = List.of("java.class", "java.properties")
        """
        The default format `List`, which contains the strings
        `"java.class"` and `"java.properties"`, in
        this order. This `List` is unmodifiable.

        See
        - .getFormats(String)
        """
        FORMAT_CLASS = List.of("java.class")
        """
        The class-only format `List` containing
        `"java.class"`. This `List` is unmodifiable.

        See
        - .getFormats(String)
        """
        FORMAT_PROPERTIES = List.of("java.properties")
        """
        The properties-only format `List` containing
        `"java.properties"`. This `List` is unmodifiable.

        See
        - .getFormats(String)
        """
        TTL_DONT_CACHE = -1
        """
        The time-to-live constant for not caching loaded resource bundle
        instances.

        See
        - .getTimeToLive(String, Locale)
        """
        TTL_NO_EXPIRATION_CONTROL = -2
        """
        The time-to-live constant for disabling the expiration control
        for loaded resource bundle instances in the cache.

        See
        - .getTimeToLive(String, Locale)
        """


        @staticmethod
        def getControl(formats: list[str]) -> "Control":
            """
            Returns a `ResourceBundle.Control` in which the .getFormats(String) getFormats method returns the specified
            `formats`. The `formats` must be equal to
            one of Control.FORMAT_PROPERTIES, Control.FORMAT_CLASS or Control.FORMAT_DEFAULT. `ResourceBundle.Control`
            instances returned by this method are singletons and thread-safe.
            
            Specifying Control.FORMAT_DEFAULT is equivalent to
            instantiating the `ResourceBundle.Control` class,
            except that this method returns a singleton.

            Arguments
            - formats: the formats to be returned by the
                   `ResourceBundle.Control.getFormats` method

            Returns
            - a `ResourceBundle.Control` supporting the
                   specified `formats`

            Raises
            - NullPointerException: if `formats` is `null`
            - IllegalArgumentException: if `formats` is unknown
            """
            ...


        @staticmethod
        def getNoFallbackControl(formats: list[str]) -> "Control":
            """
            Returns a `ResourceBundle.Control` in which the .getFormats(String) getFormats method returns the specified
            `formats` and the Control.getFallbackLocale(String, Locale) getFallbackLocale
            method returns `null`. The `formats` must
            be equal to one of Control.FORMAT_PROPERTIES, Control.FORMAT_CLASS or Control.FORMAT_DEFAULT.
            `ResourceBundle.Control` instances returned by this
            method are singletons and thread-safe.

            Arguments
            - formats: the formats to be returned by the
                   `ResourceBundle.Control.getFormats` method

            Returns
            - a `ResourceBundle.Control` supporting the
                   specified `formats` with no fallback
                   `Locale` support

            Raises
            - NullPointerException: if `formats` is `null`
            - IllegalArgumentException: if `formats` is unknown
            """
            ...


        def getFormats(self, baseName: str) -> list[str]:
            """
            Returns a `List` of `String`s containing
            formats to be used to load resource bundles for the given
            `baseName`. The `ResourceBundle.getBundle`
            factory method tries to load resource bundles with formats in the
            order specified by the list. The list returned by this method
            must have at least one `String`. The predefined
            formats are `"java.class"` for class-based resource
            bundles and `"java.properties"` for PropertyResourceBundle properties-based ones. Strings starting
            with `"java."` are reserved for future extensions and
            must not be used by application-defined formats.
            
            It is not a requirement to return an immutable (unmodifiable)
            `List`.  However, the returned `List` must
            not be mutated after it has been returned by
            `getFormats`.
            
            The default implementation returns .FORMAT_DEFAULT so
            that the `ResourceBundle.getBundle` factory method
            looks up first class-based resource bundles, then
            properties-based ones.

            Arguments
            - baseName: the base name of the resource bundle, a fully qualified class
                   name

            Returns
            - a `List` of `String`s containing
                   formats for loading resource bundles.

            Raises
            - NullPointerException: if `baseName` is null

            See
            - .FORMAT_PROPERTIES
            """
            ...


        def getCandidateLocales(self, baseName: str, locale: "Locale") -> list["Locale"]:
            """
            Returns a `List` of `Locale`s as candidate
            locales for `baseName` and `locale`. This
            method is called by the `ResourceBundle.getBundle`
            factory method each time the factory method tries finding a
            resource bundle for a target `Locale`.
            
            The sequence of the candidate locales also corresponds to the
            runtime resource lookup path (also known as the <I>parent
            chain</I>), if the corresponding resource bundles for the
            candidate locales exist and their parents are not defined by
            loaded resource bundles themselves.  The last element of the list
            must be a Locale.ROOT root locale if it is desired to
            have the base bundle as the terminal of the parent chain.
            
            If the given locale is equal to `Locale.ROOT` (the
            root locale), a `List` containing only the root
            `Locale` must be returned. In this case, the
            `ResourceBundle.getBundle` factory method loads only
            the base bundle as the resulting resource bundle.
            
            It is not a requirement to return an immutable (unmodifiable)
            `List`. However, the returned `List` must not
            be mutated after it has been returned by
            `getCandidateLocales`.
            
            The default implementation returns a `List` containing
            `Locale`s using the rules described below.  In the
            description below, *L*, *S*, *C* and *V*
            respectively represent non-empty language, script, country, and
            variant.  For example, [*L*, *C*] represents a
            `Locale` that has non-empty values only for language and
            country.  The form *L*("xx") represents the (non-empty)
            language value is "xx".  For all cases, `Locale`s whose
            final component values are empty strings are omitted.
            
            <ol>- For an input `Locale` with an empty script value,
            append candidate `Locale`s by omitting the final component
            one by one as below:
            
            
            -  [*L*, *C*, *V*] 
            -  [*L*, *C*] 
            -  [*L*] 
            -  `Locale.ROOT` 
            
            
            - For an input `Locale` with a non-empty script value,
            append candidate `Locale`s by omitting the final component
            up to language, then append candidates generated from the
            `Locale` with country and variant restored:
            
            
            -  [*L*, *S*, *C*, *V*]
            -  [*L*, *S*, *C*]
            -  [*L*, *S*]
            -  [*L*, *C*, *V*]
            -  [*L*, *C*]
            -  [*L*]
            -  `Locale.ROOT`
            
            
            - For an input `Locale` with a variant value consisting
            of multiple subtags separated by underscore, generate candidate
            `Locale`s by omitting the variant subtags one by one, then
            insert them after every occurrence of `Locale`s with the
            full variant value in the original list.  For example, if
            the variant consists of two subtags *V1* and *V2*:
            
            
            -  [*L*, *S*, *C*, *V1*, *V2*]
            -  [*L*, *S*, *C*, *V1*]
            -  [*L*, *S*, *C*]
            -  [*L*, *S*]
            -  [*L*, *C*, *V1*, *V2*]
            -  [*L*, *C*, *V1*]
            -  [*L*, *C*]
            -  [*L*]
            -  `Locale.ROOT`
            
            
            - Special cases for Chinese.  When an input `Locale` has the
            language "zh" (Chinese) and an empty script value, either "Hans" (Simplified) or
            "Hant" (Traditional) might be supplied, depending on the country.
            When the country is "CN" (China) or "SG" (Singapore), "Hans" is supplied.
            When the country is "HK" (Hong Kong SAR China), "MO" (Macau SAR China),
            or "TW" (Taiwan), "Hant" is supplied.  For all other countries or when the country
            is empty, no script is supplied.  For example, for `Locale("zh", "CN")
            `, the candidate list will be:
            
            -  [*L*("zh"), *S*("Hans"), *C*("CN")]
            -  [*L*("zh"), *S*("Hans")]
            -  [*L*("zh"), *C*("CN")]
            -  [*L*("zh")]
            -  `Locale.ROOT`
            
            
            For `Locale("zh", "TW")`, the candidate list will be:
            
            -  [*L*("zh"), *S*("Hant"), *C*("TW")]
            -  [*L*("zh"), *S*("Hant")]
            -  [*L*("zh"), *C*("TW")]
            -  [*L*("zh")]
            -  `Locale.ROOT`
            
            
            - Special cases for Norwegian.  Both `Locale("no", "NO",
            "NY")` and `Locale("nn", "NO")` represent Norwegian
            Nynorsk.  When a locale's language is "nn", the standard candidate
            list is generated up to [*L*("nn")], and then the following
            candidates are added:
            
            -  [*L*("no"), *C*("NO"), *V*("NY")]
            -  [*L*("no"), *C*("NO")]
            -  [*L*("no")]
            -  `Locale.ROOT`
            
            
            If the locale is exactly `Locale("no", "NO", "NY")`, it is first
            converted to `Locale("nn", "NO")` and then the above procedure is
            followed.
            
            Also, Java treats the language "no" as a synonym of Norwegian
            Bokm&#xE5;l "nb".  Except for the single case `Locale("no",
            "NO", "NY")` (handled above), when an input `Locale`
            has language "no" or "nb", candidate `Locale`s with
            language code "no" and "nb" are interleaved, first using the
            requested language, then using its synonym. For example,
            `Locale("nb", "NO", "POSIX")` generates the following
            candidate list:
            
            
            -  [*L*("nb"), *C*("NO"), *V*("POSIX")]
            -  [*L*("no"), *C*("NO"), *V*("POSIX")]
            -  [*L*("nb"), *C*("NO")]
            -  [*L*("no"), *C*("NO")]
            -  [*L*("nb")]
            -  [*L*("no")]
            -  `Locale.ROOT`
            
            
            `Locale("no", "NO", "POSIX")` would generate the same list
            except that locales with "no" would appear before the corresponding
            locales with "nb".
            </ol>
            
            The default implementation uses an ArrayList that
            overriding implementations may modify before returning it to the
            caller. However, a subclass must not modify it after it has
            been returned by `getCandidateLocales`.
            
            For example, if the given `baseName` is "Messages"
            and the given `locale` is
            `Locale("ja",&nbsp;"",&nbsp;"XX")`, then a
            `List` of `Locale`s:
            ```
                Locale("ja", "", "XX")
                Locale("ja")
                Locale.ROOT
            ```
            is returned. And if the resource bundles for the "ja" and
            "" `Locale`s are found, then the runtime resource
            lookup path (parent chain) is:
            ````Messages_ja -> Messages````

            Arguments
            - baseName: the base name of the resource bundle, a fully
                   qualified class name
            - locale: the locale for which a resource bundle is desired

            Returns
            - a `List` of candidate
                   `Locale`s for the given `locale`

            Raises
            - NullPointerException: if `baseName` or `locale` is
                   `null`
            """
            ...


        def getFallbackLocale(self, baseName: str, locale: "Locale") -> "Locale":
            """
            Returns a `Locale` to be used as a fallback locale for
            further resource bundle searches by the
            `ResourceBundle.getBundle` factory method. This method
            is called from the factory method every time when no resulting
            resource bundle has been found for `baseName` and
            `locale`, where locale is either the parameter for
            `ResourceBundle.getBundle` or the previous fallback
            locale returned by this method.
            
            The method returns `null` if no further fallback
            search is desired.
            
            The default implementation returns the Locale.getDefault() default {@code Locale} if the given
            `locale` isn't the default one.  Otherwise,
            `null` is returned.

            Arguments
            - baseName: the base name of the resource bundle, a fully
                   qualified class name for which
                   `ResourceBundle.getBundle` has been
                   unable to find any resource bundles (except for the
                   base bundle)
            - locale: the `Locale` for which
                   `ResourceBundle.getBundle` has been
                   unable to find any resource bundles (except for the
                   base bundle)

            Returns
            - a `Locale` for the fallback search,
                   or `null` if no further fallback search
                   is desired.

            Raises
            - NullPointerException: if `baseName` or `locale`
                   is `null`
            """
            ...


        def newBundle(self, baseName: str, locale: "Locale", format: str, loader: "ClassLoader", reload: bool) -> "ResourceBundle":
            """
            Instantiates a resource bundle for the given bundle name of the
            given format and locale, using the given class loader if
            necessary. This method returns `null` if there is no
            resource bundle available for the given parameters. If a resource
            bundle can't be instantiated due to an unexpected error, the
            error must be reported by throwing an `Error` or
            `Exception` rather than simply returning
            `null`.
            
            If the `reload` flag is `True`, it
            indicates that this method is being called because the previously
            loaded resource bundle has expired.

            Arguments
            - baseName: the base bundle name of the resource bundle, a fully
                   qualified class name
            - locale: the locale for which the resource bundle should be
                   instantiated
            - format: the resource bundle format to be loaded
            - loader: the `ClassLoader` to use to load the bundle
            - reload: the flag to indicate bundle reloading; `True`
                   if reloading an expired resource bundle,
                   `False` otherwise

            Returns
            - the resource bundle instance,
                   or `null` if none could be found.

            Raises
            - NullPointerException: if `bundleName`, `locale`,
                   `format`, or `loader` is
                   `null`, or if `null` is returned by
                   .toBundleName(String, Locale) toBundleName
            - IllegalArgumentException: if `format` is unknown, or if the resource
                   found for the given parameters contains malformed data.
            - ClassCastException: if the loaded class cannot be cast to `ResourceBundle`
            - IllegalAccessException: if the class or its nullary constructor is not
                   accessible.
            - InstantiationException: if the instantiation of a class fails for some other
                   reason.
            - ExceptionInInitializerError: if the initialization provoked by this method fails.
            - SecurityException: If a security manager is present and creation of new
                   instances is denied. See Class.newInstance()
                   for details.
            - IOException: if an error occurred when reading resources using
                   any I/O operations

            See
            - java.util.spi.ResourceBundleProvider.getBundle(String, Locale)

            Unknown Tags
            - Resource bundles in named modules are subject to the encapsulation
            rules specified by Module.getResourceAsStream Module.getResourceAsStream.
            A resource bundle in a named module visible to the given class loader
            is accessible when the package of the resource file corresponding
            to the resource bundle is open unconditionally.
            
            The default implementation instantiates a
            `ResourceBundle` as follows.
            
            
            
            - The bundle name is obtained by calling .toBundleName(String, Locale) toBundleName(baseName,
            locale).
            
            - If `format` is `"java.class"`, the
            Class specified by the bundle name is loaded with the
            given class loader. If the `Class` is found and accessible
            then the `ResourceBundle` is instantiated.  The
            resource bundle is accessible if the package of the bundle class file
            is open unconditionally; otherwise, `IllegalAccessException`
            will be thrown.
            Note that the `reload` flag is ignored for loading
            class-based resource bundles in this default implementation.
            
            
            - If `format` is `"java.properties"`,
            .toResourceName(String, String) toResourceName(bundlename,
            "properties") is called to get the resource name.
            If `reload` is `True`, ClassLoader.getResource(String) load.getResource is called
            to get a URL for creating a URLConnection. This `URLConnection` is used to
            URLConnection.setUseCaches(boolean) disable the
            caches of the underlying resource loading layers,
            and to URLConnection.getInputStream() get an
            {@code InputStream}.
            Otherwise, ClassLoader.getResourceAsStream(String)
            loader.getResourceAsStream is called to get an InputStream. Then, a PropertyResourceBundle is constructed with the
            `InputStream`.
            
            - If `format` is neither `"java.class"`
            nor `"java.properties"`, an
            `IllegalArgumentException` is thrown.
            
            - If the `locale`'s language is one of the
            <a href="./Locale.html#legacy_language_codes">Legacy language
            codes</a>, either old or new, then repeat the loading process
            if needed, with the bundle name with the other language.
            For example, "iw" for "he" and vice versa.
            
            
            - 9
            """
            ...


        def getTimeToLive(self, baseName: str, locale: "Locale") -> int:
            """
            Returns the time-to-live (TTL) value for resource bundles that
            are loaded under this
            `ResourceBundle.Control`. Positive time-to-live values
            specify the number of milliseconds a bundle can remain in the
            cache without being validated against the source data from which
            it was constructed. The value 0 indicates that a bundle must be
            validated each time it is retrieved from the cache. .TTL_DONT_CACHE specifies that loaded resource bundles are not
            put in the cache. .TTL_NO_EXPIRATION_CONTROL specifies
            that loaded resource bundles are put in the cache with no
            expiration control.
            
            The expiration affects only the bundle loading process by the
            `ResourceBundle.getBundle` factory method.  That is,
            if the factory method finds a resource bundle in the cache that
            has expired, the factory method calls the .needsReload(String, Locale, String, ClassLoader, ResourceBundle,
            long) needsReload method to determine whether the resource
            bundle needs to be reloaded. If `needsReload` returns
            `True`, the cached resource bundle instance is removed
            from the cache. Otherwise, the instance stays in the cache,
            updated with the new TTL value returned by this method.
            
            All cached resource bundles are subject to removal from the
            cache due to memory constraints of the runtime environment.
            Returning a large positive value doesn't mean to lock loaded
            resource bundles in the cache.
            
            The default implementation returns .TTL_NO_EXPIRATION_CONTROL.

            Arguments
            - baseName: the base name of the resource bundle for which the
                   expiration value is specified.
            - locale: the locale of the resource bundle for which the
                   expiration value is specified.

            Returns
            - the time (0 or a positive millisecond offset from the
                   cached time) to get loaded bundles expired in the cache,
                   .TTL_NO_EXPIRATION_CONTROL to disable the
                   expiration control, or .TTL_DONT_CACHE to disable
                   caching.

            Raises
            - NullPointerException: if `baseName` or `locale` is
                   `null`
            """
            ...


        def needsReload(self, baseName: str, locale: "Locale", format: str, loader: "ClassLoader", bundle: "ResourceBundle", loadTime: int) -> bool:
            """
            Determines if the expired `bundle` in the cache needs
            to be reloaded based on the loading time given by
            `loadTime` or some other criteria. The method returns
            `True` if reloading is required; `False`
            otherwise. `loadTime` is a millisecond offset since
            the <a href="Calendar.html#Epoch"> `Calendar`
            Epoch</a>.
            
            
            The calling `ResourceBundle.getBundle` factory method
            calls this method on the `ResourceBundle.Control`
            instance used for its current invocation, not on the instance
            used in the invocation that originally loaded the resource
            bundle.
            
            The default implementation compares `loadTime` and
            the last modified time of the source data of the resource
            bundle. If it's determined that the source data has been modified
            since `loadTime`, `True` is
            returned. Otherwise, `False` is returned. This
            implementation assumes that the given `format` is the
            same string as its file suffix if it's not one of the default
            formats, `"java.class"` or
            `"java.properties"`.

            Arguments
            - baseName: the base bundle name of the resource bundle, a
                   fully qualified class name
            - locale: the locale for which the resource bundle
                   should be instantiated
            - format: the resource bundle format to be loaded
            - loader: the `ClassLoader` to use to load the bundle
            - bundle: the resource bundle instance that has been expired
                   in the cache
            - loadTime: the time when `bundle` was loaded and put
                   in the cache

            Returns
            - `True` if the expired bundle needs to be
                   reloaded; `False` otherwise.

            Raises
            - NullPointerException: if `baseName`, `locale`,
                   `format`, `loader`, or
                   `bundle` is `null`
            """
            ...


        def toBundleName(self, baseName: str, locale: "Locale") -> str:
            """
            Converts the given `baseName` and `locale`
            to the bundle name. This method is called from the default
            implementation of the .newBundle(String, Locale, String,
            ClassLoader, boolean) newBundle and .needsReload(String,
            Locale, String, ClassLoader, ResourceBundle, long) needsReload
            methods.
            
            This implementation returns the following value:
            ```
                baseName + "_" + language + "_" + script + "_" + country + "_" + variant
            ```
            where `language`, `script`, `country`,
            and `variant` are the language, script, country, and variant
            values of `locale`, respectively. Final component values that
            are empty Strings are omitted along with the preceding '_'.  When the
            script is empty, the script value is omitted along with the preceding '_'.
            If all of the values are empty strings, then `baseName`
            is returned.
            
            For example, if `baseName` is
            `"baseName"` and `locale` is
            `Locale("ja",&nbsp;"",&nbsp;"XX")`, then
            `"baseName_ja_&thinsp;_XX"` is returned. If the given
            locale is `Locale("en")`, then
            `"baseName_en"` is returned.
            
            Overriding this method allows applications to use different
            conventions in the organization and packaging of localized
            resources.

            Arguments
            - baseName: the base name of the resource bundle, a fully
                   qualified class name
            - locale: the locale for which a resource bundle should be
                   loaded

            Returns
            - the bundle name for the resource bundle

            Raises
            - NullPointerException: if `baseName` or `locale`
                   is `null`

            See
            - java.util.spi.AbstractResourceBundleProvider.toBundleName(String, Locale)
            """
            ...


        def toResourceName(self, bundleName: str, suffix: str) -> str:
            """
            Converts the given `bundleName` to the form required
            by the ClassLoader.getResource ClassLoader.getResource
            method by replacing all occurrences of `'.'` in
            `bundleName` with `'/'` and appending a
            `'.'` and the given file `suffix`. For
            example, if `bundleName` is
            `"foo.bar.MyResources_ja_JP"` and `suffix`
            is `"properties"`, then
            `"foo/bar/MyResources_ja_JP.properties"` is returned.

            Arguments
            - bundleName: the bundle name
            - suffix: the file type suffix

            Returns
            - the converted resource name

            Raises
            - NullPointerException: if `bundleName` or `suffix`
                    is `null`
            """
            ...
