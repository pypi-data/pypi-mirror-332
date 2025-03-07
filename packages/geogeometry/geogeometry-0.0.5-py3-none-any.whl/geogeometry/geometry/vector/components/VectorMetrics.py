from typing import TYPE_CHECKING, Optional

import numpy as np

from geogeometry.geometry.operations.Angles import Angles
from geogeometry.geometry.shared.shared_components.BaseMetrics import BaseMetrics

if TYPE_CHECKING:
    from geogeometry.geometry.vector.Vector import Vector


class VectorMetrics(BaseMetrics):

    def __init__(self, vector: 'Vector'):
        self.vector: 'Vector' = vector

        self.length: Optional[float] = None

        self.is_unitary: Optional[bool] = None
        self.is_position_vector: Optional[bool] = None  # origin=(0,0,0)

        self.unit_vector: Optional[np.ndarray] = None

        self.dip: Optional[float] = None
        self.azimuth: Optional[float] = None

    def getLength(self) -> float:
        return self.length

    def isUnitary(self) -> bool:
        return self.is_unitary

    def isPositionVector(self) -> bool:
        return self.is_position_vector

    def getUnitVector(self) -> np.ndarray:
        return self.unit_vector

    def getDip(self) -> float:
        return self.dip

    def getAzimuth(self) -> float:
        return self.azimuth

    def calculateMetrics(self) -> None:
        self.calculateLength()

        self.is_unitary = (self.length == 1.)
        self.is_position_vector = (np.sum(self.vector.getOrigin()) == 0.)

        self.calculateUnitVector()
        self.calculateDipAndAzimuth()

    def calculateLength(self) -> None:
        diff = self.vector.getTip() - self.vector.getOrigin()
        self.length = np.linalg.norm(diff)

    def calculateUnitVector(self) -> None:
        if self.is_unitary and self.is_position_vector:
            self.unit_vector = self.vector.getTip()
            # self.vector.setNormalizedVector(normalized_vector=self.vector.copy())
            return

        pos = self.vector.getTip() - self.vector.getOrigin()
        norm = np.linalg.norm(pos)
        if norm == 0.:
            raise ValueError("Origin as vector.")

        self.unit_vector = np.round(pos/norm, decimals=5)

    def calculateDipAndAzimuth(self) -> None:

        # if self.vector.getNormalizedVector() is None:
        #     self.calculateNormalizedVector()

        # norm_vector = self.vector.getNormalizedVector()

        azimuth = None

        if self.vector.getDimensions() == 2:
            dip = 0.
        # if norm_vector.getOrigin().shape[0] == 2:
        #     dip = 90.
        else:
            # if abs(norm_vector.getTip()[2]) == 1.:
            if abs(self.unit_vector[2]) == 1.:
                dip, azimuth = 0, 0
            else:
                dip = Angles.calculateAngleBetweenVectorAndAxis(v=self.vector, axis_id='z')
                if dip > 90.:
                    reversed_vector = self.vector.copy()
                    reversed_vector.reverse()
                    dip = Angles.calculateAngleBetweenVectorAndAxis(v=reversed_vector, axis_id='z')

        if azimuth is None:
            azimuth = Angles.calculateAngleFromThreePoints([0., 1.], [0., 0.], self.vector.getTip()[:2])

        if self.vector.getTip()[0] < 0.:
            azimuth = 360. - azimuth

        self.dip = round(dip, 2)
        self.azimuth = round(azimuth, 2)
