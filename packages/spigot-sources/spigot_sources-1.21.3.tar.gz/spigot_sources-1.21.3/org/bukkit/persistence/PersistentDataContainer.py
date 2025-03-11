"""
Python module generated from Java source file org.bukkit.persistence.PersistentDataContainer

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import NamespacedKey
from org.bukkit.persistence import *
from typing import Any, Callable, Iterable, Tuple


class PersistentDataContainer:
    """
    This interface represents a map like object, capable of storing custom tags
    in it.
    """

    def set(self, key: "NamespacedKey", type: "PersistentDataType"["P", "C"], value: "C") -> None:
        """
        Stores a metadata value on the PersistentDataHolder instance.
        
        This API cannot be used to manipulate minecraft data, as the values will
        be stored using your namespace. This method will override any existing
        value the PersistentDataHolder may have stored under the provided
        key.
        
        Type `<P>`: the generic java type of the tag value
        
        Type `<C>`: the generic type of the object to store

        Arguments
        - key: the key this value will be stored under
        - type: the type this tag uses
        - value: the value to store in the tag

        Raises
        - IllegalArgumentException: if the key is null
        - IllegalArgumentException: if the type is null
        - IllegalArgumentException: if the value is null. Removing a tag should
        be done using .remove(NamespacedKey)
        - IllegalArgumentException: if no suitable adapter was found for
        the PersistentDataType.getPrimitiveType()
        """
        ...


    def has(self, key: "NamespacedKey", type: "PersistentDataType"["P", "C"]) -> bool:
        """
        Returns if the persistent metadata provider has metadata registered
        matching the provided parameters.
        
        This method will only return True if the found value has the same primitive
        data type as the provided key.
        
        Storing a value using a custom PersistentDataType implementation
        will not store the complex data type. Therefore storing a UUID (by
        storing a byte[]) will match has("key" ,
        PersistentDataType.BYTE_ARRAY). Likewise a stored byte[] will
        always match your UUID PersistentDataType even if it is not 16
        bytes long.
        
        This method is only usable for custom object keys. Overwriting existing
        tags, like the display name, will not work as the values are stored
        using your namespace.
        
        Type `<P>`: the generic type of the stored primitive
        
        Type `<C>`: the generic type of the eventually created complex object

        Arguments
        - key: the key the value is stored under
        - type: the type the primative stored value has to match

        Returns
        - if a value with the provided key and type exists

        Raises
        - IllegalArgumentException: if the key to look up is null
        - IllegalArgumentException: if the type to cast the found object to is
        null
        """
        ...


    def has(self, key: "NamespacedKey") -> bool:
        """
        Returns if the persistent metadata provider has metadata registered matching
        the provided parameters.
        
        This method will return True as long as a value with the given key exists,
        regardless of its type.
        
        This method is only usable for custom object keys. Overwriting existing tags,
        like the display name, will not work as the values are stored using your
        namespace.

        Arguments
        - key: the key the value is stored under

        Returns
        - if a value with the provided key exists

        Raises
        - IllegalArgumentException: if the key to look up is null
        """
        ...


    def get(self, key: "NamespacedKey", type: "PersistentDataType"["P", "C"]) -> "C":
        """
        Returns the metadata value that is stored on the
        PersistentDataHolder instance.
        
        Type `<P>`: the generic type of the stored primitive
        
        Type `<C>`: the generic type of the eventually created complex object

        Arguments
        - key: the key to look up in the custom tag map
        - type: the type the value must have and will be casted to

        Returns
        - the value or `null` if no value was mapped under the given
        value

        Raises
        - IllegalArgumentException: if the key to look up is null
        - IllegalArgumentException: if the type to cast the found object to is
        null
        - IllegalArgumentException: if a value exists under the given key,
        but cannot be accessed using the given type
        - IllegalArgumentException: if no suitable adapter was found for
        the PersistentDataType.getPrimitiveType()
        """
        ...


    def getOrDefault(self, key: "NamespacedKey", type: "PersistentDataType"["P", "C"], defaultValue: "C") -> "C":
        """
        Returns the metadata value that is stored on the
        PersistentDataHolder instance. If the value does not exist in the
        container, the default value provided is returned.
        
        Type `<P>`: the generic type of the stored primitive
        
        Type `<C>`: the generic type of the eventually created complex object

        Arguments
        - key: the key to look up in the custom tag map
        - type: the type the value must have and will be casted to
        - defaultValue: the default value to return if no value was found for
        the provided key

        Returns
        - the value or the default value if no value was mapped under the
        given key

        Raises
        - IllegalArgumentException: if the key to look up is null
        - IllegalArgumentException: if the type to cast the found object to is
        null
        - IllegalArgumentException: if a value exists under the given key,
        but cannot be accessed using the given type
        - IllegalArgumentException: if no suitable adapter was found for
        the PersistentDataType.getPrimitiveType()
        """
        ...


    def getKeys(self) -> set["NamespacedKey"]:
        """
        Get the set of keys present on this PersistentDataContainer
        instance.
        
        Any changes made to the returned set will not be reflected on the
        instance.

        Returns
        - the key set
        """
        ...


    def remove(self, key: "NamespacedKey") -> None:
        """
        Removes a custom key from the PersistentDataHolder instance.

        Arguments
        - key: the key to remove

        Raises
        - IllegalArgumentException: if the provided key is null
        """
        ...


    def isEmpty(self) -> bool:
        """
        Returns if the container instance is empty, therefore has no entries
        inside it.

        Returns
        - the boolean
        """
        ...


    def copyTo(self, other: "PersistentDataContainer", replace: bool) -> None:
        """
        Copies all values from this PersistentDataContainer to the provided
        container.
        
        This method only copies custom object keys. Existing tags, like the display
        name, will not be copied as the values are stored using your namespace.

        Arguments
        - other: the container to copy to
        - replace: whether to replace any matching values in the target container

        Raises
        - IllegalArgumentException: if the other container is null
        """
        ...


    def getAdapterContext(self) -> "PersistentDataAdapterContext":
        """
        Returns the adapter context this tag container uses.

        Returns
        - the tag context
        """
        ...
