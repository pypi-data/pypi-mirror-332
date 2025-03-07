from typing import List, TypeVar, Iterator, Optional, Union, Generic, TYPE_CHECKING

import numpy as np

from geogeometry.geometry.shared.BaseObject import BaseObject
from geogeometry.geometry.shared.observer.Observer import Observer
from geogeometry.geometry.shared.shared_components.BaseCollectionMetrics import BaseCollectionMetrics
from geogeometry.geometry.shared.shared_components.BaseCollectionPlotter import BaseCollectionPlotter

if TYPE_CHECKING:
    from geogeometry.geometry.shared.observer.Observable import Observable

CollectionType = TypeVar('CollectionType')
ElementType = TypeVar('ElementType', bound='BaseObject')


class BaseObjectCollection(BaseObject[CollectionType], Observer, Generic[CollectionType, ElementType]):

    def __init__(self, name: Optional[str] = None):
        super().__init__(name=name)

        self.elements: List[ElementType] = []

        self.metrics: BaseCollectionMetrics = BaseCollectionMetrics(self)
        self.plotter: BaseCollectionPlotter = BaseCollectionPlotter(self)

    def __len__(self) -> int:
        return len(self.elements)

    def __iter__(self) -> Iterator[ElementType]:
        for e in self.elements:
            yield e

    def __getitem__(self, identifier: Union[int, str]) -> ElementType:
        if isinstance(identifier, int):
            return self.elements[identifier]
        else:
            for e in self.elements:
                if e.getName() == identifier:
                    return e
            else:
                raise ValueError(f"Element '{identifier}' not found in collection.")

    def addElement(self, element: ElementType) -> None:
        self.elements += [element]
        element.addObserver(observer=self)

        self.notifyObservers()
        self.calculateMetrics()

    def deleteElement(self, identifier: Union[int, str]):
        for e in self.elements:
            if e.getName() == identifier:
                self.elements.remove(e)
                e.removeObserver(observer=self)

                self.notifyObservers()
                self.calculateMetrics()
                break
        else:
            raise ValueError(f"Element '{identifier}' not found in collection.")

    def getLimits(self) -> Optional[np.ndarray]:
        return self.metrics.getLimits()

    def getCenter(self) -> Optional[np.ndarray]:
        return self.metrics.getLimits()

    def onElementChange(self, observable: 'Observable'):
        self.calculateMetrics()
        self.notifyObservers()
