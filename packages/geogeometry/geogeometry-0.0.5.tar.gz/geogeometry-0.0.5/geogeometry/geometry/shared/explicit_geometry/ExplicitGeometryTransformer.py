from typing import Union, List, Callable

import numpy as np

from geogeometry.geometry.operations.Rotations import Rotations
from geogeometry.geometry.shared.TransformationRecord import TransformationRecord


def updateElementMetrics(func: Callable[..., None]) -> Callable[..., None]:

    def inner(transformer, *args, **kwargs) -> None:
        func(transformer, *args, **kwargs)
        transformer.element.calculateMetrics()

    return inner


class ExplicitGeometryTransformer(object):

    def __init__(self, element):
        self.element = element

        self.transformations: List[TransformationRecord] = []

    @updateElementMetrics
    def translate(self, translation_vector: Union[List, np.ndarray]) -> None:
        self.transformations += [TransformationRecord(transformation_type='translation', translation_vector=translation_vector)]

        self.element.setNodes(nodes=self.element.getNodes() + translation_vector)

    @updateElementMetrics
    def rotateByRotationMatrix(self, rotation_matrix: np.ndarray) -> None:
        self.transformations += [TransformationRecord(transformation_type='rotation', translation_vector=rotation_matrix)]

        rotated_nodes = Rotations.rotatePointsByRotationMatrix(points=self.element.getNodes(), rotation_matrix=rotation_matrix)
        self.element.setNodes(nodes=rotated_nodes)

    @updateElementMetrics
    def rotateByQuaternion(self, quaternion: Union[List, np.ndarray]) -> None:
        pass

