from dataclasses import dataclass
from typing import Optional


@dataclass
class Point2D:
    x: Optional[float] = float(0)
    y: Optional[float] = float(0)


@dataclass
class Point3D:
    x: Optional[float] = float(0)
    y: Optional[float] = float(0)
    z: Optional[float] = float(0)
