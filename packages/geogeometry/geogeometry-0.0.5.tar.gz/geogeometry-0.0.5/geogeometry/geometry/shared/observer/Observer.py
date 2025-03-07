from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from geogeometry.geometry.shared.observer.Observable import Observable


class Observer(ABC):

    @abstractmethod
    def onElementChange(self, observable: 'Observable'): ...

