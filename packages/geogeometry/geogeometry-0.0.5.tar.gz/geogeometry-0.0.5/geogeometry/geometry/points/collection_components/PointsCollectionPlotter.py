from typing import TYPE_CHECKING

import pyvista as pv

from geogeometry.geometry.shared.shared_components.BasePlotter import BasePlotter

if TYPE_CHECKING:
    import matplotlib.pyplot as plt
    from geogeometry.geometry.points import PointsCollection


class PointsCollectionPlotter(BasePlotter):

    def __init__(self, points_collection: 'PointsCollection'):
        super().__init__(element=points_collection)
        self.points_collection: 'PointsCollection' = points_collection

    def addToMatplotlibAx(self, ax: 'plt.Axes') -> None:
        pts = self.points_collection.getPoints()
        ax.scatter(pts[:, 0], pts[:, 1])

    def _getPyVistaPointsCloud(self) -> pv.PolyData:
        return pv.PolyData(self.points_collection.getPoints())

    def addToPyvistaPlotter(self, plotter: 'pv.Plotter', **kwargs) -> None:
        plotter.add_mesh(self._getPyVistaPointsCloud(),
                         color=self.points_collection.getColor(),
                         opacity=self.points_collection.getOpacity(),
                         point_size=10,
                         render_points_as_spheres=True)

    def addToParaviewPlotter(self, plotter, **kwargs) -> None: ...
