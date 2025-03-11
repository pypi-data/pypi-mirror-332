"""
Python module generated from Java source file org.bukkit.configuration.ConfigurationSection

Java source file obtained from artifact spigot-api version 1.21.2-R0.1-20241023.084343-5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Color
from org.bukkit import Location
from org.bukkit import OfflinePlayer
from org.bukkit.configuration import *
from org.bukkit.configuration.serialization import ConfigurationSerializable
from org.bukkit.inventory import ItemStack
from org.bukkit.util import Vector
from typing import Any, Callable, Iterable, Tuple


class ConfigurationSection:
    """
    Represents a section of a Configuration
    """

    def getKeys(self, deep: bool) -> set[str]:
        """
        Gets a set containing all keys in this section.
        
        If deep is set to True, then this will contain all the keys within any
        child ConfigurationSections (and their children, etc). These
        will be in a valid path notation for you to use.
        
        If deep is set to False, then this will contain only the keys of any
        direct children, and not their own children.

        Arguments
        - deep: Whether or not to get a deep list, as opposed to a shallow
            list.

        Returns
        - Set of keys contained within this ConfigurationSection.
        """
        ...


    def getValues(self, deep: bool) -> dict[str, "Object"]:
        """
        Gets a Map containing all keys and their values for this section.
        
        If deep is set to True, then this will contain all the keys and values
        within any child ConfigurationSections (and their children,
        etc). These keys will be in a valid path notation for you to use.
        
        If deep is set to False, then this will contain only the keys and
        values of any direct children, and not their own children.

        Arguments
        - deep: Whether or not to get a deep list, as opposed to a shallow
            list.

        Returns
        - Map of keys and values of this section.
        """
        ...


    def contains(self, path: str) -> bool:
        """
        Checks if this ConfigurationSection contains the given path.
        
        If the value for the requested path does not exist but a default value
        has been specified, this will return True.

        Arguments
        - path: Path to check for existence.

        Returns
        - True if this section contains the requested path, either via
            default or being set.

        Raises
        - IllegalArgumentException: Thrown when path is null.
        """
        ...


    def contains(self, path: str, ignoreDefault: bool) -> bool:
        """
        Checks if this ConfigurationSection contains the given path.
        
        If the value for the requested path does not exist, the boolean parameter
        of True has been specified, a default value for the path exists, this
        will return True.
        
        If a boolean parameter of False has been specified, True will only be
        returned if there is a set value for the specified path.

        Arguments
        - path: Path to check for existence.
        - ignoreDefault: Whether or not to ignore if a default value for the
        specified path exists.

        Returns
        - True if this section contains the requested path, or if a default
        value exist and the boolean parameter for this method is True.

        Raises
        - IllegalArgumentException: Thrown when path is null.
        """
        ...


    def isSet(self, path: str) -> bool:
        """
        Checks if this ConfigurationSection has a value set for the
        given path.
        
        If the value for the requested path does not exist but a default value
        has been specified, this will still return False.

        Arguments
        - path: Path to check for existence.

        Returns
        - True if this section contains the requested path, regardless of
            having a default.

        Raises
        - IllegalArgumentException: Thrown when path is null.
        """
        ...


    def getCurrentPath(self) -> str:
        """
        Gets the path of this ConfigurationSection from its root Configuration
        
        For any Configuration themselves, this will return an empty
        string.
        
        If the section is no longer contained within its root for any reason,
        such as being replaced with a different value, this may return null.
        
        To retrieve the single name of this section, that is, the final part of
        the path returned by this method, you may use .getName().

        Returns
        - Path of this section relative to its root
        """
        ...


    def getName(self) -> str:
        """
        Gets the name of this individual ConfigurationSection, in the
        path.
        
        This will always be the final part of .getCurrentPath(), unless
        the section is orphaned.

        Returns
        - Name of this section
        """
        ...


    def getRoot(self) -> "Configuration":
        """
        Gets the root Configuration that contains this ConfigurationSection
        
        For any Configuration themselves, this will return its own
        object.
        
        If the section is no longer contained within its root for any reason,
        such as being replaced with a different value, this may return null.

        Returns
        - Root configuration containing this section.
        """
        ...


    def getParent(self) -> "ConfigurationSection":
        """
        Gets the parent ConfigurationSection that directly contains
        this ConfigurationSection.
        
        For any Configuration themselves, this will return null.
        
        If the section is no longer contained within its parent for any reason,
        such as being replaced with a different value, this may return null.

        Returns
        - Parent section containing this section.
        """
        ...


    def get(self, path: str) -> "Object":
        """
        Gets the requested Object by path.
        
        If the Object does not exist but a default value has been specified,
        this will return the default value. If the Object does not exist and no
        default value was specified, this will return null.

        Arguments
        - path: Path of the Object to get.

        Returns
        - Requested Object.
        """
        ...


    def get(self, path: str, def: "Object") -> "Object":
        """
        Gets the requested Object by path, returning a default value if not
        found.
        
        If the Object does not exist then the specified default value will
        returned regardless of if a default has been identified in the root
        Configuration.

        Arguments
        - path: Path of the Object to get.
        - def: The default value to return if the path is not found.

        Returns
        - Requested Object.
        """
        ...


    def set(self, path: str, value: "Object") -> None:
        """
        Sets the specified path to the given value.
        
        If value is null, the entry will be removed. Any existing entry will be
        replaced, regardless of what the new value is.
        
        Some implementations may have limitations on what you may store. See
        their individual javadocs for details. No implementations should allow
        you to store Configurations or ConfigurationSections,
        please use .createSection(java.lang.String) for that.

        Arguments
        - path: Path of the object to set.
        - value: New value to set the path to.
        """
        ...


    def createSection(self, path: str) -> "ConfigurationSection":
        """
        Creates an empty ConfigurationSection at the specified path.
        
        Any value that was previously set at this path will be overwritten. If
        the previous value was itself a ConfigurationSection, it will
        be orphaned.

        Arguments
        - path: Path to create the section at.

        Returns
        - Newly created section
        """
        ...


    def createSection(self, path: str, map: dict[Any, Any]) -> "ConfigurationSection":
        """
        Creates a ConfigurationSection at the specified path, with
        specified values.
        
        Any value that was previously set at this path will be overwritten. If
        the previous value was itself a ConfigurationSection, it will
        be orphaned.

        Arguments
        - path: Path to create the section at.
        - map: The values to used.

        Returns
        - Newly created section
        """
        ...


    def getString(self, path: str) -> str:
        """
        Gets the requested String by path.
        
        If the String does not exist but a default value has been specified,
        this will return the default value. If the String does not exist and no
        default value was specified, this will return null.

        Arguments
        - path: Path of the String to get.

        Returns
        - Requested String.
        """
        ...


    def getString(self, path: str, def: str) -> str:
        """
        Gets the requested String by path, returning a default value if not
        found.
        
        If the String does not exist then the specified default value will
        returned regardless of if a default has been identified in the root
        Configuration.

        Arguments
        - path: Path of the String to get.
        - def: The default value to return if the path is not found or is
            not a String.

        Returns
        - Requested String.
        """
        ...


    def isString(self, path: str) -> bool:
        """
        Checks if the specified path is a String.
        
        If the path exists but is not a String, this will return False. If the
        path does not exist, this will return False. If the path does not exist
        but a default value has been specified, this will check if that default
        value is a String and return appropriately.

        Arguments
        - path: Path of the String to check.

        Returns
        - Whether or not the specified path is a String.
        """
        ...


    def getInt(self, path: str) -> int:
        """
        Gets the requested int by path.
        
        If the int does not exist but a default value has been specified, this
        will return the default value. If the int does not exist and no default
        value was specified, this will return 0.

        Arguments
        - path: Path of the int to get.

        Returns
        - Requested int.
        """
        ...


    def getInt(self, path: str, def: int) -> int:
        """
        Gets the requested int by path, returning a default value if not found.
        
        If the int does not exist then the specified default value will
        returned regardless of if a default has been identified in the root
        Configuration.

        Arguments
        - path: Path of the int to get.
        - def: The default value to return if the path is not found or is
            not an int.

        Returns
        - Requested int.
        """
        ...


    def isInt(self, path: str) -> bool:
        """
        Checks if the specified path is an int.
        
        If the path exists but is not a int, this will return False. If the
        path does not exist, this will return False. If the path does not exist
        but a default value has been specified, this will check if that default
        value is a int and return appropriately.

        Arguments
        - path: Path of the int to check.

        Returns
        - Whether or not the specified path is an int.
        """
        ...


    def getBoolean(self, path: str) -> bool:
        """
        Gets the requested boolean by path.
        
        If the boolean does not exist but a default value has been specified,
        this will return the default value. If the boolean does not exist and
        no default value was specified, this will return False.

        Arguments
        - path: Path of the boolean to get.

        Returns
        - Requested boolean.
        """
        ...


    def getBoolean(self, path: str, def: bool) -> bool:
        """
        Gets the requested boolean by path, returning a default value if not
        found.
        
        If the boolean does not exist then the specified default value will
        returned regardless of if a default has been identified in the root
        Configuration.

        Arguments
        - path: Path of the boolean to get.
        - def: The default value to return if the path is not found or is
            not a boolean.

        Returns
        - Requested boolean.
        """
        ...


    def isBoolean(self, path: str) -> bool:
        """
        Checks if the specified path is a boolean.
        
        If the path exists but is not a boolean, this will return False. If the
        path does not exist, this will return False. If the path does not exist
        but a default value has been specified, this will check if that default
        value is a boolean and return appropriately.

        Arguments
        - path: Path of the boolean to check.

        Returns
        - Whether or not the specified path is a boolean.
        """
        ...


    def getDouble(self, path: str) -> float:
        """
        Gets the requested double by path.
        
        If the double does not exist but a default value has been specified,
        this will return the default value. If the double does not exist and no
        default value was specified, this will return 0.

        Arguments
        - path: Path of the double to get.

        Returns
        - Requested double.
        """
        ...


    def getDouble(self, path: str, def: float) -> float:
        """
        Gets the requested double by path, returning a default value if not
        found.
        
        If the double does not exist then the specified default value will
        returned regardless of if a default has been identified in the root
        Configuration.

        Arguments
        - path: Path of the double to get.
        - def: The default value to return if the path is not found or is
            not a double.

        Returns
        - Requested double.
        """
        ...


    def isDouble(self, path: str) -> bool:
        """
        Checks if the specified path is a double.
        
        If the path exists but is not a double, this will return False. If the
        path does not exist, this will return False. If the path does not exist
        but a default value has been specified, this will check if that default
        value is a double and return appropriately.

        Arguments
        - path: Path of the double to check.

        Returns
        - Whether or not the specified path is a double.
        """
        ...


    def getLong(self, path: str) -> int:
        """
        Gets the requested long by path.
        
        If the long does not exist but a default value has been specified, this
        will return the default value. If the long does not exist and no
        default value was specified, this will return 0.

        Arguments
        - path: Path of the long to get.

        Returns
        - Requested long.
        """
        ...


    def getLong(self, path: str, def: int) -> int:
        """
        Gets the requested long by path, returning a default value if not
        found.
        
        If the long does not exist then the specified default value will
        returned regardless of if a default has been identified in the root
        Configuration.

        Arguments
        - path: Path of the long to get.
        - def: The default value to return if the path is not found or is
            not a long.

        Returns
        - Requested long.
        """
        ...


    def isLong(self, path: str) -> bool:
        """
        Checks if the specified path is a long.
        
        If the path exists but is not a long, this will return False. If the
        path does not exist, this will return False. If the path does not exist
        but a default value has been specified, this will check if that default
        value is a long and return appropriately.

        Arguments
        - path: Path of the long to check.

        Returns
        - Whether or not the specified path is a long.
        """
        ...


    def getList(self, path: str) -> list[Any]:
        """
        Gets the requested List by path.
        
        If the List does not exist but a default value has been specified, this
        will return the default value. If the List does not exist and no
        default value was specified, this will return null.

        Arguments
        - path: Path of the List to get.

        Returns
        - Requested List.
        """
        ...


    def getList(self, path: str, def: list[Any]) -> list[Any]:
        """
        Gets the requested List by path, returning a default value if not
        found.
        
        If the List does not exist then the specified default value will
        returned regardless of if a default has been identified in the root
        Configuration.

        Arguments
        - path: Path of the List to get.
        - def: The default value to return if the path is not found or is
            not a List.

        Returns
        - Requested List.
        """
        ...


    def isList(self, path: str) -> bool:
        """
        Checks if the specified path is a List.
        
        If the path exists but is not a List, this will return False. If the
        path does not exist, this will return False. If the path does not exist
        but a default value has been specified, this will check if that default
        value is a List and return appropriately.

        Arguments
        - path: Path of the List to check.

        Returns
        - Whether or not the specified path is a List.
        """
        ...


    def getStringList(self, path: str) -> list[str]:
        """
        Gets the requested List of String by path.
        
        If the List does not exist but a default value has been specified, this
        will return the default value. If the List does not exist and no
        default value was specified, this will return an empty List.
        
        This method will attempt to cast any values into a String if possible,
        but may miss any values out if they are not compatible.

        Arguments
        - path: Path of the List to get.

        Returns
        - Requested List of String.
        """
        ...


    def getIntegerList(self, path: str) -> list["Integer"]:
        """
        Gets the requested List of Integer by path.
        
        If the List does not exist but a default value has been specified, this
        will return the default value. If the List does not exist and no
        default value was specified, this will return an empty List.
        
        This method will attempt to cast any values into a Integer if possible,
        but may miss any values out if they are not compatible.

        Arguments
        - path: Path of the List to get.

        Returns
        - Requested List of Integer.
        """
        ...


    def getBooleanList(self, path: str) -> list["Boolean"]:
        """
        Gets the requested List of Boolean by path.
        
        If the List does not exist but a default value has been specified, this
        will return the default value. If the List does not exist and no
        default value was specified, this will return an empty List.
        
        This method will attempt to cast any values into a Boolean if possible,
        but may miss any values out if they are not compatible.

        Arguments
        - path: Path of the List to get.

        Returns
        - Requested List of Boolean.
        """
        ...


    def getDoubleList(self, path: str) -> list["Double"]:
        """
        Gets the requested List of Double by path.
        
        If the List does not exist but a default value has been specified, this
        will return the default value. If the List does not exist and no
        default value was specified, this will return an empty List.
        
        This method will attempt to cast any values into a Double if possible,
        but may miss any values out if they are not compatible.

        Arguments
        - path: Path of the List to get.

        Returns
        - Requested List of Double.
        """
        ...


    def getFloatList(self, path: str) -> list["Float"]:
        """
        Gets the requested List of Float by path.
        
        If the List does not exist but a default value has been specified, this
        will return the default value. If the List does not exist and no
        default value was specified, this will return an empty List.
        
        This method will attempt to cast any values into a Float if possible,
        but may miss any values out if they are not compatible.

        Arguments
        - path: Path of the List to get.

        Returns
        - Requested List of Float.
        """
        ...


    def getLongList(self, path: str) -> list["Long"]:
        """
        Gets the requested List of Long by path.
        
        If the List does not exist but a default value has been specified, this
        will return the default value. If the List does not exist and no
        default value was specified, this will return an empty List.
        
        This method will attempt to cast any values into a Long if possible,
        but may miss any values out if they are not compatible.

        Arguments
        - path: Path of the List to get.

        Returns
        - Requested List of Long.
        """
        ...


    def getByteList(self, path: str) -> list["Byte"]:
        """
        Gets the requested List of Byte by path.
        
        If the List does not exist but a default value has been specified, this
        will return the default value. If the List does not exist and no
        default value was specified, this will return an empty List.
        
        This method will attempt to cast any values into a Byte if possible,
        but may miss any values out if they are not compatible.

        Arguments
        - path: Path of the List to get.

        Returns
        - Requested List of Byte.
        """
        ...


    def getCharacterList(self, path: str) -> list["Character"]:
        """
        Gets the requested List of Character by path.
        
        If the List does not exist but a default value has been specified, this
        will return the default value. If the List does not exist and no
        default value was specified, this will return an empty List.
        
        This method will attempt to cast any values into a Character if
        possible, but may miss any values out if they are not compatible.

        Arguments
        - path: Path of the List to get.

        Returns
        - Requested List of Character.
        """
        ...


    def getShortList(self, path: str) -> list["Short"]:
        """
        Gets the requested List of Short by path.
        
        If the List does not exist but a default value has been specified, this
        will return the default value. If the List does not exist and no
        default value was specified, this will return an empty List.
        
        This method will attempt to cast any values into a Short if possible,
        but may miss any values out if they are not compatible.

        Arguments
        - path: Path of the List to get.

        Returns
        - Requested List of Short.
        """
        ...


    def getMapList(self, path: str) -> list[dict[Any, Any]]:
        """
        Gets the requested List of Maps by path.
        
        If the List does not exist but a default value has been specified, this
        will return the default value. If the List does not exist and no
        default value was specified, this will return an empty List.
        
        This method will attempt to cast any values into a Map if possible, but
        may miss any values out if they are not compatible.

        Arguments
        - path: Path of the List to get.

        Returns
        - Requested List of Maps.
        """
        ...


    def getObject(self, path: str, clazz: type["T"]) -> "T":
        """
        Gets the requested object at the given path.
        
        If the Object does not exist but a default value has been specified, this
        will return the default value. If the Object does not exist and no
        default value was specified, this will return null.
        
        **Note:** For example #getObject(path, String.class) is **not**
        equivalent to .getString(String) .getString(path) because
        .getString(String) .getString(path) converts internally all
        Objects to Strings. However, #getObject(path, Boolean.class) is
        equivalent to .getBoolean(String) .getBoolean(path) for example.
        
        Type `<T>`: the type of the requested object

        Arguments
        - path: the path to the object.
        - clazz: the type of the requested object

        Returns
        - Requested object
        """
        ...


    def getObject(self, path: str, clazz: type["T"], def: "T") -> "T":
        """
        Gets the requested object at the given path, returning a default value if
        not found
        
        If the Object does not exist then the specified default value will
        returned regardless of if a default has been identified in the root
        Configuration.
        
        **Note:** For example #getObject(path, String.class, def) is
        **not** equivalent to
        .getString(String, String) .getString(path, def) because
        .getString(String, String) .getString(path, def) converts
        internally all Objects to Strings. However, #getObject(path,
        Boolean.class, def) is equivalent to .getBoolean(String, boolean) .getBoolean(path,
        def) for example.
        
        Type `<T>`: the type of the requested object

        Arguments
        - path: the path to the object.
        - clazz: the type of the requested object
        - def: the default object to return if the object is not present at
        the path

        Returns
        - Requested object
        """
        ...


    def getSerializable(self, path: str, clazz: type["T"]) -> "T":
        """
        Gets the requested ConfigurationSerializable object at the given
        path.
        
        If the Object does not exist but a default value has been specified, this
        will return the default value. If the Object does not exist and no
        default value was specified, this will return null.
        
        Type `<T>`: the type of ConfigurationSerializable

        Arguments
        - path: the path to the object.
        - clazz: the type of ConfigurationSerializable

        Returns
        - Requested ConfigurationSerializable object
        """
        ...


    def getSerializable(self, path: str, clazz: type["T"], def: "T") -> "T":
        """
        Gets the requested ConfigurationSerializable object at the given
        path, returning a default value if not found
        
        If the Object does not exist then the specified default value will
        returned regardless of if a default has been identified in the root
        Configuration.
        
        Type `<T>`: the type of ConfigurationSerializable

        Arguments
        - path: the path to the object.
        - clazz: the type of ConfigurationSerializable
        - def: the default object to return if the object is not present at
        the path

        Returns
        - Requested ConfigurationSerializable object
        """
        ...


    def getVector(self, path: str) -> "Vector":
        """
        Gets the requested Vector by path.
        
        If the Vector does not exist but a default value has been specified,
        this will return the default value. If the Vector does not exist and no
        default value was specified, this will return null.

        Arguments
        - path: Path of the Vector to get.

        Returns
        - Requested Vector.
        """
        ...


    def getVector(self, path: str, def: "Vector") -> "Vector":
        """
        Gets the requested Vector by path, returning a default value if
        not found.
        
        If the Vector does not exist then the specified default value will
        returned regardless of if a default has been identified in the root
        Configuration.

        Arguments
        - path: Path of the Vector to get.
        - def: The default value to return if the path is not found or is
            not a Vector.

        Returns
        - Requested Vector.
        """
        ...


    def isVector(self, path: str) -> bool:
        """
        Checks if the specified path is a Vector.
        
        If the path exists but is not a Vector, this will return False. If the
        path does not exist, this will return False. If the path does not exist
        but a default value has been specified, this will check if that default
        value is a Vector and return appropriately.

        Arguments
        - path: Path of the Vector to check.

        Returns
        - Whether or not the specified path is a Vector.
        """
        ...


    def getOfflinePlayer(self, path: str) -> "OfflinePlayer":
        """
        Gets the requested OfflinePlayer by path.
        
        If the OfflinePlayer does not exist but a default value has been
        specified, this will return the default value. If the OfflinePlayer
        does not exist and no default value was specified, this will return
        null.

        Arguments
        - path: Path of the OfflinePlayer to get.

        Returns
        - Requested OfflinePlayer.
        """
        ...


    def getOfflinePlayer(self, path: str, def: "OfflinePlayer") -> "OfflinePlayer":
        """
        Gets the requested OfflinePlayer by path, returning a default
        value if not found.
        
        If the OfflinePlayer does not exist then the specified default value
        will returned regardless of if a default has been identified in the
        root Configuration.

        Arguments
        - path: Path of the OfflinePlayer to get.
        - def: The default value to return if the path is not found or is
            not an OfflinePlayer.

        Returns
        - Requested OfflinePlayer.
        """
        ...


    def isOfflinePlayer(self, path: str) -> bool:
        """
        Checks if the specified path is an OfflinePlayer.
        
        If the path exists but is not a OfflinePlayer, this will return False.
        If the path does not exist, this will return False. If the path does
        not exist but a default value has been specified, this will check if
        that default value is a OfflinePlayer and return appropriately.

        Arguments
        - path: Path of the OfflinePlayer to check.

        Returns
        - Whether or not the specified path is an OfflinePlayer.
        """
        ...


    def getItemStack(self, path: str) -> "ItemStack":
        """
        Gets the requested ItemStack by path.
        
        If the ItemStack does not exist but a default value has been specified,
        this will return the default value. If the ItemStack does not exist and
        no default value was specified, this will return null.

        Arguments
        - path: Path of the ItemStack to get.

        Returns
        - Requested ItemStack.
        """
        ...


    def getItemStack(self, path: str, def: "ItemStack") -> "ItemStack":
        """
        Gets the requested ItemStack by path, returning a default value
        if not found.
        
        If the ItemStack does not exist then the specified default value will
        returned regardless of if a default has been identified in the root
        Configuration.

        Arguments
        - path: Path of the ItemStack to get.
        - def: The default value to return if the path is not found or is
            not an ItemStack.

        Returns
        - Requested ItemStack.
        """
        ...


    def isItemStack(self, path: str) -> bool:
        """
        Checks if the specified path is an ItemStack.
        
        If the path exists but is not a ItemStack, this will return False. If
        the path does not exist, this will return False. If the path does not
        exist but a default value has been specified, this will check if that
        default value is a ItemStack and return appropriately.

        Arguments
        - path: Path of the ItemStack to check.

        Returns
        - Whether or not the specified path is an ItemStack.
        """
        ...


    def getColor(self, path: str) -> "Color":
        """
        Gets the requested Color by path.
        
        If the Color does not exist but a default value has been specified,
        this will return the default value. If the Color does not exist and no
        default value was specified, this will return null.

        Arguments
        - path: Path of the Color to get.

        Returns
        - Requested Color.
        """
        ...


    def getColor(self, path: str, def: "Color") -> "Color":
        """
        Gets the requested Color by path, returning a default value if
        not found.
        
        If the Color does not exist then the specified default value will
        returned regardless of if a default has been identified in the root
        Configuration.

        Arguments
        - path: Path of the Color to get.
        - def: The default value to return if the path is not found or is
            not a Color.

        Returns
        - Requested Color.
        """
        ...


    def isColor(self, path: str) -> bool:
        """
        Checks if the specified path is a Color.
        
        If the path exists but is not a Color, this will return False. If the
        path does not exist, this will return False. If the path does not exist
        but a default value has been specified, this will check if that default
        value is a Color and return appropriately.

        Arguments
        - path: Path of the Color to check.

        Returns
        - Whether or not the specified path is a Color.
        """
        ...


    def getLocation(self, path: str) -> "Location":
        """
        Gets the requested Location by path.
        
        If the Location does not exist but a default value has been specified,
        this will return the default value. If the Location does not exist and no
        default value was specified, this will return null.

        Arguments
        - path: Path of the Location to get.

        Returns
        - Requested Location.
        """
        ...


    def getLocation(self, path: str, def: "Location") -> "Location":
        """
        Gets the requested Location by path, returning a default value if
        not found.
        
        If the Location does not exist then the specified default value will
        returned regardless of if a default has been identified in the root
        Configuration.

        Arguments
        - path: Path of the Location to get.
        - def: The default value to return if the path is not found or is not
        a Location.

        Returns
        - Requested Location.
        """
        ...


    def isLocation(self, path: str) -> bool:
        """
        Checks if the specified path is a Location.
        
        If the path exists but is not a Location, this will return False. If the
        path does not exist, this will return False. If the path does not exist
        but a default value has been specified, this will check if that default
        value is a Location and return appropriately.

        Arguments
        - path: Path of the Location to check.

        Returns
        - Whether or not the specified path is a Location.
        """
        ...


    def getConfigurationSection(self, path: str) -> "ConfigurationSection":
        """
        Gets the requested ConfigurationSection by path.
        
        If the ConfigurationSection does not exist but a default value has been
        specified, this will return the default value. If the
        ConfigurationSection does not exist and no default value was specified,
        this will return null.

        Arguments
        - path: Path of the ConfigurationSection to get.

        Returns
        - Requested ConfigurationSection.
        """
        ...


    def isConfigurationSection(self, path: str) -> bool:
        """
        Checks if the specified path is a ConfigurationSection.
        
        If the path exists but is not a ConfigurationSection, this will return
        False. If the path does not exist, this will return False. If the path
        does not exist but a default value has been specified, this will check
        if that default value is a ConfigurationSection and return
        appropriately.

        Arguments
        - path: Path of the ConfigurationSection to check.

        Returns
        - Whether or not the specified path is a ConfigurationSection.
        """
        ...


    def getDefaultSection(self) -> "ConfigurationSection":
        """
        Gets the equivalent ConfigurationSection from the default
        Configuration defined in .getRoot().
        
        If the root contains no defaults, or the defaults doesn't contain a
        value for this path, or the value at this path is not a ConfigurationSection then this will return null.

        Returns
        - Equivalent section in root configuration
        """
        ...


    def addDefault(self, path: str, value: "Object") -> None:
        """
        Sets the default value in the root at the given path as provided.
        
        If no source Configuration was provided as a default
        collection, then a new MemoryConfiguration will be created to
        hold the new default value.
        
        If value is null, the value will be removed from the default
        Configuration source.
        
        If the value as returned by .getDefaultSection() is null, then
        this will create a new section at the path, replacing anything that may
        have existed there previously.

        Arguments
        - path: Path of the value to set.
        - value: Value to set the default to.

        Raises
        - IllegalArgumentException: Thrown if path is null.
        """
        ...


    def getComments(self, path: str) -> list[str]:
        """
        Gets the requested comment list by path.
        
        If no comments exist, an empty list will be returned. A null entry
        represents an empty line and an empty String represents an empty comment
        line.

        Arguments
        - path: Path of the comments to get.

        Returns
        - A unmodifiable list of the requested comments, every entry
        represents one line.
        """
        ...


    def getInlineComments(self, path: str) -> list[str]:
        """
        Gets the requested inline comment list by path.
        
        If no comments exist, an empty list will be returned. A null entry
        represents an empty line and an empty String represents an empty comment
        line.

        Arguments
        - path: Path of the comments to get.

        Returns
        - A unmodifiable list of the requested comments, every entry
        represents one line.
        """
        ...


    def setComments(self, path: str, comments: list[str]) -> None:
        """
        Sets the comment list at the specified path.
        
        If value is null, the comments will be removed. A null entry is an empty
        line and an empty String entry is an empty comment line. If the path does
        not exist, no comments will be set. Any existing comments will be
        replaced, regardless of what the new comments are.
        
        Some implementations may have limitations on what persists. See their
        individual javadocs for details.

        Arguments
        - path: Path of the comments to set.
        - comments: New comments to set at the path, every entry represents
        one line.
        """
        ...


    def setInlineComments(self, path: str, comments: list[str]) -> None:
        """
        Sets the inline comment list at the specified path.
        
        If value is null, the comments will be removed. A null entry is an empty
        line and an empty String entry is an empty comment line. If the path does
        not exist, no comment will be set. Any existing comments will be
        replaced, regardless of what the new comments are.
        
        Some implementations may have limitations on what persists. See their
        individual javadocs for details.

        Arguments
        - path: Path of the comments to set.
        - comments: New comments to set at the path, every entry represents
        one line.
        """
        ...
