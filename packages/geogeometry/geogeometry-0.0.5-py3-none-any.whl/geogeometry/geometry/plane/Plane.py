from typing import Optional, Union, List, Tuple, Callable, Literal

import numpy as np

from geogeometry.geometry.plane.components.PlaneFactory import PlaneFactory
from geogeometry.geometry.plane.components.PlaneProperties import PlaneProperties
from geogeometry.geometry.shared.BaseObject import BaseObject
from geogeometry.geometry.vector.Vector import Vector

PointType = Union[List, np.ndarray]
PlaneInputsType = Tuple[np.ndarray, Vector]


def createFromInputs(func: Callable[..., PlaneInputsType]) -> Callable[..., 'Plane']:
    def inner(*args, **kwargs) -> 'Plane':
        origin, normal_vector = func(*args, **kwargs)
        p = Plane(origin=origin, normal_vector=normal_vector)
        return p

    return inner


class Plane(BaseObject['Plane'], PlaneProperties):

    def __init__(self,
                 origin: PointType,
                 normal_vector: 'Vector',
                 name: Optional[str] = None):
        super().__init__(name=name)

        self.setOrigin(origin=origin)
        self.setNormalVector(normal_vector=normal_vector)

    def __str__(self) -> str:
        txt = f"Plane(name={self.getName()}, origin={self.getOrigin()}, normal_vector={self.getNormalVector()})"
        return txt

    @staticmethod
    @createFromInputs
    def createFromThreePoints(n0: PointType, n1: PointType, n2: PointType) -> PlaneInputsType:
        return PlaneFactory.createFromThreePoints(n0=n0, n1=n1, n2=n2)

    @staticmethod
    @createFromInputs
    def createFromDipAndDipdir(origin: PointType, dip: float, dipdir: float) -> PlaneInputsType:
        return PlaneFactory.createFromDipAndDipdir(origin=origin, dip=dip, dipdir=dipdir)

    @staticmethod
    @createFromInputs
    def createAsOrthogonal(axis: Literal['x', 'y', 'z'], level: float) -> PlaneInputsType:
        return PlaneFactory.createAsOrthogonal(axis=axis, level=level)

    @staticmethod
    @createFromInputs
    def createAsVerticalProjection(n0: PointType, n1: PointType) -> PlaneInputsType:
        return PlaneFactory.createAsVerticalProjection(n0=n0, n1=n1)
