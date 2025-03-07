from typing import Optional

import numpy as np


class CoordinateSystem(object):

    def __init__(self):
        self.origin: Optional[np.ndarray] = None

        self.x_axis: Optional[np.ndarray] = None
        self.y_axis: Optional[np.ndarray] = None
        self.z_axis: Optional[np.ndarray] = None

    def setOrigin(self, origin: np.ndarray) -> None:
        self.origin = origin

    def setXAxis(self, x_axis: np.ndarray) -> None:
        self.x_axis = x_axis

    def setYAxis(self, y_axis: np.ndarray) -> None:
        self.y_axis = y_axis

    def setZAxis(self, z_axis: np.ndarray) -> None:
        self.z_axis = z_axis

