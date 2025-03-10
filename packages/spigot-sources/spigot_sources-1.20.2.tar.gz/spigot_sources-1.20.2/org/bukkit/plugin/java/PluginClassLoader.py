"""
Python module generated from Java source file org.bukkit.plugin.java.PluginClassLoader

Java source file obtained from artifact spigot-api version 1.20.2-R0.1-20231205.164257-71

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from com.google.common.io import ByteStreams
from java.io import File
from java.io import IOException
from java.io import InputStream
from java.lang.reflect import Constructor
from java.lang.reflect import InvocationTargetException
from java.net import MalformedURLException
from java.net import URL
from java.net import URLClassLoader
from java.security import CodeSigner
from java.security import CodeSource
from java.util import Collections
from java.util import Enumeration
from java.util.concurrent import ConcurrentHashMap
from java.util.jar import JarEntry
from java.util.jar import JarFile
from java.util.jar import Manifest
from org.bukkit.plugin import InvalidPluginException
from org.bukkit.plugin import PluginDescriptionFile
from org.bukkit.plugin import SimplePluginManager
from org.bukkit.plugin.java import *
from typing import Any, Callable, Iterable, Tuple


class PluginClassLoader(URLClassLoader):
    """
    A ClassLoader for plugins, to allow shared classes across multiple plugins
    """

    def getResource(self, name: str) -> "URL":
        ...


    def getResources(self, name: str) -> "Enumeration"["URL"]:
        ...


    def close(self) -> None:
        ...
