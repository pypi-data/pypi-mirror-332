"""
This module provides classes and functions for working with points in 2D and 3D space.

In Python, you can represent an infinite value using the float type.
The float type has special values for positive and negative infinity.
You can use float('inf') for positive infinity and float('-inf') for negative infinity.
"""

import math
import re
from dataclasses import dataclass
from typing import Optional, Union


def _get_infinite_value(positive: Optional[bool] = True) -> float:
    """
    Get the infinite value based on the sign.

    :param positive: True for positive infinity, False for negative infinity
    :return: The infinite value
    :rtype: float
    """
    return float("inf") if positive else float("-inf")


def _validate_points(*points: "Point2D") -> None:
    """
    Validate the points for None values.

    :param points: A variable number of points
    :raises: ValueError if any of the points are None
    """
    none_points = [f"p{i + 1}" for i, p in enumerate(points) if p is None]
    if none_points:
        raise ValueError(f"{', '.join(none_points)} cannot be None")


@dataclass
class Point2D:
    x: Optional[float] = float(0)
    y: Optional[float] = float(0)
    name: Optional[str] = None

    def __str__(self):
        return (
            f"({self.x}, {self.y})"
            if not self.name
            else f"{self.name}: ({self.x}, {self.y})"
        )

    def __repr__(self):
        return f"Point2D(x={self.x}, y={self.y}, name={self.name})"

    @staticmethod
    def dx(p: "Point2D", q: "Point2D") -> float:
        """
        Calculate the difference in x-coordinates between two points.

        :param p: The first point
        :param q: The second point
        :return: The difference in x-coordinates
        """
        return q.x - p.x

    @staticmethod
    def dy(p: "Point2D", q: "Point2D") -> float:
        """
        Calculate the difference in y-coordinates between two points.

        :param p: The first point
        :param q: The second point
        :return: The difference in y-coordinates
        """
        return q.y - p.y

    @staticmethod
    def same_point(p: "Point2D", q: "Point2D") -> bool:
        """
        Check if two points are the same.

        :param p: The first point
        :param q: The second point
        :return: True if the points are the same, False otherwise
        """
        _validate_points(p, q)

        return p.x == q.x and p.y == q.y

    @staticmethod
    def are_distinct(p: "Point2D", q: "Point2D") -> bool:
        """
        Check if two points are distinct.

        :param p: The first point
        :param q: The second point
        :return: True if the points are distinct, False otherwise
        """
        _validate_points(p, q)

        return p.x != q.x or p.y != q.y

    @staticmethod
    def same_line(
        p: "Point2D", q: "Point2D", r: "Point2D", s: "Point2D"
    ) -> bool:
        """
        Check if the lines represented by two sets of points are the same.

        :param p: A point on the first line
        :param q: Another point on the first line
        :param r: A point on the second line
        :param s: Another point on the second line
        :return: True if the lines are the same, False otherwise
        """
        _validate_points(p, q, r, s)

        if not Point2D.are_collinear(p, q, r):
            return False

        if not Point2D.are_collinear(p, q, s):
            return False

        return True

    @staticmethod
    def parse(repr_str: str) -> "Point2D":
        match = re.match(
            r"Point2D\(x=(.*), y=(.*), name=(.*)\)|\((.*), (.*)\)", repr_str
        )

        if not match:
            raise ValueError(f"Invalid Point2D representation: {repr_str}")

        try:
            if match.groups()[0]:
                x, y, name = match.groups()[:3]
                x, y = float(x), float(y)
                name = name.strip("'\"") if name != "None" else None
            else:
                x, y = map(float, match.groups()[3:])
                name = None
        except TypeError as err:
            raise ValueError(
                f"Invalid Point2D representation: {repr_str}"
            ) from err

        return Point2D(x, y, name)

    @staticmethod
    def distance(p: Optional["Point2D"], q: Optional["Point2D"]) -> float:
        """
        Calculate the distance between two points.

        :param p: The first point
        :param q: The second point
        :return: The distance between the points
        """
        _validate_points(p, q)

        if Point2D().same_point(p, q):
            return 0

        return math.sqrt((q.x - p.x) ** 2 + (q.y - p.y) ** 2)

    @staticmethod
    def midpoint(p: "Point2D", q: "Point2D") -> "Point2D":
        """
        Calculate the midpoint between two points.

        :param p: The first point
        :param q: The second point
        :return: The midpoint between the points
        """
        _validate_points(p, q)

        if not Point2D().are_distinct(p, q):
            return p  # both points are the same so just return the first one

        return Point2D((p.x + q.x) / 2, (p.y + q.y) / 2)

    @staticmethod
    def slope(p: "Point2D", q: "Point2D") -> float:
        """
        Calculate the slope of the line through two points.

        :param p: The first point
        :param q: The second point
        :return: The slope of the line
        :raises: ValueError if the line is vertical
        """
        _validate_points(p, q)

        if Point2D().is_vertical(p, q):
            return float("nan")

        if Point2D().is_horizontal(p, q):
            return 0.0

        return (q.y - p.y) / (q.x - p.x)

    @staticmethod
    def y_intercept(p: "Point2D", q: "Point2D") -> float:
        """
        Calculate the y-intercept of the line through two points.

        If the line is vertical there are two cases:
        1. If both points are on the y-axis, there are infinite y-intercepts.
        2. Otherwise, the line is vertical but not on the y-axis, so there are no y-intercepts.

        So this function returns one of the following:

        - a float representing the location of the y-intercept
        - float('inf') if the line is vertical and both points are on the y-axis
        - float('nan') if the line is vertical but not on the y-axis

        :param p: The first point
        :param q: The second point
        :return: The y-intercept of the line
        """
        _validate_points(p, q)

        m = Point2D.slope(p, q)
        if math.isnan(m):
            return float("inf") if p.x == 0.0 and q.x == 0.0 else float("nan")

        return p.y - m * p.x

    @staticmethod
    def x_intercept(p: "Point2D", q: "Point2D") -> float:
        """
        Calculate the x-intercept of the line through two points.

        :param p: The first point
        :param q: The second point
        :return: The x-intercept of the line
        """
        _validate_points(p, q)

        return -Point2D.y_intercept(p, q) / Point2D.slope(p, q)

    @staticmethod
    def is_vertical(p: "Point2D", q: "Point2D") -> bool:
        """
        Check if the line through two points is vertical.

        :param p: The first point
        :param q: The second point
        :return: True if the line is vertical, False otherwise
        """
        _validate_points(p, q)

        delta_x = Point2D.dx(p, q)
        delta_y = Point2D.dy(p, q)

        return delta_x == 0 and delta_y != 0

    @staticmethod
    def is_horizontal(p: "Point2D", q: "Point2D") -> bool:
        """
        Check if the line through two points is horizontal.

        :param p: The first point
        :param q: The second point
        :return: True if the line is horizontal, False otherwise
        """
        _validate_points(p, q)

        delta_x = Point2D.dx(p, q)
        delta_y = Point2D.dy(p, q)

        return delta_y == 0 and delta_x != 0

    @staticmethod
    def are_parallel(
        p: "Point2D", q: "Point2D", r: "Point2D", s: "Point2D"
    ) -> bool:
        """
        Check if two lines are parallel.

        Note: A line is trivially parallel to itself by convention and logical necessity.

        :param p: A point on the first line
        :param q: Another point on the first line
        :param r: A point on the second line
        :param s: Another point on the second line
        :return: True if the lines are parallel, False otherwise
        :raises: ValueError if p, q, r, or s are None
        :raises: ValueError if p and q are the same point
        """
        _validate_points(p, q, r, s)

        if Point2D().same_line(p, q, r, s):
            return True  # Every line is considered parallel to itself.

        m1 = Point2D.slope(p, q)
        m2 = Point2D.slope(r, s)

        return m1 == m2

    @staticmethod
    def is_perpendicular(
        p: "Point2D", q: "Point2D", r: "Point2D", s: "Point2D"
    ) -> bool:
        """
        Check if two lines are perpendicular.

        :param p: A point on the first line
        :param q: Another point on the first line
        :param r: A point on the second line
        :param s: Another point on the second line
        :return: True if the lines are perpendicular, False otherwise
        """
        _validate_points(p, q, r, s)

        return Point2D.slope(p, q) * Point2D.slope(r, s) == -1

    @staticmethod
    def are_collinear(p: "Point2D", q: "Point2D", r: "Point2D") -> bool:
        """
        Check if three points are collinear.

        :param p: First point
        :param q: Second point
        :param r: Third point
        :return: True if the points are collinear, False otherwise
        """
        _validate_points(p, q, r)

        return (r.y - p.y) * (q.x - p.x) == (q.y - p.y) * (r.x - p.x)

    @staticmethod
    def create_from_coordinates(x: float, y: float) -> "Point2D":
        """
        Create a Point2D object from the given coordinates.

        :param x: The x-coordinate
        :param y: The y-coordinate
        :return: The Point2D object
        """
        return Point2D(x, y)

    @staticmethod
    def create_from_coordinate_str(repr_str: str) -> "Point2D":
        """
        Create a Point2D object from a string representation.

        :param repr_str: The string representation
        :return: The Point2D object
        :raises: ValueError if the string representation is invalid
        """
        return Point2D.parse(repr_str)

    @staticmethod
    def create_from_polar_coordinates(r: float, theta: float) -> "Point2D":
        """
        Create a Point2D object from polar coordinates.

        :param r: The radius
        :param theta: The angle in radians
        :return: The Point2D object
        """
        x = r * math.cos(theta)
        y = r * math.sin(theta)

        return Point2D(x, y)


