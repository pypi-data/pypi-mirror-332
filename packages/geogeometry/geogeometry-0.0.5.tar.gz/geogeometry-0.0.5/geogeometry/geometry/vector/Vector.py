from typing import Optional, Callable, List, Union, TYPE_CHECKING, Literal

import numpy as np

from geogeometry.geometry.shared.explicit_geometry.ExplicitGeometry import ExplicitGeometry

from geogeometry.geometry.vector.components.VectorMetrics import VectorMetrics
from geogeometry.geometry.vector.components.VectorPlotter import VectorPlotter
from geogeometry.geometry.vector.components.VectorProperties import VectorProperties
from geogeometry.geometry.vector.components.VectorQuerier import VectorQuerier
from geogeometry.geometry.vector.components.VectorTransformer import VectorTransformer


def nodesToVector(func: Callable[..., List[np.ndarray]]) -> Callable[..., 'Vector']:
    def inner(vector: 'Vector', *args, **kwargs) -> 'Vector':
        nodes = func(vector, *args, **kwargs)
        return Vector(origin=nodes[0], tip=nodes[1])

    return inner


class Vector(ExplicitGeometry, VectorProperties):

    def __init__(self,
                 tip: Union[List, np.ndarray],
                 origin: Optional[Union[List, np.ndarray]] = None,
                 name: Optional[str] = None):

        super().__init__(name=name)

        self.metrics: VectorMetrics = VectorMetrics(self)
        self.querier: VectorQuerier = VectorQuerier(self)
        self.transformer: VectorTransformer = VectorTransformer(self)
        self.plotter: VectorPlotter = VectorPlotter(self)

        if origin is None:
            origin = np.zeros(len(tip))

        self.setNodes(nodes=[origin, tip])

    def __eq__(self, other_vector: 'Vector') -> bool:
        diff = self.getNodes() - other_vector.getNodes()
        if np.linalg.norm(diff):
            return False
        return True

    def __str__(self) -> str:
        txt = f"Vector(origin={self.getOrigin()}, tip={self.getTip()})"
        return txt

    def setNodes(self, nodes: Union[List, np.ndarray]) -> None:
        super().setNodes(nodes=nodes)

        if len(nodes) != 2:
            raise ValueError("Trying to define an explicit vector without 2 nodes.")

        self.setOrigin(origin=self.getNodes()[0])
        self.setTip(tip=self.getNodes()[1])

        self.metrics.calculateMetrics()

    # QUERIER
    def calculateAngleWithVector(self, other_vector: 'Vector') -> float:
        return self.querier.calculateAngleWithVector(other_vector=other_vector)

    def isVectorParallel(self, other_vector: 'Vector') -> bool:
        diff = self.getUnitVector() - other_vector.getUnitVector()
        if np.linalg.norm(diff):
            return False
        return True

    # TRANSFORMATIONS
    def reverse(self) -> None:
        self.transformer.reverse()
