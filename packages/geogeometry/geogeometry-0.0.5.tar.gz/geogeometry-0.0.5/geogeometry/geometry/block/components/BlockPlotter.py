from typing import TYPE_CHECKING

from geogeometry.geometry.shared.shared_components.BasePlotter import BasePlotter

if TYPE_CHECKING:
    from geogeometry.geometry.block.Block import Block


class BlockPlotter(BasePlotter):

    def __init__(self, block: 'Block'):
        super().__init__(element=block)

        self.block: 'Block' = block

    def addToMatplotlibAx(self, ax: 'plt.Axes') -> None: ...

    def _createPyVistaWireframe(self) -> 'PolylinesCollection':
        wireframe = self.block.getWireframe()

    def _createPyVistaTriangulation(self) -> 'Triangulation':
        triangulation = self.block.getTriangulation()

    def addToPyvistaPlotter(self, plotter: 'pv.Plotter', **kwargs) -> None:

        plot_style = kwargs.get("plot_style", "wireframe")
        if plot_style == "wireframe":
            self._createPyVistaWireframe()
        elif plot_style == "triangualtion":
            self._createPyVistaTriangulation()

        plotter.add_mesh(self._getPyVistaPolyline(),
                         color=self.block.getColor(),
                         opacity=self.block.getOpacity(),
                         line_width=self.polyline.getLineWidth())

    def addToParaviewPlotter(self, plotter, **kwargs) -> None: ...
