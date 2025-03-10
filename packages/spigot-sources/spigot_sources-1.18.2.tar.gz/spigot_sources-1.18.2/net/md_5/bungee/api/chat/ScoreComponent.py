"""
Python module generated from Java source file net.md_5.bungee.api.chat.ScoreComponent

Java source file obtained from artifact bungeecord-chat version 1.16-R0.5-20210527.222444-33

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from net.md_5.bungee.api.chat import *
from typing import Any, Callable, Iterable, Tuple


class ScoreComponent(BaseComponent):
    """
    This component displays the score based on a player score on the scoreboard.
    
    The **name** is the name of the player stored on the scoreboard, which may
    be a "fake" player. It can also be a target selector that **must** resolve
    to 1 target, and may target non-player entities.
    
    With a book, /tellraw, or /title, using the wildcard '*' in the place of a
    name or target selector will cause all players to see their own score in the
    specified objective.
    
    **Signs cannot use the '*' wildcard**
    
    These values are filled in by the server-side implementation.
    
    As of 1.12.2, a bug ( MC-56373 ) prevents full usage within hover events.
    """

    def __init__(self, name: str, objective: str):
        """
        Creates a new score component with the specified name and objective.
        If not specifically set, value will default to an empty string;
        signifying that the scoreboard value should take precedence. If not null,
        nor empty, `value` will override any value found in the
        scoreboard.
        The value defaults to an empty string.

        Arguments
        - name: the name of the entity, or an entity selector, whose score
        should be displayed
        - objective: the internal name of the objective the entity's score is
        attached to
        """
        ...


    def __init__(self, original: "ScoreComponent"):
        """
        Creates a score component from the original to clone it.

        Arguments
        - original: the original for the new score component
        """
        ...


    def duplicate(self) -> "ScoreComponent":
        ...
