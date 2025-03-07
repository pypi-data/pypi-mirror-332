from typing import Optional, TYPE_CHECKING, Literal

from geogeometry.geometry.shared.BaseObjectCollection import BaseObjectCollection
from geogeometry.geometry.triangulation.collection_components.TriangulationsCollectionPlotter import \
    TriangulationsCollectionPlotter

if TYPE_CHECKING:
    from geogeometry.geometry.triangulation.Triangulation import Triangulation


class TriangulationsCollection(BaseObjectCollection['TriangulationCollection', 'Triangulation']):

    def __init__(self, name: Optional[str] = None):
        super().__init__(name=name)

        # self.plotter: TriangulationsCollectionPlotter = TriangulationsCollectionPlotter(self)

    def __str__(self) -> str:
        txt = f"TriangulationsCollection(name={self.getName()}, triangulations={len(self)})"
        return txt
