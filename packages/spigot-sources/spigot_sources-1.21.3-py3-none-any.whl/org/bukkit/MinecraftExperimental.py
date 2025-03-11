"""
Python module generated from Java source file org.bukkit.MinecraftExperimental

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import *
from typing import Any, Callable, Iterable, Tuple


class MinecraftExperimental:
    """
    Indicates that the annotated element (class, method, field, etc.) is part of a
    <a href="https://minecraft.wiki/w/Experimental_Gameplay">minecraft experimental feature</a>
    and is subject to changes by Mojang.
    
    **Note:** Elements marked with this annotation require the use of a datapack or otherwise
    non-standard feature to be enabled on the server.

    See
    - <a href="https://www.minecraft.net/en-us/article/testing-new-minecraft-features/feature-toggles-java-edition">Features Toggles - Minecraft Article</a>
    """

    def value(self) -> "Requires":
        """
        Get the feature that must be enabled for the annotated object to be valid.
        
        While this value is not used anywhere in Bukkit, it is a convenience value to assist
        in locating relevant annotated elements for removal once no longer deemed an experimental
        feature by Minecraft. See Requires for information about use in plugins.

        Returns
        - the required feature flag
        """
        ...
