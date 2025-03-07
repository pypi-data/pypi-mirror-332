from typing import TYPE_CHECKING

from geogeometry.geometry.shared.shared_components.BasePlotter import BasePlotter

from matplotlib.patches import Circle

if TYPE_CHECKING:
    import matplotlib.pyplot as plt
    import pyvista as pv
    from geogeometry.geometry.circle.Circle import Circle


class CirclePlotter(BasePlotter):

    def __init__(self, circle: 'Circle'):
        super().__init__(element=circle)
        self.circle: 'Circle' = circle

    def addToMatplotlibAx(self, ax: 'plt.Axes') -> None:
        circle = Circle(self.circle.getCenter(),
                        self.circle.getRadius(),
                        edgecolor='blue',
                        facecolor='none',
                        linewidth=2)
        ax.add_patch(circle)

    def addToPyvistaPlotter(self, plotter: 'pv.Plotter', **kwargs) -> None: ...

    def addToParaviewPlotter(self, plotter, **kwargs) -> None: ...
