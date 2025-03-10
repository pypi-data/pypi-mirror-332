"""
Python module generated from Java source file com.google.gson.ReflectionAccessFilter

Java source file obtained from artifact gson version 2.10

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson import *
from com.google.gson.internal import ReflectionAccessFilterHelper
from java.lang.reflect import AccessibleObject
from typing import Any, Callable, Iterable, Tuple


class ReflectionAccessFilter:
    """
    Filter for determining whether reflection based serialization and
    deserialization is allowed for a class.
    
    A filter can be useful in multiple scenarios, for example when
    upgrading to newer Java versions which use the Java Platform Module
    System (JPMS). A filter then allows to FilterResult.BLOCK_INACCESSIBLE
    prevent making inaccessible members accessible, even if the used
    Java version might still allow illegal access (but logs a warning),
    or if `java` command line arguments are used to open the inaccessible
    packages to other parts of the application. This interface defines some
    convenience filters for this task, such as .BLOCK_INACCESSIBLE_JAVA.
    
    A filter can also be useful to prevent mixing model classes of a
    project with other non-model classes; the filter could
    FilterResult.BLOCK_ALL block all reflective access to
    non-model classes.
    
    A reflection access filter is similar to an ExclusionStrategy
    with the major difference that a filter will cause an exception to be
    thrown when access is disallowed while an exclusion strategy just skips
    fields and classes.

    See
    - GsonBuilder.addReflectionAccessFilter(ReflectionAccessFilter)

    Since
    - 2.9.1
    """

    BLOCK_INACCESSIBLE_JAVA = ReflectionAccessFilter() {
    
        @Override
        public FilterResult check(Class<?> rawClass) {
            return ReflectionAccessFilterHelper.isJavaType(rawClass) ? FilterResult.BLOCK_INACCESSIBLE : FilterResult.INDECISIVE;
        }
    }
    """
    Blocks all reflection access to members of standard Java classes which are
    not accessible by default. However, reflection access is still allowed for
    classes for which all fields are accessible and which have an accessible
    no-args constructor (or for which an InstanceCreator has been registered).
    
    If this filter encounters a class other than a standard Java class it
    returns FilterResult.INDECISIVE.
    
    This filter is mainly intended to help enforcing the access checks of
    Java Platform Module System. It allows detecting illegal access, even if
    the used Java version would only log a warning, or is configured to open
    packages for reflection. However, this filter **only works for Java 9 and
    higher**, when using an older Java version its functionality will be
    limited.
    
    Note that this filter might not cover all standard Java classes. Currently
    only classes in a `java.*` or `javax.*` package are considered. The
    set of detected classes might be expanded in the future without prior notice.

    See
    - FilterResult.BLOCK_INACCESSIBLE
    """
    BLOCK_ALL_JAVA = ReflectionAccessFilter() {
    
        @Override
        public FilterResult check(Class<?> rawClass) {
            return ReflectionAccessFilterHelper.isJavaType(rawClass) ? FilterResult.BLOCK_ALL : FilterResult.INDECISIVE;
        }
    }
    """
    Blocks all reflection access to members of standard Java classes.
    
    If this filter encounters a class other than a standard Java class it
    returns FilterResult.INDECISIVE.
    
    This filter is mainly intended to prevent depending on implementation
    details of the Java platform and to help applications prepare for upgrading
    to the Java Platform Module System.
    
    Note that this filter might not cover all standard Java classes. Currently
    only classes in a `java.*` or `javax.*` package are considered. The
    set of detected classes might be expanded in the future without prior notice.

    See
    - FilterResult.BLOCK_ALL
    """
    BLOCK_ALL_ANDROID = ReflectionAccessFilter() {
    
        @Override
        public FilterResult check(Class<?> rawClass) {
            return ReflectionAccessFilterHelper.isAndroidType(rawClass) ? FilterResult.BLOCK_ALL : FilterResult.INDECISIVE;
        }
    }
    """
    Blocks all reflection access to members of standard Android classes.
    
    If this filter encounters a class other than a standard Android class it
    returns FilterResult.INDECISIVE.
    
    This filter is mainly intended to prevent depending on implementation
    details of the Android platform.
    
    Note that this filter might not cover all standard Android classes. Currently
    only classes in an `android.*` or `androidx.*` package, and standard
    Java classes in a `java.*` or `javax.*` package are considered. The
    set of detected classes might be expanded in the future without prior notice.

    See
    - FilterResult.BLOCK_ALL
    """
    BLOCK_ALL_PLATFORM = ReflectionAccessFilter() {
    
        @Override
        public FilterResult check(Class<?> rawClass) {
            return ReflectionAccessFilterHelper.isAnyPlatformType(rawClass) ? FilterResult.BLOCK_ALL : FilterResult.INDECISIVE;
        }
    }
    """
    Blocks all reflection access to members of classes belonging to programming
    language platforms, such as Java, Android, Kotlin or Scala.
    
    If this filter encounters a class other than a standard platform class it
    returns FilterResult.INDECISIVE.
    
    This filter is mainly intended to prevent depending on implementation
    details of the platform classes.
    
    Note that this filter might not cover all platform classes. Currently it
    combines the filters .BLOCK_ALL_JAVA and .BLOCK_ALL_ANDROID,
    and checks for other language-specific platform classes like `kotlin.*`.
    The set of detected classes might be expanded in the future without prior notice.

    See
    - FilterResult.BLOCK_ALL
    """


    def check(self, rawClass: type[Any]) -> "FilterResult":
        """
        Checks if reflection access should be allowed for a class.

        Arguments
        - rawClass: Class to check

        Returns
        - Result indicating whether reflection access is allowed
        """
        ...
