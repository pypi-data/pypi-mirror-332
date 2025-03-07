from typing import Optional, TYPE_CHECKING

import numpy as np

from geogeometry.geometry.shared.shared_components.BaseMetrics import BaseMetrics

if TYPE_CHECKING:
    from geogeometry.geometry.circle.Circle import Circle
    from geogeometry.geometry.vector.Vector import Vector


class CircleMetrics(BaseMetrics):

    def __init__(self, circle: 'Circle'):
        self.circle: 'Circle' = circle

        self.area: Optional[float] = None
        self.normal_vector: Optional['Vector'] = None

    def calculateMetrics(self) -> None:
        self.calculateArea()
        self.calculateNormalVector()

    def calculateArea(self) -> None:
        self.area = np.pi * (self.circle.getRadius() ** 2)

    def calculateNormalVector(self) -> None:
        if self.circle.getPlane() is None:
            self.normal_vector = Vector(tip=[0, 0, 1])
        else:
            self.normal_vector = self.circle.getPlane().getNormalVector()
