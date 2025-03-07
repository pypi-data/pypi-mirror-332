from typing import TYPE_CHECKING

import pyvista as pv

from geogeometry.geometry.shared.shared_components.BasePlotter import BasePlotter

if TYPE_CHECKING:
    import matplotlib.pyplot as plt
    from geogeometry.geometry.triangulation.TriangulationsCollection import TriangulationsCollection


class TriangulationsCollectionPlotter(BasePlotter):

    def __init__(self, triangulations_collection: 'TriangulationsCollection'):
        super().__init__(element=triangulations_collection)
        self.triangulations_collection: 'TriangulationsCollection' = triangulations_collection

    def addToMatplotlibAx(self, ax: 'plt.Axes') -> None:
        for t in self.triangulations_collection:
            t.addToMatplotlibAx(ax=ax)

    def addToPyvistaPlotter(self, plotter: 'pv.Plotter', **kwargs) -> None:
        for t in self.triangulations_collection:
            t.addToPyvistaPlotter(plotter)

    def addToParaviewPlotter(self, plotter, **kwargs) -> None: ...