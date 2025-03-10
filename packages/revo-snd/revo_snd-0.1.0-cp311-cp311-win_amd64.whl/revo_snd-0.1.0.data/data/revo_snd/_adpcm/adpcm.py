"""
Common functions related to ADPCM data
"""
import math
import struct
from typing import BinaryIO

FRAME_SIZE = 8  # Each ADPCM frame is 8 bytes.
PACKET_SAMPLES = 14  # 1 header byte + 7 data bytes => 14 samples


def align_up(val, alignment):
    return math.ceil(val / alignment) * alignment


def get_bytes_for_adpcm_samples(samples: int) -> int:
    packets = samples // PACKET_SAMPLES
    extra_samples = samples % PACKET_SAMPLES
    extra_bytes = 0

    if extra_samples != 0:
        extra_bytes = (extra_samples // 2) + (extra_samples % 2) + 1

    return FRAME_SIZE * packets + extra_bytes


class AdpcmError(Exception):
    pass


class AdpcmParam:
    def __init__(self, data: BinaryIO = None, *,
                 coefs: list[int] = None, gain: int = 0, pred_scale: int = 0, yn1: int = 0, yn2: int = 0) -> None:
        if data is not None:
            self.coefs = struct.unpack('>16h', data.read(32))
            (self.gain, self.pred_scale, self.yn1, self.yn2) = struct.unpack('>hhhh', data.read(8))
        else:
            if coefs is None:
                self.coefs = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            else:
                if len(coefs) != 16:
                    raise AdpcmError('Invalid number of coefficients! There need to be exactly 16!')

                self.coefs = coefs
                self.gain = gain
                self.pred_scale = pred_scale
                self.yn1 = yn1
                self.yn2 = yn2

    def to_bytes(self) -> bytes:
        return struct.pack('>16h', *self.coefs) + struct.pack('>hhhh', self.gain, self.pred_scale,
                                                              self.yn1, self.yn2)

    def __str__(self) -> str:
        return f'<AdpcmParams(yn1={self.yn1}, yn2={self.yn2}, coefs={self.coefs})>'

    def __repr__(self) -> str:
        return self.__str__()


class AdpcmLoopParam:
    def __init__(self, data: BinaryIO = None, *,
                 pred_scale: int = 0, yn1: int = 0, yn2: int = 0) -> None:
        if data is not None:
            self.pred_scale, self.yn1, self.yn2 = struct.unpack('>hhh', data.read(6))
        else:
            self.pred_scale = pred_scale
            self.yn1 = yn1
            self.yn2 = yn2

    def to_bytes(self) -> bytes:
        return struct.pack('>hhh', self.pred_scale, self.yn1, self.yn2)

    def __str__(self) -> str:
        return f'<AdpcmLoopParams(yn1={self.yn1}, yn2={self.yn2})>'

    def __repr__(self) -> str:
        return self.__str__()


class AdpcmParamSet:
    def __init__(self, data: BinaryIO, *,
                 coefs: list[int] = None, gain: int = 0, pred_scale: int = 0, yn1: int = 0, yn2: int = 0,
                 loop_pred_scale: int = 0, loop_yn1: int = 0, loop_yn2: int = 0) -> None:
        if data is not None:
            self.adpcm_param = AdpcmParam(data=data)
            self.adpcm_loop_param = AdpcmLoopParam(data=data)
        else:
            self.adpcm_param = AdpcmParam(coefs=coefs, gain=gain, pred_scale=pred_scale, yn1=yn1, yn2=yn2)
            self.adpcm_loop_param = AdpcmLoopParam(pred_scale=loop_pred_scale, yn1=loop_yn1, yn2=loop_yn2)

    def __str__(self) -> str:
        return f'<AdpcmParamSet(adpcm_params={self.adpcm_param}, adpcm_loop_param={self.adpcm_loop_param})>'

    def __repr__(self) -> str:
        return self.__str__()


def decode_pcm8_block(sample_data: (bytes | bytearray), n_samples: int, n_chn: int) -> list[int]:
    """
        Decodes a block of PCM8 audio data (unsigned 8-bit) to 16-bit PCM.
        Each byte is converted by subtracting 128 and shifting left 8 bits.

        :return: The decoded data.
    """
    sample_count = n_samples
    output = [0] * (sample_count * n_chn)
    for i in range(sample_count):
        # Read the 8-bit sample (unsigned)
        sample8 = sample_data[i]
        # Convert to signed (range -128..127) then scale to 16-bit
        sample = (sample8 - 128) << 8
        output[i * n_chn] = sample
    return output


def decode_pcm16_block(sample_data: (bytes | bytearray), n_samples: int, n_chn: int) -> list[int]:
    """
        Decodes a block of PCM16 audio data.
        Each sample is assumed to be stored as a little-endian 16-bit signed integer.

        :return: The decoded data.
    """
    sample_count = n_samples
    output = [0] * (sample_count * n_chn)
    for i in range(sample_count):
        # Each sample is 2 bytes; unpack as little-endian short.
        sample = struct.unpack_from('<h', sample_data, offset=i * 2)[0]
        output[i * n_chn] = sample
    return output


def decode_adpcm_block(sample_data: (bytes | bytearray), n_samples: int, n_chn: int,
                       coefs: list[int], yn1: int, yn2: int) -> tuple[list[int], int, int]:
    """
    The C function of the internal revo_snd_adpcm module is the preferred way
    to decode a chunk of ADPCM audio data. This function acts as a fallback,
    if the internal module is not available.

    Decodes a block of ADPCM audio data to PCM audio data.

    :param sample_data: The ADPCM sample data.
    :param n_samples:   The number of samples inside the data block.
    :param n_chn:       The number of channels of the audio data.
    :param coefs:       The coefficient matrix, passed as a list of 16 values. The list has to be exactly
                        16 in size.
    :param yn1:         First history data.
    :param yn2:         Second history data.
    :return: A tuple containing the decoded data in a list and both history values.
    """
    if len(coefs) != 16:
        raise AdpcmError('The coefficient list hast to be exactly of length 16')

    output = [0] * (n_samples * n_chn)
    samples_written = 0
    offset = 0
    frame_size = FRAME_SIZE
    samples_per_frame = PACKET_SAMPLES

    while samples_written < n_samples and offset + frame_size <= len(sample_data):
        frame = sample_data[offset: offset + frame_size]
        header = frame[0]
        # High nibble: predictor index; low nibble: shift factor.
        predictor = header >> 4
        shift = header & 0x0F

        # Process the 14 nibbles in the 7 data bytes.
        for i in range(samples_per_frame):
            if samples_written >= n_samples:
                break

            # Each data byte contains two 4-bit nibbles.
            nibble_byte = frame[1 + (i // 2)]
            nibble = (nibble_byte >> 4) if (i % 2 == 0) else (nibble_byte & 0x0F)

            # Sign–extend the 4–bit nibble.
            if nibble >= 8:
                nibble -= 16

            # Compute the predicted sample using the history values.
            predicted = ((coefs[predictor * 2] * yn1) + (coefs[predictor * 2 + 1] * yn2)) >> 11
            sample = (nibble << shift) + predicted

            # Clamp to signed 16–bit range.
            sample = max(-32768, min(32767, sample))
            output[samples_written * n_chn] = sample

            # Update history: shift current sample into the history.
            yn2, yn1 = yn1, sample
            samples_written += 1

        offset += frame_size

    return output, yn1, yn2
