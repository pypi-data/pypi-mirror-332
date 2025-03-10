"""
Python module generated from Java source file org.bukkit.Note

Java source file obtained from artifact spigot-api version 1.20.3-R0.1-20231207.085553-9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from com.google.common.collect import Maps
from enum import Enum
from org.bukkit import *
from typing import Any, Callable, Iterable, Tuple


class Note:
    """
    A note class to store a specific note.
    """

    def __init__(self, note: int):
        """
        Creates a new note.

        Arguments
        - note: Internal note id. .getId() always return this
            value. The value has to be in the interval [0;&nbsp;24].
        """
        ...


    def __init__(self, octave: int, tone: "Tone", sharped: bool):
        """
        Creates a new note.

        Arguments
        - octave: The octave where the note is in. Has to be 0 - 2.
        - tone: The tone within the octave. If the octave is 2 the note has
            to be F#.
        - sharped: Set if the tone is sharped (e.g. for F#).
        """
        ...


    @staticmethod
    def flat(octave: int, tone: "Tone") -> "Note":
        """
        Creates a new note for a flat tone, such as A-flat.

        Arguments
        - octave: The octave where the note is in. Has to be 0 - 1.
        - tone: The tone within the octave.

        Returns
        - The new note.
        """
        ...


    @staticmethod
    def sharp(octave: int, tone: "Tone") -> "Note":
        """
        Creates a new note for a sharp tone, such as A-sharp.

        Arguments
        - octave: The octave where the note is in. Has to be 0 - 2.
        - tone: The tone within the octave. If the octave is 2 the note has
            to be F#.

        Returns
        - The new note.
        """
        ...


    @staticmethod
    def natural(octave: int, tone: "Tone") -> "Note":
        """
        Creates a new note for a natural tone, such as A-natural.

        Arguments
        - octave: The octave where the note is in. Has to be 0 - 1.
        - tone: The tone within the octave.

        Returns
        - The new note.
        """
        ...


    def sharped(self) -> "Note":
        """
        Returns
        - The note a semitone above this one.
        """
        ...


    def flattened(self) -> "Note":
        """
        Returns
        - The note a semitone below this one.
        """
        ...


    def getId(self) -> int:
        """
        Returns the internal id of this note.

        Returns
        - the internal id of this note.

        Deprecated
        - Magic value
        """
        ...


    def getOctave(self) -> int:
        """
        Returns the octave of this note.

        Returns
        - the octave of this note.
        """
        ...


    def getTone(self) -> "Tone":
        """
        Returns the tone of this note.

        Returns
        - the tone of this note.
        """
        ...


    def isSharped(self) -> bool:
        """
        Returns if this note is sharped.

        Returns
        - if this note is sharped.
        """
        ...


    def getPitch(self) -> float:
        """
        Gets the pitch of this note. This is the value used with
        World.playSound or the /playsound command.

        Returns
        - the pitch
        """
        ...


    def hashCode(self) -> int:
        ...


    def equals(self, obj: "Object") -> bool:
        ...


    def toString(self) -> str:
        ...


    class Tone(Enum):
        """
        An enum holding tones.
        """

# Static fields
        TONES_COUNT = 12
        """
        The number of tones including sharped tones.
        """


        G = (0x1, True)
        A = (0x3, True)
        B = (0x5, False)
        C = (0x6, True)
        D = (0x8, True)
        E = (0xA, False)
        F = (0xB, True)


        def getId(self) -> int:
            """
            Returns the not sharped id of this tone.

            Returns
            - the not sharped id of this tone.

            Deprecated
            - Magic value
            """
            ...


        def getId(self, sharped: bool) -> int:
            """
            Returns the id of this tone. These method allows to return the
            sharped id of the tone. If the tone couldn't be sharped it always
            return the not sharped id of this tone.

            Arguments
            - sharped: Set to True to return the sharped id.

            Returns
            - the id of this tone.

            Deprecated
            - Magic value
            """
            ...


        def isSharpable(self) -> bool:
            """
            Returns if this tone could be sharped.

            Returns
            - if this tone could be sharped.
            """
            ...


        def isSharped(self, id: int) -> bool:
            """
            Returns if this tone id is the sharped id of the tone.

            Arguments
            - id: the id of the tone.

            Returns
            - if the tone id is the sharped id of the tone.

            Raises
            - IllegalArgumentException: if neither the tone nor the
                semitone have the id.

            Deprecated
            - Magic value
            """
            ...


        @staticmethod
        def getById(id: int) -> "Tone":
            """
            Returns the tone to id. Also returning the semitones.

            Arguments
            - id: the id of the tone.

            Returns
            - the tone to id.

            Deprecated
            - Magic value
            """
            ...
