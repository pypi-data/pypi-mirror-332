from typing import TYPE_CHECKING, Optional

import pyvista as pv

from geogeometry.geometry.shared.shared_components.BasePlotter import BasePlotter

if TYPE_CHECKING:
    import matplotlib.pyplot as plt
    from geogeometry.geometry.model.GeometryModel import GeometryModel


class GeometryModelPlotter(BasePlotter):

    def __init__(self, model: 'GeometryModel'):
        super().__init__(element=model)
        self.model: 'GeometryModel' = model

    def addToMatplotlibAx(self, ax: 'plt.Axes') -> None:
        if len(self.model.getPolylines()):
            self.model.getPolylines().addToMatplotlibAx(ax=ax)

        if len(self.model.getTriangulations()):
            self.model.getTriangulations().addToMatplotlibAx(ax=ax)

        if len(self.model.getPoints()):
            self.model.getPoints().addToMatplotlibAx(ax=ax)

    def addToPyvistaPlotter(self, plotter: 'pv.Plotter', **kwargs) -> None:
        if len(self.model.getPolylines()):
            self.model.getPolylines().addToPyvistaPlotter(plotter=plotter, **kwargs)

        if len(self.model.getTriangulations()):
            self.model.getTriangulations().addToPyvistaPlotter(plotter=plotter, **kwargs)

        if len(self.model.getPoints()):
            self.model.getPoints().addToPyvistaPlotter(plotter=plotter, **kwargs)

    def addToParaviewPlotter(self, plotter, **kwargs) -> None: ...
