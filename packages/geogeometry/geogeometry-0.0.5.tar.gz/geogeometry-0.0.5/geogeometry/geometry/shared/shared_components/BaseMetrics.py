from abc import ABC, abstractmethod
from typing import Union, TYPE_CHECKING

if TYPE_CHECKING:
    from geogeometry.geometry.shared.BaseObject import BaseObject
    from geogeometry.geometry.shared.BaseObjectCollection import BaseObjectCollection


class BaseMetrics(ABC):

    @abstractmethod
    def calculateMetrics(self) -> None: ...
