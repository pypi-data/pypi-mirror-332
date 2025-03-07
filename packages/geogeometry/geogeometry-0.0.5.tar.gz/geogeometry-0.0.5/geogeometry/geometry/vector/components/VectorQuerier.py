from typing import TYPE_CHECKING, Optional

from geogeometry.geometry.operations.Angles import Angles

if TYPE_CHECKING:
    from geogeometry.geometry.vector.Vector import Vector


class VectorQuerier(object):

    def __init__(self, vector: 'Vector'):
        self.vector = vector

    def calculateAngleWithVector(self, other_vector: 'Vector') -> float:
        return Angles.calculateAngleFromThreePoints(n0=self.vector.getUnitVector(),
                                                    n1=[0, 0, 0],
                                                    n2=other_vector.getUnitVector())
