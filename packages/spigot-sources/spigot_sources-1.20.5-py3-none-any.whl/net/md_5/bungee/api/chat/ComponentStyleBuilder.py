"""
Python module generated from Java source file net.md_5.bungee.api.chat.ComponentStyleBuilder

Java source file obtained from artifact bungeecord-chat version 1.20-R0.2-20240119.213604-65

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from net.md_5.bungee.api import ChatColor
from net.md_5.bungee.api.chat import *
from typing import Any, Callable, Iterable, Tuple


class ComponentStyleBuilder:
    """
    
    ComponentStyleBuilder simplifies creating component styles by allowing the
    use of a chainable builder.
    
    ```
    ComponentStyle style = ComponentStyle.builder()
        .color(ChatColor.RED)
        .font("custom:font")
        .bold(True).italic(True).create();
    
    BaseComponent component = new ComponentBuilder("Hello world").style(style).create();
    // Or it can be used directly on a component
    TextComponent text = new TextComponent("Hello world");
    text.applyStyle(style);
    ```

    See
    - ComponentStyle.builder(ComponentStyle)
    """

    def color(self, color: "ChatColor") -> "ComponentStyleBuilder":
        """
        Set the style color.

        Arguments
        - color: the color to set, or null to use the default

        Returns
        - this ComponentStyleBuilder for chaining
        """
        ...


    def font(self, font: str) -> "ComponentStyleBuilder":
        """
        Set the style font.

        Arguments
        - font: the font key to set, or null to use the default

        Returns
        - this ComponentStyleBuilder for chaining
        """
        ...


    def bold(self, bold: "Boolean") -> "ComponentStyleBuilder":
        """
        Set the style's bold property.

        Arguments
        - bold: the bold value to set, or null to use the default

        Returns
        - this ComponentStyleBuilder for chaining
        """
        ...


    def italic(self, italic: "Boolean") -> "ComponentStyleBuilder":
        """
        Set the style's italic property.

        Arguments
        - italic: the italic value to set, or null to use the default

        Returns
        - this ComponentStyleBuilder for chaining
        """
        ...


    def underlined(self, underlined: "Boolean") -> "ComponentStyleBuilder":
        """
        Set the style's underlined property.

        Arguments
        - underlined: the underlined value to set, or null to use the default

        Returns
        - this ComponentStyleBuilder for chaining
        """
        ...


    def strikethrough(self, strikethrough: "Boolean") -> "ComponentStyleBuilder":
        """
        Set the style's strikethrough property.

        Arguments
        - strikethrough: the strikethrough value to set, or null to use the
        default

        Returns
        - this ComponentStyleBuilder for chaining
        """
        ...


    def obfuscated(self, obfuscated: "Boolean") -> "ComponentStyleBuilder":
        """
        Set the style's obfuscated property.

        Arguments
        - obfuscated: the obfuscated value to set, or null to use the default

        Returns
        - this ComponentStyleBuilder for chaining
        """
        ...


    def build(self) -> "ComponentStyle":
        """
        Build the ComponentStyle using the values set in this builder.

        Returns
        - the created ComponentStyle
        """
        ...
