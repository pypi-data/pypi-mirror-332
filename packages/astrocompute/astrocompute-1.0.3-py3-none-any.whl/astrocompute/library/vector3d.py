import math

from astrocompute.models.vector import Vector3D


def add(u: Vector3D, v: Vector3D) -> Vector3D:
    """
    Adds two 3-dimensional vectors.

    :param u: First vector
    :param v: Second vector
    :return: Sum of the two vectors
    """
    if u is None:
        raise ValueError("u cannot be None")

    if v is None:
        raise ValueError("v cannot be None")

    return Vector3D(u.x + v.x, u.y + v.y, u.z + v.z)


def scalar_multiply(s: float, v: Vector3D) -> Vector3D:
    """
    Multiplies a 3 dimensional vector by a scalar.

    :param s: Scalar value
    :param v: 3 dimensional vector
    :return: Result of the scalar multiplication
    """
    if v is None:
        raise ValueError("vector cannot be None")

    return Vector3D(s * v.x, s * v.y, s * v.z)


def dot_product(u: Vector3D, v: Vector3D) -> float:
    """
    Calculates the dot product of two 3 dimensional vectors.

    :param u: First vector
    :param v: Second vector
    :return: Dot product of the two vectors
    """
    if u is None:
        raise ValueError("u cannot be None")

    if v is None:
        raise ValueError("v cannot be None")

    return u.x * v.x + u.y * v.y + u.z * v.z


def cross_product(u: Vector3D, v: Vector3D) -> Vector3D:
    """
    Calculates the cross product of two 3 dimensional vectors.
    :param u: First vector
    :param v: Second vector
    :return: Cross product of the two vectors
    """
    if u is None:
        raise ValueError("u cannot be None")

    if v is None:
        raise ValueError("v cannot be None")

    return Vector3D(
        u.y * v.z - u.z * v.y,
        u.z * v.x - u.x * v.z,
        u.x * v.y - u.y * v.x,
    )


def norm(v: Vector3D) -> float:
    """
    Calculates the norm of a 3 dimensional vector.

    :param v: Vector
    :return: Norm of the vector
    """
    if v is None:
        raise ValueError("v cannot be None")

    return math.sqrt(v.x**2 + v.y**2 + v.z**2)


def normalize(v: Vector3D) -> Vector3D:
    """
    Normalizes a 3 dimensional vector.
    This should return a unit vector in the same direction as the input vector.

    :param v: Vector
    :return: Normalized vector
    """
    n = norm(v)
    return Vector3D(v.x / n, v.y / n, v.z / n)
