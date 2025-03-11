"""
Python module generated from Java source file com.google.common.base.StandardSystemProperty

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import J2ktIncompatible
from com.google.common.base import *
from enum import Enum
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class StandardSystemProperty(Enum):
    """
    Represents a System.getProperties() standard system property.

    Author(s)
    - Kurt Alfred Kluever

    Since
    - 15.0
    """

    JAVA_VERSION = ("java.version")
    """
    Java Runtime Environment version.
    """
    JAVA_VENDOR = ("java.vendor")
    """
    Java Runtime Environment vendor.
    """
    JAVA_VENDOR_URL = ("java.vendor.url")
    """
    Java vendor URL.
    """
    JAVA_HOME = ("java.home")
    """
    Java installation directory.
    """
    JAVA_VM_SPECIFICATION_VERSION = ("java.vm.specification.version")
    """
    Java Virtual Machine specification version.
    """
    JAVA_VM_SPECIFICATION_VENDOR = ("java.vm.specification.vendor")
    """
    Java Virtual Machine specification vendor.
    """
    JAVA_VM_SPECIFICATION_NAME = ("java.vm.specification.name")
    """
    Java Virtual Machine specification name.
    """
    JAVA_VM_VERSION = ("java.vm.version")
    """
    Java Virtual Machine implementation version.
    """
    JAVA_VM_VENDOR = ("java.vm.vendor")
    """
    Java Virtual Machine implementation vendor.
    """
    JAVA_VM_NAME = ("java.vm.name")
    """
    Java Virtual Machine implementation name.
    """
    JAVA_SPECIFICATION_VERSION = ("java.specification.version")
    """
    Java Runtime Environment specification version.
    """
    JAVA_SPECIFICATION_VENDOR = ("java.specification.vendor")
    """
    Java Runtime Environment specification vendor.
    """
    JAVA_SPECIFICATION_NAME = ("java.specification.name")
    """
    Java Runtime Environment specification name.
    """
    JAVA_CLASS_VERSION = ("java.class.version")
    """
    Java class format version number.
    """
    JAVA_CLASS_PATH = ("java.class.path")
    """
    Java class path.
    """
    JAVA_LIBRARY_PATH = ("java.library.path")
    """
    List of paths to search when loading libraries.
    """
    JAVA_IO_TMPDIR = ("java.io.tmpdir")
    """
    Default temp file path.
    """
    JAVA_COMPILER = ("java.compiler")
    """
    Name of JIT compiler to use.
    """
    JAVA_EXT_DIRS = ("java.ext.dirs")
    """
    Path of extension directory or directories.

    Deprecated
    - This property was <a
        href="https://openjdk.java.net/jeps/220#Removed:-The-extension-mechanism">deprecated</a> in
        Java 8 and removed in Java 9. We do not plan to remove this API from Guava, but if you are
        using it, it is probably not doing what you want.
    """
    OS_NAME = ("os.name")
    """
    Operating system name.
    """
    OS_ARCH = ("os.arch")
    """
    Operating system architecture.
    """
    OS_VERSION = ("os.version")
    """
    Operating system version.
    """
    FILE_SEPARATOR = ("file.separator")
    """
    File separator ("/" on UNIX).
    """
    PATH_SEPARATOR = ("path.separator")
    """
    Path separator (":" on UNIX).
    """
    LINE_SEPARATOR = ("line.separator")
    """
    Line separator ("\n" on UNIX).
    """
    USER_NAME = ("user.name")
    """
    User's account name.
    """
    USER_HOME = ("user.home")
    """
    User's home directory.
    """
    USER_DIR = ("user.dir")
    """
    User's current working directory.
    """


    def key(self) -> str:
        """
        Returns the key used to look up this system property.
        """
        ...


    def value(self) -> str:
        """
        Returns the current value for this system property by delegating to System.getProperty(String).
        
        The value returned by this method is non-null except in rare circumstances:
        
        
          - .JAVA_EXT_DIRS was deprecated in Java 8 and removed in Java 9. We have not
              confirmed whether it is available under older versions.
          - .JAVA_COMPILER, while still listed as required as of Java 15, is typically not
              available even under older version.
          - Any property may be cleared through APIs like System.clearProperty.
          - Unusual environments like GWT may have their own special handling of system properties.
        
        
        Note that `StandardSystemProperty` does not provide constants for more recently added
        properties, including:
        
        
          - `java.vendor.version` (added in Java 11, listed as optional as of Java 13)
          - `jdk.module.*` (added in Java 9, optional)
        """
        ...


    def toString(self) -> str:
        """
        Returns a string representation of this system property.
        """
        ...
