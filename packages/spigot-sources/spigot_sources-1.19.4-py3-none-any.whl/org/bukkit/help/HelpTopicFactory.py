"""
Python module generated from Java source file org.bukkit.help.HelpTopicFactory

Java source file obtained from artifact spigot-api version 1.19.4-R0.1-20230607.155743-88

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.command import Command
from org.bukkit.help import *
from typing import Any, Callable, Iterable, Tuple


class HelpTopicFactory:
    """
    A HelpTopicFactory is used to create custom HelpTopic objects from
    commands that inherit from a common base class or have executors that
    inherit from a common base class. You can use a custom HelpTopic to change
    the way all the commands in your plugin display in the help. If your plugin
    implements a complex permissions system, a custom help topic may also be
    appropriate.
    
    To automatically bind your plugin's commands to your custom HelpTopic
    implementation, first make sure all your commands or executors derive from
    a custom base class (it doesn't have to do anything). Next implement a
    custom HelpTopicFactory that accepts your custom command base class and
    instantiates an instance of your custom HelpTopic from it. Finally,
    register your HelpTopicFactory against your command base class using the
    HelpMap.registerHelpTopicFactory(Class, HelpTopicFactory) method.
    
    As the help system iterates over all registered commands to make help
    topics, it first checks to see if there is a HelpTopicFactory registered
    for the command's base class. If so, the factory is used to make a help
    topic rather than a generic help topic. If no factory is found for the
    command's base class and the command derives from org.bukkit.command.PluginCommand, then the type of the command's executor
    is inspected looking for a registered HelpTopicFactory. Finally, if no
    factory is found, a generic help topic is created for the command.

    Arguments
    - <TCommand>: The base class for your custom commands.
    """

    def createTopic(self, command: "TCommand") -> "HelpTopic":
        """
        This method accepts a command deriving from a custom command base class
        and constructs a custom HelpTopic for it.

        Arguments
        - command: The custom command to build a help topic for.

        Returns
        - A new custom help topic or `null` to intentionally NOT
            create a topic.
        """
        ...
