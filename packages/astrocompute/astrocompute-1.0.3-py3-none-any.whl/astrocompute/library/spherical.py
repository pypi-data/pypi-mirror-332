import math

from astrocompute.models.spherical import Spherical


def to_cartesian(s: Spherical) -> tuple:
    """
    Converts spherical coordinates to Cartesian coordinates.

    :param s: Spherical coordinates
    :return: Cartesian coordinates as a tuple (x, y, z)
    """
    x = s.r * math.sin(s.theta) * math.cos(s.phi)
    y = s.r * math.sin(s.theta) * math.sin(s.phi)
    z = s.r * math.cos(s.theta)
    return (x, y, z)


def from_cartesian(x: float, y: float, z: float) -> Spherical:
    """
    Converts Cartesian coordinates to spherical coordinates.

    :param x: x-coordinate
    :param y: y-coordinate
    :param z: z-coordinate
    :return: Spherical coordinates
    """
    r = math.sqrt(x**2 + y**2 + z**2)
    theta = math.acos(z / r)
    phi = math.atan2(y, x)
    return Spherical(r, theta, phi)


def add(s1: Spherical, s2: Spherical) -> Spherical:
    """
    Adds two spherical coordinates.

    :param s1: First spherical coordinate
    :param s2: Second spherical coordinate
    :return: Sum of the two spherical coordinates
    """
    x1, y1, z1 = to_cartesian(s1)
    x2, y2, z2 = to_cartesian(s2)
    x_sum = x1 + x2
    y_sum = y1 + y2
    z_sum = z1 + z2
    return from_cartesian(x_sum, y_sum, z_sum)


def subtract(s1: Spherical, s2: Spherical) -> Spherical:
    """
    Subtracts the second spherical coordinate from the first.

    :param s1: First spherical coordinate
    :param s2: Second spherical coordinate
    :return: Difference of the two spherical coordinates
    """
    x1, y1, z1 = to_cartesian(s1)
    x2, y2, z2 = to_cartesian(s2)
    x_diff = x1 - x2
    y_diff = y1 - y2
    z_diff = z1 - z2
    return from_cartesian(x_diff, y_diff, z_diff)


def multiply(s: Spherical, scalar: float) -> Spherical:
    """
    Multiplies a spherical coordinate by a scalar.

    :param s: Spherical coordinate
    :param scalar: Scalar value
    :return: Result of the scalar multiplication
    """
    return Spherical(s.r * scalar, s.theta, s.phi)


def rotate(s: Spherical, dtheta: float, dphi: float) -> Spherical:
    """
    Rotates a spherical coordinate by given angles.

    :param s: Spherical coordinate
    :param dtheta: Angle to rotate by in the theta direction (in radians)
    :param dphi: Angle to rotate by in the phi direction (in radians)
    :return: Rotated spherical coordinate
    """
    return Spherical(s.r, s.theta + dtheta, s.phi + dphi)
