from typing import Optional, TYPE_CHECKING

import numpy as np

if TYPE_CHECKING:
    from geogeometry.geometry.vector.Vector import Vector


class PlaneProperties(object):

    def __init__(self):

        self.origin: Optional[np.ndarray] = None
        self.normal_vector: Optional['Vector'] = None

    def setOrigin(self, origin: np.ndarray) -> None:
        self.origin = origin

    def setNormalVector(self, normal_vector: 'Vector') -> None:
        self.normal_vector = normal_vector

    def getOrigin(self) -> Optional[np.ndarray]:
        return self.origin

    def getNormalVector(self) -> Optional['Vector']:
        return self.normal_vector
