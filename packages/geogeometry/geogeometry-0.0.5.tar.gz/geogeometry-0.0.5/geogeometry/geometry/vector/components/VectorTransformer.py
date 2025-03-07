from typing import TYPE_CHECKING

import numpy as np

from geogeometry.geometry.shared.explicit_geometry.ExplicitGeometryTransformer import ExplicitGeometryTransformer, updateElementMetrics

if TYPE_CHECKING:
    from geogeometry.geometry.vector.Vector import Vector


class VectorTransformer(ExplicitGeometryTransformer):

    def __init__(self, vector: 'Vector'):
        super().__init__(element=vector)
        self.vector: 'Vector' = vector

    @updateElementMetrics
    def reverse(self) -> None:
        n0 = -1 * self.vector.getOrigin()
        n1 = -1 * self.vector.getTip()
        self.vector.setNodes(nodes=np.array([n0, n1]))
