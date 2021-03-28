def _intx(value, bits):
    if value & (1 << (bits - 1)):
        value -= 1 << bits
    return value


def _int32(value):
    return _intx(value, bits=32)