"""
Python module generated from Java source file org.bukkit.inventory.meta.components.EquippableComponent

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import NamespacedKey
from org.bukkit import Sound
from org.bukkit import Tag
from org.bukkit.configuration.serialization import ConfigurationSerializable
from org.bukkit.entity import EntityType
from org.bukkit.inventory import EquipmentSlot
from org.bukkit.inventory.meta.components import *
from typing import Any, Callable, Iterable, Tuple


class EquippableComponent(ConfigurationSerializable):
    """
    Represents a component which can turn any item into equippable armor.
    """

    def getSlot(self) -> "EquipmentSlot":
        """
        Gets the slot the item can be equipped to.

        Returns
        - slot
        """
        ...


    def setSlot(self, slot: "EquipmentSlot") -> None:
        """
        Sets the slot the item can be equipped to.

        Arguments
        - slot: new slot
        """
        ...


    def getEquipSound(self) -> "Sound":
        """
        Gets the sound to play when the item is equipped.

        Returns
        - the sound
        """
        ...


    def setEquipSound(self, sound: "Sound") -> None:
        """
        Sets the sound to play when the item is equipped.

        Arguments
        - sound: sound or null for current default
        """
        ...


    def getModel(self) -> "NamespacedKey":
        """
        Gets the key of the model to use when equipped.

        Returns
        - model key
        """
        ...


    def setModel(self, key: "NamespacedKey") -> None:
        """
        Sets the key of the model to use when equipped.

        Arguments
        - key: model key
        """
        ...


    def getCameraOverlay(self) -> "NamespacedKey":
        """
        Gets the key of the camera overlay to use when equipped.

        Returns
        - camera overlay key
        """
        ...


    def setCameraOverlay(self, key: "NamespacedKey") -> None:
        """
        Sets the key of the camera overlay to use when equipped.

        Arguments
        - key: camera overlay key
        """
        ...


    def getAllowedEntities(self) -> Iterable["EntityType"]:
        """
        Gets the entities which can equip this item.

        Returns
        - the entities
        """
        ...


    def setAllowedEntities(self, entities: "EntityType") -> None:
        """
        Sets the entities which can equip this item.

        Arguments
        - entities: the entity types
        """
        ...


    def setAllowedEntities(self, entities: Iterable["EntityType"]) -> None:
        """
        Sets the entities which can equip this item.

        Arguments
        - entities: the entity types
        """
        ...


    def setAllowedEntities(self, tag: "Tag"["EntityType"]) -> None:
        """
        Set the entity types (represented as an entity Tag) which can
        equip this item.

        Arguments
        - tag: the entity tag

        Raises
        - IllegalArgumentException: if the passed `tag` is not an entity
        tag
        """
        ...


    def isDispensable(self) -> bool:
        """
        Gets whether the item can be equipped by a dispenser.

        Returns
        - equippable status
        """
        ...


    def setDispensable(self, dispensable: bool) -> None:
        """
        Sets whether the item can be equipped by a dispenser.

        Arguments
        - dispensable: new equippable status
        """
        ...


    def isSwappable(self) -> bool:
        """
        Gets if the item is swappable by right clicking.

        Returns
        - swappable status
        """
        ...


    def setSwappable(self, swappable: bool) -> None:
        """
        Sets if the item is swappable by right clicking.

        Arguments
        - swappable: new status
        """
        ...


    def isDamageOnHurt(self) -> bool:
        """
        Gets if the item will be damaged when the wearing entity is damaged.

        Returns
        - whether the item will be damaged
        """
        ...


    def setDamageOnHurt(self, damage: bool) -> None:
        """
        Sets if the item will be damaged when the wearing entity is damaged.

        Arguments
        - damage: whether the item will be damaged
        """
        ...
