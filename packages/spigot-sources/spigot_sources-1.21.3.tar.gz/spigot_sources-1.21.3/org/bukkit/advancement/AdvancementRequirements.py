"""
Python module generated from Java source file org.bukkit.advancement.AdvancementRequirements

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.advancement import *
from typing import Any, Callable, Iterable, Tuple


class AdvancementRequirements:
    """
    The list of requirements for the advancement.
    
    Requirements are complimentary to criteria. They are just lists that contain
    more lists, which in turn contains strings that equal the names of the
    criteria. Ultimately defining the logic around how criteria are completed in
    order to grant the advancement.

    See
    - <a href=https://www.minecraftforum.net/forums/minecraft-java-edition/redstone-discussion-and/commands-command-blocks-and/2809368-1-12-custom-advancements-aka-achievements.Requirements>Advancement Requirements</a>
    """

    def getRequirements(self) -> list["AdvancementRequirement"]:
        """
        Get all the requirements present in this advancement.

        Returns
        - an unmodifiable copy of all requirements.
        """
        ...
