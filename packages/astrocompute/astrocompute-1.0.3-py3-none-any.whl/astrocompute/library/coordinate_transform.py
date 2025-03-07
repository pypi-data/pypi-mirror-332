import math

from astrocompute.models import (
    Point2D,
    Point3D,
    Polar,
    Spherical,
)


def cartesian_to_polar(point: Point2D) -> Polar:
    r = math.sqrt(point.x**2 + point.y**2)
    theta = math.atan2(point.y, point.x)
    return Polar(r, theta)


def polar_to_cartesian(polar: Polar) -> Point2D:
    x = polar.r * math.cos(polar.theta)
    y = polar.r * math.sin(polar.theta)
    return Point2D(x, y)


def cartesian_to_spherical(point: Point3D) -> Spherical:
    r = math.sqrt(point.x**2 + point.y**2 + point.z**2)
    theta = math.acos(point.z / r)
    phi = math.atan2(point.y, point.x)
    return Spherical(r, theta, phi)


def spherical_to_cartesian(spherical: Spherical) -> Point3D:
    x = spherical.r * math.cos(spherical.theta) * math.cos(spherical.phi)
    y = spherical.r * math.cos(spherical.theta) * math.sin(spherical.phi)
    z = spherical.r * math.sin(spherical.theta)
    return Point3D(x, y, z)
