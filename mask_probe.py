"""Narrow reproduction of the scalar shifts reported in isce3 issue #335."""

import numpy as np


def measure(sample: dict) -> dict:
    reference = sample["reference"]
    secondary = sample["secondary"]
    if type(reference) is not int or type(secondary) is not int:
        raise ValueError("Both exception mask IDs must be integers")
    if not all(0 <= value <= 255 for value in (reference, secondary)):
        raise ValueError("Exception mask IDs must fit uint8")
    exception_mask = np.array([[reference, secondary]], dtype=np.uint8)
    packed_mask = 5 | (exception_mask[0, 0] << 16) | (exception_mask[0, 1] << 8)
    return {"packed_mask": int(packed_mask)}
