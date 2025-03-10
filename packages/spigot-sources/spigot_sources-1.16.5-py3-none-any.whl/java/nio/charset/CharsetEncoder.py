"""
Python module generated from Java source file java.nio.charset.CharsetEncoder

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.lang.ref import WeakReference
from java.nio.charset import *
from java.nio.charset import CoderMalfunctionError
from java.util import Arrays
from typing import Any, Callable, Iterable, Tuple


class CharsetEncoder:

    def charset(self) -> "Charset":
        """
        Returns the charset that created this encoder.

        Returns
        - This encoder's charset
        """
        ...


    def replacement(self) -> list[int]:
        """
        Returns this encoder's replacement value.

        Returns
        - This encoder's current replacement,
                 which is never `null` and is never empty
        """
        ...


    def replaceWith(self, newReplacement: list[int]) -> "CharsetEncoder":
        """
        Changes this encoder's replacement value.
        
         This method invokes the .implReplaceWith implReplaceWith
        method, passing the new replacement, after checking that the new
        replacement is acceptable.  

        Arguments
        - newReplacement: The new replacement; must not be
                `null`, must have non-zero length,
        
        
        
        
        
                must not be longer than the value returned by the
                .maxBytesPerChar() maxBytesPerChar method, and
                must be .isLegalReplacement legal

        Returns
        - This encoder

        Raises
        - IllegalArgumentException: If the preconditions on the parameter do not hold
        """
        ...


    def isLegalReplacement(self, repl: list[int]) -> bool:
        """
        Tells whether or not the given byte array is a legal replacement value
        for this encoder.
        
         A replacement is legal if, and only if, it is a legal sequence of
        bytes in this encoder's charset; that is, it must be possible to decode
        the replacement into one or more sixteen-bit Unicode characters.
        
         The default implementation of this method is not very efficient; it
        should generally be overridden to improve performance.  

        Arguments
        - repl: The byte array to be tested

        Returns
        - `True` if, and only if, the given byte array
                 is a legal replacement value for this encoder
        """
        ...


    def malformedInputAction(self) -> "CodingErrorAction":
        """
        Returns this encoder's current action for malformed-input errors.

        Returns
        - The current malformed-input action, which is never `null`
        """
        ...


    def onMalformedInput(self, newAction: "CodingErrorAction") -> "CharsetEncoder":
        """
        Changes this encoder's action for malformed-input errors.
        
         This method invokes the .implOnMalformedInput
        implOnMalformedInput method, passing the new action.  

        Arguments
        - newAction: The new action; must not be `null`

        Returns
        - This encoder

        Raises
        - IllegalArgumentException: If the precondition on the parameter does not hold
        """
        ...


    def unmappableCharacterAction(self) -> "CodingErrorAction":
        """
        Returns this encoder's current action for unmappable-character errors.

        Returns
        - The current unmappable-character action, which is never
                `null`
        """
        ...


    def onUnmappableCharacter(self, newAction: "CodingErrorAction") -> "CharsetEncoder":
        """
        Changes this encoder's action for unmappable-character errors.
        
         This method invokes the .implOnUnmappableCharacter
        implOnUnmappableCharacter method, passing the new action.  

        Arguments
        - newAction: The new action; must not be `null`

        Returns
        - This encoder

        Raises
        - IllegalArgumentException: If the precondition on the parameter does not hold
        """
        ...


    def averageBytesPerChar(self) -> float:
        """
        Returns the average number of bytes that will be produced for each
        character of input.  This heuristic value may be used to estimate the size
        of the output buffer required for a given input sequence.

        Returns
        - The average number of bytes produced
                 per character of input
        """
        ...


    def maxBytesPerChar(self) -> float:
        """
        Returns the maximum number of bytes that will be produced for each
        character of input.  This value may be used to compute the worst-case size
        of the output buffer required for a given input sequence. This value
        accounts for any necessary content-independent prefix or suffix
        
        bytes, such as byte-order marks.

        Returns
        - The maximum number of bytes that will be produced per
                 character of input
        """
        ...


    def encode(self, in: "CharBuffer", out: "ByteBuffer", endOfInput: bool) -> "CoderResult":
        """
        Encodes as many characters as possible from the given input buffer,
        writing the results to the given output buffer.
        
         The buffers are read from, and written to, starting at their current
        positions.  At most Buffer.remaining in.remaining() characters
        will be read and at most Buffer.remaining out.remaining()
        bytes will be written.  The buffers' positions will be advanced to
        reflect the characters read and the bytes written, but their marks and
        limits will not be modified.
        
         In addition to reading characters from the input buffer and writing
        bytes to the output buffer, this method returns a CoderResult
        object to describe its reason for termination:
        
        
        
          -  CoderResult.UNDERFLOW indicates that as much of the
          input buffer as possible has been encoded.  If there is no further
          input then the invoker can proceed to the next step of the
          <a href="#steps">encoding operation</a>.  Otherwise this method
          should be invoked again with further input.  
        
          -  CoderResult.OVERFLOW indicates that there is
          insufficient space in the output buffer to encode any more characters.
          This method should be invoked again with an output buffer that has
          more Buffer.remaining remaining bytes. This is
          typically done by draining any encoded bytes from the output
          buffer.  
        
          -  A CoderResult.malformedForLength
          malformed-input result indicates that a malformed-input
          error has been detected.  The malformed characters begin at the input
          buffer's (possibly incremented) position; the number of malformed
          characters may be determined by invoking the result object's CoderResult.length() length method.  This case applies only if the
          .onMalformedInput malformed action of this encoder
          is CodingErrorAction.REPORT; otherwise the malformed input
          will be ignored or replaced, as requested.  
        
          -  An CoderResult.unmappableForLength
          unmappable-character result indicates that an
          unmappable-character error has been detected.  The characters that
          encode the unmappable character begin at the input buffer's (possibly
          incremented) position; the number of such characters may be determined
          by invoking the result object's CoderResult.length() length
          method.  This case applies only if the .onUnmappableCharacter
          unmappable action of this encoder is CodingErrorAction.REPORT; otherwise the unmappable character will be
          ignored or replaced, as requested.  
        
        
        
        In any case, if this method is to be reinvoked in the same encoding
        operation then care should be taken to preserve any characters remaining
        in the input buffer so that they are available to the next invocation.
        
         The `endOfInput` parameter advises this method as to whether
        the invoker can provide further input beyond that contained in the given
        input buffer.  If there is a possibility of providing additional input
        then the invoker should pass `False` for this parameter; if there
        is no possibility of providing further input then the invoker should
        pass `True`.  It is not erroneous, and in fact it is quite
        common, to pass `False` in one invocation and later discover that
        no further input was actually available.  It is critical, however, that
        the final invocation of this method in a sequence of invocations always
        pass `True` so that any remaining unencoded input will be treated
        as being malformed.
        
         This method works by invoking the .encodeLoop encodeLoop
        method, interpreting its results, handling error conditions, and
        reinvoking it as necessary.  

        Arguments
        - in: The input character buffer
        - out: The output byte buffer
        - endOfInput: `True` if, and only if, the invoker can provide no
                additional input characters beyond those in the given buffer

        Returns
        - A coder-result object describing the reason for termination

        Raises
        - IllegalStateException: If an encoding operation is already in progress and the previous
                 step was an invocation neither of the .reset reset
                 method, nor of this method with a value of `False` for
                 the `endOfInput` parameter, nor of this method with a
                 value of `True` for the `endOfInput` parameter
                 but a return value indicating an incomplete encoding operation
        - CoderMalfunctionError: If an invocation of the encodeLoop method threw
                 an unexpected exception
        """
        ...


    def flush(self, out: "ByteBuffer") -> "CoderResult":
        """
        Flushes this encoder.
        
         Some encoders maintain internal state and may need to write some
        final bytes to the output buffer once the overall input sequence has
        been read.
        
         Any additional output is written to the output buffer beginning at
        its current position.  At most Buffer.remaining out.remaining()
        bytes will be written.  The buffer's position will be advanced
        appropriately, but its mark and limit will not be modified.
        
         If this method completes successfully then it returns CoderResult.UNDERFLOW.  If there is insufficient room in the output
        buffer then it returns CoderResult.OVERFLOW.  If this happens
        then this method must be invoked again, with an output buffer that has
        more room, in order to complete the current <a href="#steps">encoding
        operation</a>.
        
         If this encoder has already been flushed then invoking this method
        has no effect.
        
         This method invokes the .implFlush implFlush method to
        perform the actual flushing operation.  

        Arguments
        - out: The output byte buffer

        Returns
        - A coder-result object, either CoderResult.UNDERFLOW or
                 CoderResult.OVERFLOW

        Raises
        - IllegalStateException: If the previous step of the current encoding operation was an
                 invocation neither of the .flush flush method nor of
                 the three-argument .encode(CharBuffer,ByteBuffer,boolean) encode method
                 with a value of `True` for the `endOfInput`
                 parameter
        """
        ...


    def reset(self) -> "CharsetEncoder":
        """
        Resets this encoder, clearing any internal state.
        
         This method resets charset-independent state and also invokes the
        .implReset() implReset method in order to perform any
        charset-specific reset actions.  

        Returns
        - This encoder
        """
        ...


    def encode(self, in: "CharBuffer") -> "ByteBuffer":
        """
        Convenience method that encodes the remaining content of a single input
        character buffer into a newly-allocated byte buffer.
        
         This method implements an entire <a href="#steps">encoding
        operation</a>; that is, it resets this encoder, then it encodes the
        characters in the given character buffer, and finally it flushes this
        encoder.  This method should therefore not be invoked if an encoding
        operation is already in progress.  

        Arguments
        - in: The input character buffer

        Returns
        - A newly-allocated byte buffer containing the result of the
                encoding operation.  The buffer's position will be zero and its
                limit will follow the last byte written.

        Raises
        - IllegalStateException: If an encoding operation is already in progress
        - MalformedInputException: If the character sequence starting at the input buffer's current
                 position is not a legal sixteen-bit Unicode sequence and the current malformed-input action
                 is CodingErrorAction.REPORT
        - UnmappableCharacterException: If the character sequence starting at the input buffer's current
                 position cannot be mapped to an equivalent byte sequence and
                 the current unmappable-character action is CodingErrorAction.REPORT
        """
        ...


    def canEncode(self, c: str) -> bool:
        """
        Tells whether or not this encoder can encode the given character.
        
         This method returns `False` if the given character is a
        surrogate character; such characters can be interpreted only when they
        are members of a pair consisting of a high surrogate followed by a low
        surrogate.  The .canEncode(java.lang.CharSequence)
        canEncode(CharSequence) method may be used to test whether or not a
        character sequence can be encoded.
        
         This method may modify this encoder's state; it should therefore not
        be invoked if an <a href="#steps">encoding operation</a> is already in
        progress.
        
         The default implementation of this method is not very efficient; it
        should generally be overridden to improve performance.  

        Arguments
        - c: The given character

        Returns
        - `True` if, and only if, this encoder can encode
                 the given character

        Raises
        - IllegalStateException: If an encoding operation is already in progress
        """
        ...


    def canEncode(self, cs: "CharSequence") -> bool:
        """
        Tells whether or not this encoder can encode the given character
        sequence.
        
         If this method returns `False` for a particular character
        sequence then more information about why the sequence cannot be encoded
        may be obtained by performing a full <a href="#steps">encoding
        operation</a>.
        
         This method may modify this encoder's state; it should therefore not
        be invoked if an encoding operation is already in progress.
        
         The default implementation of this method is not very efficient; it
        should generally be overridden to improve performance.  

        Arguments
        - cs: The given character sequence

        Returns
        - `True` if, and only if, this encoder can encode
                 the given character without throwing any exceptions and without
                 performing any replacements

        Raises
        - IllegalStateException: If an encoding operation is already in progress
        """
        ...
