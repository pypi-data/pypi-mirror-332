from typing import Optional, Union, List, TYPE_CHECKING

import numpy as np

from geogeometry.geometry.circle.components.CircleMetrics import CircleMetrics
from geogeometry.geometry.circle.components.CirclePlotter import CirclePlotter
from geogeometry.geometry.circle.components.CircleProperties import CircleProperties
from geogeometry.geometry.shared.BaseObject import BaseObject

if TYPE_CHECKING:
    from geogeometry.geometry.plane.Plane import Plane


class Circle(BaseObject, CircleProperties):

    def __init__(self,
                 center: Union[List, np.ndarray],
                 radius: float,
                 plane: Optional['Plane'] = None,
                 name: Optional[str] = None):

        super().__init__(name=name)

        self.metrics: CircleMetrics = CircleMetrics(self)
        self.plotter: CirclePlotter = CirclePlotter(self)

        self.setCenter(center=center)
        self.setRadius(radius=radius)
        self.setPlane(plane=plane)
