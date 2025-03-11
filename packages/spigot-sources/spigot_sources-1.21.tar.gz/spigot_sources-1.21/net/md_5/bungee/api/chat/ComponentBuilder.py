"""
Python module generated from Java source file net.md_5.bungee.api.chat.ComponentBuilder

Java source file obtained from artifact bungeecord-chat version 1.20-R0.2-20240119.213604-65

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from enum import Enum
from net.md_5.bungee.api import ChatColor
from net.md_5.bungee.api.chat import *
from typing import Any, Callable, Iterable, Tuple


class ComponentBuilder:
    """
    
    ComponentBuilder simplifies creating basic messages by allowing the use of a
    chainable builder.
    
    ```
    new ComponentBuilder("Hello ").color(ChatColor.RED).
    append("World").color(ChatColor.BLUE). append("!").bold(True).create();
    ```
    
    All methods (excluding .append(String) and .create() work on
    the last part appended to the builder, so in the example above "Hello " would
    be net.md_5.bungee.api.ChatColor.RED and "World" would be
    net.md_5.bungee.api.ChatColor.BLUE but "!" would be bold and
    net.md_5.bungee.api.ChatColor.BLUE because append copies the previous
    part's formatting
    """

    def __init__(self, original: "ComponentBuilder"):
        """
        Creates a ComponentBuilder from the other given ComponentBuilder to clone
        it.

        Arguments
        - original: the original for the new ComponentBuilder.
        """
        ...


    def __init__(self, text: str):
        """
        Creates a ComponentBuilder with the given text as the first part.

        Arguments
        - text: the first text element
        """
        ...


    def __init__(self, component: "BaseComponent"):
        """
        Creates a ComponentBuilder with the given component as the first part.

        Arguments
        - component: the first component element
        """
        ...


    def resetCursor(self) -> "ComponentBuilder":
        """
        Resets the cursor to index of the last element.

        Returns
        - this ComponentBuilder for chaining
        """
        ...


    def setCursor(self, pos: int) -> "ComponentBuilder":
        """
        Sets the position of the current component to be modified

        Arguments
        - pos: the cursor position synonymous to an element position for a
        list

        Returns
        - this ComponentBuilder for chaining

        Raises
        - IndexOutOfBoundsException: if the index is out of range
        (`index < 0 || index >= size()`)
        """
        ...


    def append(self, component: "BaseComponent") -> "ComponentBuilder":
        """
        Appends a component to the builder and makes it the current target for
        formatting. The component will have all the formatting from previous
        part.

        Arguments
        - component: the component to append

        Returns
        - this ComponentBuilder for chaining
        """
        ...


    def append(self, component: "BaseComponent", retention: "FormatRetention") -> "ComponentBuilder":
        """
        Appends a component to the builder and makes it the current target for
        formatting. You can specify the amount of formatting retained from
        previous part.

        Arguments
        - component: the component to append
        - retention: the formatting to retain

        Returns
        - this ComponentBuilder for chaining
        """
        ...


    def append(self, components: list["BaseComponent"]) -> "ComponentBuilder":
        """
        Appends the components to the builder and makes the last element the
        current target for formatting. The components will have all the
        formatting from previous part.

        Arguments
        - components: the components to append

        Returns
        - this ComponentBuilder for chaining
        """
        ...


    def append(self, components: list["BaseComponent"], retention: "FormatRetention") -> "ComponentBuilder":
        """
        Appends the components to the builder and makes the last element the
        current target for formatting. You can specify the amount of formatting
        retained from previous part.

        Arguments
        - components: the components to append
        - retention: the formatting to retain

        Returns
        - this ComponentBuilder for chaining
        """
        ...


    def append(self, translatable: "TranslationProvider") -> "ComponentBuilder":
        """
        Appends the TranslationProvider object to the builder and makes
        the last element the current target for formatting. The components will
        have all the formatting from previous part.

        Arguments
        - translatable: the translatable object to append

        Returns
        - this ComponentBuilder for chaining
        """
        ...


    def append(self, translatable: "TranslationProvider", retention: "FormatRetention") -> "ComponentBuilder":
        """
        Appends the TranslationProvider object to the builder and makes
        the last element the current target for formatting. You can specify the
        amount of formatting retained from previous part.

        Arguments
        - translatable: the translatable object to append
        - retention: the formatting to retain

        Returns
        - this ComponentBuilder for chaining
        """
        ...


    def append(self, text: str) -> "ComponentBuilder":
        """
        Appends the text to the builder and makes it the current target for
        formatting. The text will have all the formatting from previous part.

        Arguments
        - text: the text to append

        Returns
        - this ComponentBuilder for chaining
        """
        ...


    def appendLegacy(self, text: str) -> "ComponentBuilder":
        """
        Parse text to BaseComponent[] with colors and format, appends the text to
        the builder and makes it the current target for formatting. The component
        will have all the formatting from previous part.

        Arguments
        - text: the text to append

        Returns
        - this ComponentBuilder for chaining
        """
        ...


    def append(self, text: str, retention: "FormatRetention") -> "ComponentBuilder":
        """
        Appends the text to the builder and makes it the current target for
        formatting. You can specify the amount of formatting retained from
        previous part.

        Arguments
        - text: the text to append
        - retention: the formatting to retain

        Returns
        - this ComponentBuilder for chaining
        """
        ...


    def append(self, joiner: "Joiner") -> "ComponentBuilder":
        """
        Allows joining additional components to this builder using the given
        Joiner and FormatRetention.ALL.
        
        Simply executes the provided joiner on this instance to facilitate a
        chain pattern.

        Arguments
        - joiner: joiner used for operation

        Returns
        - this ComponentBuilder for chaining
        """
        ...


    def append(self, joiner: "Joiner", retention: "FormatRetention") -> "ComponentBuilder":
        """
        Allows joining additional components to this builder using the given
        Joiner.
        
        Simply executes the provided joiner on this instance to facilitate a
        chain pattern.

        Arguments
        - joiner: joiner used for operation
        - retention: the formatting to retain

        Returns
        - this ComponentBuilder for chaining
        """
        ...


    def removeComponent(self, pos: int) -> None:
        """
        Remove the component part at the position of given index.

        Arguments
        - pos: the index to remove at

        Raises
        - IndexOutOfBoundsException: if the index is out of range
        (`index < 0 || index >= size()`)
        """
        ...


    def getComponent(self, pos: int) -> "BaseComponent":
        """
        Gets the component part at the position of given index.

        Arguments
        - pos: the index to find

        Returns
        - the component

        Raises
        - IndexOutOfBoundsException: if the index is out of range
        (`index < 0 || index >= size()`)
        """
        ...


    def getCurrentComponent(self) -> "BaseComponent":
        """
        Gets the component at the position of the cursor.

        Returns
        - the active component or null if builder is empty
        """
        ...


    def color(self, color: "ChatColor") -> "ComponentBuilder":
        """
        Sets the color of the current part.

        Arguments
        - color: the new color

        Returns
        - this ComponentBuilder for chaining
        """
        ...


    def font(self, font: str) -> "ComponentBuilder":
        """
        Sets the font of the current part.

        Arguments
        - font: the new font

        Returns
        - this ComponentBuilder for chaining
        """
        ...


    def bold(self, bold: bool) -> "ComponentBuilder":
        """
        Sets whether the current part is bold.

        Arguments
        - bold: whether this part is bold

        Returns
        - this ComponentBuilder for chaining
        """
        ...


    def italic(self, italic: bool) -> "ComponentBuilder":
        """
        Sets whether the current part is italic.

        Arguments
        - italic: whether this part is italic

        Returns
        - this ComponentBuilder for chaining
        """
        ...


    def underlined(self, underlined: bool) -> "ComponentBuilder":
        """
        Sets whether the current part is underlined.

        Arguments
        - underlined: whether this part is underlined

        Returns
        - this ComponentBuilder for chaining
        """
        ...


    def strikethrough(self, strikethrough: bool) -> "ComponentBuilder":
        """
        Sets whether the current part is strikethrough.

        Arguments
        - strikethrough: whether this part is strikethrough

        Returns
        - this ComponentBuilder for chaining
        """
        ...


    def obfuscated(self, obfuscated: bool) -> "ComponentBuilder":
        """
        Sets whether the current part is obfuscated.

        Arguments
        - obfuscated: whether this part is obfuscated

        Returns
        - this ComponentBuilder for chaining
        """
        ...


    def style(self, style: "ComponentStyle") -> "ComponentBuilder":
        """
        Applies the provided ComponentStyle to the current part.

        Arguments
        - style: the style to apply

        Returns
        - this ComponentBuilder for chaining
        """
        ...


    def insertion(self, insertion: str) -> "ComponentBuilder":
        """
        Sets the insertion text for the current part.

        Arguments
        - insertion: the insertion text

        Returns
        - this ComponentBuilder for chaining
        """
        ...


    def event(self, clickEvent: "ClickEvent") -> "ComponentBuilder":
        """
        Sets the click event for the current part.

        Arguments
        - clickEvent: the click event

        Returns
        - this ComponentBuilder for chaining
        """
        ...


    def event(self, hoverEvent: "HoverEvent") -> "ComponentBuilder":
        """
        Sets the hover event for the current part.

        Arguments
        - hoverEvent: the hover event

        Returns
        - this ComponentBuilder for chaining
        """
        ...


    def reset(self) -> "ComponentBuilder":
        """
        Sets the current part back to normal settings. Only text is kept.

        Returns
        - this ComponentBuilder for chaining
        """
        ...


    def retain(self, retention: "FormatRetention") -> "ComponentBuilder":
        """
        Retains only the specified formatting. Text is not modified.

        Arguments
        - retention: the formatting to retain

        Returns
        - this ComponentBuilder for chaining
        """
        ...


    def build(self) -> "BaseComponent":
        """
        Returns the component built by this builder. If this builder is empty, an
        empty text component will be returned.

        Returns
        - the component
        """
        ...


    def create(self) -> list["BaseComponent"]:
        """
        Returns the components needed to display the message created by this
        builder.git
        
        <strong>NOTE:</strong> .build() is preferred as it will
        consolidate all components into a single BaseComponent with extra
        contents as opposed to an array of components which is non-standard and
        may result in unexpected behavior.

        Returns
        - the created components
        """
        ...


    class Joiner:
        """
        Functional interface to join additional components to a ComponentBuilder.
        """

        def join(self, componentBuilder: "ComponentBuilder", retention: "FormatRetention") -> "ComponentBuilder":
            """
            Joins additional components to the provided ComponentBuilder
            and then returns it to fulfill a chain pattern.
            
            Retention may be ignored and is to be understood as an optional
            recommendation to the Joiner and not as a guarantee to have a
            previous component in builder unmodified.

            Arguments
            - componentBuilder: to which to append additional components
            - retention: the formatting to possibly retain

            Returns
            - input componentBuilder for chaining
            """
            ...


    class FormatRetention(Enum):

        NONE = 0
        """
        Specify that we do not want to retain anything from the previous
        component.
        """
        FORMATTING = 1
        """
        Specify that we want the formatting retained from the previous
        component.
        """
        EVENTS = 2
        """
        Specify that we want the events retained from the previous component.
        """
        ALL = 3
        """
        Specify that we want to retain everything from the previous
        component.
        """
