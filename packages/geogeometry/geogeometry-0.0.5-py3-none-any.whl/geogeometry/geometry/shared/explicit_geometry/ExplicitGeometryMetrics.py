from typing import Optional, Literal, TYPE_CHECKING

import numpy as np

from geogeometry.geometry.shared.shared_components.BaseMetrics import BaseMetrics

if TYPE_CHECKING:
    from geogeometry.geometry.shared.explicit_geometry.ExplicitGeometry import ExplicitGeometry


class ExplicitGeometryMetrics(BaseMetrics):

    def __init__(self, element: 'ExplicitGeometry'):
        self.element: 'ExplicitGeometry' = element

        # Metrics
        self.dimensions: Optional[Literal[2, 3]] = None
        self.limits: Optional[np.ndarray] = None
        self.center: Optional[np.ndarray] = None

    def getDimensions(self) -> Optional[Literal[2, 3]]:
        return self.dimensions

    def getLimits(self) -> Optional[np.ndarray]:
        return self.limits

    def getCenter(self) -> Optional[np.ndarray]:
        return self.center

    def calculateMetrics(self) -> None:
        self.calculateDimensions()
        self.calculateLimits()
        self.calculateCenter()

    def calculateDimensions(self) -> None:
        self.dimensions = self.element.getNodes().shape[1]

    def calculateLimits(self) -> None:
        _min, _max = np.min(np.array(self.element.getNodes()), axis=0), np.max(np.array(self.element.getNodes()), axis=0)
        self.limits = np.array([_min, _max])

    def calculateCenter(self) -> None:
        self.center = np.average(self.limits, axis=0)
