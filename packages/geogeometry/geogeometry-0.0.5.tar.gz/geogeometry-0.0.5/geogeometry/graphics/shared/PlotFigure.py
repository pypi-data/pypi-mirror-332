from typing import List, Union, TYPE_CHECKING

import numpy as np

if TYPE_CHECKING:
    from geogeometry.geometry.shared.BaseObject import BaseObject
    from geogeometry.geometry.shared.BaseObjectCollection import BaseObjectCollection


class PlotFigure(object):

    def __init__(self):
        self.elements: List[Union['BaseObject', 'BaseObjectCollection']] = []

    def addElement(self, element: Union['BaseObject', 'BaseObjectCollection']) -> None:
        self.elements += [element]

    def calculateLimits(self) -> np.ndarray:
        all_limits = [lim for e in self.elements for lim in e.getLimits()]
        limits = np.array([np.min(all_limits, axis=0), np.max(all_limits, axis=0)])
        return limits
