import math

from astrocompute.models.vector import Vector2D


def add(u: Vector2D, v: Vector2D) -> Vector2D:
    """
    Adds two 2-dimensional vectors.

    :param u: First vector
    :param v: Second vector
    :return: Sum of the two vectors
    """
    if u is None:
        raise ValueError("u cannot be None")

    if v is None:
        raise ValueError("v cannot be None")

    return Vector2D(u.x + v.x, u.y + v.y)


def scalar_multiply(s: float, v: Vector2D) -> Vector2D:
    """
    Multiplies a 2-dimensional vector by a scalar.

    :param s: Scalar value
    :param v: 2-dimensional vector
    :return: Result of the scalar multiplication
    """
    if v is None:
        raise ValueError("vector cannot be None")

    return Vector2D(s * v.x, s * v.y)


def dot_product(u: Vector2D, v: Vector2D) -> float:
    """
    Calculates the dot product of two 2-dimensional vectors.

    :param u: First vector
    :param v: Second vector
    :return: Dot product of the two vectors
    """
    if u is None:
        raise ValueError("u cannot be None")

    if v is None:
        raise ValueError("v cannot be None")

    return u.x * v.x + u.y * v.y


def norm(v: Vector2D) -> float:
    """
    Calculates the norm of a 2-dimensional vector.

    :param v: Vector
    :return: Norm of the vector
    """
    if v is None:
        raise ValueError("v cannot be None")

    return math.sqrt(v.x**2 + v.y**2)


def normalize(v: Vector2D) -> Vector2D:
    """
    Normalizes a 2-dimensional vector.
    This should return a unit vector in the same direction as the input vector.

    :param v: Vector
    :return: Normalized vector
    """
    n = norm(v)
    return Vector2D(v.x / n, v.y / n)
