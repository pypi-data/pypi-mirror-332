import copy
import gzip
import lzma
import pickle

from typing import Optional, TYPE_CHECKING, Literal, Generic, TypeVar

from geogeometry.geometry.shared.BaseObjectProperties import BaseObjectProperties
from geogeometry.geometry.shared.observer.Observable import Observable


if TYPE_CHECKING:
    import pyvista as pv
    import matplotlib.pyplot as plt
    from geogeometry.graphics.Figure2d import Figure2d
    from geogeometry.graphics.Figure3d import Figure3d
    from geogeometry.geometry.shared.shared_components.BaseMetrics import BaseMetrics
    from geogeometry.geometry.shared.shared_components.BasePlotter import BasePlotter


ObjectType = TypeVar('ObjectType')


class BaseObject(BaseObjectProperties, Observable, Generic[ObjectType]):

    def __init__(self, name: Optional[str] = None):
        super().__init__(name=name)

        # These components must be defined on child classes (emuling "abstract fields")
        self.metrics: Optional['BaseMetrics'] = None
        self.plotter: Optional['BasePlotter'] = None

    def copy(self):
        copy_p = copy.deepcopy(self)
        copy_p.setId(_id=id(copy_p))
        return copy_p

    # IO
    def save(self, savepath: str) -> None:
        if '.pkl.gz' in savepath:
            pickle.dump(self, gzip.open(savepath, 'wb'), pickle.HIGHEST_PROTOCOL)
        elif 'pkl.xz' in savepath:
            pickle.dump(self, lzma.open(savepath, 'wb'), pickle.HIGHEST_PROTOCOL)
        else:
            pickle.dump(self, open(savepath, 'wb'), pickle.HIGHEST_PROTOCOL)

        print(f'{self.__class__.__name__} instance saved at: "' + savepath + '"')

    @staticmethod
    def load(load_path) -> ObjectType:
        if '.pkl.gz' in load_path:
            return pickle.load(gzip.open(load_path, 'rb'))
        elif 'pkl.xz' in load_path:
            return pickle.load(lzma.open(load_path, 'rb'))
        else:
            return pickle.load(open(load_path, 'rb'))

    def calculateMetrics(self) -> None:
        self.metrics.calculateMetrics()

    def addToFigure2d(self, figure_2d: 'Figure2d') -> None:
        self.plotter.addToFigure2d(figure_2d=figure_2d)

    def addToMatplotlibAx(self, ax: 'plt.Axes') -> None:
        self.plotter.addToMatplotlibAx(ax=ax)

    def addToFigure3d(self, figure_3d: 'Figure3d') -> None:
        self.plotter.addToFigure3d(figure_3d=figure_3d)

    def addToPyvistaPlotter(self, plotter: 'pv.Plotter', **kwargs) -> None:
        self.plotter.addToPyvistaPlotter(plotter=plotter)

    def addToParaviewPlotter(self, plotter, **kwargs) -> None:
        self.plotter.addToParaviewPlotter(plotter=plotter, **kwargs)

    def plot2d(self, filepath: Optional[str] = None, projection_mode: Literal['2d', '3d'] = '2d', **kwargs) -> None:
        self.plotter.plot2d(filepath=filepath, projection_mode=projection_mode, **kwargs)

    def plot3d(self, engine: Literal['pyvista', 'paraview'] = 'pyvista',
               filepath: Optional[str] = None,
               projection_plane: Optional[Literal['xy', 'yz', 'xz']] = None,
               show_axes: bool = True,
               **kwargs) -> None:
        self.plotter.plot3d(engine=engine, filepath=filepath,
                            projection_plane=projection_plane, show_axes=show_axes, **kwargs)


