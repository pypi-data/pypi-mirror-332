from typing import TYPE_CHECKING, Optional

import numpy as np
import pyvista as pv
import matplotlib.tri as tri

from geogeometry.geometry.shared.shared_components.BasePlotter import BasePlotter

if TYPE_CHECKING:
    import matplotlib.pyplot as plt
    from geogeometry.geometry.triangulation.Triangulation import Triangulation


class TriangulationPlotter(BasePlotter):

    def __init__(self, triangulation: 'Triangulation'):
        super().__init__(element=triangulation)
        self.triangulation: 'Triangulation' = triangulation

    def addToMatplotlibAx(self, ax: 'plt.Axes') -> None:
        nodes = self.triangulation.getNodes()
        faces = self.triangulation.getFaces()

        t = tri.Triangulation(nodes[:, 0], nodes[:, 1], faces)
        ax.triplot(t, color=self.triangulation.getColor())

    def _getPyVistaTriangulation(self) -> pv.PolyData:
        pv_faces = np.hstack((np.full((self.triangulation.getFaces().shape[0], 1), 3),
                              self.triangulation.getFaces()))

        return pv.PolyData(self.triangulation.getNodes(), faces=pv_faces)

    def addToPyvistaPlotter(self, plotter: 'pv.Plotter', **kwargs) -> None:
        plotter.add_mesh(self._getPyVistaTriangulation(),
                         show_edges=False,
                         color=self.triangulation.getColor(),
                         opacity=self.triangulation.getOpacity())

    def addToParaviewPlotter(self, plotter, **kwargs) -> None: ...
