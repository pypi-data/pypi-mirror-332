import math
from typing import Callable, TYPE_CHECKING, Tuple, Union, List, Literal

import numpy as np

from geogeometry.geometry.vector.Vector import Vector
from geogeometry.geometry.operations.Rotations import Rotations

if TYPE_CHECKING:
    from geogeometry.geometry.plane.Plane import Plane


PointType = Union[List, np.ndarray]
PlaneInputsType = Tuple[np.ndarray, Vector]


class PlaneFactory(object):

    @staticmethod
    def createFromThreePoints(n0: PointType, n1: PointType, n2: PointType) -> PlaneInputsType:
        if isinstance(n0, list):
            n0 = np.array(n0)
        if isinstance(n1, list):
            n1 = np.array(n1)
        if isinstance(n2, list):
            n2 = np.array(n2)

        vec01 = n1 - n0  # Vector from origin to node 1.
        vec02 = n2 - n0  # Vector from origin to node 2.

        # noinspection PyUnreachableCode
        normal_vector = Vector(tip=np.cross(vec01, vec02))

        return n0, normal_vector

    @staticmethod
    def createFromDipAndDipdir(origin: PointType, dip: float, dipdir: float) -> PlaneInputsType:
        if isinstance(origin, list):
            origin = np.array(origin)

        if dip < 0:
            raise ValueError("Dip value must be between 0 and 90°.")

        normal_vector = Vector(tip=[0, 0, 1])

        Rx = Rotations.calculateXRotationMatrix(angle=-math.radians(dip))
        Rz = Rotations.calculateZRotationMatrix(angle=-math.radians(dipdir))

        normal_vector.rotateByRotationMatrix(rotation_matrix=Rx)
        normal_vector.rotateByRotationMatrix(rotation_matrix=Rz)

        return origin, normal_vector

    @staticmethod
    def createAsOrthogonal(axis: Literal['x', 'y', 'z'], level: float) -> PlaneInputsType:
        if axis == 'x':
            tip = [1, 0, 0]
        elif axis == 'y':
            tip = [0, 1, 0]
        elif axis == 'z':
            tip = [0, 0, 1]
        else:
            raise ValueError(f"Wrong axis definition: '{axis}'")

        tip = np.array(tip)
        normal_vector = Vector(tip=tip)
        origin = tip * level

        return origin, normal_vector

    @staticmethod
    def createAsVerticalProjection(n0: PointType, n1: PointType) -> PlaneInputsType:
        return PlaneFactory.createFromThreePoints(n0=list(n0)+[0], n1=list(n1)+[0], n2=list(n1)+[1])

