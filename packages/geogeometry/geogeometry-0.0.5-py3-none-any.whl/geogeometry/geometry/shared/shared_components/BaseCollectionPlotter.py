from typing import TypeVar, TYPE_CHECKING

from geogeometry.geometry.shared.shared_components.BasePlotter import BasePlotter

if TYPE_CHECKING:
    import pyvista as pv
    import matplotlib.pyplot as plt
    from geogeometry.geometry.shared.BaseObjectCollection import BaseObjectCollection


CollectionType = TypeVar('CollectionType', bound='BaseObjectCollection')


class BaseCollectionPlotter(BasePlotter):

    def __init__(self, collection: CollectionType):
        super().__init__(element=collection)
        self.collection: CollectionType = collection

    def addToMatplotlibAx(self, ax: 'plt.Axes') -> None:
        for p in self.collection:
            p.addToMatplotlibAx(ax)

    def addToPyvistaPlotter(self, plotter: 'pv.Plotter', **kwargs) -> None:
        for p in self.collection:
            p.addToPyvistaPlotter(plotter)

    def addToParaviewPlotter(self, plotter, **kwargs) -> None: ...
