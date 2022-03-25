"""Functions for positioning matplotlib arrows."""


import numpy as np


def rotate_center(xcenter, ycenter, length, rotation) -> tuple[float]:
    """Rotates an arrow of a specified length at its center."""

    half_length = length / 2
    rad_angle = np.radians(rotation)

    return (
        xcenter - half_length * np.sin(rad_angle),
        ycenter - half_length * np.cos(rad_angle),
        length * np.sin(rad_angle),
        length * np.cos(rad_angle)
    )

def rotate_tail(xtail, ytail, length, rotation) -> tuple[float]:
    """Rotates an arrow of a specified length at its tail."""

    rad_angle = np.radians(rotation)

    return (
        xtail,
        ytail,
        length * np.sin(rad_angle),
        length * np.cos(rad_angle)
    )
