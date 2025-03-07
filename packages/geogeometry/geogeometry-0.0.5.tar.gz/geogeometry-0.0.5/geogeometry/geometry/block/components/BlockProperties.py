from typing import Optional, TYPE_CHECKING

import numpy as np



if TYPE_CHECKING:
    from geogeometry.geometry.block.components.BlockMetrics import BlockMetrics
    from geogeometry.geometry.block.components.BlockRepresentation import BlockRepresentation
    from geogeometry.geometry.vector.Vector import Vector
    from geogeometry import Triangulation


class BlockProperties(object):

    def __init__(self):
        self.corners: Optional[np.ndarray] = None

        self.metrics: Optional['BlockMetrics'] = None
        self.representation: Optional['BlockRepresentation'] = None

    def getCorners(self) -> np.ndarray:
        return self.corners

    # def getAxisVector(self) -> Optional['Vector']:
    #     return self.axis_vector

    def getWidth(self) -> Optional[float]:
        return self.metrics.getWidth()

    def getLength(self) -> Optional[float]:
        return self.metrics.getLength()

    def getHeight(self) -> Optional[float]:
        return self.metrics.getHeight()

    def getTriangulation(self) -> Optional['Triangulation']:
        return self.representation.getTriangulation()
