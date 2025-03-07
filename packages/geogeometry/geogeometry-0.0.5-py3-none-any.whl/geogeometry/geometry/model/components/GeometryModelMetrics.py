from typing import TYPE_CHECKING, Optional

import numpy as np

from geogeometry.geometry.shared.shared_components.BaseMetrics import BaseMetrics

if TYPE_CHECKING:
    from geogeometry.geometry.model.GeometryModel import GeometryModel


class GeometryModelMetrics(BaseMetrics):

    def __init__(self, model: 'GeometryModel'):
        self.model: 'GeometryModel' = model

        self.limits: Optional[np.ndarray] = None
        self.center: Optional[np.ndarray] = None

    def getLimits(self) -> Optional[np.ndarray]:
        return self.limits

    def getCenter(self) -> Optional[np.ndarray]:
        return self.center

    def calculateMetrics(self):
        self.calculateLimits()
        self.calculateCenter()

    def calculateLimits(self):
        all_limits = [lim for t in self.model.getTriangulations() for lim in t.getLimits()]
        all_limits += [lim for p in self.model.getPolylines() for lim in p.getLimits()]

        _min, _max = np.min(all_limits, axis=0), np.max(all_limits, axis=0)
        self.limits = np.array([_min, _max])

    def calculateCenter(self) -> None:
        # all_centers = [t.getCentroid() for t in self.model.getTriangulations()]
        # all_centers += [p.getCentroid() for p in self.model.getPolylines()]
        self.center = np.average(self.limits, axis=0)
