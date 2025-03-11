"""
Python module generated from Java source file org.bukkit.profile.PlayerTextures

Java source file obtained from artifact spigot-api version 1.21.2-R0.1-20241023.084343-5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.net import URL
from org.bukkit.profile import *
from typing import Any, Callable, Iterable, Tuple


class PlayerTextures:
    """
    Provides access to the textures stored inside a PlayerProfile.
    
    Modifying the textures immediately invalidates and clears any previously
    present attributes that are specific to official player profiles, such as the
    .getTimestamp() timestamp and .isSigned() signature.
    """

    def isEmpty(self) -> bool:
        """
        Checks if the profile stores no textures.

        Returns
        - `True` if the profile stores no textures
        """
        ...


    def clear(self) -> None:
        """
        Clears the textures.
        """
        ...


    def getSkin(self) -> "URL":
        """
        Gets the URL that points to the player's skin.

        Returns
        - the URL of the player's skin, or `null` if not set
        """
        ...


    def setSkin(self, skinUrl: "URL") -> None:
        """
        Sets the player's skin to the specified URL, and the skin model to
        SkinModel.CLASSIC.
        
        The URL **must** point to the Minecraft texture server. Example URL:
        ```
        http://textures.minecraft.net/texture/b3fbd454b599df593f57101bfca34e67d292a8861213d2202bb575da7fd091ac
        ```

        Arguments
        - skinUrl: the URL of the player's skin, or `null` to
        unset it
        """
        ...


    def setSkin(self, skinUrl: "URL", skinModel: "SkinModel") -> None:
        """
        Sets the player's skin and SkinModel.
        
        The URL **must** point to the Minecraft texture server. Example URL:
        ```
        http://textures.minecraft.net/texture/b3fbd454b599df593f57101bfca34e67d292a8861213d2202bb575da7fd091ac
        ```
        
        A skin model of `null` results in SkinModel.CLASSIC to
        be used.

        Arguments
        - skinUrl: the URL of the player's skin, or `null` to
        unset it
        - skinModel: the skin model, ignored if the skin URL is
        `null`
        """
        ...


    def getSkinModel(self) -> "SkinModel":
        """
        Gets the model of the player's skin.
        
        This returns SkinModel.CLASSIC if no skin is set.

        Returns
        - the model of the player's skin
        """
        ...


    def getCape(self) -> "URL":
        """
        Gets the URL that points to the player's cape.

        Returns
        - the URL of the player's cape, or `null` if not set
        """
        ...


    def setCape(self, capeUrl: "URL") -> None:
        """
        Sets the URL that points to the player's cape.
        
        The URL **must** point to the Minecraft texture server. Example URL:
        ```
        http://textures.minecraft.net/texture/2340c0e03dd24a11b15a8b33c2a7e9e32abb2051b2481d0ba7defd635ca7a933
        ```

        Arguments
        - capeUrl: the URL of the player's cape, or `null` to
        unset it
        """
        ...


    def getTimestamp(self) -> int:
        """
        Gets the timestamp at which the profile was last updated.

        Returns
        - the timestamp, or `0` if unknown
        """
        ...


    def isSigned(self) -> bool:
        """
        Checks if the textures are signed and the signature is valid.

        Returns
        - `True` if the textures are signed and the signature is
        valid
        """
        ...
