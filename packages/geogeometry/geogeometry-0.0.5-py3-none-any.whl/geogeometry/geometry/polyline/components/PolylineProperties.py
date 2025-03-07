from typing import Optional, Union, List, Literal, TYPE_CHECKING

import numpy as np

from geogeometry.geometry.polyline.components.PolylinePlotProperties import PolylinePlotProperties

if TYPE_CHECKING:
    from geogeometry.geometry.polyline.components.PolylineMetrics import PolylineMetrics


class PolylineProperties(PolylinePlotProperties):

    def __init__(self):
        super().__init__()

        # self.nodes: Optional[np.ndarray] = None
        self.segments: Optional[np.ndarray] = None

        self.metrics: Optional['PolylineMetrics'] = None

        # self.closed: Optional[bool] = None
        # self.length: Optional[float] = None
        #
        # self.mid_point: Optional[np.ndarray] = None
        #
        # # 2D properties
        # self.area: Optional[float] = None

        # Plot properties
        # self.line_width: float = 2.

    # def setNodes(self, nodes: Union[List, np.ndarray]) -> None:
    #     self.nodes = np.array(nodes)
    #     self.segments = [[j, j + 1] for j, n in enumerate(self.nodes[:-1])]

    # def setClosed(self, closed: bool) -> None:
    #     self.closed = closed
    #
    # def setLength(self, length: float) -> None:
    #     self.length = length
    #
    # def setMidPoint(self, mid_point: np.ndarray) -> None:
    #     self.mid_point = mid_point
    #
    # def setArea(self, area: float) -> None:
    #     self.area = area

    # def setLineWidth(self, line_width: float) -> None:
    #     self.line_width = line_width

    # def getNodes(self) -> Optional[np.ndarray]:
    #     return self.nodes

    def getSegments(self) -> Optional[np.ndarray]:
        return self.segments

    def isClosed(self) -> Optional[bool]:
        return self.metrics.isClosed()

    def getLength(self) -> Optional[float]:
        return self.metrics.getLength()

    def getMidPoints(self) -> Optional[np.ndarray]:
        return self.mid_point

    def getArea(self) -> Optional[float]:
        return self.area

    # def getLineWidth(self) -> float:
    #     return self.line_width
