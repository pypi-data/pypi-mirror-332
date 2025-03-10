"""
Python module generated from Java source file com.google.common.base.Ascii

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.base import *
from typing import Any, Callable, Iterable, Tuple


class Ascii:
    """
    Static methods pertaining to ASCII characters (those in the range of values `0x00` through
    `0x7F`), and to strings containing such characters.
    
    ASCII utilities also exist in other classes of this package:
    
    
      <!-- TODO(kevinb): how can we make this not produce a warning when building gwt javadoc? -->
      - Charsets.US_ASCII specifies the `Charset` of ASCII characters.
      - CharMatcher.ascii matches ASCII characters and provides text processing methods
          which operate only on the ASCII characters of a string.

    Author(s)
    - Gregory Kick

    Since
    - 7.0
    """

    NUL = 0
    """
    Null ('\0'): The all-zeros character which may serve to accomplish time fill and media fill.
    Normally used as a C string terminator.
    
    Although RFC 20 names this as "Null", note that it is distinct from the C/C++ "NULL"
    pointer.

    Since
    - 8.0
    """
    SOH = 1
    """
    Start of Heading: A communication control character used at the beginning of a sequence of
    characters which constitute a machine-sensible address or routing information. Such a sequence
    is referred to as the "heading." An STX character has the effect of terminating a heading.

    Since
    - 8.0
    """
    STX = 2
    """
    Start of Text: A communication control character which precedes a sequence of characters that
    is to be treated as an entity and entirely transmitted through to the ultimate destination.
    Such a sequence is referred to as "text." STX may be used to terminate a sequence of characters
    started by SOH.

    Since
    - 8.0
    """
    ETX = 3
    """
    End of Text: A communication control character used to terminate a sequence of characters
    started with STX and transmitted as an entity.

    Since
    - 8.0
    """
    EOT = 4
    """
    End of Transmission: A communication control character used to indicate the conclusion of a
    transmission, which may have contained one or more texts and any associated headings.

    Since
    - 8.0
    """
    ENQ = 5
    """
    Enquiry: A communication control character used in data communication systems as a request for
    a response from a remote station. It may be used as a "Who Are You" (WRU) to obtain
    identification, or may be used to obtain station status, or both.

    Since
    - 8.0
    """
    ACK = 6
    """
    Acknowledge: A communication control character transmitted by a receiver as an affirmative
    response to a sender.

    Since
    - 8.0
    """
    BEL = 7
    """
    Bell ('\a'): A character for use when there is a need to call for human attention. It may
    control alarm or attention devices.

    Since
    - 8.0
    """
    BS = 8
    """
    Backspace ('\b'): A format effector which controls the movement of the printing position one
    printing space backward on the same printing line. (Applicable also to display devices.)

    Since
    - 8.0
    """
    HT = 9
    """
    Horizontal Tabulation ('\t'): A format effector which controls the movement of the printing
    position to the next in a series of predetermined positions along the printing line.
    (Applicable also to display devices and the skip function on punched cards.)

    Since
    - 8.0
    """
    LF = 10
    """
    Line Feed ('\n'): A format effector which controls the movement of the printing position to the
    next printing line. (Applicable also to display devices.) Where appropriate, this character may
    have the meaning "New Line" (NL), a format effector which controls the movement of the printing
    point to the first printing position on the next printing line. Use of this convention requires
    agreement between sender and recipient of data.

    Since
    - 8.0
    """
    NL = 10
    """
    Alternate name for .LF. (`LF` is preferred.)

    Since
    - 8.0
    """
    VT = 11
    """
    Vertical Tabulation ('\v'): A format effector which controls the movement of the printing
    position to the next in a series of predetermined printing lines. (Applicable also to display
    devices.)

    Since
    - 8.0
    """
    FF = 12
    """
    Form Feed ('\f'): A format effector which controls the movement of the printing position to the
    first pre-determined printing line on the next form or page. (Applicable also to display
    devices.)

    Since
    - 8.0
    """
    CR = 13
    """
    Carriage Return ('\r'): A format effector which controls the movement of the printing position
    to the first printing position on the same printing line. (Applicable also to display devices.)

    Since
    - 8.0
    """
    SO = 14
    """
    Shift Out: A control character indicating that the code combinations which follow shall be
    interpreted as outside of the character set of the standard code table until a Shift In
    character is reached.

    Since
    - 8.0
    """
    SI = 15
    """
    Shift In: A control character indicating that the code combinations which follow shall be
    interpreted according to the standard code table.

    Since
    - 8.0
    """
    DLE = 16
    """
    Data Link Escape: A communication control character which will change the meaning of a limited
    number of contiguously following characters. It is used exclusively to provide supplementary
    controls in data communication networks.

    Since
    - 8.0
    """
    DC1 = 17
    XON = 17
    DC2 = 18
    """
    Device Control 2. Characters for the control of ancillary devices associated with data
    processing or telecommunication systems, more especially switching devices "on" or "off." (If a
    single "stop" control is required to interrupt or turn off ancillary devices, DC4 is the
    preferred assignment.)

    Since
    - 8.0
    """
    DC3 = 19
    XOFF = 19
    DC4 = 20
    """
    Device Control 4. Characters for the control of ancillary devices associated with data
    processing or telecommunication systems, more especially switching devices "on" or "off." (If a
    single "stop" control is required to interrupt or turn off ancillary devices, DC4 is the
    preferred assignment.)

    Since
    - 8.0
    """
    NAK = 21
    """
    Negative Acknowledge: A communication control character transmitted by a receiver as a negative
    response to the sender.

    Since
    - 8.0
    """
    SYN = 22
    """
    Synchronous Idle: A communication control character used by a synchronous transmission system
    in the absence of any other character to provide a signal from which synchronism may be
    achieved or retained.

    Since
    - 8.0
    """
    ETB = 23
    """
    End of Transmission Block: A communication control character used to indicate the end of a
    block of data for communication purposes. ETB is used for blocking data where the block
    structure is not necessarily related to the processing format.

    Since
    - 8.0
    """
    CAN = 24
    """
    Cancel: A control character used to indicate that the data with which it is sent is in error or
    is to be disregarded.

    Since
    - 8.0
    """
    EM = 25
    """
    End of Medium: A control character associated with the sent data which may be used to identify
    the physical end of the medium, or the end of the used, or wanted, portion of information
    recorded on a medium. (The position of this character does not necessarily correspond to the
    physical end of the medium.)

    Since
    - 8.0
    """
    SUB = 26
    """
    Substitute: A character that may be substituted for a character which is determined to be
    invalid or in error.

    Since
    - 8.0
    """
    ESC = 27
    """
    Escape: A control character intended to provide code extension (supplementary characters) in
    general information interchange. The Escape character itself is a prefix affecting the
    interpretation of a limited number of contiguously following characters.

    Since
    - 8.0
    """
    FS = 28
    """
    File Separator: These four information separators may be used within data in optional fashion,
    except that their hierarchical relationship shall be: FS is the most inclusive, then GS, then
    RS, and US is least inclusive. (The content and length of a File, Group, Record, or Unit are
    not specified.)

    Since
    - 8.0
    """
    GS = 29
    """
    Group Separator: These four information separators may be used within data in optional fashion,
    except that their hierarchical relationship shall be: FS is the most inclusive, then GS, then
    RS, and US is least inclusive. (The content and length of a File, Group, Record, or Unit are
    not specified.)

    Since
    - 8.0
    """
    RS = 30
    """
    Record Separator: These four information separators may be used within data in optional
    fashion, except that their hierarchical relationship shall be: FS is the most inclusive, then
    GS, then RS, and US is least inclusive. (The content and length of a File, Group, Record, or
    Unit are not specified.)

    Since
    - 8.0
    """
    US = 31
    """
    Unit Separator: These four information separators may be used within data in optional fashion,
    except that their hierarchical relationship shall be: FS is the most inclusive, then GS, then
    RS, and US is least inclusive. (The content and length of a File, Group, Record, or Unit are
    not specified.)

    Since
    - 8.0
    """
    SP = 32
    """
    Space: A normally non-printing graphic character used to separate words. It is also a format
    effector which controls the movement of the printing position, one printing position forward.
    (Applicable also to display devices.)

    Since
    - 8.0
    """
    SPACE = 32
    """
    Alternate name for .SP.

    Since
    - 8.0
    """
    DEL = 127
    """
    Delete: This character is used primarily to "erase" or "obliterate" erroneous or unwanted
    characters in perforated tape.

    Since
    - 8.0
    """
    MIN = 0
    """
    The minimum value of an ASCII character.

    Since
    - 9.0 (was type `int` before 12.0)
    """
    MAX = 127
    """
    The maximum value of an ASCII character.

    Since
    - 9.0 (was type `int` before 12.0)
    """


    @staticmethod
    def toLowerCase(string: str) -> str:
        """
        Returns a copy of the input string in which all .isUpperCase(char) uppercase ASCII
        characters have been converted to lowercase. All other characters are copied without
        modification.
        """
        ...


    @staticmethod
    def toLowerCase(chars: "CharSequence") -> str:
        """
        Returns a copy of the input character sequence in which all .isUpperCase(char)
        uppercase ASCII characters have been converted to lowercase. All other characters are copied
        without modification.

        Since
        - 14.0
        """
        ...


    @staticmethod
    def toLowerCase(c: str) -> str:
        """
        If the argument is an .isUpperCase(char) uppercase ASCII character, returns the
        lowercase equivalent. Otherwise returns the argument.
        """
        ...


    @staticmethod
    def toUpperCase(string: str) -> str:
        """
        Returns a copy of the input string in which all .isLowerCase(char) lowercase ASCII
        characters have been converted to uppercase. All other characters are copied without
        modification.
        """
        ...


    @staticmethod
    def toUpperCase(chars: "CharSequence") -> str:
        """
        Returns a copy of the input character sequence in which all .isLowerCase(char)
        lowercase ASCII characters have been converted to uppercase. All other characters are copied
        without modification.

        Since
        - 14.0
        """
        ...


    @staticmethod
    def toUpperCase(c: str) -> str:
        """
        If the argument is a .isLowerCase(char) lowercase ASCII character, returns the
        uppercase equivalent. Otherwise returns the argument.
        """
        ...


    @staticmethod
    def isLowerCase(c: str) -> bool:
        """
        Indicates whether `c` is one of the twenty-six lowercase ASCII alphabetic characters
        between `'a'` and `'z'` inclusive. All others (including non-ASCII characters)
        return `False`.
        """
        ...


    @staticmethod
    def isUpperCase(c: str) -> bool:
        """
        Indicates whether `c` is one of the twenty-six uppercase ASCII alphabetic characters
        between `'A'` and `'Z'` inclusive. All others (including non-ASCII characters)
        return `False`.
        """
        ...


    @staticmethod
    def truncate(seq: "CharSequence", maxLength: int, truncationIndicator: str) -> str:
        """
        Truncates the given character sequence to the given maximum length. If the length of the
        sequence is greater than `maxLength`, the returned string will be exactly `maxLength` chars in length and will end with the given `truncationIndicator`. Otherwise,
        the sequence will be returned as a string with no changes to the content.
        
        Examples:
        
        ````Ascii.truncate("foobar", 7, "..."); // returns "foobar"
        Ascii.truncate("foobar", 5, "..."); // returns "fo..."````
        
        **Note:** This method *may* work with certain non-ASCII text but is not safe for use
        with arbitrary Unicode text. It is mostly intended for use with text that is known to be safe
        for use with it (such as all-ASCII text) and for simple debugging text. When using this method,
        consider the following:
        
        
          - it may split surrogate pairs
          - it may split characters and combining characters
          - it does not consider word boundaries
          - if truncating for display to users, there are other considerations that must be taken
              into account
          - the appropriate truncation indicator may be locale-dependent
          - it is safe to use non-ASCII characters in the truncation indicator

        Raises
        - IllegalArgumentException: if `maxLength` is less than the length of `truncationIndicator`

        Since
        - 16.0
        """
        ...


    @staticmethod
    def equalsIgnoreCase(s1: "CharSequence", s2: "CharSequence") -> bool:
        """
        Indicates whether the contents of the given character sequences `s1` and `s2` are
        equal, ignoring the case of any ASCII alphabetic characters between `'a'` and `'z'`
        or `'A'` and `'Z'` inclusive.
        
        This method is significantly faster than String.equalsIgnoreCase and should be used
        in preference if at least one of the parameters is known to contain only ASCII characters.
        
        Note however that this method does not always behave identically to expressions such as:
        
        
          - `string.toUpperCase().equals("UPPER CASE ASCII")`
          - `string.toLowerCase().equals("lower case ascii")`
        
        
        due to case-folding of some non-ASCII characters (which does not occur in String.equalsIgnoreCase). However in almost all cases that ASCII strings are used, the author
        probably wanted the behavior provided by this method rather than the subtle and sometimes
        surprising behavior of `toUpperCase()` and `toLowerCase()`.

        Since
        - 16.0
        """
        ...
