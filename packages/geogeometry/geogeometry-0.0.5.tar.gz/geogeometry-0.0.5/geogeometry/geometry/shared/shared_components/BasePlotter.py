from abc import ABC, abstractmethod
from typing import Optional, Literal, Union, TYPE_CHECKING

from geogeometry.graphics.Figure2d import Figure2d
from geogeometry.graphics.Figure3d import Figure3d

if TYPE_CHECKING:
    import pyvista as pv
    import matplotlib.pyplot as plt
    from geogeometry.geometry.shared.BaseObject import BaseObject
    from geogeometry.geometry.shared.BaseObjectCollection import BaseObjectCollection


class BasePlotter(ABC):

    def __init__(self, element: Union['BaseObject', 'BaseObjectCollection']):
        self.element: Union['BaseObject', 'BaseObjectCollection'] = element

    def addToFigure2d(self, figure_2d: 'Figure2d') -> None:
        figure_2d.addElement(self.element)

    @abstractmethod
    def addToMatplotlibAx(self, ax: 'plt.Axes') -> None: ...

    def addToFigure3d(self, figure_3d: 'Figure3d') -> None:
        figure_3d.addElement(self.element)

    @abstractmethod
    def addToPyvistaPlotter(self, plotter: 'pv.Plotter', **kwargs) -> None: ...

    @abstractmethod
    def addToParaviewPlotter(self, plotter, **kwargs) -> None: ...

    def plot2d(self, filepath: Optional[str] = None,
               projection_mode: Literal['2d', '3d'] = '2d',
               projection_plane: Literal['xy', 'yz', 'xz'] = 'xy',
               **kwargs) -> None:

        figure_2d = Figure2d()
        self.addToFigure2d(figure_2d=figure_2d)
        figure_2d.plot(filepath=filepath, projection_mode=projection_mode, projection_plane=projection_plane)

    def plot3d(self, engine: Literal['pyvista', 'paraview'] = 'pyvista',
               filepath: Optional[str] = None,
               projection_plane: Optional[Literal['xy', 'yz', 'xz']] = None,
               show_axes: bool = True,
               **kwargs) -> None:

        figure_3d = Figure3d(engine=engine)
        self.addToFigure3d(figure_3d=figure_3d)
        figure_3d.plot(filepath=filepath, projection_plane=projection_plane, show_axes=show_axes)