# Create an instance of Point2D with infinite coordinates
INFINITE_POINT_2D = Point2D(_get_infinite_value(), _get_infinite_value())


@dataclass
class Point3D:
    x: Optional[float] = float(0)
    y: Optional[float] = float(0)
    z: Optional[float] = float(0)

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __repr__(self):
        return f"Point3D(x={self.x}, y={self.y}, z={self.z})"

    @staticmethod
    def parse(repr_str: str) -> "Point3D":
        match = re.match(
            r"Point3D\(x=(.*), y=(.*), z=(.*)\)|\((.*), (.*), (.*)\)", repr_str
        )
        if match:
            x, y, z = map(
                float,
                match.groups()[:3] if match.groups()[0] else match.groups()[3:],
            )
            return Point3D(x, y, z)
        raise ValueError(f"Invalid Point3D representation: {repr_str}")

    @staticmethod
    def distance(p: "Point3D", q: "Point3D") -> float:
        return math.sqrt((q.x - p.x) ** 2 + (q.y - p.y) ** 2 + (q.z - p.z) ** 2)

    @staticmethod
    def midpoint(p: "Point3D", q: "Point3D") -> "Point3D":
        """
        Calculate the midpoint between two points.

        :param p: The first point
        :param q: The second point
        :return: The midpoint between the points
        """
        return Point3D((p.x + q.x) / 2, (p.y + q.y) / 2, (p.z + q.z) / 2)

    @staticmethod
    def are_collinear(p: "Point3D", q: "Point3D", r: "Point3D") -> bool:
        """
        Check if three points are collinear.

        :param p: First point
        :param q: Second point
        :param r: Third point
        :return: True if the points are collinear, False otherwise
        """
        # Calculate vectors
        v1 = (q.x - p.x, q.y - p.y, q.z - p.z)
        v2 = (r.x - q.x, r.y - q.y, r.z - q.z)

        # Calculate cross product
        cross_product = (
            v1[1] * v2[2] - v1[2] * v2[1],
            v1[2] * v2[0] - v1[0] * v2[2],
            v1[0] * v2[1] - v1[1] * v2[0],
        )

        # If cross product is (0, 0, 0), the points are collinear
        return cross_product == (0, 0, 0)

    @staticmethod
    def are_coplanar(
        p: "Point3D", q: "Point3D", r: "Point3D", s: "Point3D"
    ) -> bool:
        """
        Check if four points are coplanar.

        :param p: First point
        :param q: Second point
        :param r: Third point
        :param s: Fourth point
        :return: True if the points are coplanar, False otherwise
        """
        # Calculate vectors
        v1 = (q.x - p.x, q.y - p.y, q.z - p.z)
        v2 = (r.x - p.x, r.y - p.y, r.z - p.z)
        v3 = (s.x - p.x, s.y - p.y, s.z - p.z)

        # Calculate scalar triple product
        scalar_triple_product = (
            v1[0] * (v2[1] * v3[2] - v2[2] * v3[1])
            - v1[1] * (v2[0] * v3[2] - v2[2] * v3[0])
            + v1[2] * (v2[0] * v3[1] - v2[1] * v3[0])
        )

        # If scalar triple product is 0, the points are coplanar
        return scalar_triple_product == 0

    @staticmethod
    def are_cocircular(p: "Point3D", q: "Point3D", r: "Point3D") -> bool:
        """
        Check if three points are cocircular.

        :param p: First point
        :param q: Second point
        :param r: Third point
        :return: True if the points are cocircular, False otherwise
        """
        # Calculate the determinant of the matrix
        determinant = (
            p.x * (q.y * r.z - q.z * r.y)
            - p.y * (q.x * r.z - q.z * r.x)
            + p.z * (q.x * r.y - q.y * r.x)
        )

        # If the determinant is 0, the points are cocircular
        return determinant == 0

    @staticmethod
    def create_from_coordinates(x: float, y: float, z: float) -> "Point3D":
        return Point3D(x, y, z)

    @staticmethod
    def create_from_coordinate_str(repr_str: str) -> "Point3D":
        return Point3D.parse(repr_str)


def parse_point(repr_str: str) -> Union[Point2D, Point3D]:
    """
    Parse a Point2D or Point3D object from its string representation.

    :param repr_str: String representation of the Point2D or Point3D object
    :return: Point2D or Point3D object
    :raises: ValueError if the string representation is invalid
    """
    if (
        repr_str.startswith("Point2D")
        or repr_str.startswith("(")
        and repr_str.count(",") == 1
    ):
        return Point2D.parse(repr_str)

    if (
        repr_str.startswith("Point3D")
        or repr_str.startswith("(")
        and repr_str.count(",") == 2
    ):
        return Point3D.parse(repr_str)

    raise ValueError(f"Unknown point representation: {repr_str}")


def create_point(x: float, y: float, z: float = 0) -> Union[Point2D, Point3D]:
    """
    Create a Point2D or Point3D object from the given coordinates.

    :param x: The x-coordinate
    :param y: The y-coordinate
    :param z: The z-coordinate (default: 0)
    :return: Point2D or Point3D object
    """
    if z == 0:
        return Point2D(x, y)
    return Point3D(x, y, z)
