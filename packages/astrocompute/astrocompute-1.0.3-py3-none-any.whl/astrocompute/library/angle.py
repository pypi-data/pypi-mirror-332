from dataclasses import dataclass
from enum import Enum


class AngleFormat(Enum):
    Dd = "Dd"  # pylint: disable=invalid-name
    DMM = "DMM"
    DMMm = "DMMm"  # pylint: disable=invalid-name
    DMMSS = "DMMSS"
    DMMSSs = "DMMSSs"  # pylint: disable=invalid-name


def dms(alpha: float):
    """
    Convert an angle in decimal degrees to degrees, minutes, and seconds

    :param alpha:
    :return:
    """
    d = int(alpha)
    m = int((alpha - d) * 60)
    s = ((alpha - d) * 60 - m) * 60
    return d, m, s


@dataclass
class Angle:
    def __init__(
        self, alpha: float, angle_format: AngleFormat = AngleFormat.Dd
    ):
        self.alpha = alpha
        self.format = angle_format

    def set(self, angle_format: AngleFormat):
        self.format = angle_format


class AngleSerializer:
    """
    AngleSerializer class to serialize and deserialize angles
    """

    def __init__(self, precision: int = 2, width: int = 12):
        """
        Initialize the AngleSerializer

        :param precision:
        :param width:
        """
        self.precision = precision
        self.width = width

    def serialize(self, angle: Angle) -> str:
        """
        Serialize an angle to a string

        :param angle:
        :return:
        """
        d, m, s = dms(angle.alpha)
        if angle.format == AngleFormat.Dd:
            return f"{angle.alpha:0.{self.precision}f}"

        if angle.format == AngleFormat.DMM:
            return f"{d} {m:02d}"

        if angle.format == AngleFormat.DMMm:
            decimal_minutes = m + s / 60
            return f"{d} {decimal_minutes:0.{self.precision}f}"

        if angle.format == AngleFormat.DMMSS:
            return f"{d} {m:02d} {int(s):02d}"

        if angle.format == AngleFormat.DMMSSs:
            return f"{d} {m:02d} {s:0.{self.precision}f}"

        raise ValueError("Invalid AngleFormat")
