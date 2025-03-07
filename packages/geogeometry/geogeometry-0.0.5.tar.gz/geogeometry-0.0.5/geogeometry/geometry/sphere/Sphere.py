from typing import Optional, Union, List

import numpy as np

from geogeometry.geometry.shared.BaseObject import BaseObject
from geogeometry.geometry.sphere.components.SphereProperties import SphereProperties


class Sphere(BaseObject, SphereProperties):

    def __init__(self,
                 center: Union[List, np.ndarray],
                 radius: float,
                 name: Optional[str] = None):
        super().__init__(name=name)

        self.setCenter(center=center)
        self.setRadius(radius=radius)

    def __str__(self) -> str:
        txt = ("Sphere("
               f"center={self.getCenter()}, "
               f"radius={self.getRadius()} [m])")
        return txt

    def arePointsInside(self, points: Union[List, np.ndarray]) -> np.ndarray[bool]:
        dist = np.linalg.norm(self.getCenter() - points, axis=1)
        return dist < self.getRadius()
