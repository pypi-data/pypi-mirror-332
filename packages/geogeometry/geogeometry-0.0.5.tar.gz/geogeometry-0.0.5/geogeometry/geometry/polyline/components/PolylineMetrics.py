from typing import Optional, TYPE_CHECKING

import numpy as np

from geogeometry.geometry.shared.explicit_geometry.ExplicitGeometryMetrics import ExplicitGeometryMetrics
from geogeometry.geometry.shared.shared_components.BaseMetrics import BaseMetrics

if TYPE_CHECKING:
    from geogeometry.geometry.polyline.Polyline import Polyline


class PolylineMetrics(BaseMetrics):

    def __init__(self, polyline: 'Polyline'):
        self.polyline: 'Polyline' = polyline

        self.length: Optional[float] = None
        self.closed: Optional[bool] = None
        self.mid_point: Optional[np.ndarray] = None

    def getLength(self) -> Optional[float]:
        return self.length

    def isClosed(self) -> Optional[bool]:
        return self.closed

    def getMidPoints(self) -> Optional[np.ndarray]:
        return self.mid_point

    def calculateMetrics(self) -> None:
        self.calculateClosed()
        self.calculateLength()
        self.calculateMidPoint()

        # if self.polyline.getDimensions() == 2 and self.polyline.isClosed():
        #     self.calculate2DArea()

    def calculateClosed(self) -> None:
        nodes = self.polyline.getNodes()
        self.closed = False
        if not np.linalg.norm(nodes[0] - nodes[-1]):
            self.closed = True

    def calculateLength(self) -> None:
        nodes = self.polyline.getNodes()
        ds = [np.linalg.norm(n - nodes[i + 1]) for i, n in enumerate(nodes[:-1])]
        self.length = np.sum(ds)

    def calculateMidPoint(self) -> None:
        """
        Mid at (total length) / 2
        """
        self.mid_point = self.polyline.getPointAtDistanceFromOrigin(distance=self.polyline.getLength() / 2.)

    # def calculate2DArea(self) -> None:
    #     """
    #     Considers XY space, even if nodes dimensions is greater than 2.
    #     Gets area even if the polyline is open.
    #     """
    #     nodes = self.polyline.getNodes()
    #     if self.polyline.isClosed():
    #         x, y = nodes[:-1][:, 0], nodes[:-1][:, 1]
    #     else:
    #         x, y = nodes[:, 0], nodes[:, 1]
    #
    #     area = 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))
    #
    #     self.polyline.setArea(area=area)


