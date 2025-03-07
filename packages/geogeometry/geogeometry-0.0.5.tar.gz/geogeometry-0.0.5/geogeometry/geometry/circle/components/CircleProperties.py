from typing import Optional, Union, List, TYPE_CHECKING

import numpy as np

if TYPE_CHECKING:
    from geogeometry.geometry.plane.Plane import Plane


class CircleProperties(object):

    def __init__(self):
        self.center: Optional[np.ndarray] = None
        self.radius: Optional[float] = None
        self.plane: Optional['Plane'] = None

    def setCenter(self, center: Union[List, np.ndarray]) -> None:
        if isinstance(center, list):
            center = np.array(center)
        self.center = center

    def setRadius(self, radius: float) -> None:
        self.radius = radius

    def setPlane(self, plane: 'Plane') -> None:
        self.plane = plane

    def getCenter(self) -> np.ndarray:
        return self.center

    def getRadius(self) -> float:
        return self.radius

    def getPlane(self) -> Optional['Plane']:
        return self.plane
