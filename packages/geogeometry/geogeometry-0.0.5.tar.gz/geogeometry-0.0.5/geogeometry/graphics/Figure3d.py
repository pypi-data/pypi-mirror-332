from typing import Literal, Optional, Union

import numpy as np
import pyvista as pv

from geogeometry.graphics.shared.PlotFigure import PlotFigure


class Figure3d(PlotFigure):

    def __init__(self, engine: Literal['pyvista', 'paraview'] = 'pyvista'):
        super().__init__()

        self.engine: Literal['pyvista', 'paraview'] = engine

        self.plotter: Optional[Union[pv.Plotter]] = None

    def getEngine(self) -> Literal['pyvista', 'paraview']:
        return self.engine

    def setParallelPlaneView(self, projection_plane: Literal['xy', 'yz', 'xz']) -> None:
        self.plotter.camera.parallel_projection = True

        limits = self.calculateLimits()
        mid_point = np.average(limits, axis=0)

        xmin, ymin, zmin = limits[0]
        xmax, ymax, zmax = limits[1]

        if projection_plane == 'xy':
            # Set camera position above the triangulation and looking at the XY plane
            self.plotter.camera_position = [
                (0.5 * (xmin + xmax), 0.5 * (ymin + ymax), zmax + 100),  # Safe Z above the scene
                mid_point,  # Focus point
                (0, 1, 0)  # Up direction
            ]

            self.plotter.camera.SetParallelScale((ymax - ymin) / 2)

            # Calculate the aspect ratio for the screenshot
            x_range = xmax - xmin
            y_range = ymax - ymin
            aspect_ratio = x_range / y_range

        elif projection_plane == 'yz':
            # Set camera position above the triangulation and looking at the XY plane
            self.plotter.camera_position = [
                (xmax + 100, 0.5 * (ymin + ymax), 0.5 * (zmin + zmax)),  # Safe Z above the scene
                mid_point,  # Focus point
                (0, 0, 1)  # Up direction
            ]

            self.plotter.camera.SetParallelScale((zmax - zmin) / 2)

            # Calculate the aspect ratio for the screenshot
            y_range = ymax - ymin
            z_range = zmax - zmin
            aspect_ratio = y_range / z_range

        elif projection_plane == 'xz':
            # Set camera position above the triangulation and looking at the XY plane
            self.plotter.camera_position = [
                (0.5 * (xmin + xmax), ymax - 100, 0.5 * (zmin + zmax)),  # Safe Z above the scene
                mid_point,  # Focus point
                (0, 0, 1)  # Up direction
            ]

            self.plotter.camera.SetParallelScale((zmax - zmin) / 2)

            # Calculate the aspect ratio for the screenshot
            x_range = xmax - xmin
            z_range = zmax - zmin
            aspect_ratio = x_range / z_range

        # Adjust plotter window size for the correct aspect ratio
        height = 500  # Set height of the image (adjust as needed)
        width = int(height * aspect_ratio)
        self.plotter.window_size = [width, height]

    def plot(self, filepath: Optional[str] = None,
             projection_plane: Optional[Literal['xy', 'yz', 'xz']] = None,
             show_axes: bool = True) -> None:

        if self.plotter is None:
            if self.engine == 'pyvista':
                self.plotter = pv.Plotter(off_screen=filepath is not None)
            else:
                raise ValueError("Not yet implemented.")

        for e in self.elements:
            e.addToPyvistaPlotter(self.plotter)

        if projection_plane is not None:
            self.setParallelPlaneView(projection_plane=projection_plane)

        if show_axes:
            self.plotter.add_axes()

        if filepath is not None:
            self.plotter.screenshot(filepath)  # Save the plot to an image file
        else:
            self.plotter.show()

