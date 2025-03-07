from typing import TYPE_CHECKING

from geogeometry.geometry.shared.explicit_geometry.ExplicitGeometryTransformer import ExplicitGeometryTransformer

if TYPE_CHECKING:
    from geogeometry.geometry.polyline.Polyline import Polyline


class PolylineTransformer(ExplicitGeometryTransformer):

    def __init__(self, polyline: 'Polyline'):
        super().__init__(element=polyline)
