"""
Python module generated from Java source file net.md_5.bungee.api.chat.BaseComponent

Java source file obtained from artifact bungeecord-chat version 1.20-R0.2-20240119.213604-65

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from net.md_5.bungee.api import ChatColor
from net.md_5.bungee.api.chat import *
from net.md_5.bungee.api.chat.ComponentBuilder import FormatRetention
from typing import Any, Callable, Iterable, Tuple


class BaseComponent:

    def __init__(self):
        """
        Default constructor.

        Deprecated
        - for use by internal classes only, will be removed.
        """
        ...


    def copyFormatting(self, component: "BaseComponent") -> None:
        """
        Copies the events and formatting of a BaseComponent. Already set
        formatting will be replaced.

        Arguments
        - component: the component to copy from
        """
        ...


    def copyFormatting(self, component: "BaseComponent", replace: bool) -> None:
        """
        Copies the events and formatting of a BaseComponent.

        Arguments
        - component: the component to copy from
        - replace: if already set formatting should be replaced by the new
        component
        """
        ...


    def copyFormatting(self, component: "BaseComponent", retention: "FormatRetention", replace: bool) -> None:
        """
        Copies the specified formatting of a BaseComponent.

        Arguments
        - component: the component to copy from
        - retention: the formatting to copy
        - replace: if already set formatting should be replaced by the new
        component
        """
        ...


    def retain(self, retention: "FormatRetention") -> None:
        """
        Retains only the specified formatting.

        Arguments
        - retention: the formatting to retain
        """
        ...


    def duplicate(self) -> "BaseComponent":
        """
        Clones the BaseComponent and returns the clone.

        Returns
        - The duplicate of this BaseComponent
        """
        ...


    def duplicateWithoutFormatting(self) -> "BaseComponent":
        """
        Clones the BaseComponent without formatting and returns the clone.

        Returns
        - The duplicate of this BaseComponent

        Deprecated
        - API use discouraged, use traditional duplicate
        """
        ...


    @staticmethod
    def toLegacyText(*components: Tuple["BaseComponent", ...]) -> str:
        """
        Converts the components to a string that uses the old formatting codes
        (net.md_5.bungee.api.ChatColor.COLOR_CHAR

        Arguments
        - components: the components to convert

        Returns
        - the string in the old format
        """
        ...


    @staticmethod
    def toPlainText(*components: Tuple["BaseComponent", ...]) -> str:
        """
        Converts the components into a string without any formatting

        Arguments
        - components: the components to convert

        Returns
        - the string as plain text
        """
        ...


    def setStyle(self, style: "ComponentStyle") -> None:
        """
        Set the ComponentStyle for this component.
        
        Unlike .applyStyle(ComponentStyle), this method will overwrite
        all style values on this component.

        Arguments
        - style: the style to set, or null to set all style values to default
        """
        ...


    def setColor(self, color: "ChatColor") -> None:
        """
        Set this component's color.

        Arguments
        - color: the component color, or null to use the default
        """
        ...


    def getColor(self) -> "ChatColor":
        """
        Returns the color of this component. This uses the parent's color if this
        component doesn't have one. net.md_5.bungee.api.ChatColor.WHITE
        is returned if no color is found.

        Returns
        - the color of this component
        """
        ...


    def getColorRaw(self) -> "ChatColor":
        """
        Returns the color of this component without checking the parents color.
        May return null

        Returns
        - the color of this component
        """
        ...


    def setFont(self, font: str) -> None:
        """
        Set this component's font.

        Arguments
        - font: the font to set, or null to use the default
        """
        ...


    def getFont(self) -> str:
        """
        Returns the font of this component. This uses the parent's font if this
        component doesn't have one.

        Returns
        - the font of this component, or null if default font
        """
        ...


    def getFontRaw(self) -> str:
        """
        Returns the font of this component without checking the parents font. May
        return null

        Returns
        - the font of this component
        """
        ...


    def setBold(self, bold: "Boolean") -> None:
        """
        Set whether or not this component is bold.

        Arguments
        - bold: the new bold state, or null to use the default
        """
        ...


    def isBold(self) -> bool:
        """
        Returns whether this component is bold. This uses the parent's setting if
        this component hasn't been set. False is returned if none of the parent
        chain has been set.

        Returns
        - whether the component is bold
        """
        ...


    def isBoldRaw(self) -> "Boolean":
        """
        Returns whether this component is bold without checking the parents
        setting. May return null

        Returns
        - whether the component is bold
        """
        ...


    def setItalic(self, italic: "Boolean") -> None:
        """
        Set whether or not this component is italic.

        Arguments
        - italic: the new italic state, or null to use the default
        """
        ...


    def isItalic(self) -> bool:
        """
        Returns whether this component is italic. This uses the parent's setting
        if this component hasn't been set. False is returned if none of the
        parent chain has been set.

        Returns
        - whether the component is italic
        """
        ...


    def isItalicRaw(self) -> "Boolean":
        """
        Returns whether this component is italic without checking the parents
        setting. May return null

        Returns
        - whether the component is italic
        """
        ...


    def setUnderlined(self, underlined: "Boolean") -> None:
        """
        Set whether or not this component is underlined.

        Arguments
        - underlined: the new underlined state, or null to use the default
        """
        ...


    def isUnderlined(self) -> bool:
        """
        Returns whether this component is underlined. This uses the parent's
        setting if this component hasn't been set. False is returned if none of
        the parent chain has been set.

        Returns
        - whether the component is underlined
        """
        ...


    def isUnderlinedRaw(self) -> "Boolean":
        """
        Returns whether this component is underlined without checking the parents
        setting. May return null

        Returns
        - whether the component is underlined
        """
        ...


    def setStrikethrough(self, strikethrough: "Boolean") -> None:
        """
        Set whether or not this component is strikethrough.

        Arguments
        - strikethrough: the new strikethrough state, or null to use the
        default
        """
        ...


    def isStrikethrough(self) -> bool:
        """
        Returns whether this component is strikethrough. This uses the parent's
        setting if this component hasn't been set. False is returned if none of
        the parent chain has been set.

        Returns
        - whether the component is strikethrough
        """
        ...


    def isStrikethroughRaw(self) -> "Boolean":
        """
        Returns whether this component is strikethrough without checking the
        parents setting. May return null

        Returns
        - whether the component is strikethrough
        """
        ...


    def setObfuscated(self, obfuscated: "Boolean") -> None:
        """
        Set whether or not this component is obfuscated.

        Arguments
        - obfuscated: the new obfuscated state, or null to use the default
        """
        ...


    def isObfuscated(self) -> bool:
        """
        Returns whether this component is obfuscated. This uses the parent's
        setting if this component hasn't been set. False is returned if none of
        the parent chain has been set.

        Returns
        - whether the component is obfuscated
        """
        ...


    def isObfuscatedRaw(self) -> "Boolean":
        """
        Returns whether this component is obfuscated without checking the parents
        setting. May return null

        Returns
        - whether the component is obfuscated
        """
        ...


    def applyStyle(self, style: "ComponentStyle") -> None:
        """
        Apply the style from the given ComponentStyle to this component.
        
        Any style values that have been explicitly set in the style will be
        applied to this component. If a value is not set in the style, it will
        not override the style set in this component.

        Arguments
        - style: the style to apply
        """
        ...


    def setExtra(self, components: list["BaseComponent"]) -> None:
        ...


    def addExtra(self, text: str) -> None:
        """
        Appends a text element to the component. The text will inherit this
        component's formatting

        Arguments
        - text: the text to append
        """
        ...


    def addExtra(self, component: "BaseComponent") -> None:
        """
        Appends a component to the component. The text will inherit this
        component's formatting

        Arguments
        - component: the component to append
        """
        ...


    def hasStyle(self) -> bool:
        """
        Returns whether the component has any styling applied to it.

        Returns
        - Whether any styling is applied
        """
        ...


    def hasFormatting(self) -> bool:
        """
        Returns whether the component has any formatting or events applied to it

        Returns
        - Whether any formatting or events are applied
        """
        ...


    def toPlainText(self) -> str:
        """
        Converts the component into a string without any formatting

        Returns
        - the string as plain text
        """
        ...


    def toLegacyText(self) -> str:
        """
        Converts the component to a string that uses the old formatting codes
        (net.md_5.bungee.api.ChatColor.COLOR_CHAR

        Returns
        - the string in the old format
        """
        ...
