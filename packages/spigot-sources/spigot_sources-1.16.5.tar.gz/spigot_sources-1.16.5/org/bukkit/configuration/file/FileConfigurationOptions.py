"""
Python module generated from Java source file org.bukkit.configuration.file.FileConfigurationOptions

Java source file obtained from artifact spigot-api version 1.16.5-R0.1-20210611.041013-99

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.configuration import MemoryConfiguration
from org.bukkit.configuration import MemoryConfigurationOptions
from org.bukkit.configuration.file import *
from typing import Any, Callable, Iterable, Tuple


class FileConfigurationOptions(MemoryConfigurationOptions):
    """
    Various settings for controlling the input and output of a FileConfiguration
    """

    def configuration(self) -> "FileConfiguration":
        ...


    def copyDefaults(self, value: bool) -> "FileConfigurationOptions":
        ...


    def pathSeparator(self, value: str) -> "FileConfigurationOptions":
        ...


    def header(self) -> str:
        """
        Gets the header that will be applied to the top of the saved output.
        
        This header will be commented out and applied directly at the top of
        the generated output of the FileConfiguration. It is not
        required to include a newline at the end of the header as it will
        automatically be applied, but you may include one if you wish for extra
        spacing.
        
        Null is a valid value which will indicate that no header is to be
        applied. The default value is null.

        Returns
        - Header
        """
        ...


    def header(self, value: str) -> "FileConfigurationOptions":
        """
        Sets the header that will be applied to the top of the saved output.
        
        This header will be commented out and applied directly at the top of
        the generated output of the FileConfiguration. It is not
        required to include a newline at the end of the header as it will
        automatically be applied, but you may include one if you wish for extra
        spacing.
        
        Null is a valid value which will indicate that no header is to be
        applied.

        Arguments
        - value: New header

        Returns
        - This object, for chaining
        """
        ...


    def copyHeader(self) -> bool:
        """
        Gets whether or not the header should be copied from a default source.
        
        If this is True, if a default FileConfiguration is passed to
        FileConfiguration.setDefaults(org.bukkit.configuration.Configuration)
        then upon saving it will use the header from that config, instead of
        the one provided here.
        
        If no default is set on the configuration, or the default is not of
        type FileConfiguration, or that config has no header (.header()
        returns null) then the header specified in this configuration will be
        used.
        
        Defaults to True.

        Returns
        - Whether or not to copy the header
        """
        ...


    def copyHeader(self, value: bool) -> "FileConfigurationOptions":
        """
        Sets whether or not the header should be copied from a default source.
        
        If this is True, if a default FileConfiguration is passed to
        FileConfiguration.setDefaults(org.bukkit.configuration.Configuration)
        then upon saving it will use the header from that config, instead of
        the one provided here.
        
        If no default is set on the configuration, or the default is not of
        type FileConfiguration, or that config has no header (.header()
        returns null) then the header specified in this configuration will be
        used.
        
        Defaults to True.

        Arguments
        - value: Whether or not to copy the header

        Returns
        - This object, for chaining
        """
        ...
