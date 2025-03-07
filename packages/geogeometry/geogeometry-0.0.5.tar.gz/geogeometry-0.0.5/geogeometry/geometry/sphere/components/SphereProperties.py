from typing import Optional, Union, List

import numpy as np


class SphereProperties(object):

    def __init__(self):
        self.center: Optional[np.ndarray] = None
        self.radius: Optional[float] = None

    def setCenter(self, center: Union[List, np.ndarray]) -> None:
        if isinstance(center, list):
            center = np.array(center)
        self.center = center

    def setRadius(self, radius: float) -> None:
        self.radius = radius

    def getCenter(self) -> np.ndarray:
        return self.center

    def getRadius(self) -> float:
        return self.radius
