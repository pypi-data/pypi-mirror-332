from typing import TypeVar, TYPE_CHECKING, Optional

import numpy as np

from geogeometry.geometry.shared.shared_components.BaseMetrics import BaseMetrics

if TYPE_CHECKING:
    from geogeometry.geometry.shared.BaseObjectCollection import BaseObjectCollection


CollectionType = TypeVar('CollectionType', bound='BaseObjectCollection')


class BaseCollectionMetrics(BaseMetrics):

    def __init__(self, collection: CollectionType):
        self.collection: CollectionType = collection

        self.limits: Optional[np.ndarray] = None
        self.center: Optional[np.ndarray] = None

    def getLimits(self) -> Optional[np.ndarray]:
        return self.limits

    def getCenter(self) -> Optional[np.ndarray]:
        return self.center

    def calculateMetrics(self) -> None:
        for e in self.collection:
            if e.getLimits() is not None:
                break
        else:
            return

        self.calculateLimits()
        self.calculateCenter()

    def calculateLimits(self) -> None:
        all_limits = [lim for e in self.collection if e.getLimits() is not None for lim in e.getLimits()]
        _min, _max = np.min(all_limits, axis=0), np.max(all_limits, axis=0)
        self.limits = np.array([_min, _max])

    def calculateCenter(self) -> None:
        all_centers = [e.getCenter() for e in self.collection if e.getCenter() is not None]
        self.center = np.average(all_centers, axis=0)
