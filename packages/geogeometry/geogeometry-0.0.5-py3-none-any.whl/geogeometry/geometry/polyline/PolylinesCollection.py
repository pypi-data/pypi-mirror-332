from typing import Optional, TYPE_CHECKING, Literal

from geogeometry.geometry.polyline.collection_components.PolylinesCollectionPlotter import PolylinesCollectionPlotter
from geogeometry.geometry.shared.BaseObjectCollection import BaseObjectCollection

if TYPE_CHECKING:
    from geogeometry.geometry.polyline.Polyline import Polyline


class PolylinesCollection(BaseObjectCollection['PolylinesCollection', 'Polyline']):

    def __init__(self, name: Optional[str] = None):
        super().__init__(name=name)

        # self.plotter: PolylinesCollectionPlotter = PolylinesCollectionPlotter(self)

    def __str__(self) -> str:
        txt = f"PolylinesCollection(name={self.getName()}, polylines={len(self)})"
        return txt
