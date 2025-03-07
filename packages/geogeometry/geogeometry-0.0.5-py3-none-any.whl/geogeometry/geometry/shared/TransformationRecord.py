from typing import Literal, Optional, TYPE_CHECKING, Union, List

import numpy as np

if TYPE_CHECKING:
    from geogeometry.geometry.plane.Plane import Plane


TransformationTypes = Literal['translation', 'rotation', 'reflection']


class TransformationRecord(object):

    def __init__(self, transformation_type: TransformationTypes,
                 translation_vector: Optional[Union[List, np.ndarray]] = None,
                 rotation_matrix: Optional[np.ndarray] = None,
                 reflection_plane: Optional['Plane'] = None):

        self.transformation_type: TransformationTypes = transformation_type

        self.translation_vector: Optional[Union[List, np.ndarray]] = translation_vector
        self.rotation_matrix: Optional[np.ndarray] = rotation_matrix
        self.reflection_plane: Optional['Plane'] = reflection_plane

    def getTranslationVector(self) -> Optional[Union[List, np.ndarray]]:
        return self.translation_vector

    def getRotationMatrix(self) -> Optional[np.ndarray]:
        return self.rotation_matrix

    def getReflectionPlane(self) -> Optional['Plane']:
        return self.reflection_plane
