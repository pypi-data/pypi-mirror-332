from typing import TYPE_CHECKING

from geogeometry.geometry.shared.shared_components.BasePlotter import BasePlotter

if TYPE_CHECKING:
    import matplotlib.pyplot as plt
    import pyvista as pv
    from geogeometry.geometry.vector.Vector import Vector


class VectorPlotter(BasePlotter):

    def __init__(self, vector: 'Vector'):
        super().__init__(element=vector)
        self.vector: 'Vector' = vector

    def addToMatplotlibAx(self, ax: 'plt.Axes') -> None: ...

    def addToPyvistaPlotter(self, plotter: 'pv.Plotter', **kwargs) -> None: ...

    def addToParaviewPlotter(self, plotter, **kwargs) -> None: ...
