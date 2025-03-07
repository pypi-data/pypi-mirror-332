import math

from astrocompute.models.polar import Polar


def to_cartesian(p: Polar) -> tuple:
    """
    Converts polar coordinates to Cartesian coordinates.

    :param p: Polar coordinates
    :return: Cartesian coordinates as a tuple (x, y)
    """
    x = p.r * math.cos(p.theta)
    y = p.r * math.sin(p.theta)
    return (x, y)


def from_cartesian(x: float, y: float) -> Polar:
    """
    Converts Cartesian coordinates to polar coordinates.

    :param x: x-coordinate
    :param y: y-coordinate
    :return: Polar coordinates
    """
    r = math.sqrt(x**2 + y**2)
    theta = math.atan2(y, x)
    return Polar(r, theta)


def add(p1: Polar, p2: Polar) -> Polar:
    """
    Adds two polar coordinates.

    :param p1: First polar coordinate
    :param p2: Second polar coordinate
    :return: Sum of the two polar coordinates
    """
    x1, y1 = to_cartesian(p1)
    x2, y2 = to_cartesian(p2)
    x_sum = x1 + x2
    y_sum = y1 + y2
    return from_cartesian(x_sum, y_sum)


def subtract(p1: Polar, p2: Polar) -> Polar:
    """
    Subtracts the second polar coordinate from the first.

    :param p1: First polar coordinate
    :param p2: Second polar coordinate
    :return: Difference of the two polar coordinates
    """
    x1, y1 = to_cartesian(p1)
    x2, y2 = to_cartesian(p2)
    x_diff = x1 - x2
    y_diff = y1 - y2
    return from_cartesian(x_diff, y_diff)


def multiply(p: Polar, scalar: float) -> Polar:
    """
    Multiplies a polar coordinate by a scalar.

    :param p: Polar coordinate
    :param scalar: Scalar value
    :return: Result of the scalar multiplication
    """
    return Polar(p.r * scalar, p.theta)


def rotate(p: Polar, angle: float) -> Polar:
    """
    Rotates a polar coordinate by a given angle.

    :param p: Polar coordinate
    :param angle: Angle to rotate by (in radians)
    :return: Rotated polar coordinate
    """
    return Polar(p.r, p.theta + angle)
