from typing import TYPE_CHECKING

from geogeometry.geometry.shared.explicit_geometry.ExplicitGeometryMetrics import ExplicitGeometryMetrics
from geogeometry.geometry.shared.shared_components.BaseMetrics import BaseMetrics

if TYPE_CHECKING:
    from geogeometry.geometry.triangulation.Triangulation import Triangulation


class TriangulationMetrics(BaseMetrics):

    def __init__(self, triangulation: 'Triangulation'):
        self.triangulation: 'Triangulation' = triangulation

    def calculateMetrics(self) -> None:
        pass
