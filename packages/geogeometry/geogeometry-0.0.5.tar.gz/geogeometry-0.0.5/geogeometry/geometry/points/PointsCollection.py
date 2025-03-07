from typing import Optional, TYPE_CHECKING, Union, List, Literal

import numpy as np

from geogeometry.geometry.points.collection_components.PointsCollectionPlotter import PointsCollectionPlotter
from geogeometry.geometry.shared.BaseObjectCollection import BaseObjectCollection


class PointsCollection(BaseObjectCollection['PointsCollection', np.ndarray]):

    def __init__(self, name: Optional[str] = None, points: Optional[Union[List, np.ndarray]] = None):
        super().__init__(name=name)

        if points is not None:
            self.setPoints(points=points)

        self.plotter: PointsCollectionPlotter = PointsCollectionPlotter(self)

    def setPoints(self, points: Union[List, np.ndarray]) -> None:
        if isinstance(points, list):
            points = np.array(points)
        self.elements = points

    def getPoints(self) -> Union[List, np.ndarray]:
        return self.elements
