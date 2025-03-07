import os
import tempfile
from typing import Optional, Literal

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

from geogeometry.graphics.Figure3d import Figure3d
from geogeometry.graphics.shared.PlotFigure import PlotFigure


class Figure2d(PlotFigure):

    def __init__(self):
        super().__init__()
        self.figure: Optional[plt.Figure] = None
        self.ax: Optional[plt.Axes] = None

    def getFigure(self) -> Optional[plt.Figure]:
        return self.figure

    def getAx(self) -> Optional[plt.Axes]:
        return self.ax

    def setAxesLabels(self, projection_plane: Literal['xy', 'yz', 'xz'] = 'xy'):

        limits = self.calculateLimits()

        if projection_plane == 'xy':
            self.ax.set_xlabel('East [m]', fontsize=8)
            self.ax.set_ylabel('North [m]', fontsize=8)
            self.ax.set_xlim(limits[0][0], limits[1][0])
            self.ax.set_ylim(limits[0][1], limits[1][1])
        elif projection_plane == 'yz':
            self.ax.set_xlabel('North [m]', fontsize=8)
            self.ax.set_ylabel('Elevation [m]', fontsize=8)
            self.ax.set_xlim(limits[0][1], limits[1][1])
            self.ax.set_ylim(limits[0][2], limits[1][2])
        elif projection_plane == 'xz':
            self.ax.set_xlabel('East [m]', fontsize=8)
            self.ax.set_ylabel('Elevation [m]', fontsize=8)
            self.ax.set_xlim(limits[0][0], limits[1][0])
            self.ax.set_ylim(limits[0][2], limits[1][2])

    def plot(self, filepath: Optional[str] = None,
             projection_mode: Literal['2d', '3d'] = '2d',
             projection_plane: Literal['xy', 'yz', 'xz'] = 'xy') -> None:

        self.figure = plt.figure()
        self.ax = self.figure.add_subplot()

        if projection_mode == '2d':
            for e in self.elements:
                e.addToMatplotlibAx(ax=self.ax)
            self.ax.set_aspect("equal")

        else:
            fig3d = Figure3d()
            for e in self.elements:
                e.addToFigure3d(figure_3d=fig3d)

            tmpfile = tempfile.NamedTemporaryFile(suffix=".png", delete=False)
            fig3d.plot(filepath=tmpfile.name, projection_plane=projection_plane, show_axes=False)

            img = mpimg.imread(tmpfile.name)
            limits = self.calculateLimits()

            if projection_plane == 'xy':
                extent = [limits[0][0], limits[1][0], limits[0][1], limits[1][1]]
            elif projection_plane == 'yz':
                extent = [limits[0][1], limits[1][1], limits[0][2], limits[1][2]]
            elif projection_plane == 'xz':
                extent = [limits[0][0], limits[1][0], limits[0][2], limits[1][2]]

            self.ax.imshow(img, extent=extent)

            tmpfile.close()
            if os.path.exists(tmpfile.name):
                os.remove(tmpfile.name)

            self.setAxesLabels(projection_plane=projection_plane)

        if filepath is not None:
            plt.savefig(filepath, bbox_inches="tight", dpi=110)
        else:

            plt.show()

        plt.close(self.figure)
