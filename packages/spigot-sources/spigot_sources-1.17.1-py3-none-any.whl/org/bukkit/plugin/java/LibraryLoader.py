"""
Python module generated from Java source file org.bukkit.plugin.java.LibraryLoader

Java source file obtained from artifact spigot-api version 1.17.1-R0.1-20211121.234319-104

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import File
from java.net import MalformedURLException
from java.net import URL
from java.net import URLClassLoader
from java.util import Arrays
from org.apache.maven.repository.internal import MavenRepositorySystemUtils
from org.bukkit.plugin import PluginDescriptionFile
from org.bukkit.plugin.java import *
from org.eclipse.aether import DefaultRepositorySystemSession
from org.eclipse.aether import RepositorySystem
from org.eclipse.aether.artifact import Artifact
from org.eclipse.aether.artifact import DefaultArtifact
from org.eclipse.aether.collection import CollectRequest
from org.eclipse.aether.connector.basic import BasicRepositoryConnectorFactory
from org.eclipse.aether.graph import Dependency
from org.eclipse.aether.impl import DefaultServiceLocator
from org.eclipse.aether.repository import LocalRepository
from org.eclipse.aether.repository import RemoteRepository
from org.eclipse.aether.repository import RepositoryPolicy
from org.eclipse.aether.resolution import ArtifactResult
from org.eclipse.aether.resolution import DependencyRequest
from org.eclipse.aether.resolution import DependencyResolutionException
from org.eclipse.aether.resolution import DependencyResult
from org.eclipse.aether.spi.connector import RepositoryConnectorFactory
from org.eclipse.aether.spi.connector.transport import TransporterFactory
from org.eclipse.aether.transfer import AbstractTransferListener
from org.eclipse.aether.transfer import TransferCancelledException
from org.eclipse.aether.transfer import TransferEvent
from org.eclipse.aether.transport.http import HttpTransporterFactory
from typing import Any, Callable, Iterable, Tuple


class LibraryLoader:

    def __init__(self, logger: "Logger"):
        ...


    def createLoader(self, desc: "PluginDescriptionFile") -> "ClassLoader":
        ...
