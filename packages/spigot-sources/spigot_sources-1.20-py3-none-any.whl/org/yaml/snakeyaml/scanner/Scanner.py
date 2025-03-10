"""
Python module generated from Java source file org.yaml.snakeyaml.scanner.Scanner

Java source file obtained from artifact snakeyaml version 2.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.yaml.snakeyaml.scanner import *
from org.yaml.snakeyaml.tokens import Token
from typing import Any, Callable, Iterable, Tuple


class Scanner:
    """
    This interface represents an input stream of Tokens.
    
    The parser and the scanner form together the 'Parse' step in the loading process (see chapter 3.1
    of the <a href="http://yaml.org/spec/1.1/">YAML Specification</a>).

    See
    - org.yaml.snakeyaml.tokens.Token
    """

    def checkToken(self, *choices: Tuple["Token.ID", ...]) -> bool:
        """
        Check if the next token is one of the given types.

        Arguments
        - choices: token IDs to match with

        Returns
        - `True` if the next token is one of the given types. Returns
                `False` if no more tokens are available.

        Raises
        - ScannerException: Thrown in case of malformed input.
        """
        ...


    def peekToken(self) -> "Token":
        """
        Return the next token, but do not delete it from the stream.

        Returns
        - The token that will be returned on the next call to .getToken

        Raises
        - ScannerException: Thrown in case of malformed input.
        - IndexOutOfBoundsException: if no more token left
        """
        ...


    def getToken(self) -> "Token":
        """
        Returns the next token.
        
        The token will be removed from the stream. (Every invocation of this method must happen after
        calling either .checkToken or .peekToken()

        Returns
        - the coming token

        Raises
        - ScannerException: Thrown in case of malformed input.
        - IndexOutOfBoundsException: if no more token left
        """
        ...
