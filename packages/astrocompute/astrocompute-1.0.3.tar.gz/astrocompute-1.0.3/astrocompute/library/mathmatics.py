"""
The module mathmatics.py provides (among others) the two functions:

frac and modulo
"""

from typing import Tuple


def frac(x: float) -> float:
    """
    Calculate the fractional part of x

    :param x:
    :return:
    :rtype: float
    :raises: ZeroDivisionError
    """
    return abs(x) - abs(int(x))


def modulo(x: float, y: float) -> float:
    """
    Calculate the modulo of x and y

    :param x:
    :param y:
    :return:
    :rtype: float
    :raises: ZeroDivisionError
    """
    return y * frac(x / y)


def ddd(d: int, m: int, s: float) -> float:
    """
    Convert degrees, minutes, seconds to decimal degrees

    :param d: degrees
    :param m: minutes
    :param s: seconds
    :return: Angle in decimal representation
    """
    sign = -1.0 if d < 0 or m < 0 or s < 0 else 1.0
    return sign * (
        abs(float(d)) + abs(float(m)) / 60.0 + abs(float(s)) / 3600.0
    )


def dms(dd: float) -> Tuple[int, int, float]:
    """
    Convert decimal degrees to degrees, minutes, seconds

    :param dd: Angle in decimal representation
    :return: Tuple of degrees, minutes, seconds
    """
    sign = -1 if dd < 0 else 1
    dd = abs(dd)
    d = int(dd)
    m = int((dd - d) * 60)
    s = (dd - d - m / 60) * 3600

    if sign == -1:
        if d != 0:
            d = -d
        elif m != 0:
            m = -m
        else:
            s = -s

    return d, m, s
