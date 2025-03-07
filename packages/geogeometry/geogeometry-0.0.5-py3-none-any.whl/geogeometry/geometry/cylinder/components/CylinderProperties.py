from typing import Optional, TYPE_CHECKING

import numpy as np

if TYPE_CHECKING:
    from geogeometry.geometry.vector.Vector import Vector


class CylinderProperties(object):

    def __init__(self):
        self.radius: Optional[float] = None
        self.origin: Optional[np.ndarray] = None
        self.axis_vector: Optional['Vector'] = None
        self.length: Optional[float] = None

    def setRadius(self, radius: float) -> None:
        self.radius = radius

    def setOrigin(self, origin: np.ndarray) -> None:
        self.origin = origin

    def setAxisVector(self, axis_vector: 'Vector'):
        self.axis_vector = axis_vector

    def setLength(self, length: float) -> None:
        self.length = length

    def getRadius(self) -> float:
        return self.radius

    def getOrigin(self) -> np.ndarray:
        return self.origin

    def getAxisVector(self) -> 'Vector':
        return self.axis_vector

    def getLength(self) -> float:
        return self.length
