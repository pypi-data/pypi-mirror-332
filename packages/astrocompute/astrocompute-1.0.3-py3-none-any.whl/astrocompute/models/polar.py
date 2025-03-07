from dataclasses import dataclass
from typing import Optional


@dataclass
class Polar:
    r: Optional[float] = 0.0
    theta: Optional[float] = 0.0  # Angle in radians
