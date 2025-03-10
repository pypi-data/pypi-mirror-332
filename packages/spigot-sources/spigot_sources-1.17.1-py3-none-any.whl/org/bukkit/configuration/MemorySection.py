"""
Python module generated from Java source file org.bukkit.configuration.MemorySection

Java source file obtained from artifact spigot-api version 1.17.1-R0.1-20211121.234319-104

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import LinkedHashSet
from org.apache.commons.lang import Validate
from org.bukkit import Color
from org.bukkit import Location
from org.bukkit import OfflinePlayer
from org.bukkit.configuration import *
from org.bukkit.configuration.serialization import ConfigurationSerializable
from org.bukkit.inventory import ItemStack
from org.bukkit.util import Vector
from typing import Any, Callable, Iterable, Tuple


class MemorySection(ConfigurationSection):
    """
    A type of ConfigurationSection that is stored in memory.
    """

    def getKeys(self, deep: bool) -> set[str]:
        ...


    def getValues(self, deep: bool) -> dict[str, "Object"]:
        ...


    def contains(self, path: str) -> bool:
        ...


    def contains(self, path: str, ignoreDefault: bool) -> bool:
        ...


    def isSet(self, path: str) -> bool:
        ...


    def getCurrentPath(self) -> str:
        ...


    def getName(self) -> str:
        ...


    def getRoot(self) -> "Configuration":
        ...


    def getParent(self) -> "ConfigurationSection":
        ...


    def addDefault(self, path: str, value: "Object") -> None:
        ...


    def getDefaultSection(self) -> "ConfigurationSection":
        ...


    def set(self, path: str, value: "Object") -> None:
        ...


    def get(self, path: str) -> "Object":
        ...


    def get(self, path: str, def: "Object") -> "Object":
        ...


    def createSection(self, path: str) -> "ConfigurationSection":
        ...


    def createSection(self, path: str, map: dict[Any, Any]) -> "ConfigurationSection":
        ...


    def getString(self, path: str) -> str:
        ...


    def getString(self, path: str, def: str) -> str:
        ...


    def isString(self, path: str) -> bool:
        ...


    def getInt(self, path: str) -> int:
        ...


    def getInt(self, path: str, def: int) -> int:
        ...


    def isInt(self, path: str) -> bool:
        ...


    def getBoolean(self, path: str) -> bool:
        ...


    def getBoolean(self, path: str, def: bool) -> bool:
        ...


    def isBoolean(self, path: str) -> bool:
        ...


    def getDouble(self, path: str) -> float:
        ...


    def getDouble(self, path: str, def: float) -> float:
        ...


    def isDouble(self, path: str) -> bool:
        ...


    def getLong(self, path: str) -> int:
        ...


    def getLong(self, path: str, def: int) -> int:
        ...


    def isLong(self, path: str) -> bool:
        ...


    def getList(self, path: str) -> list[Any]:
        ...


    def getList(self, path: str, def: list[Any]) -> list[Any]:
        ...


    def isList(self, path: str) -> bool:
        ...


    def getStringList(self, path: str) -> list[str]:
        ...


    def getIntegerList(self, path: str) -> list["Integer"]:
        ...


    def getBooleanList(self, path: str) -> list["Boolean"]:
        ...


    def getDoubleList(self, path: str) -> list["Double"]:
        ...


    def getFloatList(self, path: str) -> list["Float"]:
        ...


    def getLongList(self, path: str) -> list["Long"]:
        ...


    def getByteList(self, path: str) -> list["Byte"]:
        ...


    def getCharacterList(self, path: str) -> list["Character"]:
        ...


    def getShortList(self, path: str) -> list["Short"]:
        ...


    def getMapList(self, path: str) -> list[dict[Any, Any]]:
        ...


    def getObject(self, path: str, clazz: type["T"]) -> "T":
        ...


    def getObject(self, path: str, clazz: type["T"], def: "T") -> "T":
        ...


    def getSerializable(self, path: str, clazz: type["T"]) -> "T":
        ...


    def getSerializable(self, path: str, clazz: type["T"], def: "T") -> "T":
        ...


    def getVector(self, path: str) -> "Vector":
        ...


    def getVector(self, path: str, def: "Vector") -> "Vector":
        ...


    def isVector(self, path: str) -> bool:
        ...


    def getOfflinePlayer(self, path: str) -> "OfflinePlayer":
        ...


    def getOfflinePlayer(self, path: str, def: "OfflinePlayer") -> "OfflinePlayer":
        ...


    def isOfflinePlayer(self, path: str) -> bool:
        ...


    def getItemStack(self, path: str) -> "ItemStack":
        ...


    def getItemStack(self, path: str, def: "ItemStack") -> "ItemStack":
        ...


    def isItemStack(self, path: str) -> bool:
        ...


    def getColor(self, path: str) -> "Color":
        ...


    def getColor(self, path: str, def: "Color") -> "Color":
        ...


    def isColor(self, path: str) -> bool:
        ...


    def getLocation(self, path: str) -> "Location":
        ...


    def getLocation(self, path: str, def: "Location") -> "Location":
        ...


    def isLocation(self, path: str) -> bool:
        ...


    def getConfigurationSection(self, path: str) -> "ConfigurationSection":
        ...


    def isConfigurationSection(self, path: str) -> bool:
        ...


    @staticmethod
    def createPath(section: "ConfigurationSection", key: str) -> str:
        """
        Creates a full path to the given ConfigurationSection from its
        root Configuration.
        
        You may use this method for any given ConfigurationSection, not
        only MemorySection.

        Arguments
        - section: Section to create a path for.
        - key: Name of the specified section.

        Returns
        - Full path of the section from its root.
        """
        ...


    @staticmethod
    def createPath(section: "ConfigurationSection", key: str, relativeTo: "ConfigurationSection") -> str:
        """
        Creates a relative path to the given ConfigurationSection from
        the given relative section.
        
        You may use this method for any given ConfigurationSection, not
        only MemorySection.

        Arguments
        - section: Section to create a path for.
        - key: Name of the specified section.
        - relativeTo: Section to create the path relative to.

        Returns
        - Full path of the section from its root.
        """
        ...


    def toString(self) -> str:
        ...
