from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from geogeometry.geometry.shared.observer.Observer import Observer


class Observable(object):

    def __init__(self):
        super().__init__()
        self.observers: List['Observer'] = []

    def addObserver(self, observer: 'Observer'):
        self.observers += [observer]

    def removeObserver(self, observer: 'Observer'):
        self.observers.remove(observer)

    def notifyObservers(self):
        for observer in self.observers:
            observer.onElementChange(self)
