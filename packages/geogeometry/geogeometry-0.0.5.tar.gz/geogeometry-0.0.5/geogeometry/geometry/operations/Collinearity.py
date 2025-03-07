from typing import Union, List

import numpy as np

from geogeometry.geometry.vector.Vector import Vector


class Collinearity(object):

    @staticmethod
    def isNodeWithinSegment(point: np.ndarray, segment: Union[List[float], np.ndarray],
                            cross_tolerance: float = 1e-6, dot_tolerance: float = 1e-12) -> bool:
        if isinstance(segment, list):
            segment = np.array(segment)

        segment_vector = Vector(origin=segment[0], tip=segment[1])
        test_vector = Vector(origin=segment[0], tip=point)

        if test_vector.getLength() > segment_vector.getLength():
            return False

        # noinspection PyUnreachableCode
        cross_vector = Vector(tip=np.cross(segment_vector.getUnitVector(), test_vector.getUnitVector()))

        # Si colinean checkeo que node esta en segment
        if cross_vector.getLength() < cross_tolerance:
            # Debe ser mayor que 0 para que el punto este dentro del segment.
            dot = np.dot(segment_vector.getUnitVector(), test_vector.getUnitVector())
            if dot >= -dot_tolerance:  # - toleran ya que puede estar muy cerca por el otro lado
                return True

        return False
