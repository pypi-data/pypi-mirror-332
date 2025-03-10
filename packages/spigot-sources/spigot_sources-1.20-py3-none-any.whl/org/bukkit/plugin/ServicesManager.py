"""
Python module generated from Java source file org.bukkit.plugin.ServicesManager

Java source file obtained from artifact spigot-api version 1.20-R0.1-20230612.113428-32

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.plugin import *
from typing import Any, Callable, Iterable, Tuple


class ServicesManager:
    """
    Manages services and service providers. Services are an interface
    specifying a list of methods that a provider must implement. Providers are
    implementations of these services. A provider can be queried from the
    services manager in order to use a service (if one is available). If
    multiple plugins register a service, then the service with the highest
    priority takes precedence.
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
        Queries for a provider. This may return null if no provider has been
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
        Queries for a provider registration. This may return null if no provider
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


    def getRegistrations(self, service: type["T"]) -> Iterable["RegisteredServiceProvider"["T"]]:
        """
        Get registrations of providers for a service. The returned list is
        unmodifiable.
        
        Type `<T>`: The service interface

        Arguments
        - service: The service interface

        Returns
        - list of registrations
        """
        ...


    def getKnownServices(self) -> Iterable[type[Any]]:
        """
        Get a list of known services. A service is known if it has registered
        providers for it.

        Returns
        - list of known services
        """
        ...


    def isProvidedFor(self, service: type["T"]) -> bool:
        """
        Returns whether a provider has been registered for a service. Do not
        check this first only to call `load(service)` later, as that
        would be a non-thread safe situation.
        
        Type `<T>`: service

        Arguments
        - service: service to check

        Returns
        - whether there has been a registered provider
        """
        ...
