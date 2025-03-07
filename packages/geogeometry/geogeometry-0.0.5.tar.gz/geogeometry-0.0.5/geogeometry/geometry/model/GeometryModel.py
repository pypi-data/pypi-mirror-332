from typing import Union, List, Optional, TYPE_CHECKING

import numpy as np

from geogeometry.geometry.model.components.GeometryModelMetrics import GeometryModelMetrics
from geogeometry.geometry.model.components.GeometryModelPlotter import GeometryModelPlotter
from geogeometry.geometry.shared.BaseObject import BaseObject
from geogeometry.geometry.model.components.GeometryModelProperties import GeometryModelProperties
from geogeometry.geometry.shared.observer.Observer import Observer

if TYPE_CHECKING:
    from geogeometry.geometry.shared.observer.Observable import Observable


class GeometryModel(BaseObject['GeometryModel'], GeometryModelProperties, Observer):

    def __init__(self, name: Optional[str] = None):
        super().__init__(name=name)

        self.getTriangulations().addObserver(observer=self)
        self.getPolylines().addObserver(observer=self)
        self.getPoints().addObserver(observer=self)

        self.metrics: GeometryModelMetrics = GeometryModelMetrics(self)
        self.plotter: GeometryModelPlotter = GeometryModelPlotter(self)

    def __len__(self) -> int:
        total = 0
        total += len(self.getTriangulations())
        total += len(self.getPolylines())
        return total

    def __str__(self) -> str:
        txt = (f"GeometryModel(name={self.getName()}, "
               f"triangulations={len(self.getTriangulations())}, "
               f"polylines={len(self.getPolylines())}, "
               f"points={len(self.getPoints())})")
        return txt

    # def calculateMetrics(self):
    #     self.calculateLimits()
    #     self.calculateCentroid()
    #
    # def calculateLimits(self):
    #     all_limits = [lim for t in self.getTriangulations() for lim in t.getLimits()]
    #     all_limits += [lim for p in self.getPolylines() for lim in p.getLimits()]
    #
    #     _min, _max = np.min(all_limits, axis=0), np.max(all_limits, axis=0)
    #     self.setLimits(limits=np.array([_min, _max]))
    #
    # def calculateCentroid(self) -> None:
    #     all_centers = [t.getCentroid() for t in self.getTriangulations()]
    #     all_centers += [p.getCentroid() for p in self.getPolylines()]
    #
    #     center = np.average(all_centers, axis=0)
    #     self.setCentroid(centroid=center)

    def onElementChange(self, observable: 'Observable'):
        self.calculateMetrics()
        self.notifyObservers()
