from typing import TYPE_CHECKING

import pyvista as pv

from geogeometry.geometry.shared.shared_components.BasePlotter import BasePlotter

if TYPE_CHECKING:
    import matplotlib.pyplot as plt
    from geogeometry.geometry.model.GeometryModelsCollection import GeometryModelsCollection


class GeometryModelsCollectionPlotter(BasePlotter):

    def __init__(self, geometrymodels_collection: 'GeometryModelsCollection'):
        super().__init__(element=geometrymodels_collection)
        self.geometrymodels_collection: 'GeometryModelsCollection' = geometrymodels_collection

    def addToMatplotlibAx(self, ax: 'plt.Axes') -> None: ...

    def addToPyvistaPlotter(self, plotter: 'pv.Plotter', **kwargs) -> None:
        for m in self.geometrymodels_collection:
            m.addToPyvistaPlotter(plotter=plotter, **kwargs)

    def addToParaviewPlotter(self, plotter, **kwargs) -> None: ...
