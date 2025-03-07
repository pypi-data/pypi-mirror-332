from dataclasses import dataclass
from typing import Optional


@dataclass
class Spherical:
    r: Optional[float] = float(0)
    theta: Optional[float] = float(0)  # Polar angle in radians
    phi: Optional[float] = float(0)  # Azimuthal angle in radians
