"""
Python module generated from Java source file org.bukkit.plugin.SimpleServicesManager

Java source file obtained from artifact spigot-api version 1.19.4-R0.1-20230607.155743-88

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.collect import ImmutableList
from com.google.common.collect import ImmutableSet
from java.util import Collections
from java.util import Iterator
from java.util import NoSuchElementException
from org.bukkit import Bukkit
from org.bukkit.event.server import ServiceRegisterEvent
from org.bukkit.event.server import ServiceUnregisterEvent
from org.bukkit.plugin import *
from typing import Any, Callable, Iterable, Tuple


class SimpleServicesManager(ServicesManager):
    """
    A simple services manager.
    """

    def register(self, service: type["T"], provider: "T", plugin: "Plugin", priority: "ServicePriority") -> None:
        """
        Register a provider of a service.
        
        Type `<T>`: Provider

        Arguments
        - service: service class
        - provider: provider to register
        - plugin: plugin with the provider
        - priority: priority of the provider
        """
        ...


    def unregisterAll(self, plugin: "Plugin") -> None:
        """
        Unregister all the providers registered by a particular plugin.

        Arguments
        - plugin: The plugin
        """
        ...


    def unregister(self, service: type[Any], provider: "Object") -> None:
        """
        Unregister a particular provider for a particular service.

        Arguments
        - service: The service interface
        - provider: The service provider implementation
        """
        ...


    def unregister(self, provider: "Object") -> None:
        """
        Unregister a particular provider.

        Arguments
        - provider: The service provider implementation
        """
        ...


    def load(self, service: type["T"]) -> "T":
        """
        Queries for a provider. This may return if no provider has been
        registered for a service. The highest priority provider is returned.
        
        Type `<T>`: The service interface

        Arguments
        - service: The service interface

        Returns
        - provider or null
        """
        ...


    def getRegistration(self, service: type["T"]) -> "RegisteredServiceProvider"["T"]:
        """
        Queries for a provider registration. This may return if no provider
        has been registered for a service.
        
        Type `<T>`: The service interface

        Arguments
        - service: The service interface

        Returns
        - provider registration or null
        """
        ...


    def getRegistrations(self, plugin: "Plugin") -> list["RegisteredServiceProvider"[Any]]:
        """
        Get registrations of providers for a plugin.

        Arguments
        - plugin: The plugin

        Returns
        - provider registrations
        """
        ...


    def getRegistrations(self, service: type["T"]) -> list["RegisteredServiceProvider"["T"]]:
        """
        Get registrations of providers for a service. The returned list is
        an unmodifiable copy.
        
        Type `<T>`: The service interface

        Arguments
        - service: The service interface

        Returns
        - a copy of the list of registrations
        """
        ...


    def getKnownServices(self) -> set[type[Any]]:
        """
        Get a list of known services. A service is known if it has registered
        providers for it.

        Returns
        - a copy of the set of known services
        """
        ...


    def isProvidedFor(self, service: type["T"]) -> bool:
        """
        Returns whether a provider has been registered for a service.
        
        Type `<T>`: service

        Arguments
        - service: service to check

        Returns
        - True if and only if there are registered providers
        """
        ...
