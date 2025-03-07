from typing import TYPE_CHECKING, Optional

import pyvista as pv


from geogeometry.geometry.shared.shared_components.BasePlotter import BasePlotter

if TYPE_CHECKING:
    import matplotlib.pyplot as plt
    from geogeometry.geometry.polyline.PolylinesCollection import PolylinesCollection


class PolylinesCollectionPlotter(BasePlotter):

    def __init__(self, polylines_collection: 'PolylinesCollection'):
        super().__init__(element=polylines_collection)
        self.polylines_collection: 'PolylinesCollection' = polylines_collection

    def addToMatplotlibAx(self, ax: 'plt.Axes') -> None:
        for p in self.polylines_collection:
            p.addToMatplotlibAx(ax)

    def addToPyvistaPlotter(self, plotter: 'pv.Plotter', **kwargs) -> None:
        for p in self.polylines_collection:
            p.addToPyvistaPlotter(plotter)

    def addToParaviewPlotter(self, plotter, **kwargs) -> None: ...
