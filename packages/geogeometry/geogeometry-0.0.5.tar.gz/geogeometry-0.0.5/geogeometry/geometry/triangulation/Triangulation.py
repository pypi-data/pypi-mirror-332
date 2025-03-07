from typing import Optional, TYPE_CHECKING, Literal, Callable, Union, List

import numpy as np
import trimesh

from geogeometry.geometry.shared.BaseObject import BaseObject
from geogeometry.geometry.shared.explicit_geometry.ExplicitGeometry import ExplicitGeometry
from geogeometry.geometry.triangulation.components.TriangulationMetrics import TriangulationMetrics
from geogeometry.geometry.triangulation.components.TriangulationPlotter import TriangulationPlotter
from geogeometry.geometry.triangulation.components.TriangulationProperties import TriangulationProperties


def processTrimeshAndMetrics(func: Callable[..., None]) -> Callable[..., None]:

    def inner(triangulation: 'Triangulation', *args, **kwargs) -> None:
        if triangulation.trimesh_t is not None:
            raise ValueError("Triangulation already set.")

        func(triangulation, *args, **kwargs)

        if triangulation.getNodes() is not None and triangulation.getFaces() is not None:
            trimesh_t = trimesh.Trimesh(vertices=triangulation.getNodes(), faces=triangulation.getFaces(), process=True)
            triangulation.setTrimesh(trimesh_t=trimesh_t)

            triangulation.resetNodes()  # Nodes within trimesh now

            triangulation.metrics.calculateMetrics()

    return inner


class Triangulation(ExplicitGeometry, TriangulationProperties):

    def __init__(self, name: Optional[str] = None):
        super().__init__(name=name)

        self.metrics: TriangulationMetrics = TriangulationMetrics(self)
        self.plotter: TriangulationPlotter = TriangulationPlotter(self)

    def __len__(self) -> int:
        if self.getFaces() is None:
            return 0
        return len(self.getFaces())

    def __str__(self) -> str:
        txt = f"Triangle(name={self.getName()}, faces={len(self)})"
        return txt

    def getNodes(self) -> Optional[np.ndarray]:
        if self.getTrimesh() is not None:
            return np.asarray(self.getTrimesh().vertices)
        else:
            return super().getNodes()

    @processTrimeshAndMetrics
    def setNodes(self, nodes: Union[List, np.ndarray]) -> None:
        super().setNodes(nodes=nodes)

    @processTrimeshAndMetrics
    def setFaces(self, faces: Union[List[int], np.ndarray[int]]) -> None:
        if isinstance(faces, list):
            faces = np.array(faces).astype(int)
        self.faces = faces
