"""
Python module generated from Java source file org.bukkit.persistence.PersistentDataContainer

Java source file obtained from artifact spigot-api version 1.16.5-R0.1-20210611.041013-99

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

    def set(self, key: "NamespacedKey", type: "PersistentDataType"["T", "Z"], value: "Z") -> None:
        """
        Stores a metadata value on the PersistentDataHolder instance.
        
        This API cannot be used to manipulate minecraft data, as the values will
        be stored using your namespace. This method will override any existing
        value the PersistentDataHolder may have stored under the provided
        key.
        
        Type `<T>`: the generic java type of the tag value
        
        Type `<Z>`: the generic type of the object to store

        Arguments
        - key: the key this value will be stored under
        - type: the type this tag uses
        - value: the value stored in the tag

        Raises
        - NullPointerException: if the key is null
        - NullPointerException: if the type is null
        - NullPointerException: if the value is null. Removing a tag should
        be done using .remove(NamespacedKey)
        - IllegalArgumentException: if no suitable adapter will be found for
        the PersistentDataType.getPrimitiveType()
        """
        ...


    def has(self, key: "NamespacedKey", type: "PersistentDataType"["T", "Z"]) -> bool:
        """
        Returns if the persistent metadata provider has metadata registered
        matching the provided parameters.
        
        This method will only return if the found value has the same primitive
        data type as the provided key.
        
        Storing a value using a custom PersistentDataType implementation
        will not store the complex data type. Therefore storing a UUID (by
        storing a byte[]) will match has("key" ,
        PersistentDataType.BYTE_ARRAY). Likewise a stored byte[] will
        always match your UUID PersistentDataType even if it is not 16
        bytes long.
        
        This method is only usable for custom object keys. Overwriting existing
        tags, like the the display name, will not work as the values are stored
        using your namespace.
        
        Type `<T>`: the generic type of the stored primitive
        
        Type `<Z>`: the generic type of the eventually created complex object

        Arguments
        - key: the key the value is stored under
        - type: the type which primitive storage type has to match the value

        Returns
        - if a value

        Raises
        - NullPointerException: if the key to look up is null
        - NullPointerException: if the type to cast the found object to is
        null
        """
        ...


    def get(self, key: "NamespacedKey", type: "PersistentDataType"["T", "Z"]) -> "Z":
        """
        Returns the metadata value that is stored on the
        PersistentDataHolder instance.
        
        Type `<T>`: the generic type of the stored primitive
        
        Type `<Z>`: the generic type of the eventually created complex object

        Arguments
        - key: the key to look up in the custom tag map
        - type: the type the value must have and will be casted to

        Returns
        - the value or `null` if no value was mapped under the given
        value

        Raises
        - NullPointerException: if the key to look up is null
        - NullPointerException: if the type to cast the found object to is
        null
        - IllegalArgumentException: if the value exists under the given key,
        but cannot be access using the given type
        - IllegalArgumentException: if no suitable adapter will be found for
        the PersistentDataType.getPrimitiveType()
        """
        ...


    def getOrDefault(self, key: "NamespacedKey", type: "PersistentDataType"["T", "Z"], defaultValue: "Z") -> "Z":
        """
        Returns the metadata value that is stored on the
        PersistentDataHolder instance. If the value does not exist in the
        container, the default value provided is returned.
        
        Type `<T>`: the generic type of the stored primitive
        
        Type `<Z>`: the generic type of the eventually created complex object

        Arguments
        - key: the key to look up in the custom tag map
        - type: the type the value must have and will be casted to
        - defaultValue: the default value to return if no value was found for
        the provided key

        Returns
        - the value or the default value if no value was mapped under the
        given value

        Raises
        - NullPointerException: if the key to look up is null
        - NullPointerException: if the type to cast the found object to is
        null
        - IllegalArgumentException: if the value exists under the given key,
        but cannot be access using the given type
        - IllegalArgumentException: if no suitable adapter will be found for
        the PersistentDataType.getPrimitiveType()
        """
        ...


    def getKeys(self) -> set["NamespacedKey"]:
        """
        Get a set of keys present on this PersistentDataContainer
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
        - key: the key

        Raises
        - NullPointerException: if the provided key is null
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


    def getAdapterContext(self) -> "PersistentDataAdapterContext":
        """
        Returns the adapter context this tag container uses.

        Returns
        - the tag context
        """
        ...
