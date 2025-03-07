from typing import Union, List, Optional, TYPE_CHECKING, Iterable, Literal

import numpy as np

from geogeometry.geometry.polyline.components.PolylineTransformer import PolylineTransformer

from geogeometry.geometry.polyline.components.PolylinePlotter import PolylinePlotter
from geogeometry.geometry.polyline.components.PolylineProperties import PolylineProperties

from geogeometry.geometry.polyline.components.PolylineMetrics import PolylineMetrics
from geogeometry.geometry.polyline.components.PolylineQuerier import PolylineQuerier
from geogeometry.geometry.shared.explicit_geometry.ExplicitGeometry import ExplicitGeometry


class Polyline(ExplicitGeometry, PolylineProperties):

    def __init__(self,
                 nodes: Optional[Union[List, np.ndarray]] = None,
                 name: Optional[str] = None):
        super().__init__(name=name)

        self.metrics: PolylineMetrics = PolylineMetrics(self)
        self.querier: PolylineQuerier = PolylineQuerier(self)
        self.transformer: PolylineTransformer = PolylineTransformer(self)

        self.plotter: PolylinePlotter = PolylinePlotter(self)

        if nodes is not None:
            self.setNodes(nodes=nodes)

    def __len__(self) -> int:
        if self.getNodes() is None:
            return 0
        return len(self.getNodes())

    def __iter__(self) -> Iterable[np.ndarray]:
        for n in self.getNodes():
            yield n

    def __str__(self) -> str:
        txt = f"Polyline(name={self.getName()}, nodes={len(self)}, closed={self.isClosed()})"
        return txt

    def setNodes(self, nodes: Union[List, np.ndarray]) -> None:
        super().setNodes(nodes=nodes)
        self.segments = [[j, j + 1] for j, n in enumerate(self.nodes[:-1])]

        self.metrics.calculateMetrics()

    # QUERIES
    def getPointAtDistanceFromOrigin(self, distance: float) -> Optional[np.ndarray]:
        return self.querier.getPointAtDistanceFromOrigin(distance=distance)
