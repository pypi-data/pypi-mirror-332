"""
Python module generated from Java source file java.nio.charset.CharsetDecoder

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


class CharsetDecoder:

    def charset(self) -> "Charset":
        """
        Returns the charset that created this decoder.

        Returns
        - This decoder's charset
        """
        ...


    def replacement(self) -> str:
        """
        Returns this decoder's replacement value.

        Returns
        - This decoder's current replacement,
                 which is never `null` and is never empty
        """
        ...


    def replaceWith(self, newReplacement: str) -> "CharsetDecoder":
        """
        Changes this decoder's replacement value.
        
         This method invokes the .implReplaceWith implReplaceWith
        method, passing the new replacement, after checking that the new
        replacement is acceptable.  

        Arguments
        - newReplacement: The new replacement; must not be
                `null`, must have non-zero length,
        
                and must not be longer than the value returned by the
                .maxCharsPerByte() maxCharsPerByte method

        Returns
        - This decoder

        Raises
        - IllegalArgumentException: If the preconditions on the parameter do not hold
        """
        ...


    def malformedInputAction(self) -> "CodingErrorAction":
        """
        Returns this decoder's current action for malformed-input errors.

        Returns
        - The current malformed-input action, which is never `null`
        """
        ...


    def onMalformedInput(self, newAction: "CodingErrorAction") -> "CharsetDecoder":
        """
        Changes this decoder's action for malformed-input errors.
        
         This method invokes the .implOnMalformedInput
        implOnMalformedInput method, passing the new action.  

        Arguments
        - newAction: The new action; must not be `null`

        Returns
        - This decoder

        Raises
        - IllegalArgumentException: If the precondition on the parameter does not hold
        """
        ...


    def unmappableCharacterAction(self) -> "CodingErrorAction":
        """
        Returns this decoder's current action for unmappable-character errors.

        Returns
        - The current unmappable-character action, which is never
                `null`
        """
        ...


    def onUnmappableCharacter(self, newAction: "CodingErrorAction") -> "CharsetDecoder":
        """
        Changes this decoder's action for unmappable-character errors.
        
         This method invokes the .implOnUnmappableCharacter
        implOnUnmappableCharacter method, passing the new action.  

        Arguments
        - newAction: The new action; must not be `null`

        Returns
        - This decoder

        Raises
        - IllegalArgumentException: If the precondition on the parameter does not hold
        """
        ...


    def averageCharsPerByte(self) -> float:
        """
        Returns the average number of characters that will be produced for each
        byte of input.  This heuristic value may be used to estimate the size
        of the output buffer required for a given input sequence.

        Returns
        - The average number of characters produced
                 per byte of input
        """
        ...


    def maxCharsPerByte(self) -> float:
        """
        Returns the maximum number of characters that will be produced for each
        byte of input.  This value may be used to compute the worst-case size
        of the output buffer required for a given input sequence. This value
        accounts for any necessary content-independent prefix or suffix
        
        
        
        
        characters.

        Returns
        - The maximum number of characters that will be produced per
                 byte of input
        """
        ...


    def decode(self, in: "ByteBuffer", out: "CharBuffer", endOfInput: bool) -> "CoderResult":
        """
        Decodes as many bytes as possible from the given input buffer,
        writing the results to the given output buffer.
        
         The buffers are read from, and written to, starting at their current
        positions.  At most Buffer.remaining in.remaining() bytes
        will be read and at most Buffer.remaining out.remaining()
        characters will be written.  The buffers' positions will be advanced to
        reflect the bytes read and the characters written, but their marks and
        limits will not be modified.
        
         In addition to reading bytes from the input buffer and writing
        characters to the output buffer, this method returns a CoderResult
        object to describe its reason for termination:
        
        
        
          -  CoderResult.UNDERFLOW indicates that as much of the
          input buffer as possible has been decoded.  If there is no further
          input then the invoker can proceed to the next step of the
          <a href="#steps">decoding operation</a>.  Otherwise this method
          should be invoked again with further input.  
        
          -  CoderResult.OVERFLOW indicates that there is
          insufficient space in the output buffer to decode any more bytes.
          This method should be invoked again with an output buffer that has
          more Buffer.remaining remaining characters. This is
          typically done by draining any decoded characters from the output
          buffer.  
        
          -  A CoderResult.malformedForLength
          malformed-input result indicates that a malformed-input
          error has been detected.  The malformed bytes begin at the input
          buffer's (possibly incremented) position; the number of malformed
          bytes may be determined by invoking the result object's CoderResult.length() length method.  This case applies only if the
          .onMalformedInput malformed action of this decoder
          is CodingErrorAction.REPORT; otherwise the malformed input
          will be ignored or replaced, as requested.  
        
          -  An CoderResult.unmappableForLength
          unmappable-character result indicates that an
          unmappable-character error has been detected.  The bytes that
          decode the unmappable character begin at the input buffer's (possibly
          incremented) position; the number of such bytes may be determined
          by invoking the result object's CoderResult.length() length
          method.  This case applies only if the .onUnmappableCharacter
          unmappable action of this decoder is CodingErrorAction.REPORT; otherwise the unmappable character will be
          ignored or replaced, as requested.  
        
        
        
        In any case, if this method is to be reinvoked in the same decoding
        operation then care should be taken to preserve any bytes remaining
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
        pass `True` so that any remaining undecoded input will be treated
        as being malformed.
        
         This method works by invoking the .decodeLoop decodeLoop
        method, interpreting its results, handling error conditions, and
        reinvoking it as necessary.  

        Arguments
        - in: The input byte buffer
        - out: The output character buffer
        - endOfInput: `True` if, and only if, the invoker can provide no
                additional input bytes beyond those in the given buffer

        Returns
        - A coder-result object describing the reason for termination

        Raises
        - IllegalStateException: If a decoding operation is already in progress and the previous
                 step was an invocation neither of the .reset reset
                 method, nor of this method with a value of `False` for
                 the `endOfInput` parameter, nor of this method with a
                 value of `True` for the `endOfInput` parameter
                 but a return value indicating an incomplete decoding operation
        - CoderMalfunctionError: If an invocation of the decodeLoop method threw
                 an unexpected exception
        """
        ...


    def flush(self, out: "CharBuffer") -> "CoderResult":
        """
        Flushes this decoder.
        
         Some decoders maintain internal state and may need to write some
        final characters to the output buffer once the overall input sequence has
        been read.
        
         Any additional output is written to the output buffer beginning at
        its current position.  At most Buffer.remaining out.remaining()
        characters will be written.  The buffer's position will be advanced
        appropriately, but its mark and limit will not be modified.
        
         If this method completes successfully then it returns CoderResult.UNDERFLOW.  If there is insufficient room in the output
        buffer then it returns CoderResult.OVERFLOW.  If this happens
        then this method must be invoked again, with an output buffer that has
        more room, in order to complete the current <a href="#steps">decoding
        operation</a>.
        
         If this decoder has already been flushed then invoking this method
        has no effect.
        
         This method invokes the .implFlush implFlush method to
        perform the actual flushing operation.  

        Arguments
        - out: The output character buffer

        Returns
        - A coder-result object, either CoderResult.UNDERFLOW or
                 CoderResult.OVERFLOW

        Raises
        - IllegalStateException: If the previous step of the current decoding operation was an
                 invocation neither of the .flush flush method nor of
                 the three-argument .decode(ByteBuffer,CharBuffer,boolean) decode method
                 with a value of `True` for the `endOfInput`
                 parameter
        """
        ...


    def reset(self) -> "CharsetDecoder":
        """
        Resets this decoder, clearing any internal state.
        
         This method resets charset-independent state and also invokes the
        .implReset() implReset method in order to perform any
        charset-specific reset actions.  

        Returns
        - This decoder
        """
        ...


    def decode(self, in: "ByteBuffer") -> "CharBuffer":
        """
        Convenience method that decodes the remaining content of a single input
        byte buffer into a newly-allocated character buffer.
        
         This method implements an entire <a href="#steps">decoding
        operation</a>; that is, it resets this decoder, then it decodes the
        bytes in the given byte buffer, and finally it flushes this
        decoder.  This method should therefore not be invoked if a decoding
        operation is already in progress.  

        Arguments
        - in: The input byte buffer

        Returns
        - A newly-allocated character buffer containing the result of the
                decoding operation.  The buffer's position will be zero and its
                limit will follow the last character written.

        Raises
        - IllegalStateException: If a decoding operation is already in progress
        - MalformedInputException: If the byte sequence starting at the input buffer's current
                 position is not legal for this charset and the current malformed-input action
                 is CodingErrorAction.REPORT
        - UnmappableCharacterException: If the byte sequence starting at the input buffer's current
                 position cannot be mapped to an equivalent character sequence and
                 the current unmappable-character action is CodingErrorAction.REPORT
        """
        ...


    def isAutoDetecting(self) -> bool:
        """
        Tells whether or not this decoder implements an auto-detecting charset.
        
         The default implementation of this method always returns
        `False`; it should be overridden by auto-detecting decoders to
        return `True`.  

        Returns
        - `True` if, and only if, this decoder implements an
                 auto-detecting charset
        """
        ...


    def isCharsetDetected(self) -> bool:
        """
        Tells whether or not this decoder has yet detected a
        charset&nbsp;&nbsp;*(optional operation)*.
        
         If this decoder implements an auto-detecting charset then at a
        single point during a decoding operation this method may start returning
        `True` to indicate that a specific charset has been detected in
        the input byte sequence.  Once this occurs, the .detectedCharset
        detectedCharset method may be invoked to retrieve the detected charset.
        
         That this method returns `False` does not imply that no bytes
        have yet been decoded.  Some auto-detecting decoders are capable of
        decoding some, or even all, of an input byte sequence without fixing on
        a particular charset.
        
         The default implementation of this method always throws an UnsupportedOperationException; it should be overridden by
        auto-detecting decoders to return `True` once the input charset
        has been determined.  

        Returns
        - `True` if, and only if, this decoder has detected a
                 specific charset

        Raises
        - UnsupportedOperationException: If this decoder does not implement an auto-detecting charset
        """
        ...


    def detectedCharset(self) -> "Charset":
        """
        Retrieves the charset that was detected by this
        decoder&nbsp;&nbsp;*(optional operation)*.
        
         If this decoder implements an auto-detecting charset then this
        method returns the actual charset once it has been detected.  After that
        point, this method returns the same value for the duration of the
        current decoding operation.  If not enough input bytes have yet been
        read to determine the actual charset then this method throws an IllegalStateException.
        
         The default implementation of this method always throws an UnsupportedOperationException; it should be overridden by
        auto-detecting decoders to return the appropriate value.  

        Returns
        - The charset detected by this auto-detecting decoder,
                 or `null` if the charset has not yet been determined

        Raises
        - IllegalStateException: If insufficient bytes have been read to determine a charset
        - UnsupportedOperationException: If this decoder does not implement an auto-detecting charset
        """
        ...
