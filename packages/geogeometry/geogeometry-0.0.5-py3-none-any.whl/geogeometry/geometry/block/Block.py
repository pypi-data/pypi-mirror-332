from typing import Optional, Union, List

import numpy as np

from geogeometry.geometry.block.components.BlockMetrics import BlockMetrics
from geogeometry.geometry.block.components.BlockPlotter import BlockPlotter
from geogeometry.geometry.block.components.BlockProperties import BlockProperties
from geogeometry.geometry.block.components.BlockRepresentation import BlockRepresentation

from geogeometry.geometry.shared.explicit_geometry.ExplicitGeometry import ExplicitGeometry

from geogeometry.geometry.vector.Vector import Vector


class Block(ExplicitGeometry, BlockProperties):

    def __init__(self,
                 corners: Union[List, np.ndarray],
                 name: Optional[str] = None):
        super().__init__(name=name)

        self.setCorners(corners=corners)

        self.metrics: BlockMetrics = BlockMetrics(self)
        self.representation: BlockRepresentation = BlockRepresentation(self)
        self.plotter: BlockPlotter = BlockPlotter(self)

    def setCorners(self, corners: Union[List, np.ndarray]) -> None:
        self.corners = np.array([np.min(corners, axis=0), np.max(corners, axis=0)])

        self.representation.createNodes()
        self.representation.createWireframe()
        self.representation.createTriangulation()

    def __str__(self) -> str:
        txt = ("Block("
               f"c0={self.getNodes()[0]}, "
               f"c1={self.getNodes()[1]}, "
               f"center={self.getCenter()})")
        return txt

    # # Translate point to the block's local space
    # local_point = point - block_center
    #
    # # Rotate the point into the block's local axis-aligned space
    # local_point = np.dot(rotation_matrix.T, local_point)
    #
    # # Half-dimensions of the block
    # half_dimensions = block_dimensions / 2
    #
    # # Check if the point lies within the bounds of the block
    # return all(-half_dimensions[i] <= local_point[i] <= half_dimensions[i] for i in range(3))

    # def arePointsInside(self, points: Union[List, np.ndarray]) -> np.ndarray[bool]:
    #     dist = np.linalg.norm(self.getCenter() - points, axis=1)
    #     return dist < self.getRadius()
