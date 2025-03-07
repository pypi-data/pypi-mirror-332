from typing import Optional, TYPE_CHECKING

import numpy as np

from geogeometry.geometry.cylinder.components.CylinderProperties import CylinderProperties
from geogeometry.geometry.shared.BaseObject import BaseObject

if TYPE_CHECKING:
    from geogeometry import Vector


class Cylinder(BaseObject, CylinderProperties):

    def __init__(self,
                 radius: float,
                 origin: np.ndarray,
                 axis_vector: 'Vector',
                 length: float,
                 name: Optional[str] = None):
        super().__init__(name=name)

        self.setRadius(radius=radius)
        self.setOrigin(origin=origin)
        self.setAxisVector(axis_vector=axis_vector)
        self.setLength(length=length)
